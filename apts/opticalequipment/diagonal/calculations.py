from ...utils import ConnectionType, Gender, map_conn, map_gender


def normalize_diagonal_database_entry(entry: dict) -> dict:
    """
    Normalizes database dictionary entries for a star diagonal into standard fields.
    """
    norm_entry = entry.copy()

    brand = norm_entry.get("brand", "")
    name = norm_entry.get("name", "")
    if brand or name:
        vendor = f"{brand} {name}".strip()
    else:
        vendor = norm_entry.get("vendor", "unknown diagonal")

    if "in_connection_type" not in norm_entry and "tside_thread" in norm_entry:
        conn = map_conn(norm_entry.get("tside_thread"))
        if conn is not None:
            norm_entry["in_connection_type"] = conn.value
    if "out_connection_type" not in norm_entry and "cside_thread" in norm_entry:
        conn = map_conn(norm_entry.get("cside_thread"))
        if conn is not None:
            norm_entry["out_connection_type"] = conn.value
    if "in_gender" not in norm_entry and "tside_gender" in norm_entry:
        g = map_gender(norm_entry.get("tside_gender")) or Gender.MALE
        norm_entry["in_gender"] = g.value
    if "out_gender" not in norm_entry and "cside_gender" in norm_entry:
        g = map_gender(norm_entry.get("cside_gender")) or Gender.MALE
        norm_entry["out_gender"] = g.value

    ol = norm_entry.get("optical_length", 0)
    mass = norm_entry.get("mass", 0)
    is_erecting = norm_entry.get("is_erecting", False)

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
        if norm_entry.get("t2_output", False):
            outputs.append((ConnectionType.T2, Gender.MALE))
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
            "is_erecting": is_erecting,
            "inputs": inputs,
            "outputs": outputs,
        }
    )
    return norm_entry
