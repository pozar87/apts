import re
from ...utils import extract_number, map_conn, map_gender


def normalize_eyepiece_database_entry(entry: dict) -> dict:
    """
    Normalizes an eyepiece database entry by extracting missing focal length and
    field of view parameters from the entry name using regex and mapping input connection formats.
    """
    entry = entry.copy()
    name = entry.get("name", "")
    if "focal_length_mm" not in entry and "focal_length" not in entry:
        focal_length = extract_number(name)
        if focal_length:
            entry["focal_length_mm"] = focal_length
    if "field_of_view_deg" not in entry and "field_of_view" not in entry:
        match = re.search(r"(\d+)°", name) or re.search(r"(\d+)\s*deg", name)
        if match:
            entry["field_of_view_deg"] = float(match.group(1))

    inputs = entry.get("inputs")
    if inputs is None:
        tt = map_conn(entry.get("tside_thread"))
        tg = map_gender(entry.get("tside_gender"))
        entry["inputs"] = [(tt, tg)] if tt else []
    else:
        entry["inputs"] = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in inputs
        ]

    return entry
