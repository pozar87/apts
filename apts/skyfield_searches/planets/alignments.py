from collections import defaultdict
from datetime import timedelta
from typing import Any, cast

import numpy as np
from skyfield.positionlib import Apparent
from skyfield.searchlib import find_minima

from ...cache import get_ephemeris, get_timescale
from ...constants import astronomy
from ...utils import planetary

# Thresholds for different numbers of planets (number: arc_degrees)
_PLANET_ALIGNMENT_THRESHOLDS = {
    3: 15,
    4: 30,
    5: 60,
    6: 160,
    7: 180,
}


def find_oppositions(observer, planet_name, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    planet = planetary.get_skyfield_obj(planet_name)
    sun = planetary.get_skyfield_obj("sun")

    def ecliptic_longitude_difference(t):
        # Use apparent topocentric positions for maximum observational accuracy
        planet_lon = (
            observer.at(t).observe(planet).apparent().ecliptic_latlon()[1].degrees
        )
        sun_lon = observer.at(t).observe(sun).apparent().ecliptic_latlon()[1].degrees
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
            v_obs = observer.at(t).observe(mars).apparent()
            alt, _, _ = v_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

            sun_alt = (
                observer.at(t)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

            event.update(
                {
                    "altitude": float(alt.degrees),
                    "sun_altitude": float(sun_alt),
                    "is_visible": bool(alt.degrees > 0 and sun_alt <= -6),
                }
            )

        events.append(event)

    return events


def _get_best_alignment_at_time(lons_at_t):
    """
    Identifies the largest and tightest planetary alignment for a given set of longitudes.
    """
    sorted_indices = np.argsort(lons_at_t)
    sorted_lons = lons_at_t[sorted_indices]
    n = len(sorted_lons)
    lons_extended = np.concatenate([sorted_lons, sorted_lons + 360])

    best_k = 0
    best_arc = 360
    best_indices = []

    for k in range(3, n + 1):
        min_arc_k = 360
        min_indices_k = []
        for i in range(n):
            arc = lons_extended[i + k - 1] - lons_extended[i]
            if arc < min_arc_k:
                min_arc_k = arc
                # Indices of planets in the arc
                min_indices_k = [sorted_indices[j % n] for j in range(i, i + k)]

        if min_arc_k < _PLANET_ALIGNMENT_THRESHOLDS.get(k, 360):
            best_k = k
            best_arc = min_arc_k
            best_indices = min_indices_k

    return best_k, best_arc, best_indices


def _calculate_step_results(times, longitudes, altitudes, is_dark):
    """
    Calculates alignment and visibility stats for each time step.
    """
    step_results = []
    for i in range(len(times)):
        k, arc, indices = _get_best_alignment_at_time(longitudes[:, i])

        # Count visible planets among those in the alignment
        visible_in_alignment = 0
        visible_indices = []
        if k >= 3:
            for idx in indices:
                if altitudes[idx, i] > 0 and is_dark[i]:
                    visible_in_alignment += 1
                    visible_indices.append(idx)

        step_results.append(
            {
                "k": k,
                "arc": arc,
                "indices": indices,
                "num_visible": visible_in_alignment,
                "visible_indices": visible_indices,
            }
        )
    return step_results


def _aggregate_to_daily_results(times, step_results):
    """
    Aggregates hourly results to find the best representative alignment for each day.
    Best means: max k, then max num_visible, then min arc.
    """
    by_day = defaultdict(list)
    for i, res in enumerate(step_results):
        day = times[i].utc_datetime().date()
        by_day[day].append((times[i], res))

    daily_results = []
    sorted_days = sorted(by_day.keys())
    for day in sorted_days:
        day_steps = by_day[day]
        best_step = max(
            day_steps, key=lambda x: (x[1]["k"], x[1]["num_visible"], -x[1]["arc"])
        )
        daily_results.append(best_step)
    return daily_results


def _format_alignment_events(daily_results, planets):
    """
    Identifies alignment windows from daily results and formats them into events.
    """
    events = []
    i = 0
    while i < len(daily_results):
        if daily_results[i][1]["k"] >= 3:
            # Start of an alignment period
            start_i = i
            while i < len(daily_results) and daily_results[i][1]["k"] >= 3:
                i += 1
            end_i = i

            # Find the best representative day in the window
            window = daily_results[start_i:end_i]
            best_day_tuple = max(
                window, key=lambda x: (x[1]["k"], x[1]["num_visible"], -x[1]["arc"])
            )

            t_best, res = best_day_tuple
            k = res["k"]
            arc = res["arc"]
            indices = res["indices"]
            num_visible = res["num_visible"]
            visible_indices = res["visible_indices"]

            aligned_planets = [
                planetary.get_simple_name(planets[idx]) for idx in indices
            ]
            visible_names = [
                planetary.get_simple_name(planets[idx]) for idx in visible_indices
            ]

            event_label = f"Alignment of {k} planets"
            if num_visible >= 3:
                event_label += f" ({num_visible} visible)"

            events.append(
                {
                    "date": t_best.utc_datetime(),
                    "event": event_label,
                    "planets": aligned_planets,
                    "visible_planets": visible_names,
                    "arc_degrees": arc,
                    "num_visible": num_visible,
                }
            )
        else:
            i += 1
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

    # Optimization: Consolidate observations.
    # We use a single topocentric observation for both ecliptic longitude and altitude.
    # While alignments are traditionally geocentric, the topocentric difference is
    # negligible for discovery thresholds (arcseconds vs degrees).
    for _, obj in planet_objs:
        # Topocentric observation
        obj_topo_ast = observer.at(times).observe(obj)

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
    sun_topo_ast = observer.at(times).observe(sun)
    sun_app = Apparent(
        sun_topo_ast.position.au, sun_topo_ast.velocity.au_per_d, sun_topo_ast.t
    )
    sun_app.center = sun_topo_ast.center
    sun_alts = sun_app.altaz()[0].degrees
    is_dark = sun_alts < 0  # type: ignore[operator]

    # Calculate stats for every hour
    step_results = _calculate_step_results(times, longitudes, altitudes, is_dark)

    # Aggregate to daily results to maintain consistent grouping
    daily_results = _aggregate_to_daily_results(times, step_results)

    return _format_alignment_events(daily_results, planets)
