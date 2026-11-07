import numpy

from ..base.calculations import normalize_intermediate_database_entry


def normalize_naked_eye_database_entry(entry: dict) -> dict:
    """
    Normalizes a naked eye database entry into standard fields.
    """
    brand = entry.get("brand", "")
    name = entry.get("name", "")
    if brand or name:
        default_vendor = f"{brand} {name}".strip()
    else:
        default_vendor = "Naked Eye"

    norm_entry = normalize_intermediate_database_entry(entry)
    vendor = entry.get("vendor", default_vendor)
    magnification = entry.get("magnification", 1)
    objective_diameter = entry.get("objective_diameter", 7)
    apparent_fov_deg = entry.get("apparent_fov_deg", 180)
    focal_length = entry.get("focal_length", 1)

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


def calculate_naked_eye_fov(apparent_fov_deg: float, magnification: float) -> float:
    """
    True Field of View = Apparent FOV / Magnification.
    Returns FOV value in degrees.
    """
    return apparent_fov_deg / magnification


def calculate_naked_eye_exit_pupil(
    objective_diameter_mm: float, magnification: float
) -> float:
    """
    Exit pupil = objective diameter / magnification.
    Returns exit pupil in mm.
    """
    return objective_diameter_mm / magnification


def calculate_naked_eye_dawes_limit(objective_diameter_cm: float) -> float:
    """
    Calculate maximum resolving power using Dawes' Limit formula.
    Returns limit in arcseconds.
    """
    return round(11.6 / objective_diameter_cm, 3)


def calculate_naked_eye_rayleigh_limit(
    objective_diameter_cm: float, wavelength_nm: float = 550
) -> float:
    """
    Calculate maximum resolving power using Rayleigh Limit formula for naked eye.
    Empirical approximation: 13.8 / objective_diameter_cm.
    Returns limit in arcseconds.
    """
    # For simplicity and backward compatibility with current implementation,
    # we don't use wavelength_nm here yet, but we accept it.
    return round(13.8 / objective_diameter_cm, 3)


def calculate_naked_eye_limiting_magnitude(objective_diameter_cm: float) -> float:
    """
    Calculate approximate limiting magnitude based on objective diameter in cm.
    """
    return float(7.7 + 5 * numpy.log10(objective_diameter_cm))


def calculate_naked_eye_brightness(exit_pupil_mm: float) -> float:
    """
    Relative brightness: (Exit Pupil (mm) / 7mm)^2 * 100.
    Assuming 7mm is the max human eye pupil diameter.
    """
    return float((exit_pupil_mm / 7) ** 2 * 100)
