from aenum import Enum, auto


class OpticalType(Enum):
  OPTICAL = auto()
  INPUT = auto()
  OUTPUT = auto()
  GENERIC = auto()


class GraphConstants:
  SPACE_ID = "Space"
  EYE_ID = "Eye"
  IMAGE_ID = "Image"

  COLORS = {
    OpticalType.GENERIC: "#FFFF00",
    OpticalType.INPUT: "#D3D3D3",
    OpticalType.OPTICAL: "#4B0082",
    OpticalType.OUTPUT: "#A9A9A9"
  }
