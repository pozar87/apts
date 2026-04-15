import numpy as np
from typing import Any, Union, cast
from skyfield import magnitudelib

from apts.cache import get_ephemeris, get_timescale
from .constants import PLANET_RADII_KM, PLANET_POLAR_RADII_KM, PLANET_ROTATION_PERIODS_S
from .base import get_simple_name, get_skyfield_obj


def get_planet_radius_km(planet_name: str) -> float:
    """
    Returns the equatorial radius of a planet in km.
    """
    # Normalize name to simple name
    simple_name = get_simple_name(planet_name).lower()
    radius = PLANET_RADII_KM.get(simple_name)
    if radius is None:
        raise ValueError(f"Radius for object '{planet_name}' not found.")
    return radius


def get_planet_rotation_period(planet_name: str) -> float:
    """
    Returns the sidereal rotation period of a planet in seconds.
    """
    simple_name = get_simple_name(planet_name).lower()
    period = PLANET_ROTATION_PERIODS_S.get(simple_name)
    if period is None:
        raise ValueError(
            f"Sidereal rotation period for object '{planet_name}' not found."
        )
    return period


def get_planet_distance_km(
    planet_name: str, time: Any, observer: Any = None, astrometric: Any = None
) -> Union[float, np.ndarray]:
    """
    Returns the geocentric (or topocentric) distance to the planet in km.
    """
    if astrometric is not None:
        res = astrometric.distance().km
    else:
        eph = get_ephemeris()
        obs_obj = observer if observer is not None else eph["earth"]
        planet_obj = get_skyfield_obj(planet_name)
        res = cast(Any, obs_obj).at(time).observe(planet_obj).distance().km
    return float(cast(Any, res)) if np.isscalar(res) else res


def get_planet_pole_coords(
    planet_name: str, time: Any
) -> tuple[Union[float, np.ndarray], Union[float, np.ndarray]]:
    """
    Returns the planet's North Pole coordinates (RA, Dec) in degrees for the given time.
    Uses the IAU 2015 model.
    """
    # This function depends on planets and moon specific orientation functions
    # We will import them inside to avoid circular dependencies if any
    from .planets import get_saturn_pole
    from .moon import _get_moon_orientation_elements

    # Time in Julian centuries from J2000.0
    T = (time.tdb - 2451545.0) / 36525.0
    name_norm = get_simple_name(planet_name).lower()

    if name_norm == "mars":
        return 317.68143 - 0.1061 * T, 52.88650 - 0.0609 * T
    if name_norm == "jupiter":
        return 268.05659 - 0.00649 * T, 64.49530 + 0.00331 * T
    if name_norm == "saturn":
        return get_saturn_pole(time)
    if name_norm == "uranus":
        if hasattr(T, "shape") and T.shape:
            return np.full_like(T, 257.311), np.full_like(T, -15.175)
        return 257.311, -15.175
    if name_norm == "neptune":
        # IAU 2015 model for Neptune (including nutation)
        # N = 357.85 + 52.316 * T
        # alpha = 299.36 + 0.70 sin N
        # delta = 43.46 - 0.51 cos N
        N_rad = np.radians(357.85 + 52.316 * T)
        alpha = 299.36 + 0.70 * np.sin(N_rad)
        delta = 43.46 - 0.51 * np.cos(N_rad)
        return alpha, delta
    if name_norm == "moon":
        alpha0, delta0, _ = _get_moon_orientation_elements(time)
        return np.degrees(alpha0), np.degrees(delta0)

    # Default to Earth pole (approx) or raise error
    if name_norm == "earth":
        if hasattr(T, "shape") and T.shape:
            return np.full_like(T, 0.0), np.full_like(T, 90.0)
        return 0.0, 90.0

    raise ValueError(f"Pole coordinates for '{planet_name}' not supported.")


