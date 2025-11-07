import re


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


from skyfield.data import mpc
from skyfield.constants import GM_SUN_Pitjeva_2005_km3_s2 as GM_SUN_KM3_S2
from types import SimpleNamespace
from apts.cache import get_ephemeris, get_mpcorb_data, get_timescale


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


def get_moon_illumination(time):
    """
    Returns the moon illumination percentage and waxing/waning status for a given time.
    """
    from apts.cache import get_ephemeris
    from skyfield import almanac
    import numpy as np

    eph = get_ephemeris()
    moon = eph['moon']
    sun = eph['sun']

    # Get the phase angle
    phase_angle = almanac.moon_phase(eph, time).degrees

    # Determine if waxing or waning
    is_waxing = 0 < phase_angle < 180


    illumination = (1 - np.cos(np.deg2rad(phase_angle))) / 2
    return illumination * 100, is_waxing


def get_moon_phase(time):
    """
    Returns the moon illumination percentage for a given time.
    """
    illumination, _ = get_moon_phase_details(time)
    return illumination
