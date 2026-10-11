from ...utils import extract_number
from ..base.calculations import normalize_intermediate_database_entry


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
    entry = normalize_intermediate_database_entry(entry)
    entry["required_backfocus"] = entry.get("required_backfocus", 55)

    if "magnification" not in entry:
        if parse_magnification:
            name = entry.get("name", "")
            entry["magnification"] = (
                extract_number(name, suffix="x") or default_magnification
            )
        else:
            entry["magnification"] = default_magnification

    return entry
