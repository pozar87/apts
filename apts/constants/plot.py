from aenum import Enum


class CoordinateSystem(str, Enum):  # pyright: ignore
    HORIZONTAL = "Horizontal"
    EQUATORIAL = "Equatorial"
