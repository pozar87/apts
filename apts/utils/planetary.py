import ephem
import re
from datetime import timedelta

import numpy as np
from types import SimpleNamespace
from typing import Any, cast

import ephem
from skyfield.data import mpc
from skyfield.constants import GM_SUN_Pitjeva_2005_km3_s2 as GM_SUN_KM3_S2
from skyfield import almanac

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
    "moon",
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


def get_planet_distance_km(planet_name: str, time: Any) -> float:
    """
    Returns the geocentric distance to the planet in km.
    """
    eph = get_ephemeris()
    earth = eph["earth"]
    planet_obj = get_skyfield_obj(planet_name)
    return cast(Any, earth).at(time).observe(planet_obj).distance().km


def get_planet_angular_diameter(planet_name: str, time: Any) -> float:
    """
    Returns the apparent angular diameter of the planet in arcseconds.
    Formula: diameter = 2 * arcsin(Radius / Distance)
    """
    radius = get_planet_radius_km(planet_name)
    distance = get_planet_distance_km(planet_name, time)

    # Angular diameter in radians
    # Using arcsin(R/D) gives the angular radius, so multiply by 2 for diameter.
    alpha_rad = 2 * np.arcsin(radius / distance)

    # Convert to arcseconds
    return float(np.degrees(alpha_rad) * 3600.0)


def get_saturn_pole(time: Any) -> tuple[float, float]:
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
    astrometric = cast(Any, earth).at(time).observe(saturn)
    # Unit vector from Saturn to Earth
    v_sat_earth = -astrometric.position.au / astrometric.distance().au

    # Saturn's pole in J2000.0
    alpha_p_deg, delta_p_deg = get_saturn_pole(time)
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
    sin_B = np.dot(p, v_sat_earth)
    B_rad = np.arcsin(np.clip(sin_B, -1.0, 1.0))
    B_deg = float(np.degrees(B_rad))

    # Major axis (outer edge of A ring)
    dist_km = astrometric.distance().km
    radius_km = astronomy.SATURN_RING_OUTER_RADIUS_KM
    major_arcsec = float(2 * np.degrees(np.arcsin(radius_km / dist_km)) * 3600.0)

    # Minor axis
    minor_arcsec = major_arcsec * abs(np.sin(B_rad))

    return {
        "tilt_degrees": B_deg,
        "major_axis_arcsec": major_arcsec,
        "minor_axis_arcsec": minor_arcsec,
    }


def get_planet_fraction_illuminated(planet_name: str, time: Any) -> float:
    """
    Returns the illuminated fraction of a planet (0.0 to 1.0) for a given time.
    Uses the phase angle 'i' between the Sun and Earth as seen from the planet.
    Formula: k = (1 + cos(i)) / 2
    """
    eph = get_ephemeris()
    sun = eph["sun"]
    earth = eph["earth"]
    planet_obj = get_skyfield_obj(planet_name)

    # Position of the planet as seen from Earth
    astrometric = cast(Any, earth).at(time).observe(planet_obj)
    # Phase angle: angle Sun-Planet-Earth
    i_rad = astrometric.phase_angle(sun).radians

    return float((1 + np.cos(i_rad)) / 2)


def get_jupiter_system_ii_longitude(time: Any) -> float:
    """
    Returns Jupiter's Central Meridian Longitude (System II) in degrees.
    Uses ephem for calculation.
    """
    j = ephem.Jupiter()
    j.compute(time.utc_datetime())
    # ephem returns longitude in radians, convert to degrees
    return float(np.degrees(j.cmlII))


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

def get_jupiter_system_ii_longitude(t):
    """
    Calculates the System II central meridian longitude of Jupiter.
    Uses ephem (PyEphem) for calculation.
    """
    jup = ephem.Jupiter()
    # Convert Skyfield Time to PyEphem date (UTC)
    jup.compute(t.utc_datetime())
    return float(jup.cmlII) * 180.0 / np.pi
