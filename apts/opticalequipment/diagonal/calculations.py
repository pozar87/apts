from ...utils import ConnectionType, Gender, map_conn, map_gender
from ..base.calculations import normalize_intermediate_database_entry


def normalize_diagonal_database_entry(entry: dict) -> dict:
    """
    Normalizes database dictionary entries for a star diagonal into standard fields.
    """
    brand = entry.get("brand", "")
    name = entry.get("name", "")
    t2_output = entry.get("t2_output", False) and "outputs" not in entry

    norm_entry = normalize_intermediate_database_entry(entry)

    if "vendor" not in entry:
        norm_entry["vendor"] = (
            f"{brand} {name}".strip() if (brand or name) else "unknown diagonal"
        )

    if "in_connection_type" not in norm_entry and "tside_thread" in norm_entry:
        conn = map_conn(entry.get("tside_thread"))
        if conn is not None:
            norm_entry["in_connection_type"] = conn.value
    if "out_connection_type" not in norm_entry and "cside_thread" in norm_entry:
        conn = map_conn(entry.get("cside_thread"))
        if conn is not None:
            norm_entry["out_connection_type"] = conn.value
    if "in_gender" not in norm_entry and "tside_gender" in norm_entry:
        g = map_gender(entry.get("tside_gender")) or Gender.MALE
        norm_entry["in_gender"] = g.value
    if "out_gender" not in norm_entry and "cside_gender" in norm_entry:
        g = map_gender(entry.get("cside_gender")) or Gender.MALE
        norm_entry["out_gender"] = g.value

    norm_entry["is_erecting"] = entry.get("is_erecting", False)

    if t2_output:
        outputs = list(norm_entry.get("outputs", []))
        if (ConnectionType.T2, Gender.MALE) not in outputs:
            outputs.append((ConnectionType.T2, Gender.MALE))
        norm_entry["outputs"] = outputs

    return norm_entry
