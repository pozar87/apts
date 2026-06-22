import math
import numpy as np
from typing import Union, cast


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


def calculate_snr(
    obj_flux: Union[float, np.ndarray],
    sky_flux: Union[float, np.ndarray],
    read_noise: float,
    exposure_time: float,
    n_subs: int = 1,
    n_pix: int = 4,
    in_db: bool = False,
) -> Union[float, np.ndarray]:
    """
    Calculates the Signal-to-Noise Ratio (SNR) for an object.
    The model accounts for object shot noise, sky background shot noise, and sensor read noise.
    It assumes aperture photometry where the object signal is integrated over `n_pix` pixels.

    :param obj_flux: Total integrated object flux in e-/s.
    :param sky_flux: Sky background flux in e-/s/pixel.
    :param read_noise: Sensor read noise in e- RMS.
    :param exposure_time: Exposure time per sub-exposure in seconds.
    :param n_subs: Number of sub-exposures stacked.
    :param n_pix: Number of pixels over which the object signal is integrated.
    :param in_db: If True, returns SNR in decibels (20 * log10).
    :return: SNR (dimensionless linear ratio or dB).
    """
    # Total signal
    signal = obj_flux * exposure_time * n_subs

    # Noise components (squared)
    shot_noise_sq = obj_flux * exposure_time * n_subs
    sky_noise_sq = sky_flux * exposure_time * n_subs * n_pix
    read_noise_sq = (read_noise**2) * n_subs * n_pix

    total_noise = np.sqrt(shot_noise_sq + sky_noise_sq + read_noise_sq)

    if np.isscalar(total_noise):
        if cast(float, total_noise) == 0:
            snr_linear = 0.0
        else:
            snr_linear = signal / cast(float, total_noise)
    else:
        snr_linear = np.divide(
            signal,
            cast(np.ndarray, total_noise),
            out=np.zeros_like(signal),
            where=cast(np.ndarray, total_noise) != 0,
        )

    if in_db:
        if np.isscalar(snr_linear):
            if cast(float, snr_linear) <= 0:
                return -np.inf
            return 20.0 * math.log10(cast(float, snr_linear))
        else:
            return 20.0 * np.log10(
                cast(np.ndarray, snr_linear),
                out=np.full_like(cast(np.ndarray, snr_linear), -np.inf),
                where=cast(np.ndarray, snr_linear) > 0,
            )

    return snr_linear
