from .calculations.evaluations import (
    RARITY_HANDLERS,
    _get_conjunction_rarity,
    _get_flyby_rarity,
    _get_inferior_conjunction_rarity,
    _get_lunar_eclipse_rarity,
    _get_meteor_shower_rarity,
    _get_opposition_rarity,
    _get_planet_alignment_rarity,
    _get_solar_eclipse_rarity,
    calculate_event_rarity,
)


def get_rarity(event_type: str, data: dict) -> int:
    """
    Delegates rarity calculation to the pure calculation engine in evaluations.py.
    Maintained for full backward compatibility.
    """
    return calculate_event_rarity(event_type, data)


__all__ = [
    "get_rarity",
    "calculate_event_rarity",
    "RARITY_HANDLERS",
    "_get_conjunction_rarity",
    "_get_opposition_rarity",
    "_get_meteor_shower_rarity",
    "_get_inferior_conjunction_rarity",
    "_get_solar_eclipse_rarity",
    "_get_lunar_eclipse_rarity",
    "_get_flyby_rarity",
    "_get_planet_alignment_rarity",
]
