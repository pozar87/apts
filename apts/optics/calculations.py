import math
from typing import Any, Union, cast

import numpy as np


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


def calculate_npf_rule(
    focal_ratio: float,
    pixel_pitch_um: float,
    focal_length_mm: float,
    declination_deg: float = 0,
    k: float = 1.0,
    simplified: bool = False,
) -> float:
    """
    Calculates the maximum exposure time to avoid star trailing using the NPF rule.
    The NPF rule is more accurate than the 'Rule of 500' for modern high-resolution sensors.

    Two versions are available:
    1. Complete (default): t = k * (16.9 * N + 0.10 * F + 13.7 * P) / (F * cos(dec))
    2. Simplified: t = k * (35 * N + 30 * P) / (F * cos(dec))

    Where:
    - N: f-number (focal ratio)
    - P: pixel pitch in micrometers (µm)
    - F: focal length in millimeters (mm)
    - dec: declination of the target in degrees
    - k: tolerance factor (1.0 for pinpoint stars, up to 3.0 for slightly elongated)

    Source: Frédéric Michaud, Société Astronomique du Havre (SAH)
    https://sahavre.fr/wp/regle-npf-rule/
    """
    if focal_length_mm == 0:
        return 0.0

    cos_dec = math.cos(math.radians(declination_deg))

    if abs(cos_dec) < 1e-10:
        # At the celestial poles, star movement is minimal.
        # We return a 1-hour cap (3600s) to avoid infinity.
        return 3600.0

    if simplified:
        t = k * (35 * focal_ratio + 30 * pixel_pitch_um) / (focal_length_mm * cos_dec)
    else:
        t = (
            k
            * (16.9 * focal_ratio + 0.10 * focal_length_mm + 13.7 * pixel_pitch_um)
            / (focal_length_mm * cos_dec)
        )

    return float(t)


def calculate_field_rotation_rate(
    latitude_deg: float, azimuth_deg: float, altitude_deg: float
) -> float:
    """
    Calculates the field rotation rate for an Alt-Az mount in arcseconds per second.
    Formula: omega_rot = omega_earth * cos(lat) * cos(az) / cos(alt)
    Where omega_earth is the sidereal rotation rate (15.041067 "/s).
    Source: "Field Rotation" - Bill Keicher
    """
    # Sidereal rotation rate in arcseconds per second
    omega_earth = 15.041067

    phi = math.radians(latitude_deg)
    az = math.radians(azimuth_deg)
    alt = math.radians(min(altitude_deg, 89.99))  # Avoid division by zero at zenith

    rate = omega_earth * math.cos(phi) * math.cos(az) / math.cos(alt)
    return abs(rate)


def calculate_airy_disk_diameter(
    focal_ratio: float, wavelength_nm: float = 550
) -> float:
    """
    Calculates the physical diameter of the Airy disk (first dark ring) in micrometers.
    Formula: D = 2.44 * lambda * f/D
    Where lambda is the wavelength and f/D is the effective focal ratio.
    This represents the diffraction-limited spot size on the focal plane.
    """
    # wavelength in nm -> micron
    lambda_um = wavelength_nm / 1000.0
    diameter = 2.44 * lambda_um * focal_ratio
    return float(diameter)

def calculate_exit_pupil(aperture: Any, zoom: Any) -> Any:
    """
    Calculates the exit pupil of an optical system.
    Formula: EP = aperture / zoom
    """
    from ..units import get_unit_registry
    ureg = get_unit_registry()
    # Default unit for exit pupil if telescope aperture is problematic
    default_mm_unit = ureg.mm

    # Validate aperture
    if (
        aperture is None
        or not hasattr(aperture, "units")
        or not hasattr(aperture, "magnitude")
        or np.isnan(float(aperture.magnitude))
    ):
        return np.nan * default_mm_unit  # Aperture is invalid

    aperture_units = aperture.units

    # Validate zoom
    zoom_magnitude = getattr(zoom, "magnitude", np.nan)
    if (
        not hasattr(zoom, "units")
        or np.isnan(float(zoom_magnitude))
        or zoom_magnitude == 0
    ):
        return np.nan * aperture_units

    try:
        result = aperture / zoom
        # Ensure result has the same dimensionality as aperture (length)
        if result.dimensionality != aperture.dimensionality:
            return np.nan * aperture_units
        return result
    except Exception:
        return np.nan * aperture_units


def calculate_brightness(exit_pupil: Any) -> Any:
    """
    Calculates the relative brightness of an optical system compared to the human eye.
    Formula: B = (exit_pupil / 7mm)^2 * 100
    """
    from ..units import get_unit_registry
    ureg = get_unit_registry()

    # After calling exit_pupil, ep_val should always be a Quantity.
    # Check if its magnitude is NaN (this means exit_pupil determined a NaN result).
    ep_magnitude = getattr(exit_pupil, "magnitude", np.nan)
    if not hasattr(exit_pupil, "units") or np.isnan(float(ep_magnitude)):
        return np.nan * ureg.dimensionless

    try:
        # ep_val should have length units (e.g., mm, inch) from robust exit_pupil.
        ep_mm = exit_pupil.to(ureg.mm)
    except Exception:
        return np.nan * ureg.dimensionless

    # Check if ep_mm.magnitude became NaN after conversion or if units are missing
    ep_mm_magnitude = getattr(ep_mm, "magnitude", np.nan)
    if not hasattr(ep_mm, "units") or np.isnan(float(ep_mm_magnitude)):
        return np.nan * ureg.dimensionless

    seven_mm = 7 * ureg.mm

    # Avoid division by zero if seven_mm is somehow misconfigured
    seven_mm_magnitude = getattr(seven_mm, "magnitude", 0)
    if seven_mm_magnitude == 0:
        return np.nan * ureg.dimensionless

    ratio = (
        ep_mm / seven_mm
    )

    # Check if ratio.magnitude is NaN or if units are unexpectedly missing
    ratio_magnitude = getattr(ratio, "magnitude", np.nan)
    if not hasattr(ratio, "units") or np.isnan(float(ratio_magnitude)):
        return np.nan * ureg.dimensionless

    return (ratio**2) * 100 * ureg.dimensionless
