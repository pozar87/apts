from ...utils import guess_optical_properties
from ..base.calculations import normalize_intermediate_database_entry


def normalize_guide_scope_database_entry(entry: dict) -> dict:
    """
    Normalizes a guide scope database entry by delegating intermediate database entry normalization
    to normalize_intermediate_database_entry, guessing missing aperture and focal length,
    and setting backfocus based on bf_role.
    """
    entry = normalize_intermediate_database_entry(entry)
    name = entry.get("name", "")

    aperture, focal_length = guess_optical_properties(name)
    entry["aperture"] = aperture or 30
    entry["focal_length"] = focal_length or 120

    bf_val = entry.get("bf_role") == "start"
    entry["backfocus"] = entry["optical_length"] if bf_val else None

    return entry
