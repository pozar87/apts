import ephem
import numpy as np
from datetime import timedelta
from typing import Any, cast, Union

from apts.cache import get_ephemeris, get_timescale
from apts.constants import astronomy
from .base import get_skyfield_obj


def _get_planet_cml_iau_model(
    planet_name: str, time: Any, w0: float, wd: float
) -> float | np.ndarray:
    """
    Internal helper for planetary Central Meridian Longitude calculation using IAU models.
    W = w0 + wd * d (degrees), where d is days from J2000.0 (TT).
    Longitude increases westward.
    """
    from .physical import get_planet_pole_coords

    eph = get_ephemeris()
    earth = eph["earth"]
    planet_obj = get_skyfield_obj(planet_name)

    # Observation of planet from Earth (includes light-time correction)
    astrometric = cast(Any, earth).at(time).observe(planet_obj)
    lt_days = astrometric.light_time

    # Rotation state of planet when light left it
    ts = get_timescale()
    t_eval = ts.tt_jd(time.tt - lt_days)

    # Planet pole at evaluation time
    alpha0_deg, delta0_deg = get_planet_pole_coords(planet_name, t_eval)
    alpha0 = np.radians(alpha0_deg)
    delta0 = np.radians(delta0_deg)

    # Direction from Planet(t-lt) to Earth(t) in ICRS
    v_pe = -astrometric.position.au

    if hasattr(time, "shape") and time.shape:
        # Vectorized norm for array times
        norms = np.linalg.norm(v_pe, axis=0)
        u_v = v_pe / norms
    else:
        # Scalar time
        u_v = v_pe / np.linalg.norm(v_pe)

    # Transform to planet-centric frame (Z to North Pole, X to Ascending Node)
    # The sub-observer longitude from the node is atan2(y, x)
    x = u_v[0] * (-np.sin(alpha0)) + u_v[1] * np.cos(alpha0)
    y = (
        u_v[0] * (-np.sin(delta0) * np.cos(alpha0))
        + u_v[1] * (-np.sin(delta0) * np.sin(alpha0))
        + u_v[2] * np.cos(delta0)
    )

    phi = np.degrees(np.arctan2(y, x))

    # IAU W: angle from node to prime meridian (increasing eastward)
    d = t_eval.tt - 2451545.0
    W = (w0 + wd * d) % 360

    # CML = (W - phi) mod 360 (increasing westward)
    return (W - phi) % 360


def get_saturn_pole(
    time: Any,
) -> tuple[Union[float, np.ndarray], Union[float, np.ndarray]]:
    """
    Returns Saturn's North Pole coordinates (RA, Dec) in degrees for the given time.
    Uses the IAU 2015 model.
    """
    # Time in Julian centuries from J2000.0
    T = (time.tdb - 2451545.0) / 36525.0
    # alpha_0 = 40.589 - 0.036 * T
    # delta_0 = 83.537 - 0.004 * T
    return 40.589 - 0.036 * T, 83.537 - 0.004 * T


def get_saturn_ring_details(time: Any) -> dict:
    """
    Calculates Saturn's ring inclination (tilt) and angular dimensions.
    Tilt 'B' is the geocentric latitude of the Earth relative to the ring plane.
    Formula source: Explanatory Supplement to the Astronomical Almanac.
    """
    eph = get_ephemeris()
    earth = eph["earth"]
    saturn = eph["saturn barycenter"]

    # Geocentric observation of Saturn (ICRS)
    # Oracle: use astrometric() for consistency with searches
    pos = cast(Any, earth).at(time).observe(saturn)
    # Unit vector from Saturn to Earth
    v_sat_earth = -pos.position.au / pos.distance().au

    # Oracle: apply light-time correction for the pole orientation.
    # This evaluates the pole at the moment the light left Saturn.
    t_eval = get_timescale().tt_jd(time.tt - pos.light_time)

    # Saturn's pole in J2000.0
    alpha_p_deg, delta_p_deg = get_saturn_pole(t_eval)
    alpha_p = np.radians(alpha_p_deg)
    delta_p = np.radians(delta_p_deg)

    # Pole unit vector
    p = np.array(
        [
            np.cos(delta_p) * np.cos(alpha_p),
            np.cos(delta_p) * np.sin(alpha_p),
            np.sin(delta_p),
        ]
    )

    # sin(B) is the dot product of the pole vector and the Saturn-Earth vector
    if hasattr(time, "shape") and time.shape:
        sin_B = np.sum(p * v_sat_earth, axis=0)
    else:
        sin_B = np.dot(p, v_sat_earth)

    B_rad = np.arcsin(np.clip(sin_B, -1.0, 1.0))
    B_deg = np.degrees(B_rad)

    # Major axis (outer edge of A ring)
    dist_km = pos.distance().km
    radius_km = astronomy.SATURN_RING_OUTER_RADIUS_KM
    major_arcsec = 2 * np.degrees(np.arcsin(radius_km / dist_km)) * 3600.0

    # Minor axis
    minor_arcsec = major_arcsec * abs(np.sin(B_rad))

    def _maybe_float(val):
        return float(cast(Any, val)) if np.isscalar(val) else val

    return {
        "tilt_degrees": _maybe_float(B_deg),
        "major_axis_arcsec": _maybe_float(major_arcsec),
        "minor_axis_arcsec": _maybe_float(minor_arcsec),
    }


# Global instance of Jupiter for efficient longitude calculation
_JUPITER_EPHEM = ephem.Jupiter()


