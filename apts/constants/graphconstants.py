from aenum import Enum, auto


class OpticalType(Enum):  # pyright: ignore
    OPTICAL = auto()
    INPUT = auto()
    OUTPUT = auto()
    GENERIC = auto()
    BINOCULARS = auto()


class GraphConstants:
    SPACE_ID = "Space"
    EYE_ID = "Eye"
    IMAGE_ID = "Image"

    COLORS = {
        OpticalType.GENERIC: "#FFFF00",
        OpticalType.INPUT: "#D3D3D3",
        OpticalType.OPTICAL: "#4B0082",
        OpticalType.OUTPUT: "#A9A9A9",
        OpticalType.BINOCULARS: "#00FF00",  # Green for Binoculars
    }

    DARK_COLORS = {
        OpticalType.GENERIC: "#5A1A75",  # Bright Purple
        OpticalType.INPUT: "#999999",  # Muted Light Gray
        OpticalType.OPTICAL: "#5A1A75",  # Bright Purple
        OpticalType.OUTPUT: "#BBBBBB",  # Another Muted Light Gray
        OpticalType.BINOCULARS: "#007447",  # Vibrant Green
    }

    DARK_MODE_STYLE = {
        "BACKGROUND_COLOR": "#1C1C3A",  # Deep Space Blue
        "FIGURE_FACE_COLOR": "#1C1C3A",  # Deep Space Blue
        "AXES_FACE_COLOR": "#2A004F",  # Dark Indigo variant
        "TEXT_COLOR": "#FFFFFF",  # White
        "AXIS_COLOR": "#CCCCCC",  # Light Gray
        "TICK_COLOR": "#CCCCCC",  # Light Gray
        "GRID_COLOR": "#404040",  # Subtle Dark Gray
        "SPAN_BACKGROUND_COLOR": "#2A2A4A",  # Dark blueish gray
        "GOOD_CONDITION_HL_COLOR": "#007447",  # Vibrant Green (for low alpha highlights)
        "MOON_SPAN_COLOR": "#FFFFE0",  # Light Yellow
        "ERROR_TEXT_COLOR": "#FF6B6B",  # Light red
        "WARNING_TEXT_COLOR": "#FFCC00",  # Light orange
        # AXES_EDGE_COLOR is often the same as AXIS_COLOR or TEXT_COLOR depending on theme.
        # Using AXIS_COLOR for now. If a different edge is needed, it can be added.
        "AXES_EDGE_COLOR": "#CCCCCC",  # Light Gray (same as AXIS_COLOR)
    }

    LIGHT_MODE_STYLE = {
        "BACKGROUND_COLOR": "#FFFFFF",
        "TEXT_COLOR": "#000000",
        "AXIS_COLOR": "#333333",
        "GRID_COLOR": "#D3D3D3",
        "FIGURE_FACE_COLOR": "#FFFFFF",
        "AXES_FACE_COLOR": "#F0F0F0",
        "AXES_EDGE_COLOR": "#333333",
        "TICK_COLOR": "#333333",
    }

    PLANET_COLORS_LIGHT = {
        "Mercury": "#A9A9A9",
        "Venus": "#F0E68C",
        "Mars": "#C1440E",
        "Jupiter": "#B08968",
        "Saturn": "#CEB888",
        "Uranus": "#7FC9E0",
        "Neptune": "#3B71A0",
    }

    PLANET_COLORS_DARK = {
        "Mercury": "#BEBEBE",
        "Venus": "#FFFACD",
        "Mars": "#E27B58",
        "Jupiter": "#D8A976",
        "Saturn": "#E3D6A8",
        "Uranus": "#A4D8E8",
        "Neptune": "#5B8FBF",
    }


def get_plot_colors(dark_mode_enabled: bool) -> dict:
    """
    Returns the appropriate color dictionary based on dark mode status.
    """
    if dark_mode_enabled:
        return GraphConstants.DARK_COLORS
    else:
        return GraphConstants.COLORS


def get_plot_style(dark_mode_enabled: bool) -> dict:
    """
    Returns the appropriate style dictionary based on dark mode status.
    """
    if dark_mode_enabled:
        return GraphConstants.DARK_MODE_STYLE
    else:
        return GraphConstants.LIGHT_MODE_STYLE


def get_planet_color(
    planet_name: str, dark_mode_enabled: bool, default_color: str
) -> str:
    """
    Retrieves the specific color for a planet based on the theme.
    Falls back to default_color if the planet is not found.
    """
    if dark_mode_enabled:
        colors_dict = GraphConstants.PLANET_COLORS_DARK
    else:
        colors_dict = GraphConstants.PLANET_COLORS_LIGHT
    return colors_dict.get(planet_name, default_color)
