import numpy as np
from typing import Optional


def calculate_saturation_magnitude_analytical(
    full_well: float,
    flux_at_zero_mag: float,
    exposure_time: float,
    psf_peak_fraction: float,
) -> float:
    """
    Analytically calculates the magnitude that saturates the sensor.

    :param full_well: Sensor full-well capacity in electrons.
    :param flux_at_zero_mag: Object flux for a 0th magnitude star in e-/s.
    :param exposure_time: Exposure time in seconds.
    :param psf_peak_fraction: Fraction of light in the central pixel (PSF model).
    :return: Magnitude at saturation.
    """
    if psf_peak_fraction <= 0 or exposure_time <= 0 or flux_at_zero_mag <= 0:
        return float(np.nan)

    # target_flux = full_well / (t * f)
    target_flux = full_well / (exposure_time * psf_peak_fraction)

    # target_flux = flux_at_zero * 10^(-0.4 * m_eff)
    # m_eff = -2.5 * log10(target_flux / flux_at_zero)
    m_eff = -2.5 * np.log10(target_flux / flux_at_zero_mag)
    return float(m_eff)


def calculate_saturation_magnitude(
    full_well: float,
    flux_at_zero_mag: float,
    exposure_time: float,
    psf_peak_fraction: float,
    airmass_val: Optional[float] = None,
    extinction_k: float = 0.2,
) -> Optional[float]:
    """
    Calculates the magnitude of a point source that would just saturate the sensor
    at the given exposure time, considering PSF peak fraction and optional atmospheric extinction.

    :param full_well: Sensor full-well capacity in electrons.
    :param flux_at_zero_mag: Object flux for a 0th magnitude star in e-/s.
    :param exposure_time: Exposure time in seconds.
    :param psf_peak_fraction: Fraction of light in the central pixel (PSF model).
    :param airmass_val: Optional airmass value at a given altitude.
    :param extinction_k: Atmospheric extinction coefficient (default 0.2).
    :return: Magnitude at saturation, or None if invalid inputs.
    """
    m_eff = calculate_saturation_magnitude_analytical(
        full_well, flux_at_zero_mag, exposure_time, psf_peak_fraction
    )
    if np.isnan(m_eff):
        return None

    if airmass_val is not None:
        return float(m_eff - extinction_k * airmass_val)

    return float(m_eff)


def calculate_saturation_time(
    full_well: float,
    obj_flux: float,
    psf_peak_fraction: float,
) -> Optional[float]:
    """
    Calculates the maximum exposure time before the central pixel of a point source saturates.
    Based on the full-well capacity of the sensor and the Gaussian PSF model.

    :param full_well: Sensor full-well capacity in electrons.
    :param obj_flux: Total integrated object flux in e-/s.
    :param psf_peak_fraction: Fraction of light in the central pixel (PSF model).
    :return: Maximum exposure time in seconds, or None if calculation is invalid.
    """
    if obj_flux <= 0 or psf_peak_fraction <= 0:
        return None
    return full_well / (obj_flux * psf_peak_fraction)
