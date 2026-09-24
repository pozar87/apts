from ...utils import map_conn, map_gender


def normalize_filter_wheel_database_entry(entry: dict) -> dict:
    """
    Normalizes a filter wheel / filter holder database entry by parsing vendor name,
    optical length, mass, and mapping input and output connections.
    """
    entry = entry.copy()
    brand = entry.get("brand", "Unknown")
    name = entry.get("name", "Unknown")
    entry["vendor"] = f"{brand} {name}"
    entry["optical_length"] = entry.get("optical_length", 0)
    entry["mass"] = entry.get("mass", 0)

    tt = map_conn(entry.get("tside_thread"))
    tg = map_gender(entry.get("tside_gender"))
    ct = map_conn(entry.get("cside_thread"))
    cg = map_gender(entry.get("cside_gender"))

    inputs = entry.get("inputs")
    if inputs is None:
        entry["inputs"] = [(tt, tg)] if tt else []
    else:
        entry["inputs"] = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in inputs
        ]

    outputs = entry.get("outputs")
    if outputs is None:
        entry["outputs"] = [(ct, cg)] if ct else []
    else:
        entry["outputs"] = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in outputs
        ]

    return entry
