import re
from enum import Enum
from typing import Optional


class ConnectionType(Enum):
    F_1_25 = "1.25"
    F_2 = "2"
    T2 = "T2"
    M42 = "M42"
    M48 = "M48"
    M54 = "M54"
    M56 = "M56"
    M63 = "M63"
    M68 = "M68"
    M72 = "M72"
    M81 = "M81"
    M82 = "M82"
    M84 = "M84"
    M92 = "M92"
    M117 = "M117"
    EOS = "EOS"
    CANON_RF = "Canon RF"
    NIKON_F = "Nikon F"
    NIKON_Z = "Nikon Z"
    SONY_E = "Sony E"
    FUJI_X = "Fuji X"
    MFT = "MFT"
    PENTAX_K = "Pentax K"
    CS = "CS"
    SC = "SC (Schmidt-Cassegrain)"
    ZWO_6_BOLT = "ZWO 6-bolt"
    ZWO_4_BOLT = "ZWO 4-bolt"
    QHY_4_BOLT = "QHY 4-bolt"

    def __str__(self) -> str:
        return str(self.value)


class Gender(Enum):
    MALE = "M"
    FEMALE = "F"

    def __str__(self) -> str:
        return str(self.value)


def map_conn(thread_str):
    if not thread_str:
        return ConnectionType.F_1_25  # Default
    # Try to match ConnectionType
    for ct in ConnectionType:
        if ct.value.lower() in thread_str.lower():
            return ct
    return ConnectionType.F_1_25


def map_gender(gender_str):
    if gender_str in ["Male", "M"]:
        return Gender.MALE
    if gender_str in ["Female", "F"]:
        return Gender.FEMALE
    return None


def guess_optical_properties(name: str):
    # Very simple heuristic
    aperture = None
    focal_length = None

    # Match 80ED, 100ED etc
    match = re.search(r"(\d+)ED", name)
    if match:
        aperture = float(match.group(1))

    # Match C8, C11
    match = re.search(r"C(\d+)", name)
    if match:
        inches = float(match.group(1))
        if inches < 20:  # Heuristic for SCTs
            aperture = round(inches * 25.4, 1)

    # Match 135mm f/2
    match = re.search(r"(\d+)mm", name)
    if match:
        val = float(match.group(1))
        if val > 10:
            if "f/" in name:
                focal_length = val
            else:
                aperture = val

    return aperture, focal_length
