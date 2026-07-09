import numpy as np
from ...constants import astronomy

def calculate_dawes_limit(aperture_mm: float) -> float:
    """
    Calculate the maximum resolving power of a telescope using the Dawes' Limit formula.
    https://en.wikipedia.org/wiki/Dawes%27_limit

    :param aperture_mm: aperture in mm
    :return: limit in arcseconds
    """
    if aperture_mm <= 0:
        return 0.0
    # Formula: 11.6 / aperture_cm
    return round(11.6 / (aperture_mm / 10.0), 3)

def calculate_rayleigh_limit(aperture_mm: float, wavelength_nm: float = 550) -> float:
    """
    Calculate the maximum resolving power of a telescope using the Rayleigh Limit formula.
    θ = 1.22 * λ / D
    Where λ is the wavelength and D is the aperture.
    https://en.wikipedia.org/wiki/Angular_resolution

    :param aperture_mm: aperture in mm
    :param wavelength_nm: wavelength in nanometers (default 550nm for green light)
    :return: limit in arcseconds
    """
    if aperture_mm <= 0:
        return 0.0
    wavelength_m = wavelength_nm * 1e-9
    aperture_m = aperture_mm * 1e-3
    limit_rad = 1.22 * wavelength_m / aperture_m
    limit_arcsec = limit_rad * astronomy.RAD_TO_ARCSEC
    return round(limit_arcsec, 3)

def calculate_limiting_magnitude(aperture_mm: float, central_obstruction_mm: float = 0.0) -> float:
    """
    Calculate a telescope's approximate limiting magnitude.
    Uses effective aperture diameter for better accuracy when central obstruction is present.

    :param aperture_mm: aperture in mm
    :param central_obstruction_mm: central obstruction in mm
    :return: limiting magnitude
    """
    effective_aperture_mm = np.sqrt(aperture_mm**2 - central_obstruction_mm**2)
    if effective_aperture_mm <= 0:
        return 0.0
    # Formula: 7.7 + 5 * log10(aperture_cm)
    return 7.7 + 5 * np.log10(effective_aperture_mm / 10.0)

def calculate_highest_useful_magnification(aperture_mm: float) -> float:
    """
    Calculate the theoretical highest useful magnification for the telescope.
    Rule of thumb: 2.0x aperture in mm.
    """
    return float(aperture_mm * 2.0)

def calculate_lowest_useful_magnification(aperture_mm: float, pupil_diameter_mm: float = 7.0) -> float:
    """
    Calculate the theoretical lowest useful magnification for the telescope.
    Formula: aperture / pupil_diameter.
    """
    if pupil_diameter_mm <= 0:
        return 0.0
    return float(aperture_mm / pupil_diameter_mm)
