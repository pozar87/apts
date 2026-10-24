import numpy

from ...constants import astronomy
from ...utils import extract_number, map_conn, map_gender


def normalize_binoculars_database_entry(entry: dict) -> dict:
    """
    Normalizes a binoculars database entry by parsing vendor name, mass,
    magnification, objective diameter, apparent FOV, and output connections.
    """
    entry = entry.copy()
    brand = entry.get("brand", "Unknown")
    name = entry.get("name", "Unknown")
    entry["vendor"] = f"{brand} {name}".strip()

    entry["mass"] = entry.get("mass", 0)

    mag = extract_number(name) or 10
    obj = extract_number(name, prefix=f"{int(mag)}x") or 50
    entry["magnification"] = entry.get("magnification", mag)
    entry["objective_diameter"] = entry.get("objective_diameter", obj)
    entry["apparent_fov_deg"] = entry.get("apparent_fov_deg", 60)

    ct = map_conn(entry.get("cside_thread"))
    cg = map_gender(entry.get("cside_gender"))

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


def calculate_binoculars_fov(apparent_fov_deg: float, magnification: float) -> float:
    """
    True Field of View = Apparent FOV / Magnification.
    Returns FOV value in degrees.
    """
    return apparent_fov_deg / magnification


def calculate_binoculars_exit_pupil(
    objective_diameter_mm: float, magnification: float
) -> float:
    """
    Exit pupil = objective diameter / magnification.
    Returns exit pupil in mm.
    """
    return objective_diameter_mm / magnification


def calculate_binoculars_dawes_limit(objective_diameter_cm: float) -> float:
    """
    Calculate maximum resolving power using Dawes' Limit formula.
    Returns limit in arcseconds.
    """
    return round(11.6 / objective_diameter_cm, 3)


def calculate_binoculars_rayleigh_limit(
    objective_diameter_m: float, wavelength_nm: float = 550
) -> float:
    """
    Calculate maximum resolving power using Rayleigh Limit formula.
    θ = 1.22 * λ / D
    Where λ is the wavelength and D is the aperture (objective diameter).
    Returns limit in arcseconds.
    """
    wavelength_m = wavelength_nm * 1e-9
    limit_rad = 1.22 * wavelength_m / objective_diameter_m
    limit_arcsec = limit_rad * astronomy.RAD_TO_ARCSEC
    return round(limit_arcsec, 3)


def calculate_binoculars_limiting_magnitude(objective_diameter_cm: float) -> float:
    """
    Calculate approximate limiting magnitude based on objective diameter in cm.
    """
    return float(7.7 + 5 * numpy.log10(objective_diameter_cm))


def calculate_binoculars_brightness(exit_pupil_mm: float) -> float:
    """
    Relative brightness: (Exit Pupil (mm) / 7mm)^2 * 100.
    Assuming 7mm is the max human eye pupil diameter.
    """
    return float((exit_pupil_mm / 7) ** 2 * 100)
