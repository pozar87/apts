from ..base.calculations import normalize_intermediate_database_entry


def normalize_rotator_database_entry(entry: dict) -> dict:
    """
    Normalizes a rotator database entry using standard intermediate equipment normalization.
    """
    return normalize_intermediate_database_entry(entry)
