import re
from functools import lru_cache
from types import SimpleNamespace
from skyfield.data import mpc
from skyfield.constants import GM_SUN_Pitjeva_2005_km3_s2 as GM_SUN_KM3_S2

from apts.cache import get_ephemeris, get_mpcorb_data, get_timescale
from apts.i18n import language_context, gettext_

from .constants import PLANET_NAMES, MINOR_PLANET_NAMES, SIMPLE_NAMES


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


@lru_cache(maxsize=8)
def get_reverse_translated_planet_names(language: str) -> dict:
    """
    Returns a dictionary mapping translated planet names back to their English originals.
    Optimization: cached to avoid repeatedly building the same dictionary and calling gettext_ repeatedly.
    """
    reverse_map = {}
    with language_context(language):
        for name in SIMPLE_NAMES:
            translated_name = gettext_(name)
            reverse_map[translated_name] = name
    return reverse_map
