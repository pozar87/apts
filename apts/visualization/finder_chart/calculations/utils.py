import logging
from typing import TYPE_CHECKING

import numpy as np

from ..constants import COMPASS_POINTS, LONG_EVENT_CATEGORIES

if TYPE_CHECKING:
    from apts.events.event import Event

logger = logging.getLogger(__name__)


def _get_compass_labels(az_min: float, az_max: float) -> list[tuple[float, str]]:
    """Returns compass direction labels that fall within the given azimuth window."""
    labels = []
    for deg, code in COMPASS_POINTS:
        d = deg
        if d < az_min and d + 360.0 <= az_max:
            d += 360.0
        elif d > az_max and d - 360.0 >= az_min:
            d -= 360.0

        if az_min <= d <= az_max:
            labels.append((d, code))

    return labels


def _get_event_moon_phase_frac(event_obj: "Event") -> float:
    """Helper to determine float phase fraction (0.0-1.0) for Moon rendering."""
    p_val = getattr(event_obj, "extra_data", {}).get("phase")
    if isinstance(p_val, (int, float)):
        if float(p_val) > 1.0:
            return (float(p_val) % 360.0) / 360.0
        return float(p_val)

    title_lower = f"{event_obj.title} {event_obj.category} {p_val}".lower()
    if (
        "first quarter" in title_lower
        or "pierwsza kwadra" in title_lower
        or "cuarto creciente" in title_lower
        or "erstes viertel" in title_lower
        or "primeiro quarto" in title_lower
    ):
        return 0.25
    if (
        "third quarter" in title_lower
        or "last quarter" in title_lower
        or "trzecia kwadra" in title_lower
        or "ostatnia kwadra" in title_lower
        or "cuarto menguante" in title_lower
        or "drittes viertel" in title_lower
        or "quarto minguante" in title_lower
    ):
        return 0.75
    if (
        "full moon" in title_lower
        or "pełnia" in title_lower
        or "luna llena" in title_lower
        or "vollmond" in title_lower
        or "lua cheia" in title_lower
    ):
        return 0.5
    if (
        "new moon" in title_lower
        or "nów" in title_lower
        or "luna nueva" in title_lower
        or "neumond" in title_lower
        or "lua nova" in title_lower
    ):
        return 0.0

    return 0.25


def _parse_separation_deg(sep_str: str | None) -> float:
    """Parses angular separation degrees from string representation."""
    if not sep_str:
        return 1.2
    try:
        clean_sep = sep_str.replace("°", "").replace("'", "").strip()
        val = float(clean_sep)
        if "'" in sep_str:
            val = val / 60.0
        return max(0.2, min(5.0, val))
    except ValueError:
        return 1.2


def _hex_to_rgb(hex_str: str) -> np.ndarray:
    clean = hex_str.lstrip("#")
    return np.array([int(clean[i : i + 2], 16) / 255.0 for i in (0, 2, 4)])


def is_long_event(category: str, title: str = "") -> bool:
    """Checks if an event category or title represents a multi-hour / long-duration event."""
    cat = str(category).upper()
    title_lower = str(title).lower()
    if cat in LONG_EVENT_CATEGORIES:
        return True
    long_keywords = [
        "conjunction",
        "alignment",
        "opposition",
        "elongation",
        "phase",
        "shower",
        "solstice",
        "equinox",
    ]
    return any(kw in title_lower for kw in long_keywords)


def _get_satellite_name(event_obj: "Event") -> str:
    """Helper to derive clean satellite name (ISS, Tiangong, etc.) without generic fallback."""
    if event_obj.objects:
        obj_name = str(event_obj.objects[0])
        if obj_name and obj_name.lower() != "target":
            return obj_name

    title_lower = str(event_obj.title).lower()
    cat_lower = str(event_obj.category).lower()

    if "tiangong" in title_lower or "tiangong" in cat_lower or "css" in title_lower:
        return "Tiangong"
    if "iss" in title_lower or "iss" in cat_lower or "station" in title_lower:
        return "ISS"

    return "Satellite"
