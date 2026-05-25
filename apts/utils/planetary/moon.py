import numpy as np
from datetime import timedelta
from typing import Any, cast
from skyfield import almanac

from apts.cache import get_ephemeris, get_timescale
from apts.i18n import gettext_


def get_moon_illumination_details(time):
    """
    Returns the moon illumination percentage and waxing/waning status for a given time.
    Supports both scalar and array Skyfield Time objects.
    """
    eph = get_ephemeris()

    # Get the phase angle
    phase_angle = cast(Any, almanac.moon_phase(eph, time).degrees)

    # Determine if waxing or waning
    if np.isscalar(phase_angle):
        is_waxing = 0 < phase_angle < 180  # type: ignore
    else:
        is_waxing = (0 < phase_angle) & (phase_angle < 180)  # type: ignore

    illumination = (1 - np.cos(np.deg2rad(phase_angle))) / 2
    return illumination * 100, is_waxing


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
    # Get the phase angle in degrees (0-360)
    # 0 = New Moon, 90 = First Quarter, 180 = Full Moon, 270 = Last Quarter
    phase_angle = cast(Any, almanac.moon_phase(eph, time).degrees)

    if phase_angle < 1.0 or phase_angle > 359.0:
        return gettext_("New Moon")
    elif phase_angle < 89.0:
        return gettext_("Waxing Crescent")
    elif phase_angle < 91.0:
        return gettext_("First Quarter")
    elif phase_angle < 179.0:
        return gettext_("Waxing Gibbous")
    elif phase_angle < 181.0:
        return gettext_("Full Moon")
    elif phase_angle < 269.0:
        return gettext_("Waning Gibbous")
    elif phase_angle < 271.0:
        return gettext_("Last Quarter")
    else:
        return gettext_("Waning Crescent")


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

    if hasattr(time, "shape") and time.shape:
        u_v = v_mo / np.linalg.norm(v_mo, axis=0)
    else:
        u_v = v_mo / np.linalg.norm(v_mo)

    # Transformation to selenographic frame
    # x_node = intersection of Moon's equator and ICRS equator
    x_node = u_v[0] * (-np.sin(alpha0)) + u_v[1] * np.cos(alpha0)
    y_node = (
        u_v[0] * (-np.sin(delta0) * np.cos(alpha0))
        + u_v[1] * (-np.sin(delta0) * np.sin(alpha0))
        + u_v[2] * np.cos(delta0)
    )
    z = (
        u_v[0] * (np.cos(delta0) * np.cos(alpha0))
        + u_v[1] * (np.cos(delta0) * np.sin(alpha0))
        + u_v[2] * np.sin(delta0)
    )

    # Latitude (latitude of sub-Earth point)
    lat_lib = np.degrees(np.arcsin(np.clip(z, -1.0, 1.0)))

    # Longitude from node (eastward)
    phi = np.degrees(np.arctan2(y_node, x_node))
    # Selenographic longitude (eastward from prime meridian)
    lon_lib = (phi - np.degrees(W) + 180) % 360 - 180

    def _maybe_float(val):
        return float(cast(Any, val)) if np.isscalar(val) else val

    return _maybe_float(lon_lib), _maybe_float(lat_lib)


def get_moon_position_angle_bright_limb(time: Any) -> float:
    """
    Returns the position angle of the Moon's bright limb in degrees.
    This is the orientation of the line from the Moon's center to the midpoint
    of the illuminated limb, measured counterclockwise from North.
    """
    # Calculate using Skyfield
    eph = get_ephemeris()
    sun = eph["sun"]
    earth = eph["earth"]
    moon = eph["moon"]

    t = time
    astrometric_moon = cast(Any, earth).at(t).observe(moon).apparent()
    astrometric_sun = cast(Any, earth).at(t).observe(sun).apparent()

    # Position angle of the bright limb
    # Reference: https://rhodesmill.org/skyfield/api-almanac.html#skyfield.almanac.fraction_illuminated
    # Actually Skyfield doesn't have it directly in almanac,
    # but we can calculate it from the relative positions.

    ra_m, dec_m, _ = astrometric_moon.radec()
    ra_s, dec_s, _ = astrometric_sun.radec()

    # Formula from Meeus, Astronomical Algorithms, Chapter 48
    # tan(X) = cos(dec_s) * sin(ra_s - ra_m) / (cos(dec_m) * sin(dec_s) - sin(dec_m) * cos(dec_s) * cos(ra_s - ra_m))

    num = np.cos(dec_s.radians) * np.sin(ra_s.radians - ra_m.radians)
    den = np.cos(dec_m.radians) * np.sin(dec_s.radians) - np.sin(dec_m.radians) * np.cos(dec_s.radians) * np.cos(ra_s.radians - ra_m.radians)

    pa_rad = np.arctan2(num, den)
    return float(np.degrees(pa_rad) % 360)


