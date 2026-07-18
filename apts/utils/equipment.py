import re
from enum import Enum


class ConnectionType(Enum):
    F_1_25 = "1.25"
    F_2 = "2"
    T2 = "T2"
    M42 = "M42"
    M48 = "M48"
    M54 = "M54"
    M56 = "M56"
    M60 = "M60"
    M63 = "M63"
    M68 = "M68"
    M72 = "M72"
    M81 = "M81"
    M82 = "M82"
    M84 = "M84"
    M90 = "M90"
    M92 = "M92"
    M117 = "M117"
    M28_5 = "M28.5"
    EOS = "EOS"
    EOS_M = "EOS M"
    EOS_R = "EOS R"
    CANON_RF = "Canon RF"
    NIKON_F = "Nikon F"
    NIKON_Z = "Nikon Z"
    SONY_A = "Sony A"
    SONY_E = "Sony E"
    FUJI_X = "Fuji X"
    MFT = "MFT"
    PENTAX_K = "Pentax K"
    CS = "CS"
    SC = "SC (Schmidt-Cassegrain)"
    NX4 = "1.375\"-24"
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


# Pre-sorted connection types for efficient matching in map_conn
# Sorted by length of value descending to avoid partial matches (e.g., "T2" matching "2" before "T2")
_SORTED_CONNECTION_TYPES = sorted(
    ConnectionType, key=lambda ct: len(str(ct.value)), reverse=True
)


def map_conn(thread_str):
    if not thread_str:
        return ConnectionType.F_1_25  # Default
    # Try to match ConnectionType
    for ct in _SORTED_CONNECTION_TYPES:
        if ct.value.lower() in thread_str.lower():
            return ct
    return ConnectionType.F_1_25


def map_gender(gender_str):
    if gender_str in ["Male", "M"]:
        return Gender.MALE
    if gender_str in ["Female", "F"]:
        return Gender.FEMALE
    return None


def get_default_gender(connection_type, is_input):
    """
    Get the default gender for a connection type based on common astronomical conventions.
    - Push-fit (1.25", 2"): Input is Male (barrel), Output is Female (receiver).
    - Threaded (T2, M42, M48, etc.): Input is Female, Output is Male.
    """
    if connection_type in (ConnectionType.F_1_25, ConnectionType.F_2):
        return Gender.MALE if is_input else Gender.FEMALE
    return Gender.FEMALE if is_input else Gender.MALE


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
