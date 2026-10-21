import math
import numpy as np
from typing import Union, cast


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


def calculate_required_subs(
    target_snr: float,
    obj_flux: float,
    sky_flux: float,
    read_noise: float,
    exposure_time: float,
    n_pix: int = 4,
) -> float:
    """
    Calculates the number of sub-exposures needed to reach a target SNR.

    :param target_snr: Target Signal-to-Noise Ratio.
    :param obj_flux: Total integrated object flux in e-/s.
    :param sky_flux: Sky background flux in e-/s/pixel.
    :param read_noise: Sensor read noise in e- RMS.
    :param exposure_time: Exposure time per sub-exposure in seconds.
    :param n_pix: Number of pixels over which the object signal is integrated.
    :return: Number of required sub-exposures (rounded up).
    """
    # Signal and noise per single sub
    s = obj_flux * exposure_time
    b = sky_flux * exposure_time * n_pix
    r = (read_noise**2) * n_pix

    if s <= 0:
        return float(np.inf)

    n_required = (target_snr**2) * (s + b + r) / (s**2)
    return float(np.ceil(n_required))


def calculate_optimum_sub_exposure(
    sky_flux: float, read_noise: float, swamp_factor: float = 10.0
) -> float:
    """
    Calculates the exposure time at which the sky noise becomes dominant over
    the sensor's read noise by a given 'swamp factor'.

    :param sky_flux: Sky background flux in e-/s/pixel.
    :param read_noise: Sensor read noise in e- RMS.
    :param swamp_factor: Ratio of sky noise power to read noise power (default 10.0).
    :return: Optimum sub-exposure time in seconds.
    """
    if sky_flux <= 0:
        return float(np.inf)

    # Time where SkyNoise^2 = swamp_factor * ReadNoise^2
    # SkyNoise^2 = Flux * Time
    # Time = swamp_factor * ReadNoise^2 / Flux
    return (swamp_factor * read_noise**2) / sky_flux
