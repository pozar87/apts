from ...utils import ConnectionType, map_conn
from ..base.calculations import normalize_intermediate_database_entry


def normalize_filter_database_entry(entry: dict) -> dict:
    """
    Normalizes a filter database entry by constructing vendor, setting default name/transmission/mass/optical_length,
    and mapping input and output connection configurations.
    """
    normalized = normalize_intermediate_database_entry(entry)
    tt = map_conn(entry.get("tside_thread"))
    # Filters usually have the same thread on both sides or are just glass.
    # Defaulting to 1.25" if not specified.
    conn = tt or ConnectionType.F_1_25
    normalized["name"] = entry.get("name", "Unknown")
    normalized["connection_type"] = conn
    normalized["transmission"] = entry.get("transmission", 1.0)

    if entry.get("inputs") is None:
        normalized["inputs"] = None
    if entry.get("outputs") is None:
        normalized["outputs"] = None

    return normalized
