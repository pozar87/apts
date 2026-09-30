def normalize_smart_telescope_database_entry(entry: dict) -> dict:
    """
    Normalizes a smart telescope database entry by creating a shallow copy
    and filling default fields.
    """
    entry = entry.copy()
    entry.setdefault("brand", "Unknown")
    entry.setdefault("name", "Unknown")
    entry.setdefault("mass", 0)
    return entry
