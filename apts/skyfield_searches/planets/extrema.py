from typing import Any, cast

import numpy as np
from skyfield import almanac, magnitudelib
from skyfield.searchlib import find_maxima, find_minima

from ...cache import get_ephemeris, get_timescale
from ...utils import planetary
from ..utils import fast_altaz


def find_planetary_dichotomy(
    observer,
    start_date,
    end_date,
    precomputed_positions=None,
):
    """
    Finds when Mercury or Venus reach exactly 50% illumination (phase angle = 90°).
    This event is known as dichotomy.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    sun = planetary.get_skyfield_obj("sun")

    planets = ["mercury", "venus"]
    events = []

    for p_name in planets:
        planet_obj = planetary.get_skyfield_obj(p_name)
        simple_name = planetary.get_simple_name(p_name)

        def phase_angle_state(t):
            # We want to find when phase angle crosses 90 degrees.
            # Use geocentric position for standard dichotomy calculation.
            # Geocentric Earth position is used as the reference for astronomical dichotomy.
            eph = get_ephemeris()
            earth = cast(Any, eph["earth"])
            astrometric = earth.at(t).observe(planet_obj)

            # Phase angle Sun-Planet-Earth
            phase_angle = astrometric.phase_angle(sun).degrees
            return (phase_angle > 90).astype(int)

        # Dichotomy happens twice per synodic period.
        # Step of 5 days is safe for Mercury (~116d synodic) and Venus (~584d synodic).
        setattr(phase_angle_state, "step_days", 5.0)
        times, codes = almanac.find_discrete(t0, t1, phase_angle_state)

        for t in times:
            # High-precision observation at the event time
            astrometric = observer.at(t).observe(planet_obj).apparent()
            alt, _, _ = astrometric.altaz(temperature_C=10.0, pressure_mbar=1013.25)

            # Visibility check: Planet above horizon and Sun below -6 degrees
            # Optimization: Use fast_altaz for Sun visibility check.
            sun_alt = fast_altaz(observer.at(t), sun)[0].degrees

            events.append(
                {
                    "date": t.utc_datetime(),
                    "event": f"{simple_name} Dichotomy (50% Illumination)",
                    "object": simple_name,
                    "type": "Planetary Dichotomy",
                    "altitude": float(alt.degrees),
                    "is_visible": bool(alt.degrees > 0 and sun_alt <= -6),  # type: ignore[operator]
                }
            )

    return events


def find_venus_greatest_brilliancy(observer: Any, start_date: Any, end_date: Any):
    """
    Finds when Venus reaches its greatest brilliancy (minimum apparent magnitude).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    venus = planetary.get_skyfield_obj("venus")

    # For planetary magnitude, we use geocentric position (earth.at(t))
    # to match standard almanac definitions for greatest brilliancy.
    earth = cast(Any, get_ephemeris()["earth"])

    def magnitude(t):
        astrometric = earth.at(t).observe(venus)
        return magnitudelib.planetary_magnitude(astrometric)  # type: ignore[arg-type]

    # Venus greatest brilliancy occurs every ~584 days.
    # A step of 30 days is safe to find the minimum.
    setattr(magnitude, "step_days", 30.0)
    times, values = find_minima(t0, t1, magnitude)

    events = []
    for t, mag in zip(times, values):
        # Calculate altitude and visibility at the observer's location
        v_obs = observer.at(t).observe(venus).apparent()
        alt, _, _ = v_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

        # Sun altitude for visibility check
        sun = planetary.get_skyfield_obj("sun")
        # Optimization: Use fast_altaz for Sun visibility check.
        sun_alt = fast_altaz(observer.at(t), sun)[0].degrees

        events.append(
            {
                "date": t.utc_datetime(),
                "event": "Venus Greatest Brilliancy",
                "object": "Venus",
                "type": "Venus Greatest Brilliancy",
                "magnitude": float(mag),
                "altitude": float(alt.degrees),
                "sun_altitude": float(sun_alt),  # type: ignore[arg-type]
            }
        )

    return events