def _get_moon_orientation_elements(
    time: Any,
) -> tuple[np.ndarray | float, np.ndarray | float, np.ndarray | float]:
    """
    Internal helper to calculate Moon orientation elements (alpha0, delta0, W)
    using the IAU 2015 model. Results are in radians.
    """
    # Evaluate orientation at observation time (Terrestrial Time)
    d = time.tt - 2451545.0
    T = d / 36525.0

    # IAU 2015 Lunar rotation parameters (Archinal et al. 2018)
    E1 = np.radians((125.045 - 0.0529921 * d) % 360)
    E2 = np.radians((250.089 - 0.1059842 * d) % 360)
    E3 = np.radians((260.008 + 13.0120009 * d) % 360)
    E4 = np.radians((176.625 + 13.3407154 * d) % 360)
    E5 = np.radians((357.529 + 0.9856003 * d) % 360)
    E6 = np.radians((311.589 + 26.4057084 * d) % 360)
    E7 = np.radians((134.963 + 13.0649930 * d) % 360)
    E8 = np.radians((276.617 + 0.3287146 * d) % 360)
    E10 = np.radians((15.134 - 0.1589763 * d) % 360)
    E11 = np.radians((119.743 + 0.0036096 * d) % 360)
    E12 = np.radians((239.961 + 0.1295801 * d) % 360)
    E13 = np.radians((25.053 + 12.5126625 * d) % 360)

    alpha0 = np.radians(
        (
            269.9949
            + 0.0031 * T
            - 3.8787 * np.sin(E1)
            - 0.1204 * np.sin(E2)
            - 0.0700 * np.sin(E3)
            - 0.0172 * np.sin(E4)
            + 0.0072 * np.sin(E6)
            - 0.0052 * np.sin(E10)
            + 0.0043 * np.sin(E13)
        )
        % 360
    )

    delta0 = np.radians(
        (
            66.5392
            + 0.0130 * T
            + 1.5419 * np.cos(E1)
            + 0.0239 * np.cos(E2)
            + 0.0278 * np.cos(E3)
            + 0.0068 * np.cos(E4)
            - 0.0029 * np.cos(E6)
            + 0.0009 * np.cos(E7)
            + 0.0008 * np.cos(E10)
            - 0.0009 * np.cos(E13)
        )
        % 360
    )

    W = np.radians(
        (
            38.3213
            + 13.17635815 * d
            + 3.5610 * np.sin(E1)
            + 0.1108 * np.sin(E2)
            + 0.0642 * np.sin(E3)
            + 0.0158 * np.sin(E4)
            - 0.0252 * np.sin(E5)
            - 0.0066 * np.sin(E6)
            - 0.0047 * np.sin(E7)
            - 0.0027 * np.sin(E8)
            + 0.0048 * np.sin(E10)
            + 0.0028 * np.sin(E11)
            + 0.0052 * np.sin(E12)
            - 0.0040 * np.sin(E13)
        )
        % 360
    )

    return alpha0, delta0, W


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

    if hasattr(time, "shape") and time.shape:
        u_v = v_ms / np.linalg.norm(v_ms, axis=0)
    else:
        u_v = v_ms / np.linalg.norm(v_ms)

    # Transformation to selenographic frame
    # x_node = intersection of Moon's equator and ICRS equator
    x_node = u_v[0] * (-np.sin(alpha0)) + u_v[1] * np.cos(alpha0)
    y_node = (
        u_v[0] * (-np.sin(delta0) * np.cos(alpha0))
        + u_v[1] * (-np.sin(delta0) * np.sin(alpha0))
        + u_v[2] * np.cos(delta0)
    )

    # Longitude from node (eastward)
    phi = np.degrees(np.arctan2(y_node, x_node))
    # Selenographic longitude (eastward from prime meridian)
    lon_selenographic = (phi - np.degrees(W)) % 360

    # Colongitude C = (90 - lon_selenographic) % 360
    return (90 - lon_selenographic) % 360