def get_sub_observer_latitude(planet_name: str, time: Any) -> Union[float, np.ndarray]:
    """
    Calculates the sub-observer latitude (planetocentric latitude of the Earth) in degrees.
    This represents the tilt of the planet's equator relative to the observer.
    """
    # Geocentric observation (sufficient for sub-observer latitude calculation)
    eph = get_ephemeris()
    earth = eph["earth"]
    planet_obj = get_skyfield_obj(planet_name)
    astrometric = cast(Any, earth).at(time).observe(planet_obj)
    ra_rad, dec_rad, _ = astrometric.radec()

    # Correct for light time for the pole orientation
    ts = get_timescale()
    t_eval = ts.tt_jd(time.tt - astrometric.light_time)

    alpha_rad = ra_rad.radians
    delta_rad = dec_rad.radians

    alpha0_deg, delta0_deg = get_planet_pole_coords(planet_name, t_eval)
    alpha0_rad = np.radians(alpha0_deg)
    delta0_rad = np.radians(delta0_deg)

    # Formula for sub-observer latitude De:
    # sin(De) = -sin(delta0)*sin(delta) - cos(delta0)*cos(delta)*cos(alpha0 - alpha)
    # This represents the latitude of the sub-observer point.
    # Reference: Explanatory Supplement to the Astronomical Almanac.
    sin_De = -np.sin(delta0_rad) * np.sin(delta_rad) - np.cos(delta0_rad) * np.cos(
        delta_rad
    ) * np.cos(alpha0_rad - alpha_rad)
    De_rad = np.arcsin(np.clip(sin_De, -1.0, 1.0))

    res = np.degrees(De_rad)
    return float(cast(Any, res)) if np.isscalar(res) else res


def get_planet_angular_diameter(
    planet_name: str, time: Any, which: str = "equatorial", observer: Any = None
) -> Union[float, np.ndarray]:
    """
    Returns the apparent angular diameter of the planet in arcseconds.

    Parameters:
    - which: 'equatorial' (default), 'polar', or 'apparent_polar'.
      'apparent_polar' accounts for the planet's tilt (sub-observer latitude).
    - observer: Optional Skyfield observer for topocentric correction.
    """
    radius_eq = get_planet_radius_km(planet_name)
    distance = get_planet_distance_km(planet_name, time, observer=observer)

    if which == "equatorial":
        radius = radius_eq
    else:
        # Get polar radius
        simple_name = get_simple_name(planet_name).lower()
        radius_pol = PLANET_POLAR_RADII_KM.get(simple_name, radius_eq)

        if which == "polar":
            radius = radius_pol
        elif which == "apparent_polar":
            # Apparent polar diameter depends on tilt
            # Formula: r_app = r_eq * sqrt(1 - e^2 * cos^2(De))
            # where e^2 = (r_eq^2 - r_pol^2) / r_eq^2
            De = get_sub_observer_latitude(planet_name, time)
            De_rad = np.radians(De)
            e_sq = (radius_eq**2 - radius_pol**2) / (radius_eq**2)
            radius = radius_eq * np.sqrt(1 - e_sq * np.cos(De_rad) ** 2)
        else:
            raise ValueError(f"Invalid 'which' parameter: {which}")

    # Angular diameter in radians
    alpha_rad = 2 * np.arcsin(radius / distance)

    # Convert to arcseconds
    res = np.degrees(alpha_rad) * 3600.0
    return float(cast(Any, res)) if np.isscalar(res) else res


def get_planet_fraction_illuminated(
    planet_name: str, time: Any, astrometric: Any = None
) -> float | np.ndarray:
    """
    Returns the illuminated fraction of a planet (0.0 to 1.0) for a given time.
    Uses the phase angle 'i' between the Sun and Earth as seen from the planet.
    Formula: k = (1 + cos(i)) / 2
    """
    eph = get_ephemeris()
    sun = eph["sun"]
    if astrometric is None:
        earth = eph["earth"]
        planet_obj = get_skyfield_obj(planet_name)
        # Position of the planet as seen from Earth
        astrometric = cast(Any, earth).at(time).observe(planet_obj)

    # Phase angle: angle Sun-Planet-Earth
    i_rad = astrometric.phase_angle(sun).radians

    return (1 + np.cos(i_rad)) / 2


def get_planet_phase(planet_name: str, time: Any) -> float | np.ndarray:
    """
    Returns the illuminated fraction of the planet as a percentage (0-100).
    """
    return get_planet_fraction_illuminated(planet_name, time) * 100.0


def get_planet_phase_angle(planet_name: str, time: Any) -> float | np.ndarray:
    """
    Returns the phase angle of a planet in degrees.
    The phase angle is the angle Sun-Planet-Earth.
    """
    eph = get_ephemeris()
    sun = eph["sun"]
    earth = eph["earth"]
    planet_obj = get_skyfield_obj(planet_name)

    astrometric = cast(Any, earth).at(time).observe(planet_obj)
    return astrometric.phase_angle(sun).degrees


