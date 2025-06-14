from aenum import Enum, auto


class OpticalType(Enum):
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
    OpticalType.BINOCULARS: "#00FF00"  # Green for Binoculars
  }

  DARK_COLORS = {
    OpticalType.GENERIC: "#FFFFE0",  # Light Yellow
    OpticalType.INPUT: "#C0C0C0",  # Silver
    OpticalType.OPTICAL: "#BB86FC",  # Light Purple
    OpticalType.OUTPUT: "#BEBEBE",  # LightGray
    OpticalType.BINOCULARS: "#90EE90"  # Light Green
  }

  DARK_MODE_STYLE = {
    "BACKGROUND_COLOR": "#121212",
    "TEXT_COLOR": "#E0E0E0",
    "AXIS_COLOR": "#B0B0B0",
    "GRID_COLOR": "#4A4A4A",
    "FIGURE_FACE_COLOR": "#121212",
    "AXES_FACE_COLOR": "#202020",
    "AXES_EDGE_COLOR": "#B0B0B0",
    "TICK_COLOR": "#B0B0B0"
  }

  LIGHT_MODE_STYLE = {
    "BACKGROUND_COLOR": "#FFFFFF",
    "TEXT_COLOR": "#000000",
    "AXIS_COLOR": "#333333",
    "GRID_COLOR": "#D3D3D3",
    "FIGURE_FACE_COLOR": "#FFFFFF",
    "AXES_FACE_COLOR": "#F0F0F0",
    "AXES_EDGE_COLOR": "#333333",
    "TICK_COLOR": "#333333"
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
