import ephem
import re
from datetime import timedelta

import numpy as np
from types import SimpleNamespace
from typing import Any, Union, cast

from skyfield.data import mpc
from skyfield.constants import GM_SUN_Pitjeva_2005_km3_s2 as GM_SUN_KM3_S2
from skyfield import almanac, magnitudelib

from apts.cache import get_ephemeris, get_mpcorb_data, get_timescale
from apts.i18n import language_context, gettext_
from apts.constants import astronomy

MINOR_PLANET_NAMES = {
    "ceres": "(1) Ceres",
    "haumea": "(136108) Haumea",
    "makemake": "(136472) Makemake",
    "eris": "(136199) Eris",
}

PLANET_NAMES = {
    "mercury": "Mercury",
    "venus": "Venus",
    "moon": "Moon",
    "mars barycenter": "Mars",
    "jupiter barycenter": "Jupiter",
    "saturn barycenter": "Saturn",
    "uranus barycenter": "Uranus",
    "neptune barycenter": "Neptune",
    "sun": "Sun",
    "earth": "Earth",
    "ceres": "Ceres",
    "pluto barycenter": "Pluto",
    "haumea": "Haumea",
    "makemake": "Makemake",
    "eris": "Eris",
}

TECHNICAL_NAMES = list(PLANET_NAMES.keys())
SIMPLE_NAMES = list(PLANET_NAMES.values())

OPPOSITION_PLANETS = [
    "mars barycenter",
    "jupiter barycenter",
    "saturn barycenter",
    "uranus barycenter",
    "neptune barycenter",
    "ceres",
    "pluto barycenter",
    "haumea",
    "makemake",
    "eris",
]

CONJUNCTION_PLANETS = {
    "mercury": "Mercury",
    "venus": "Venus",
    "mars barycenter": "Mars",
    "jupiter barycenter": "Jupiter",
    "saturn barycenter": "Saturn",
    "uranus barycenter": "Uranus",
    "neptune barycenter": "Neptune",
}

APHELION_PERIHELION_PLANETS = [
    "mercury",
    "venus",
    "mars barycenter",
    "jupiter barycenter",
    "saturn barycenter",
    "uranus barycenter",
    "neptune barycenter",
    "earth",
    "ceres",
    "pluto barycenter",
    "haumea",
    "makemake",
    "eris",
]

PLANET_RADII_KM = {
    "mercury": astronomy.MERCURY_RADIUS_KM,
    "venus": astronomy.VENUS_RADIUS_KM,
    "earth": astronomy.EARTH_RADIUS_KM,
    "mars": astronomy.MARS_RADIUS_KM,
    "jupiter": astronomy.JUPITER_RADIUS_KM,
    "saturn": astronomy.SATURN_RADIUS_KM,
    "uranus": astronomy.URANUS_RADIUS_KM,
    "neptune": astronomy.NEPTUNE_RADIUS_KM,
    "pluto": astronomy.PLUTO_RADIUS_KM,
    "ceres": astronomy.CERES_RADIUS_KM,
    "haumea": astronomy.HAUMEA_RADIUS_KM,
    "makemake": astronomy.MAKEMAKE_RADIUS_KM,
    "eris": astronomy.ERIS_RADIUS_KM,
    "moon": astronomy.MOON_RADIUS_KM,
    "sun": astronomy.SUN_RADIUS_KM,
}

PLANET_POLAR_RADII_KM = {
    "earth": astronomy.EARTH_POLAR_RADIUS_KM,
    "mars": astronomy.MARS_POLAR_RADIUS_KM,
    "jupiter": astronomy.JUPITER_POLAR_RADIUS_KM,
    "saturn": astronomy.SATURN_POLAR_RADIUS_KM,
    "uranus": astronomy.URANUS_POLAR_RADIUS_KM,
    "neptune": astronomy.NEPTUNE_POLAR_RADIUS_KM,
}

PLANET_ROTATION_PERIODS_S = {
    "mercury": astronomy.MERCURY_ROTATION_PERIOD_S,
    "venus": astronomy.VENUS_ROTATION_PERIOD_S,
    "earth": astronomy.EARTH_ROTATION_PERIOD_S,
    "mars": astronomy.MARS_ROTATION_PERIOD_S,
    "jupiter": astronomy.JUPITER_ROTATION_PERIOD_S,
    "saturn": astronomy.SATURN_ROTATION_PERIOD_S,
    "uranus": astronomy.URANUS_ROTATION_PERIOD_S,
    "neptune": astronomy.NEPTUNE_ROTATION_PERIOD_S,
    "pluto": astronomy.PLUTO_ROTATION_PERIOD_S,
}


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


