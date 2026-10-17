from ..base.calculations import normalize_intermediate_database_entry


def normalize_oag_database_entry(entry: dict) -> dict:
    """
    Normalizes database dictionary entries for an Off-Axis Guider (OAG) into standard fields
    using intermediate equipment normalization.
    """
    brand = entry.get("brand")
    name = entry.get("name")
    vendor = entry.get("vendor")

    norm_entry = normalize_intermediate_database_entry(entry)

    if vendor is not None:
        norm_entry["vendor"] = vendor
    elif brand or name:
        norm_entry["vendor"] = f"{brand or ''} {name or ''}".strip()
    else:
        norm_entry["vendor"] = "Unknown OAG"

    return norm_entry
