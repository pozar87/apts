from ...utils import extract_number, map_conn, map_gender


def normalize_binoculars_database_entry(entry: dict) -> dict:
    """
    Normalizes a binoculars database entry by parsing vendor name, mass,
    magnification, objective diameter, apparent FOV, and output connections.
    """
    entry = entry.copy()
    brand = entry.get("brand", "Unknown")
    name = entry.get("name", "Unknown")
    entry["vendor"] = f"{brand} {name}".strip()

    entry["mass"] = entry.get("mass", 0)

    mag = extract_number(name) or 10
    obj = extract_number(name, prefix=f"{int(mag)}x") or 50
    entry["magnification"] = entry.get("magnification", mag)
    entry["objective_diameter"] = entry.get("objective_diameter", obj)
    entry["apparent_fov_deg"] = entry.get("apparent_fov_deg", 60)

    ct = map_conn(entry.get("cside_thread"))
    cg = map_gender(entry.get("cside_gender"))

    outputs = entry.get("outputs")
    if outputs is None:
        outputs = [(ct, cg)] if ct else []
    else:
        outputs = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in outputs
        ]
    entry["outputs"] = outputs

    return entry
