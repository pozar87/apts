from ...utils import extract_number, map_conn, map_gender


def normalize_binoculars_database_entry(entry: dict) -> dict:
    """
    Normalizes a binoculars database entry by extracting magnification,
    objective diameter, vendor name, and output connection types.
    """
    entry = entry.copy()
    brand = entry.get("brand", "")
    name = entry.get("name", "")
    entry["vendor"] = f"{brand} {name}".strip()
    entry["mass"] = entry.get("mass", 0)

    mag = extract_number(name) or 10
    obj = extract_number(name, prefix=f"{int(mag)}x") or 50
    entry["magnification"] = mag
    entry["objective_diameter"] = obj

    ct = map_conn(entry.get("cside_thread"))
    cg = map_gender(entry.get("cside_gender"))

    outputs = entry.get("outputs")
    if outputs is None:
        entry["outputs"] = [(ct, cg)] if ct else []
    else:
        entry["outputs"] = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in outputs
        ]

    return entry
