from ...utils import ConnectionType, Gender, extract_number
from ..base.calculations import normalize_intermediate_database_entry


def normalize_barlow_database_entry(entry: dict) -> dict:
    """
    Normalizes a Barlow database entry using standard intermediate equipment
    normalization while processing magnification and t2_output flags.
    """
    name = entry.get("name", "")
    t2_output = entry.get("t2_output", False) and "outputs" not in entry

    normalized = normalize_intermediate_database_entry(entry)

    brand = entry.get("brand", "")
    if "vendor" not in entry:
        normalized["vendor"] = f"{brand} {name}".strip() if (brand or name) else "unknown barlow"

    if "magnification" not in normalized:
        mag = (
            extract_number(name, suffix="x")
            or extract_number(name, prefix="x")
            or extract_number(name)
            or 2.0
        )
        normalized["magnification"] = mag

    if t2_output:
        outputs = list(normalized.get("outputs", []))
        if (ConnectionType.T2, Gender.MALE) not in outputs:
            outputs.append((ConnectionType.T2, Gender.MALE))
        normalized["outputs"] = outputs

    return normalized