def find_stationary_points(observer, planet_name, start_date, end_date):
    """
    Finds when a planet becomes stationary in Right Ascension (transitioning
    between direct and retrograde motion).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    planet = planetary.get_skyfield_obj(planet_name)

    def ra_velocity(t):
        # We want to find where d(RA)/dt = 0
        # Use a small delta for numerical differentiation
        dt = 0.001  # ~1.4 minutes
        t_minus = ts.tt_jd(t.tt - dt)
        t_plus = ts.tt_jd(t.tt + dt)

        ra1 = (
            observer.at(t_minus).observe(planet).apparent().radec(epoch="date")[0].hours
        )
        ra2 = (
            observer.at(t_plus).observe(planet).apparent().radec(epoch="date")[0].hours
        )

        # Handle wrap-around at 24h
        diff = (ra2 - ra1 + 12) % 24 - 12
        return diff / (2 * dt)

    # Stationary points occur when RA velocity is zero.
    # We search for zero-crossings of the velocity.
    def ra_state(t):
        return (ra_velocity(t) > 0).astype(int)

    # Planets stay retrograde for weeks/months, so 2 days step is safe.
    setattr(ra_state, "step_days", 2.0)
    times, codes = almanac.find_discrete(t0, t1, ra_state)

    events = []
    simple_name = planetary.get_simple_name(planet_name)
    for t, code in zip(times, codes):
        direction = "Stationary (Direct)" if code == 1 else "Stationary (Retrograde)"
        events.append(
            {
                "date": t.utc_datetime(),
                "event": f"{simple_name} {direction}",
                "object": simple_name,
                "type": "Planet Stationary Point",
            }
        )
    return events


def find_highest_altitude(observer, planet, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    def altitude(t):
        # Account for atmospheric refraction for high-precision altitude
        return (
            observer.at(t)
            .observe(planet)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )

    setattr(altitude, "step_days", 0.1)
    times, altitudes = find_maxima(t0, t1, altitude)

    if len(times) == 0:
        return None, 0

    # find the index of the highest altitude
    max_altitude_index = np.argmax(altitudes)

    return times[max_altitude_index].utc_datetime(), altitudes[max_altitude_index]


def find_greatest_elongations(observer, start_date, end_date):
    """
    Finds greatest elongations for Mercury and Venus.
    Greatest Eastern Elongation is in the evening sky.
    Greatest Western Elongation is in the morning sky.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
    sun = eph["sun"]
    earth = eph["earth"]

    planets = ["mercury", "venus"]
    events = []

    for p_name in planets:
        planet = planetary.get_skyfield_obj(p_name)

        def elongation(t):
            # Elongation is the angle between the Sun and the planet as seen from Earth
            # We use Earth center (barycentric) for standard elongation values
            s = earth.at(t).observe(sun)
            p = earth.at(t).observe(planet)
            return s.separation_from(p).degrees

        setattr(elongation, "step_days", 2.0)  # Elongations change slowly
        times, separations = find_maxima(t0, t1, elongation)

        for t, sep in zip(cast(Any, times), separations):
            # Determine if it's Eastern or Western elongation
            # Eastern elongation: planet is east of the Sun (evening sky)
            # Western elongation: planet is west of the Sun (morning sky)
            s_lon = cast(Any, earth).at(t).observe(sun).ecliptic_latlon()[1].degrees
            p_lon = cast(Any, earth).at(t).observe(planet).ecliptic_latlon()[1].degrees

            diff = (p_lon - s_lon + 180) % 360 - 180
            direction = "Eastern" if diff > 0 else "Western"

            events.append(
                {
                    "date": t.utc_datetime(),
                    "event": f"{planetary.get_simple_name(p_name)} Greatest {direction} Elongation",
                    "object": planetary.get_simple_name(p_name),
                    "type": "Greatest Elongation",
                    "separation_degrees": float(sep),
                    "direction": direction,
                }
            )

    return events
