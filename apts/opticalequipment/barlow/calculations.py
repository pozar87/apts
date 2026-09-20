from ...utils import ConnectionType, Gender, extract_number, map_conn, map_gender


def normalize_barlow_database_entry(entry: dict) -> dict:
    """
    Normalizes a Barlow database entry by constructing the full vendor string,
    extracting magnification from the item name, and mapping input and output
    connection configurations.
    """
    entry = entry.copy()
    brand = entry.get("brand", "")
    name = entry.get("name", "")

    if "vendor" not in entry:
        entry["vendor"] = f"{brand} {name}".strip() if (brand or name) else "unknown barlow"

    entry["optical_length"] = entry.get("optical_length", 0)
    entry["mass"] = entry.get("mass", 0)

    if "magnification" not in entry:
        mag = (
            extract_number(name, suffix="x")
            or extract_number(name, prefix="x")
            or extract_number(name)
            or 2.0
        )
        entry["magnification"] = mag

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
        outputs = [(ct, cg)] if ct else []
        if entry.get("t2_output", False):
            outputs.append((ConnectionType.T2, Gender.MALE))
        entry["outputs"] = outputs
    else:
        entry["outputs"] = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in outputs
        ]

    return entry
