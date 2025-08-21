PLANET_NAMES = {
    "mercury": "Mercury",
    "venus": "Venus",
    "moon": "Moon",
    "mars": "Mars",
    "jupiter barycenter": "Jupiter",
    "saturn barycenter": "Saturn",
    "uranus barycenter": "Uranus",
    "neptune barycenter": "Neptune",
    "sun": "Sun",
}

TECHNICAL_NAMES = list(PLANET_NAMES.keys())
SIMPLE_NAMES = list(PLANET_NAMES.values())

OPPOSITION_PLANETS = [
    "mars",
    "jupiter barycenter",
    "saturn barycenter",
    "uranus barycenter",
    "neptune barycenter",
]

CONJUNCTION_PLANETS = {
    "mercury": "Mercury",
    "venus": "Venus",
    "mars": "Mars",
    "jupiter barycenter": "Jupiter",
    "saturn barycenter": "Saturn",
    "uranus barycenter": "Uranus",
    "neptune barycenter": "Neptune",
}

APHELION_PERIHELION_PLANETS = [
    "mercury",
    "venus",
    "mars",
    "jupiter barycenter",
    "saturn barycenter",
    "uranus barycenter",
    "neptune barycenter",
    "moon",
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
