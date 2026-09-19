from ...utils import (
    ConnectionType,
    Gender,
    guess_optical_properties,
    map_conn,
    map_gender,
)
from .enums import TelescopeType


def normalize_telescope_database_entry(entry: dict) -> dict:
    """
    Normalizes a telescope database entry by guessing missing aperture and focal length,
    mapping the telescope type string to TelescopeType enum, and normalizing output connections.
    """
    entry = entry.copy()
    name = entry.get("name", "")

    # Guess missing aperture and focal length if not present
    aperture = entry.get("aperture_mm") or entry.get("aperture")
    focal_length = entry.get("focal_length_mm") or entry.get("focal_length")

    if aperture is None or focal_length is None:
        g_aperture, g_focal_length = guess_optical_properties(name)
        if aperture is None and g_aperture:
            entry["aperture_mm"] = g_aperture
        if focal_length is None and g_focal_length:
            entry["focal_length_mm"] = g_focal_length

    # Map telescope type string
    type_str = entry.get("type", "")
    telescope_type = TelescopeType.REFRACTOR
    if "refractor" in type_str:
        telescope_type = TelescopeType.REFRACTOR
    elif "newtonian" in type_str:
        telescope_type = TelescopeType.NEWTONIAN_REFLECTOR
    elif "schmidt_cassegrain" in type_str or "sct" in type_str:
        telescope_type = TelescopeType.SCHMIDT_CASSEGRAIN
    elif "maksutov" in type_str:
        telescope_type = TelescopeType.MAKSUTOV_CASSEGRAIN
    elif "catadioptric" in type_str or "astrograph" in type_str:
        telescope_type = TelescopeType.CATADIOPTRIC
    entry["telescope_type"] = telescope_type

    # Map output connections
    ct = map_conn(entry.get("cside_thread"))
    cg = map_gender(entry.get("cside_gender"))

    outputs = entry.get("outputs")
    if outputs is None:
        outputs = [(ct, cg)] if ct else []
        if entry.get("t2_output", False):
            outputs.append((ConnectionType.T2, Gender.MALE))
    else:
        outputs = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in outputs
        ]
    entry["outputs"] = outputs

    return entry