def _get_jupiter_cml_internal(time: Any, attr: str) -> float | np.ndarray:
    """
    Internal helper for Jupiter Central Meridian Longitude calculation.
    """
    # Calculate light-travel time from Jupiter to Earth
    eph = get_ephemeris()
    earth = eph["earth"]
    jupiter = eph["jupiter barycenter"]

    # Vectorized position of Jupiter as seen from Earth
    astrometric = cast(Any, earth).at(time).observe(jupiter)
    lt_days = astrometric.light_time

    # Account for light-travel time by subtracting it from the observation time
    # This evaluates the rotation state of Jupiter at the moment the light left it.
    if hasattr(time, "shape") and time.shape:
        # Optimization: Use bulk utc_datetime() conversion and reuse a single
        # ephem.Jupiter instance for a ~15x performance boost on large arrays.
        times_dt = time.utc_datetime()
        res = np.empty(len(time))
        for i, t_dt in enumerate(times_dt):
            t_light = t_dt - timedelta(days=lt_days[i])
            _JUPITER_EPHEM.compute(t_light)
            res[i] = float(np.degrees(float(getattr(_JUPITER_EPHEM, attr))))
        return res
    else:
        # Scalar time
        t_light = time.utc_datetime() - timedelta(days=lt_days)
        _JUPITER_EPHEM.compute(t_light)
        return float(np.degrees(float(getattr(_JUPITER_EPHEM, attr))))


def get_jupiter_system_i_longitude(time: Any) -> float | np.ndarray:
    """
    Returns Jupiter's Central Meridian Longitude (System I) in degrees.
    System I is used for the equatorial region.
    Supports both scalar and array Skyfield Time objects.
    """
    return _get_jupiter_cml_internal(time, "cmlI")


def get_jupiter_system_ii_longitude(time: Any) -> float | np.ndarray:
    """
    Returns Jupiter's Central Meridian Longitude (System II) in degrees.
    System II is used for the temperate regions (including the GRS).
    Supports both scalar and array Skyfield Time objects.
    """
    return _get_jupiter_cml_internal(time, "cmlII")


def get_jupiter_cml(time: Any, system: int = 2) -> float | np.ndarray:
    """
    Returns Jupiter's Central Meridian Longitude for the specified system (1, 2 or 3).
    System I/II use PyEphem's model. System III uses IAU 2015 model.
    """
    if system == 1:
        return get_jupiter_system_i_longitude(time)
    elif system == 2:
        return get_jupiter_system_ii_longitude(time)
    elif system == 3:
        # IAU 2015/Archinal et al. (2018) System III: w0 = 284.95, wd = 870.5360000
        return _get_planet_cml_iau_model("jupiter barycenter", time, 284.95, 870.5360)
    else:
        raise ValueError(
            "Only System I (1), II (2), and III (3) are supported for Jupiter CML."
        )


def get_saturn_cml(time: Any, system: int = 3) -> float | np.ndarray:
    """
    Returns Saturn's Central Meridian Longitude (CML) in degrees for the specified system.
    System I: Equatorial region (w0=38.90, wd=844.3000000)
    System II: Intermediate latitudes (w0=40.30, wd=812.0000000)
    System III: Magnetic field/Radio rotation (w0=38.90, wd=810.7939024)
    Uses the IAU 2015/Archinal et al. (2018) model. Longitude increases westward.
    Supports both scalar and array Skyfield Time objects.
    """
    # IAU 2015/Archinal et al. (2018) parameters for Saturn
    if system == 1:
        # System I: w0 = 38.90, wd = 844.3000000
        return _get_planet_cml_iau_model("saturn barycenter", time, 38.90, 844.30)
    elif system == 2:
        # System II: w0 = 40.30, wd = 812.0000000
        return _get_planet_cml_iau_model("saturn barycenter", time, 40.30, 812.0)
    elif system == 3:
        # System III: w0 = 38.90, wd = 810.7939024
        return _get_planet_cml_iau_model("saturn barycenter", time, 38.90, 810.7939024)
    else:
        raise ValueError(
            "Only System I (1), II (2), and III (3) are supported for Saturn CML."
        )


def get_mars_cml(time: Any) -> float | np.ndarray:
    """
    Returns Mars' Central Meridian Longitude (CML) in degrees.
    Uses the IAU 2015 model. Longitude increases westward.
    Supports both scalar and array Skyfield Time objects.
    """
    # IAU 2015/Archinal et al. (2018) parameters for Mars
    # W = 176.630 + 350.89198226 * d
    return _get_planet_cml_iau_model("mars barycenter", time, 176.630, 350.89198226)


def get_jupiter_grs_longitude(time: Any) -> float | np.ndarray:
    """
    Returns the projected longitude of the Great Red Spot (System II) for a given time.
    Uses a linear drift model based on recent observations.
    Reference: 55.2° (intrinsic) on 2026-03-18 with a drift of approx 16.0°/year.
    Supports both scalar and array Skyfield Time objects.
    """
    # Reference epoch: 2026-03-18 12:21:00 UTC (Transit)
    # Pull intrinsic reference longitude from constants
    ref_lon = astronomy.JUPITER_GRS_LONGITUDE_SYSTEM_II
    drift_per_day = 16.0 / 365.25

    # Use .tt (Terrestrial Time) for precise day counting
    ts = get_timescale()
    ref_tt = ts.utc(2026, 3, 18, 12, 21).tt
    dt = time.tt - ref_tt

    return (ref_lon + dt * drift_per_day) % 360