def get_simple_name(technical_name: str) -> str:
    """
    Returns the simple name for a given technical planet name.
    """
    # First, check the PLANET_NAMES mapping for major planets.
    simple_name = PLANET_NAMES.get(technical_name.lower())
    if simple_name:
        return simple_name

    # If not found, it could be a minor planet designation like "(1) Ceres".
    # We'll use regex to extract the name part.
    match = re.match(r"\(\d+\)\s*(.*)", technical_name)
    if match:
        # We got a match, so extract the name, strip whitespace, and capitalize it.
        name_part = match.group(1).strip()
        return name_part.capitalize()

    # As a fallback, for any other cases, just capitalize the original string.
    return technical_name.capitalize()


def get_technical_name(simple_name: str) -> str:
    """
    Returns the technical name for a given simple planet name.
    """
    for technical, simple in PLANET_NAMES.items():
        if simple.lower() == simple_name.lower():
            return technical
    return simple_name.lower()


def get_skyfield_obj(planet_name: str):
    """
    Returns a Skyfield object for a given planet name.
    Handles both major planets from the ephemeris and minor planets from MPCORB data.
    """
    eph = get_ephemeris()

    # Determine the name to use for lookup.
    # If it's a simple name for a minor planet, get the full designation.
    # Otherwise, use the name as is (it could be a major planet simple name,
    # or a minor planet full designation).
    name_to_lookup = MINOR_PLANET_NAMES.get(planet_name.lower(), planet_name)

    # First, try to load from ephemeris (for major planets)
    try:
        # get_technical_name will convert 'Mars' to 'mars barycenter'
        # and leave '(1) Ceres' alone (after lowercasing)
        technical_name = get_technical_name(name_to_lookup)
        return eph[technical_name]
    except (ValueError, KeyError):
        # Not a major planet, so proceed to check minor planets.
        pass

    # Next, try to load from MPCORB data
    try:
        minor_planets_df = get_mpcorb_data()
        kepler_orbit_row = minor_planets_df.loc[name_to_lookup]

        # We found it, now build the Skyfield object for it.
        kepler_orbit_obj = SimpleNamespace(**kepler_orbit_row.to_dict())
        kepler_orbit_obj.designation = kepler_orbit_row.name
        ts = get_timescale()
        sun = eph["sun"]
        minor_planet_orbit = mpc.mpcorb_orbit(kepler_orbit_obj, ts, GM_SUN_KM3_S2)
        return sun + minor_planet_orbit
    except KeyError:
        raise ValueError(
            f"Object '{planet_name}' not found in JPL ephemeris or MPCORB database."
        )
    except Exception as e:
        raise RuntimeError(f"Failed to create Skyfield object for '{planet_name}': {e}")


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




def get_reverse_translated_planet_names(language: str) -> dict:
    """
    Returns a dictionary mapping translated planet names back to their English originals.
    """
    reverse_map = {}
    with language_context(language):
        for name in SIMPLE_NAMES:
            translated_name = gettext_(name)
            reverse_map[translated_name] = name
    return reverse_map

