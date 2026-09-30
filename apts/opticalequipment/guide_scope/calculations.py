from ...utils import guess_optical_properties, map_conn, map_gender


def normalize_guide_scope_database_entry(entry: dict) -> dict:
    """
    Normalizes a guide scope database entry by parsing vendor name, optical length, mass,
    aperture, focal length, backfocus, and mapping output connections.
    """
    entry = entry.copy()
    brand = entry.get("brand", "Unknown")
    name = entry.get("name", "Unknown")
    entry["vendor"] = f"{brand} {name}"

    ol = entry.get("optical_length", 0)
    mass = entry.get("mass", 0)
    entry["optical_length"] = ol
    entry["mass"] = mass

    ct = map_conn(entry.get("cside_thread"))
    cg = map_gender(entry.get("cside_gender"))

    aperture, focal_length = guess_optical_properties(name)
    entry["aperture"] = aperture or 30
    entry["focal_length"] = focal_length or 120

    bf_val = entry.get("bf_role") == "start"
    entry["backfocus"] = ol if bf_val else None

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
