from ...utils import guess_optical_properties
from ..base.calculations import normalize_intermediate_database_entry


def normalize_guide_scope_database_entry(entry: dict) -> dict:
    """
    Normalizes a guide scope database entry by parsing vendor name, optical length, mass,
    aperture, focal length, backfocus, and mapping output connections.
    """
    entry = normalize_intermediate_database_entry(entry)
    name = entry.get("name", "Unknown")

    aperture, focal_length = guess_optical_properties(name)
    entry["aperture"] = entry.get("aperture") or aperture or 30
    entry["focal_length"] = entry.get("focal_length") or focal_length or 120

    bf_val = entry.get("bf_role") == "start"
    entry["backfocus"] = entry.get("optical_length", 0) if bf_val else None

    return entry
