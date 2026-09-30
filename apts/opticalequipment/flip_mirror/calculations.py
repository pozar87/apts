from ..base.calculations import normalize_intermediate_database_entry


def normalize_flip_mirror_database_entry(entry: dict) -> dict:
    """
    Normalizes a flip mirror database entry using standard intermediate equipment normalization.
    """
    return normalize_intermediate_database_entry(entry)
