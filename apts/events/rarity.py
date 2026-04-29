def _get_conjunction_rarity(data: dict) -> int:
    sep = data.get("separation_degrees", 5.0)
    if sep < 0.15:
        return 5
    if sep < 0.4:
        return 4
    if sep < 1.2:
        return 3
    if sep < 2.5:
        return 2
    return 1


def _get_opposition_rarity(data: dict) -> int:
    obj = data.get("object", "")
    if obj in ["Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return 4
    return 3


def _get_meteor_shower_rarity(data: dict) -> int:
    if data.get("phase") == "Peak":
        return 4
    return 1


def _get_inferior_conjunction_rarity(data: dict) -> int:
    if data.get("is_transit"):
        return 5
    return 3


def _get_solar_eclipse_rarity(data: dict) -> int:
    kind = str(data.get("eclipse_type", "")).lower()
    if "total" in kind or "annular" in kind:
        return 5
    return 4


def _get_lunar_eclipse_rarity(data: dict) -> int:
    kind = str(data.get("eclipse_kind", "")).lower()
    if "total" in kind:
        return 5
    if "partial" in kind:
        return 4
    return 3


def _get_flyby_rarity(data: dict) -> int:
    mag = data.get("peak_magnitude", 0)
    if mag < -3:
        return 4
    if mag < -1:
        return 3
    return 1


def _get_planet_alignment_rarity(data: dict) -> int:
    planets_count = len(data.get("planets", []))
    if planets_count >= 6:
        return 5
    if planets_count == 5:
        return 4
    if planets_count == 4:
        return 3
    return 2


RARITY_HANDLERS = {
    "Moon Phase": lambda _: 1,
    "Conjunction": _get_conjunction_rarity,
    "Moon-Messier Conjunction": _get_conjunction_rarity,
    "Moon-Star Conjunction": _get_conjunction_rarity,
    "Planet-Messier Conjunction": _get_conjunction_rarity,
    "Planet-Star Conjunction": _get_conjunction_rarity,
    "Opposition": _get_opposition_rarity,
    "Meteor Shower": _get_meteor_shower_rarity,
    "Planet Altitude": lambda _: 3,
    "Lunar Occultation": lambda _: 4,
    "Lunar Planetary Occultation": lambda _: 4,
    "Aphelion/Perihelion": lambda _: 1,
    "Moon Apogee/Perigee": lambda _: 1,
    "Inferior Conjunction": _get_inferior_conjunction_rarity,
    "Solar Eclipse": _get_solar_eclipse_rarity,
    "Lunar Eclipse": _get_lunar_eclipse_rarity,
    "Space Launch": lambda _: 2,
    "Space Event": lambda _: 2,
    "ISS Flyby": _get_flyby_rarity,
    "Tiangong Flyby": _get_flyby_rarity,
    "Comet": lambda _: 5,
    "Planet Alignment": _get_planet_alignment_rarity,
    "Greatest Elongation": lambda _: 3,
    "Season": lambda _: 2,
    "Messier Culmination": lambda _: 2,
    "Jovian Moon Event": lambda _: 1,
    "Jovian Mutual Occultation": lambda _: 5,
    "Jovian Mutual Eclipse": lambda _: 5,
    "Jupiter GRS Transit": lambda _: 1,
    "Planet Stationary Point": lambda _: 3,
    "Planet Solar Conjunction": lambda _: 3,
    "Lunar Feature": lambda _: 4,
    "Moon Libration Maximum": lambda _: 3,
    "Planet-Planet Occultation": lambda _: 5,
    "Venus Greatest Brilliancy": lambda _: 4,
    "Supermoon": lambda _: 3,
    "Planetary Dichotomy": lambda _: 3,
    "Mars Closest Approach": lambda _: 4,
}


def get_rarity(event_type: str, data: dict) -> int:
    handler = RARITY_HANDLERS.get(event_type)
    if handler:
        return handler(data)
    return 1
