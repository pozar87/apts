import logging
from typing import TYPE_CHECKING
from importlib import resources
from unittest.mock import MagicMock

import matplotlib.font_manager as font_manager

if TYPE_CHECKING:
    from ...place import Place

logger = logging.getLogger(__name__)

MOON_FONT = font_manager.FontProperties(
    fname=str(resources.files("apts").joinpath("data/moon_phases.ttf")), size=50
)

def add_marker(ax, label, position, text_color, grid_color):
    """Adds a vertical marker with a label to the plot."""
    ax.axvline(position, color=grid_color, linestyle="--", linewidth=1)
    ax.text(
        position,
        1,
        label,
        weight="bold",
        horizontalalignment="center",
        color=text_color,
    )

def is_southern_hemisphere(place: "Place") -> bool:
    """Checks if the place is in the southern hemisphere, handling mocks."""
    try:
        if hasattr(place, "lat_decimal") and not isinstance(place.lat_decimal, MagicMock):
            if place.lat_decimal < 0:
                return True
    except Exception:
        pass
    return False

def setup_cardinal_markers(ax, is_southern, style):
    """Sets up cardinal direction markers and x-axis limits based on hemisphere."""
    if is_southern:  # Southern Hemisphere
        add_marker(ax, "W", -90, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "N", 0, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "E", 90, style["TEXT_COLOR"], style["GRID_COLOR"])
        ax.set_xlim(135, -135)  # Inverted for South-up view, SE to SW
    else:  # Northern Hemisphere
        add_marker(ax, "E", 90, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "S", 180, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "W", 270, style["TEXT_COLOR"], style["GRID_COLOR"])
        ax.set_xlim(45, 315)
