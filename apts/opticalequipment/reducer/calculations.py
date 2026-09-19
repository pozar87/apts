from ...utils import extract_number, map_conn, map_gender


def normalize_reducer_database_entry(
    entry: dict,
    default_magnification: float = 0.8,
    parse_magnification: bool = False,
) -> dict:
    """
    Normalizes a reducer, flattener, or corrector database entry by constructing
    the full vendor string, backfocus, magnification, and mapping input and output
    connection configurations.
    """
    entry = entry.copy()
    brand = entry["brand"]
    name = entry["name"]
    entry["vendor"] = f"{brand} {name}"
    entry["optical_length"] = entry.get("optical_length", 0)
    entry["mass"] = entry.get("mass", 0)
    entry["required_backfocus"] = entry.get("required_backfocus", 55)

    if "magnification" not in entry:
        if parse_magnification:
            entry["magnification"] = (
                extract_number(name, suffix="x") or default_magnification
            )
        else:
            entry["magnification"] = default_magnification

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
