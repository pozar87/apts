import numpy as np
from datetime import timedelta
from typing import Any, cast
from skyfield import almanac

from apts.cache import get_ephemeris, get_timescale
from .calculations import (
    calculate_moon_orientation_elements,
    calculate_moon_illumination_and_waxing,
    calculate_moon_phase_name,
    calculate_moon_position_angle_bright_limb,
    calculate_moon_selenographic_coords,
)


def get_moon_illumination_details(time):
    """
    Returns the moon illumination percentage and waxing/waning status for a given time.
    Supports both scalar and array Skyfield Time objects.
    """
    eph = get_ephemeris()
    phase_angle = cast(Any, almanac.moon_phase(eph, time).degrees)
    return calculate_moon_illumination_and_waxing(phase_angle)


def get_moon_illumination(time):
    """
    Returns the moon illumination percentage for a given time.
    """
    illumination, _ = get_moon_illumination_details(time)
    return illumination


def get_moon_phase_name(time):
    """
    Returns the name of the moon phase for a given time.
    """
    eph = get_ephemeris()
    phase_angle = float(cast(Any, almanac.moon_phase(eph, time).degrees))
    return calculate_moon_phase_name(phase_angle)


def get_moon_age(time):
    """
    Returns the moon age in days since the last new moon.
    Uses Skyfield's almanac for high accuracy.
    """
    ts = get_timescale()
    eph = get_ephemeris()
    t1 = time
    # Search backwards for up to 31 days to find the last new moon
    t0 = ts.utc(t1.utc_datetime() - timedelta(days=31))
    f = almanac.moon_phases(eph)
    t, y = almanac.find_discrete(t0, t1, f)
    # y == 0 corresponds to New Moon
    new_moons = [ti for ti, yi in zip(t, y) if yi == 0]
    if not new_moons:
        # Fallback to a simple geometric approximation if for some reason search fails
        phase_angle = cast(Any, almanac.moon_phase(eph, time).degrees)
        return (phase_angle / 360.0) * 29.53059
    last_new_moon = new_moons[-1]
    return t1 - last_new_moon


def get_moon_distance(time):
    """
    Returns the distance to the moon in km.
    """
    eph = get_ephemeris()
    moon = eph["moon"]
    earth = eph["earth"]
    return cast(Any, earth).at(time).observe(moon).distance().km


# Cache for Moon's astrometric position to avoid redundant observations
# in high-frequency loops (e.g., discovery scoring).
_moon_pos_cache = {}


def get_moon_separation(obj, observer, time):
    """
    Calculates the angular distance in degrees between the target object and the Moon.
    """
    eph = get_ephemeris()
    moon = eph["moon"]
    astrometric_obj = observer.at(time).observe(obj).apparent()

    # Use a simple cache key based on time and observer identity
    cache_key = (time.tt, id(observer))
    if cache_key in _moon_pos_cache:
        astrometric_moon = _moon_pos_cache[cache_key]
    else:
        astrometric_moon = observer.at(time).observe(moon).apparent()
        # Keep cache size small
        if len(_moon_pos_cache) > 100:
            _moon_pos_cache.clear()
        _moon_pos_cache[cache_key] = astrometric_moon

    return astrometric_obj.separation_from(astrometric_moon).degrees


def get_moon_libration(
    time: Any, observer: Any = None
) -> tuple[float, float] | tuple[np.ndarray, np.ndarray]:
    """
    Returns the Moon's libration in longitude and latitude in degrees.
    Uses the IAU 2015 rotation model for high precision and vectorization.
    Supports both scalar and array Skyfield Time objects.
    If observer is provided, returns topocentric libration.
    """
    eph = get_ephemeris()
    moon = eph["moon"]

    # Observation of Earth (or observer) from Moon center (includes light-time correction)
    if observer is None:
        observer = eph["earth"]

    astrometric = cast(Any, moon).at(time).observe(observer).apparent()
    v_mo = astrometric.position.au

    alpha0, delta0, W = _get_moon_orientation_elements(time)
    is_array = bool(hasattr(time, "shape") and time.shape)

    return calculate_moon_selenographic_coords(v_mo, alpha0, delta0, W, is_array=is_array)


def get_moon_position_angle_bright_limb(time: Any) -> float:
    """
    Returns the position angle of the Moon's bright limb in degrees.
    This is the orientation of the line from the Moon's center to the midpoint
    of the illuminated limb, measured counterclockwise from North.
    """
    eph = get_ephemeris()
    sun = eph["sun"]
    earth = eph["earth"]
    moon = eph["moon"]

    t = time
    astrometric_moon = cast(Any, earth).at(t).observe(moon).apparent()
    astrometric_sun = cast(Any, earth).at(t).observe(sun).apparent()

    ra_m, dec_m, _ = astrometric_moon.radec()
    ra_s, dec_s, _ = astrometric_sun.radec()

    return calculate_moon_position_angle_bright_limb(
        ra_moon_rad=ra_m.radians,
        dec_moon_rad=dec_m.radians,
        ra_sun_rad=ra_s.radians,
        dec_sun_rad=dec_s.radians,
    )


def _get_moon_orientation_elements(
    time: Any,
) -> tuple[np.ndarray | float, np.ndarray | float, np.ndarray | float]:
    """
    Internal helper to calculate Moon orientation elements (alpha0, delta0, W)
    using the IAU 2015 model. Results are in radians.
    """
    return calculate_moon_orientation_elements(time.tt)


def get_moon_colongitude(time: Any) -> float | np.ndarray:
    """
    Returns the Moon's colongitude in degrees.
    Uses the IAU 2015 rotation model for high precision and vectorization.
    Supports both scalar and array Skyfield Time objects.
    """
    eph = get_ephemeris()
    sun = eph["sun"]
    moon = eph["moon"]

    # Observation of Sun from Moon center (includes light-time correction)
    astrometric = cast(Any, moon).at(time).observe(sun).apparent()
    v_ms = astrometric.position.au

    alpha0, delta0, W = _get_moon_orientation_elements(time)
    is_array = bool(hasattr(time, "shape") and time.shape)

    lon_selenographic, _ = calculate_moon_selenographic_coords(
        v_ms, alpha0, delta0, W, is_array=is_array
    )

    # Colongitude C = (90 - lon_selenographic) % 360
    return (90 - lon_selenographic) % 360
