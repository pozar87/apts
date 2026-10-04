def normalize_naked_eye_database_entry(entry: dict) -> dict:
    """
    Normalizes a naked eye database entry into standard fields.
    """
    norm_entry = entry.copy()
    brand = norm_entry.get("brand", "")
    name = norm_entry.get("name", "")
    if brand or name:
        vendor = f"{brand} {name}".strip()
    else:
        vendor = norm_entry.get("vendor", "Naked Eye")

    magnification = norm_entry.get("magnification", 1)
    objective_diameter = norm_entry.get("objective_diameter", 7)
    apparent_fov_deg = norm_entry.get("apparent_fov_deg", 180)
    focal_length = norm_entry.get("focal_length", 1)

    norm_entry.update(
        {
            "vendor": vendor,
            "magnification": magnification,
            "objective_diameter": objective_diameter,
            "apparent_fov_deg": apparent_fov_deg,
            "focal_length": focal_length,
        }
    )
    return norm_entry
