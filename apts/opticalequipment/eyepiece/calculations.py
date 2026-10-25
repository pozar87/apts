import re

from ...utils import extract_number
from ..base.calculations import normalize_intermediate_database_entry


def normalize_eyepiece_database_entry(entry: dict) -> dict:
    """
    Normalizes an eyepiece database entry by extracting missing focal length and
    field of view parameters from the entry name using regex and delegating intermediate
    entry normalization logic.
    """
    brand = entry.get("brand", "")
    name = entry.get("name", "")

    norm_entry = normalize_intermediate_database_entry(entry)

    if "vendor" not in entry:
        norm_entry["vendor"] = (
            f"{brand} {name}".strip() if (brand or name) else "unknown ocular"
        )

    if "focal_length_mm" not in norm_entry and "focal_length" not in norm_entry:
        focal_length = extract_number(name)
        if focal_length:
            norm_entry["focal_length_mm"] = focal_length

    if "field_of_view_deg" not in norm_entry and "field_of_view" not in norm_entry:
        match = re.search(r"(\d+)°", name) or re.search(r"(\d+)\s*deg", name)
        if match:
            norm_entry["field_of_view_deg"] = float(match.group(1))

    return norm_entry
