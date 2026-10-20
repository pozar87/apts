from ..base.calculations import normalize_intermediate_database_entry


def normalize_adapter_database_entry(entry: dict) -> dict:
    """
    Normalizes an adapter or spacer database entry by constructing vendor, setting default mass and optical_length,
    and mapping input and output connection configurations.
    """
    normalized = normalize_intermediate_database_entry(entry)
    if "vendor" in entry:
        normalized["vendor"] = entry["vendor"]
    return normalized
