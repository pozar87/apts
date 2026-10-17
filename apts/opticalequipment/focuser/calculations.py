from ..base.calculations import normalize_intermediate_database_entry


def normalize_focuser_database_entry(entry: dict) -> dict:
    """
    Normalizes a focuser database entry using standard intermediate equipment normalization.
    """
    brand = entry.get("brand")
    name = entry.get("name")
    vendor = entry.get("vendor")

    norm_entry = normalize_intermediate_database_entry(entry)

    if vendor is not None:
        norm_entry["vendor"] = vendor
    elif brand or name:
        norm_entry["vendor"] = f"{brand or ''} {name or ''}".strip()

    if brand is not None:
        norm_entry["brand"] = brand
    if name is not None:
        norm_entry["name"] = name

    return norm_entry
