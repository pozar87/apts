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
