from datetime import datetime
from typing import Optional


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
    "Culmination": lambda _: 2,
    "Messier Culmination": lambda _: 2,
    "Golden Hour": lambda _: 1,
    "Blue Hour": lambda _: 1,
    "Jovian Moon Event": lambda _: 1,
    "Jovian Mutual Occultation": lambda _: 5,
    "Jovian Mutual Eclipse": lambda _: 5,
    "Jupiter GRS Transit": lambda _: 1,
    "Saturn Ring Crossing": lambda _: 5,
    "Planet Stationary Point": lambda _: 3,
    "Planet Solar Conjunction": lambda _: 3,
    "Lunar Feature": lambda _: 4,
    "Moon Libration Maximum": lambda _: 1,
    "Planet-Planet Occultation": lambda _: 5,
    "Venus Greatest Brilliancy": lambda _: 4,
    "Supermoon": lambda _: 3,
    "Planetary Dichotomy": lambda _: 3,
    "Mars Closest Approach": lambda _: 4,
}


def calculate_event_rarity(event_type: str, data: dict) -> int:
    """
    Calculates the rarity level (1-5) for an astronomical event based on its type and properties.
    """
    handler = RARITY_HANDLERS.get(event_type)
    if handler:
        return handler(data)
    return 1


# Alias for backward compatibility
get_rarity = calculate_event_rarity


def _get_time_diff_seconds(
    t1: Optional[datetime], t2: Optional[datetime]
) -> Optional[int]:
    if t1 and t2:
        return int(abs((t1 - t2).total_seconds()))
    return None


def calculate_event_duration(event_type: str, data: dict) -> int:
    """
    Calculates the duration of an astronomical event in seconds.
    Prioritizes dynamic calculation if time bounds are available in the data.
    """
    # 1. Dynamic calculation if time bounds are present
    # Flybys
    if event_type in ["ISS Flyby", "Tiangong Flyby"]:
        duration = _get_time_diff_seconds(data.get("rise_time"), data.get("set_time"))
        if duration:
            return duration

    # Occultations
    if "Occultation" in event_type:
        duration = _get_time_diff_seconds(
            data.get("ingress_time"), data.get("egress_time")
        )
        if duration:
            return duration

    # 2. Defaults based on astronomical relevance
    # Fast events (seconds to hours)
    duration_map = {
        "ISS Flyby": 600,  # 10 minutes
        "Tiangong Flyby": 600,  # 10 minutes
        "Lunar Occultation": 3600,  # 1 hour
        "Lunar Planetary Occultation": 3600,
        "Planet-Planet Occultation": 3600,
        "Solar Eclipse": 7200,  # 2 hours
        "Lunar Eclipse": 14400,  # 4 hours
        "Jovian Moon Event": 7200,  # 2 hours (Transit, Shadow, etc.)
        "Jovian Mutual Occultation": 1800,  # 30 minutes
        "Jovian Mutual Eclipse": 1800,
        "Jupiter GRS Transit": 7200,  # 2 hours
        "Golden Hour": 3600,  # 1 hour
        "Blue Hour": 3600,  # 1 hour
        "Culmination": 3600,  # 1 hour
        "Messier Culmination": 3600,
        "Space Launch": 600,  # 10 minutes
        "Space Event": 3600,  # 1 hour
    }

    if event_type in duration_map:
        return duration_map[event_type]

    # Slow events (days)
    # Default for conjunctions and other slow-moving events is 2 days (172800s)
    if "Conjunction" in event_type or event_type == "Planet Solar Conjunction":
        return 172800

    # Default for oppositions and closest approach is 3 days (259200s)
    if event_type in ["Opposition", "Mars Closest Approach"]:
        return 259200

    # Standard default for most other events (Moon phases, seasons, elongations, etc.) is 1 day
    return 86400


# Alias for backward compatibility
get_duration = calculate_event_duration
