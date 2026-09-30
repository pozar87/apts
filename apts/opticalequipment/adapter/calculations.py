from ...utils import map_conn, map_gender


def normalize_adapter_database_entry(entry: dict) -> dict:
    """
    Normalizes an adapter or spacer database entry by constructing vendor, setting default mass and optical_length,
    and mapping input and output connection configurations.
    """
    entry = entry.copy()
    brand = entry.get("brand", "Unknown")
    name = entry.get("name", "Unknown")
    vendor = entry.get("vendor", f"{brand} {name}")
    ol = entry.get("optical_length", 0)
    mass = entry.get("mass", 0)

    tt = map_conn(entry.get("tside_thread"))
    tg = map_gender(entry.get("tside_gender"))
    ct = map_conn(entry.get("cside_thread"))
    cg = map_gender(entry.get("cside_gender"))

    inputs = entry.get("inputs")
    if inputs is None:
        inputs = [(tt, tg)] if tt else []
    else:
        inputs = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in inputs
        ]

    outputs = entry.get("outputs")
    if outputs is None:
        outputs = [(ct, cg)] if ct else []
    else:
        outputs = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in outputs
        ]

    entry["brand"] = brand
    entry["name"] = name
    entry["vendor"] = vendor
    entry["optical_length"] = ol
    entry["mass"] = mass
    entry["inputs"] = inputs
    entry["outputs"] = outputs

    return entry
