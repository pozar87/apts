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
    OpticalType.GENERIC: '#5A1A75',      # Bright Purple
    OpticalType.INPUT: '#999999',        # Muted Light Gray
    OpticalType.OPTICAL: '#5A1A75',      # Bright Purple
    OpticalType.OUTPUT: '#BBBBBB',       # Another Muted Light Gray
    OpticalType.BINOCULARS: '#007447'    # Vibrant Green
  }

  DARK_MODE_STYLE = {
    'BACKGROUND_COLOR': '#1C1C3A',      # Deep Space Blue
    'FIGURE_FACE_COLOR': '#1C1C3A',     # Deep Space Blue
    'AXES_FACE_COLOR': '#2A004F',       # Dark Indigo variant
    'TEXT_COLOR': '#FFFFFF',            # White
    'AXIS_COLOR': '#CCCCCC',            # Light Gray
    'TICK_COLOR': '#CCCCCC',            # Light Gray
    'GRID_COLOR': '#404040',            # Subtle Dark Gray
    'SPAN_BACKGROUND_COLOR': '#FFFFFF', # White (for low alpha spans)
    'GOOD_CONDITION_HL_COLOR': '#007447',# Vibrant Green (for low alpha highlights)
    'MOON_SPAN_COLOR': '#5A1A75',       # Bright Purple (for low alpha moon spans)
    'ERROR_TEXT_COLOR': '#FF6B6B',      # Light red
    'WARNING_TEXT_COLOR': '#FFCC00',    # Light orange
    # AXES_EDGE_COLOR is often the same as AXIS_COLOR or TEXT_COLOR depending on theme.
    # Using AXIS_COLOR for now. If a different edge is needed, it can be added.
    'AXES_EDGE_COLOR': '#CCCCCC'        # Light Gray (same as AXIS_COLOR)
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
