from enum import Enum, auto


class DSOType(Enum):
    EN = auto()  # Emission Nebula
    PN = auto()  # Planetary Nebula
    GC = auto()  # Globular Cluster
    GX = auto()  # Galaxy
    RN = auto()  # Reflection Nebula
    OC = auto()  # Open Cluster
    DN = auto()  # Diffuse Nebula (often EN or RN)
    SNR = auto()  # Supernova Remnant
    DS = auto()  # Double Star
    AST = auto()  # Asterism
    SC = auto()  # Star Cloud
    OTHER = auto()


class FilterStrategy(Enum):
    BROADBAND = auto()
    NARROWBAND = auto()
