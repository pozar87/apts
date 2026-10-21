import numpy as np
from typing import Union


def calculate_sky_flux(
    sqm: Union[float, np.ndarray],
    aperture_area_cm2: float,
    quantum_efficiency: float,
    pixel_scale_arcsec: float,
    filter_transmission: float = 1.0,
) -> Union[float, np.ndarray]:
    """
    Calculates the sky background flux in electrons per second per pixel.
    Assumes an L-band (clear) filter equivalent and a zero point where a 21.83 mag/arcsec^2
    sky produces a specific reference flux.

    :param sqm: Sky Quality Meter reading in mag/arcsec^2.
    :param aperture_area_cm2: Aperture area in square centimeters.
    :param quantum_efficiency: Peak Quantum Efficiency of the sensor (0-100).
    :param pixel_scale_arcsec: Pixel scale in arcseconds per pixel.
    :param filter_transmission: Combined transmission of any filters (0.0 to 1.0).
    :return: Sky flux in e-/s/pixel.
    """
    qe = quantum_efficiency / 100.0
    pixel_area_arcsec2 = pixel_scale_arcsec**2

    # Formula: Reference flux scaled by aperture, QE, and sky brightness
    flux = (
        0.005
        * 10 ** (0.4 * (21.83 - sqm))
        * aperture_area_cm2
        * qe
        * filter_transmission
        * pixel_area_arcsec2
    )
    return flux


def calculate_object_flux(
    magnitude: Union[float, np.ndarray],
    aperture_area_cm2: float,
    quantum_efficiency: float,
    filter_transmission: float = 1.0,
) -> Union[float, np.ndarray]:
    """
    Calculates the total integrated flux from an object in electrons per second.
    The calculation is based on the object's magnitude and the setup's aperture and QE.

    :param magnitude: Apparent magnitude of the object.
    :param aperture_area_cm2: Aperture area in square centimeters.
    :param quantum_efficiency: Peak Quantum Efficiency of the sensor (0-100).
    :param filter_transmission: Combined transmission of any filters (0.0 to 1.0).
    :return: Total integrated object flux in e-/s.
    """
    qe = quantum_efficiency / 100.0

    # Total integrated flux from the object
    # Based on the same zero point as sky_flux
    flux = (
        0.005
        * 10 ** (0.4 * (21.83 - magnitude))
        * aperture_area_cm2
        * qe
        * filter_transmission
    )
    return flux
