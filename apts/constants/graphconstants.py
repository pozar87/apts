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
    OpticalType.OPTICAL: "#4B0082",
    OpticalType.INPUT: "#D3D3D3",
    OpticalType.OUTPUT: "#A9A9A9",
    OpticalType.GENERIC: "yellow"
  }