def _get_planet_cml_iau_model(
    planet_name: str, time: Any, w0: float, wd: float
) -> float | np.ndarray:
    """
    Internal helper for planetary Central Meridian Longitude calculation using IAU models.
    W = w0 + wd * d (degrees), where d is days from J2000.0 (TT).
    Longitude increases westward.
    """
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
    Reference: 79.6° on 2026-03-18 with a drift of approx +0.8° per month.
    Supports both scalar and array Skyfield Time objects.
    """
    # Reference epoch: 2026-03-18 00:00:00 UTC
    ref_lon = 79.6
    drift_per_day = 0.8 / 30.44  # approx 0.8 degrees per month

    # Use .tt (Terrestrial Time) for precise day counting
    ts = get_timescale()
    ref_tt = ts.utc(2026, 3, 18).tt
    dt = time.tt - ref_tt

    return (ref_lon + dt * drift_per_day) % 360

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
    # Mercury, Venus, Mars, Jupiter, Saturn, Uranus, and Neptune.
    # We wrap in try-except to handle unsupported bodies like Pluto or Ceres gracefully.
    try:
        return magnitudelib.planetary_magnitude(astrometric)
    except (ValueError, TypeError, KeyError):
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


def get_moon_libration(time: Any) -> tuple[float, float] | tuple[np.ndarray, np.ndarray]:
    """
    Returns the Moon's libration in longitude and latitude in degrees.
    Uses the IAU 2015 rotation model for high precision and vectorization.
    Supports both scalar and array Skyfield Time objects.
    """
    eph = get_ephemeris()
    earth = eph["earth"]
    moon = eph["moon"]

    # Observation of Earth from Moon center (includes light-time correction)
    astrometric = cast(Any, moon).at(time).observe(earth).apparent()
    v_me = astrometric.position.au

    alpha0, delta0, W = _get_moon_orientation_elements(time)

    if hasattr(time, "shape") and time.shape:
        u_v = v_me / np.linalg.norm(v_me, axis=0)
    else:
        u_v = v_me / np.linalg.norm(v_me)

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


def get_sun_physical_details(time: Any) -> dict:
    """
    Calculates the physical details of the Sun for a given time.
    - P_degrees: Position angle of the Sun's North Pole (degrees).
    - B0_degrees: Heliographic latitude of the Earth (degrees).
    - L0_degrees: Carrington longitude of the central meridian (degrees).

    Source: Jean Meeus, Astronomical Algorithms, Chapter 29.
    """
    jd = time.tt
    # Time in Julian centuries from J2000.0
    T = (jd - 2451545.0) / 36525.0

    # Solar elements:
    # Longitude of the ascending node of the solar equator on the ecliptic (Omega)
    # Using Meeus formula (accuracy ~0.01 deg)
    omega = np.radians(73.6667 + 1.395833 * (jd - 2396758.0) / 36525.0)
    inclination = np.radians(7.25)

    # Solar Apparent Longitude (lambda) and Obliquity (epsilon) from Skyfield
    eph = get_ephemeris()
    sun = eph["sun"]
    earth = eph["earth"]
    astrometric = cast(Any, earth).at(time).observe(sun).apparent()

    # Solar Ecliptic Longitude (lambda) and Obliquity (epsilon)
    # For physical ephemeris, we need the geometric longitude, not apparent.
    # However, Meeus uses the apparent longitude corrected for aberration
    # and nutation for P, but for B0 and L0 he uses the longitude corrected
    # ONLY for aberration (mean equinox of date).
    _, lon, _ = astrometric.ecliptic_latlon()
    lam = lon.radians

    # Obliquity of the ecliptic (epsilon)
    # Simplified high-accuracy formula from Meeus
    eps = np.radians(
        23.4392911 - (46.8150 * T + 0.00059 * T**2 - 0.001813 * T**3) / 3600.0
    )

    # 1. Calculate P (Position Angle)
    # P = arctan(-cos(lam_app) * tan(eps)) + arctan(-cos(lam - omega) * tan(inclination))
    theta = lam - omega
    x = np.arctan(-np.cos(lam) * np.tan(eps))
    y = np.arctan(-np.cos(theta) * np.tan(inclination))
    p_rad = x + y

    # 2. Calculate B0 (Heliographic latitude of Earth)
    # sin(B0) = sin(lam - omega) * sin(inclination)
    sin_b0 = np.sin(theta) * np.sin(inclination)
    b0_rad = np.arcsin(sin_b0)

    # 3. Calculate L0 (Carrington longitude)
    # Correct formulas from Meeus (Chapter 29):
    # L = λ - 0.00569° - Ω
    # m = 360° - (360° / 25.38) * (JD - 2398220.0)
    # L0 = m - arctan2(sin(L) * cos(I), -cos(L))
    l_meeus = lam - omega
    l0_corr_rad = np.arctan2(np.sin(l_meeus) * np.cos(inclination), -np.cos(l_meeus))
    m_deg = 360.0 - (360.0 / 25.38) * (jd - 2398220.0)
    l0_deg = (m_deg - np.degrees(l0_corr_rad)) % 360

    return {
        "P_degrees": float(np.degrees(p_rad)),
        "B0_degrees": float(np.degrees(b0_rad)),
        "L0_degrees": float(l0_deg),
    }
