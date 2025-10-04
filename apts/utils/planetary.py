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
    return PLANET_NAMES.get(technical_name.lower(), technical_name.capitalize())


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
import pandas as pd
from apts.cache import get_ephemeris, get_mpcorb_data, get_timescale


def get_skyfield_obj(planet_name: str):
    """
    Returns a Skyfield object for a given planet name.
    """
    eph = get_ephemeris()
    technical_name = get_technical_name(planet_name)

    minor_planet_names = {
        "ceres": "(1) Ceres",
        "haumea": "(136108) Haumea",
        "makemake": "(136472) Makemake",
        "eris": "(136199) Eris",
    }

    if technical_name in minor_planet_names:
        try:
            minor_planets_df = get_mpcorb_data()
            full_designation = minor_planet_names[technical_name]
            kepler_orbit_row = minor_planets_df.loc[full_designation]
            kepler_orbit_obj = SimpleNamespace(**kepler_orbit_row.to_dict())
            kepler_orbit_obj.designation = kepler_orbit_row.name
            ts = get_timescale()
            sun = eph['sun']
            minor_planet_orbit = mpc.mpcorb_orbit(kepler_orbit_obj, ts, GM_SUN_KM3_S2)
            return sun + minor_planet_orbit
        except KeyError:
            raise ValueError(f"Minor planet '{planet_name}' not found in MPCORB data.")
    else:
        return eph[technical_name]


def get_moon_phase(time):
    """
    Returns the moon illumination percentage for a given time.
    """
    from apts.cache import get_ephemeris
    from skyfield import almanac
    import numpy as np

    eph = get_ephemeris()
    phase_angle = almanac.moon_phase(eph, time).degrees
    illumination = (1 - np.cos(np.deg2rad(phase_angle))) / 2
    return illumination * 100