def get_planet_magnitude(
    planet_name: str, time: Any, astrometric: Any = None
) -> float | np.ndarray:
    """
    Calculates the apparent visual magnitude (V) for a planet, the Moon, or the Sun.

    - Major Planets: Uses Mallama & Hilton (2018) model via Skyfield.
    - The Moon: Uses Krisciunas & Schaefer (1991) phase-based model with distance correction.
    - The Sun: Uses standard inverse-square law based on AU distance.

    Sources:
    - Mallama, A., & Hilton, J. L. (2018). Computing Apparent Planetary Magnitudes for The Astronomical Almanac.
    - Krisciunas, K., & Schaefer, B. E. (1991). A model of the brightness of moonlight.
    """
    eph = get_ephemeris()
    sun = eph["sun"]
    earth = eph["earth"]

    name_norm = get_simple_name(planet_name).lower()

    if astrometric is None:
        if name_norm == "sun":
            planet_obj = sun
        else:
            planet_obj = get_skyfield_obj(planet_name)
        astrometric = cast(Any, earth).at(time).observe(planet_obj)

    if name_norm == "sun":
        # Sun magnitude: M = -26.74 at 1 AU
        dist_au = astrometric.distance().au
        return -26.74 + 5 * np.log10(dist_au)

    if name_norm == "moon":
        # Moon magnitude using Krisciunas & Schaefer (1991)
        # alpha is the phase angle Sun-Moon-Earth in degrees
        alpha = astrometric.phase_angle(sun).degrees
        # V(R, alpha) = -12.73 + 0.026 * |alpha| + 4e-9 * alpha^4
        v_base = -12.73 + 0.026 * np.abs(alpha) + 4.0e-9 * (alpha**4)

        # Distance correction: delta is distance in km
        dist_km = astrometric.distance().km
        # correction = 5 * log10(dist / 384400)
        v_dist = 5 * np.log10(dist_km / 384400.0)
        return v_base + v_dist

    # Major planets and others supported by skyfield
    # Skyfield's magnitudelib.planetary_magnitude(astrometric) handles
    # Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, and Pluto.
    try:
        return magnitudelib.planetary_magnitude(astrometric)
    except Exception:
        # Fallback for minor planets or unsupported bodies
        return np.nan


def get_planet_surface_brightness(planet_name: str, time: Any) -> float | np.ndarray:
    """
    Calculates the average surface brightness of a celestial body (Sun, Moon, or planets)
    in magnitudes per square arcsecond (mag/arcsec²).

    Formula: S = V + 2.5 * log10(Area)
    Where V is the integrated apparent magnitude and Area is the illuminated
    visual area in square arcseconds.

    Sources:
    - Wikipedia: Surface Brightness
    - Explanatory Supplement to the Astronomical Almanac
    """
    eph = get_ephemeris()
    earth = eph["earth"]
    name_norm = get_simple_name(planet_name).lower()

    if name_norm == "sun":
        planet_obj = eph["sun"]
    else:
        planet_obj = get_skyfield_obj(planet_name)

    # Optimization: Consolidate redundant Skyfield observations into a single call.
    # Apparent positions are expensive; reusing the result for magnitude, diameter,
    # and illuminated fraction provides a significant speedup.
    astrometric = cast(Any, earth).at(time).observe(planet_obj)

    v = get_planet_magnitude(planet_name, time, astrometric=astrometric)

    # Angular diameter calculation using precomputed astrometric object
    radius_eq = get_planet_radius_km(planet_name)
    distance_km = astrometric.distance().km
    alpha_rad = 2 * np.arcsin(radius_eq / distance_km)
    d = np.degrees(alpha_rad) * 3600.0

    if name_norm == "sun":
        k = 1.0
    else:
        k = get_planet_fraction_illuminated(planet_name, time, astrometric=astrometric)

    # Area of illuminated portion of the disk in arcsec^2
    # Area = pi * (radius)^2 * k
    area = np.pi * (d / 2.0) ** 2 * k

    # Handle cases where area might be zero or negative to avoid log10 errors
    if np.isscalar(area):
        if cast(Any, area) <= 0:
            return float("inf")
        # Ensure we return a Python float for consistency
        res_scalar = v + 2.5 * np.log10(area)
        return float(cast(Any, res_scalar))
    else:
        # For arrays, use np.where to handle zeros and return inf.
        # We use np.log10's 'where' and 'out' parameters to avoid RuntimeWarnings
        # when area contains zeros or negative values.
        res = np.full_like(area, np.inf, dtype=float)
        valid = area > 0
        np.log10(area, where=valid, out=res)
        res = np.where(valid, v + 2.5 * res, np.inf)
        return cast(np.ndarray, res)
