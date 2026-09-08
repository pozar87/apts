from datetime import timedelta
from typing import Any, cast

import numpy as np
from skyfield.positionlib import Apparent
from skyfield.searchlib import find_minima

from ...cache import get_ephemeris, get_timescale
from ...constants import astronomy
from ...utils import planetary
from ..utils import fast_altaz
from .calculations import (
    aggregate_alignment_daily_results as _aggregate_to_daily_results,
    calculate_alignment_step_results as _calculate_step_results,
    format_alignment_events as _format_alignment_events,
)


def find_oppositions(observer, planet_name, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    planet = planetary.get_skyfield_obj(planet_name)
    sun = planetary.get_skyfield_obj("sun")

    def ecliptic_longitude_difference(t):
        # Use apparent topocentric positions for maximum observational accuracy
        # Optimization: Hoist observer.at(t) to avoid evaluating observer state twice per step
        obs_at_t = observer.at(t)
        planet_lon = obs_at_t.observe(planet).apparent().ecliptic_latlon()[1].degrees
        sun_lon = obs_at_t.observe(sun).apparent().ecliptic_latlon()[1].degrees
        diff = sun_lon - planet_lon
        return (diff + 180) % 360 - 180

    def opposition_angle_difference(t):
        return abs(abs(ecliptic_longitude_difference(t)) - 180)

    setattr(opposition_angle_difference, "step_days", 180)

    times, _ = find_minima(t0, t1, opposition_angle_difference)

    events = []
    for t in times:
        # Calculate physical data at the moment of opposition
        astrometric = observer.at(t).observe(planet).apparent()

        mag = planetary.get_planet_magnitude(planet_name, t, astrometric=astrometric)
        dist_km = planetary.get_planet_distance_km(
            planet_name, t, astrometric=astrometric
        )
        diam = planetary.get_planet_angular_diameter(planet_name, t, observer=observer)

        events.append(
            {
                "date": t.utc_datetime(),
                "planet": planet_name,
                "magnitude": float(mag),
                "distance_au": float(dist_km / astronomy.AU_KM),
                "angular_diameter_arcsec": float(diam),
            }
        )

    return events


def find_mars_closest_approach(start_date, end_date, observer=None):
    """
    Finds when Mars is at its closest point to Earth (perigee).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = get_ephemeris()
    earth = eph["earth"]
    mars = eph["mars barycenter"]
    sun = eph["sun"]

    def distance_to_earth(t):
        return cast(Any, earth).at(t).observe(mars).distance().au

    # Mars closest approach happens every ~780 days.
    # Step of 30 days is safe for find_minima.
    setattr(distance_to_earth, "step_days", 30.0)
    times, values = find_minima(t0, t1, distance_to_earth)

    events = []
    for t, dist in zip(times, values):
        event = {
            "date": t.utc_datetime(),
            "event": "Mars Closest Approach",
            "object": "Mars",
            "type": "Mars Closest Approach",
            "distance_au": float(dist),
        }

        if observer is not None:
            # Optimization: Hoist observer.at(t) and use fast_altaz for Sun visibility check
            obs_at_t = observer.at(t)
            v_obs = obs_at_t.observe(mars).apparent()
            alt, _, _ = v_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

            sun_alt = fast_altaz(obs_at_t, sun)[0].degrees

            event.update(
                {
                    "altitude": float(alt.degrees),
                    "sun_altitude": float(cast(float, sun_alt)),
                    "is_visible": bool(alt.degrees > 0 and cast(float, sun_alt) <= -6),
                }
            )

        events.append(event)

    return events


def find_planet_alignments(observer, start_date, end_date):
    """
    Finds planetary alignments (multiple planets close together in ecliptic longitude).
    Takes into account visibility from the observer's location to highlight "planet parades".
    """
    ts = get_timescale()
    t_start = ts.utc(start_date)
    t_end = ts.utc(end_date)

    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]
    planet_objs = [(p, planetary.get_skyfield_obj(p)) for p in planets]
    sun = planetary.get_skyfield_obj("sun")

    # Use 1-hour steps to find best visibility and alignment
    duration_days = float(t_end - t_start)
    if duration_days <= 0:
        return []

    num_steps = int(duration_days * 24) + 1
    t_list = [t_start.utc_datetime() + timedelta(hours=i) for i in range(num_steps)]
    times = ts.from_datetimes(t_list)

    # Pre-calculate longitudes, altitudes and sun altitude vectorized
    longitudes = []
    altitudes = []

    # Optimization: Hoist observer.at(times) out of the loop to avoid redundant
    # coordinate transformations for each planet and the sun.
    obs_at_times = observer.at(times)

    # Optimization: Consolidate observations.
    # We use a single topocentric observation for both ecliptic longitude and altitude.
    # While alignments are traditionally geocentric, the topocentric difference is
    # negligible for discovery thresholds (arcseconds vs degrees).
    for _, obj in planet_objs:
        # Topocentric observation
        obj_topo_ast = obs_at_times.observe(obj)

        # 1. Ecliptic longitudes (topocentric)
        lons = obj_topo_ast.ecliptic_latlon()[1].degrees
        longitudes.append(lons)

        # 2. Altitude for visibility gating
        # Optimization: Use astrometric positions wrapped in Apparent for faster visibility checks.
        # This bypasses expensive nutation/aberration calculations while maintaining sufficient
        # accuracy for horizon gating.
        obj_app = Apparent(
            obj_topo_ast.position.au, obj_topo_ast.velocity.au_per_d, obj_topo_ast.t
        )
        obj_app.center = obj_topo_ast.center
        alts = obj_app.altaz()[0].degrees
        altitudes.append(alts)

    longitudes = np.array(longitudes)  # (n_planets, n_times)
    altitudes = np.array(altitudes)  # (n_planets, n_times)

    # Optimization: Use manual Apparent for Sun visibility check as well
    sun_topo_ast = obs_at_times.observe(sun)
    sun_app = Apparent(
        sun_topo_ast.position.au, sun_topo_ast.velocity.au_per_d, sun_topo_ast.t
    )
    sun_app.center = sun_topo_ast.center
    sun_alts = sun_app.altaz()[0].degrees
    # Planets are visible in twilight. We use -2 degrees as a compromise
    # between sunset (0) and civil twilight (-6) to capture parades.
    is_dark = sun_alts < -2  # type: ignore[operator]

    # Calculate stats for every hour
    step_results = _calculate_step_results(times, longitudes, altitudes, is_dark)

    # Aggregate to daily results to maintain consistent grouping
    daily_results = _aggregate_to_daily_results(times, step_results)

    return _format_alignment_events(daily_results, planets)
