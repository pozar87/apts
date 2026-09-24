from ...utils import ConnectionType, map_conn, map_gender


def normalize_filter_database_entry(entry: dict) -> dict:
    """
    Normalizes a filter database entry by constructing vendor, setting default name/transmission/mass/optical_length,
    and mapping input and output connection configurations.
    """
    entry = entry.copy()
    brand = entry.get("brand", "Unknown")
    name = entry.get("name", "Unknown")
    vendor = entry.get("vendor", f"{brand} {name}")
    tt = map_conn(entry.get("tside_thread"))
    # Filters usually have the same thread on both sides or are just glass.
    # Defaulting to 1.25" if not specified.
    conn = tt or ConnectionType.F_1_25
    trans = entry.get("transmission", 1.0)
    ol = entry.get("optical_length", 0)
    mass = entry.get("mass", 0)

    inputs = entry.get("inputs")
    if inputs:
        inputs = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in inputs
        ]

    outputs = entry.get("outputs")
    if outputs:
        outputs = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in outputs
        ]

    entry["name"] = name
    entry["vendor"] = vendor
    entry["connection_type"] = conn
    entry["transmission"] = trans
    entry["optical_length"] = ol
    entry["mass"] = mass
    entry["inputs"] = inputs
    entry["outputs"] = outputs

    return entry
