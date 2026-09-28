from ..base.calculations import normalize_intermediate_database_entry


def normalize_anti_tilt_database_entry(entry: dict) -> dict:
    """
    Normalizes an anti-tilt database entry using standard intermediate equipment normalization.
    """
    return normalize_intermediate_database_entry(entry)
