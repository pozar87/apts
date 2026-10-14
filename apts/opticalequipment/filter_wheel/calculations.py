from ..base.calculations import normalize_intermediate_database_entry


def normalize_filter_wheel_database_entry(entry: dict) -> dict:
    """
    Normalizes a filter wheel / filter holder database entry by parsing vendor name,
    optical length, mass, and mapping input and output connections.
    """
    return normalize_intermediate_database_entry(entry)
