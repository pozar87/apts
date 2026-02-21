from typing import Optional

from aenum import Enum, auto


class OpticalType(Enum):  # pyright: ignore
    OPTICAL = auto()
    INPUT = auto()
    OUTPUT = auto()
    GENERIC = auto()
    BINOCULARS = auto()
    VISUAL = auto()
    IMAGE = auto()
    REDUCER = auto()
    FLATTENER = auto()
    CORRECTOR = auto()
    FILTER_WHEEL = auto()
    FILTER_HOLDER = auto()
    OAG = auto()
    ROTATOR = auto()
    FOCUSER = auto()
    ADAPTER = auto()
    SPACER = auto()
    ANTI_TILT = auto()
    FLIP_MIRROR = auto()
    GUIDE_SCOPE = auto()


class GraphConstants:
    SPACE_ID = "Space"
    EYE_ID = "Visual"
    IMAGE_ID = "Image"

    COLORS = {
        OpticalType.GENERIC: "#FFFF00",
        OpticalType.INPUT: "#D3D3D3",
        OpticalType.OPTICAL: "#4B0082",
        OpticalType.OUTPUT: "#A9A9A9",
        OpticalType.BINOCULARS: "#00FF00",  # Green for Binoculars
        OpticalType.VISUAL: "#90EE90", # Light Green for Visual
        OpticalType.IMAGE: "#ADD8E6", # Light Blue for Image
    }

    DARK_COLORS = {
        OpticalType.GENERIC: "#5A1A75",  # Bright Purple
        OpticalType.INPUT: "#999999",  # Muted Light Gray
        OpticalType.OPTICAL: "#5A1A75",  # Bright Purple
        OpticalType.OUTPUT: "#BBBBBB",  # Another Muted Light Gray
        OpticalType.BINOCULARS: "#007447",  # Vibrant Green
        OpticalType.VISUAL: "#3CB371", # Medium Sea Green for Visual
        OpticalType.IMAGE: "#4682B4", # Steel Blue for Image
    }

    DARK_MODE_STYLE = {
        "BACKGROUND_COLOR": "#1C1C3A",  # Deep Space Blue
        "FIGURE_FACE_COLOR": "#1C1C3A",  # Deep Space Blue
        "AXES_FACE_COLOR": "#14142B",  # Darker Indigo variant
        "TEXT_COLOR": "#FFFFFF",  # White
        "AXIS_COLOR": "#CCCCCC",  # Light Gray
        "TICK_COLOR": "#CCCCCC",  # Light Gray
        "GRID_COLOR": "#404040",  # Subtle Dark Gray
        "SPAN_BACKGROUND_COLOR": "#050510",  # Very dark night
        "DAY_SPAN_COLOR": "#FFD700",  # Gold for Day
        "GOOD_CONDITION_HL_COLOR": "#00FF7F",  # Spring Green (for low alpha highlights)
        "MOON_SPAN_COLOR": "#4A90E2",  # Bright Sky Blue for Moon
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
        "AXES_FACE_COLOR": "#F5F5F5",
        "AXES_EDGE_COLOR": "#333333",
        "TICK_COLOR": "#333333",
        "SPAN_BACKGROUND_COLOR": "#BDBDBD",  # Darker Gray for Night
        "DAY_SPAN_COLOR": "#FFF59D",  # More vivid Yellow for Day
        "MOON_SPAN_COLOR": "#BBDEFB",  # Light Blue for Moon Presence
        "GOOD_CONDITION_HL_COLOR": "#90EE90",
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

    MESSIER_COLORS_LIGHT = {
        "Spiral Galaxy": "#6A1B9A",     # Deep Purple
        "Elliptical Galaxy": "#8E24AA", # Purple
        "Irregular Galaxy": "#9C27B0",  # Light Purple
        "Lenticular (S0) Galaxy": "#AB47BC", # Lighter Purple
        "Galaxy": "#6A1B9A",            # Fallback for Galaxy
        "Globular Cluster": "#F9A825",  # Dark Yellow/Gold
        "Open Cluster": "#1565C0",      # Dark Blue
        "Diffuse Nebula": "#C62828",    # Dark Red
        "Nebula": "#C62828",            # Fallback for Nebula
        "Planetary Nebula": "#00695C",  # Dark Teal
        "Supernova Remnant": "#D84315", # Dark Orange
        "Double Star": "#795548",       # Brown
        "Group/Asterism": "#0277BD",    # Light Blue
        "Star Cloud": "#EF6C00",        # Orange
        "Other": "#616161",             # Gray
    }

    MESSIER_COLORS_DARK = {
        "Spiral Galaxy": "#A569BD",     # Purple
        "Elliptical Galaxy": "#AF7AC5", # Soft Purple
        "Irregular Galaxy": "#C39BD3",  # Lavender
        "Lenticular (S0) Galaxy": "#D2B4DE", # Light Lavender
        "Galaxy": "#A569BD",            # Fallback for Galaxy
        "Globular Cluster": "#F4D03F",  # Yellow
        "Open Cluster": "#5DADE2",      # Blue
        "Diffuse Nebula": "#EC7063",    # Red
        "Nebula": "#EC7063",            # Fallback for Nebula
        "Planetary Nebula": "#48C9B0",  # Turquoise
        "Supernova Remnant": "#EB984E", # Orange
        "Double Star": "#F7DC6F",       # Light Yellow
        "Group/Asterism": "#85C1E9",    # Light Blue
        "Star Cloud": "#F8C471",        # Light Orange
        "Other": "#ABB2B9",             # Gray
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


def get_messier_color(
    messier_type: str, dark_mode_enabled: bool, default_color: Optional[str] = None
) -> str:
    """
    Retrieves the specific color for a Messier object type based on the theme.
    Handles translated messier_type by matching against translated technical names.
    """
    from apts.i18n import gettext_

    if dark_mode_enabled:
        colors_dict = GraphConstants.MESSIER_COLORS_DARK
    else:
        colors_dict = GraphConstants.MESSIER_COLORS_LIGHT

    if default_color is None:
        default_color = colors_dict["Other"]

    # Iterate through technical names, translate them and check for match
    for tech_name, color in colors_dict.items():
        if gettext_(tech_name) == messier_type:
            return color

    # Special case for "Galaxy" and "Nebula" if they are part of the translated string
    # but not an exact match (e.g. "Spiral Galaxy" matching "Galaxy" if "Spiral Galaxy" was missing)
    # However, we have specific entries for most types now.
    if gettext_("Galaxy") in messier_type:
        return colors_dict["Galaxy"]
    if gettext_("Nebula") in messier_type:
        return colors_dict["Nebula"]

    return default_color

# Translatable object types for Babel
def _(text):
    return text


_TRANSLATABLE_STRINGS = [
    _("Spiral Galaxy"),
    _("Elliptical Galaxy"),
    _("Irregular Galaxy"),
    _("Lenticular (S0) Galaxy"),
    _("Galaxy"),
    _("Globular Cluster"),
    _("Open Cluster"),
    _("Diffuse Nebula"),
    _("Nebula"),
    _("Planetary Nebula"),
    _("Supernova Remnant"),
    _("Double Star"),
    _("Group/Asterism"),
    _("Star Cloud"),
    _("Other"),
    _("New Moon"),
    _("First Quarter"),
    _("Full Moon"),
    _("Last Quarter"),
    _("Space Launch"),
    _("Space Event"),
    _("Solar Eclipse"),
    _("Lunar Eclipse"),
    _("Moon Phase"),
    _("Conjunction"),
    _("Opposition"),
    _("Meteor Shower"),
    _("Highest altitude"),
    _("Planet Altitude"),
    _("NPF Rule (s)"),
    _("Rule of 500 (s)"),
    _("Lunar Occultation"),
    _("Aphelion/Perihelion"),
    _("Moon Apogee/Perigee"),
    _("Inferior Conjunction"),
    _("Mercury Transit"),
    _("Moon-Messier Conjunction"),
    _("Comet"),
    _("Mercury"),
    _("Venus"),
    _("Mars"),
    _("Jupiter"),
    _("Saturn"),
    _("Uranus"),
    _("Neptune"),
    _("Pluto"),
    _("Sun"),
    _("Moon"),
    _("Start"),
    _("Peak"),
    _("End"),
    _("Quadrantids"),
    _("Lyrids"),
    _("Eta Aquarids"),
    _("Delta Aquarids"),
    _("Perseids"),
    _("Orionids"),
    _("Leonids"),
    _("Geminids"),
    _("Ursids"),
    _("Ceres"),
    _("Haumea"),
    _("Makemake"),
    _("Eris"),
]
