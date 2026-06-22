import numpy as np
from typing import Union, cast


def calculate_airmass(
    altitude_degrees: Union[float, np.ndarray]
) -> Union[float, np.ndarray]:
    """
    Calculates the relative airmass using the Kasten-Young (1989) formula.
    Formula: X = 1 / (sin(h) + 0.50572 * (h + 6.07995)^-1.6364)
    Where h is the apparent altitude in degrees.
    Source: https://en.wikipedia.org/wiki/Air_mass_(astronomy)
    """
    # Ensure altitude is at least 0 to avoid complex numbers/errors
    h = np.maximum(altitude_degrees, 0.0)
    return 1.0 / (np.sin(np.radians(h)) + 0.50572 * (h + 6.07995) ** -1.6364)


def calculate_atmospheric_extinction(
    magnitude: Union[float, np.ndarray],
    airmass: Union[float, np.ndarray],
    extinction_k: float = 0.2,
) -> Union[float, np.ndarray]:
    """
    Calculates the apparent magnitude of an object accounting for atmospheric extinction.
    Formula: m_apparent = m_zero + k * X
    Where k is the extinction coefficient and X is the airmass.
    """
    return magnitude + extinction_k * airmass


def calculate_atmospheric_dispersion(
    altitude_degrees: Union[float, np.ndarray],
    lambda1_nm: float = 400,
    lambda2_nm: float = 700,
) -> Union[float, np.ndarray]:
    """
    Calculates the atmospheric dispersion (angular separation) in arcseconds between two wavelengths
    at a given altitude using the Peck and Reeder (1972) refractive index formula.
    Formula: (n-1) * 10^6 = 64.328 + 29498.1 / (146 - lambda^-2) + 255.4 / (41 - lambda^-2)
    Dispersion Delta R = (n1 - n2) * tan(zenith_distance)
    Source: Peck & Reeder (1972), "Refractive Index of Air in the Near Infrared"
    """
    z = np.radians(90.0 - np.maximum(altitude_degrees, 0.1))  # Avoid tan(90)

    def get_n_minus_1(l_nm):
        l_um = l_nm / 1000.0
        l_inv_sq = 1.0 / (l_um**2)
        n_minus_1_e6 = (
            64.328 + 29498.1 / (146.0 - l_inv_sq) + 255.4 / (41.0 - l_inv_sq)
        )
        return n_minus_1_e6 * 1e-6

    n1_m_1 = get_n_minus_1(lambda1_nm)
    n2_m_1 = get_n_minus_1(lambda2_nm)

    dispersion_rad = abs(n1_m_1 - n2_m_1) * np.tan(z)
    dispersion_arcsec = np.degrees(dispersion_rad) * 3600.0

    if np.isscalar(altitude_degrees):
        if cast(float, altitude_degrees) >= 90:
            return 0.0
    else:
        dispersion_arcsec = np.where(
            cast(np.ndarray, altitude_degrees) >= 90, 0.0, dispersion_arcsec
        )

    return dispersion_arcsec
