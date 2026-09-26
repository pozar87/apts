from ...utils import map_conn, map_gender


def normalize_oag_database_entry(entry: dict) -> dict:
    """
    Normalizes database dictionary entries for an Off-Axis Guider (OAG) into standard fields.
    """
    norm_entry = entry.copy()

    brand = norm_entry.get("brand", "")
    name = norm_entry.get("name", "")
    if brand or name:
        vendor = f"{brand} {name}".strip()
    else:
        vendor = norm_entry.get("vendor", "Unknown OAG")

    ol = norm_entry.get("optical_length", 0)
    mass = norm_entry.get("mass", 0)
    tt = map_conn(norm_entry.get("tside_thread"))
    tg = map_gender(norm_entry.get("tside_gender"))
    ct = map_conn(norm_entry.get("cside_thread"))
    cg = map_gender(norm_entry.get("cside_gender"))

    inputs = norm_entry.get("inputs")
    if inputs is None:
        inputs = [(tt, tg)] if tt else []
    else:
        inputs = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in inputs
        ]

    outputs = norm_entry.get("outputs")
    if outputs is None:
        outputs = [(ct, cg)] if ct else []
    else:
        outputs = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in outputs
        ]

    norm_entry.update(
        {
            "vendor": vendor,
            "optical_length": ol,
            "mass": mass,
            "inputs": inputs,
            "outputs": outputs,
        }
    )
    return norm_entry
