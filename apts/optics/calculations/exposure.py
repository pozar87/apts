import math
from typing import Optional


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


def calculate_estimated_star_trailing(
    exposure_time: float, declination_deg: float, pixel_scale: float
) -> float:
    """
    Estimates the amount of star trailing in pixels for a given exposure time and declination
    assuming a stationary (non-tracking) mount.
    """
    if pixel_scale == 0:
        return 0.0

    sidereal_rate = 15.041067
    cos_dec = math.cos(math.radians(declination_deg))
    trailing_arcsec = sidereal_rate * exposure_time * cos_dec
    return float(trailing_arcsec / pixel_scale)


def calculate_max_exposure_alt_az(
    rot_rate: float,
    sensor_width_pixels: float,
    sensor_height_pixels: float,
    tolerance_pixels: float = 1.0,
) -> float:
    """
    Calculates the maximum exposure time for an Alt-Az mount to avoid field rotation trailing.
    """
    if rot_rate < 1e-10:
        return 3600.0

    # Distance from center to corner in pixels
    r = 0.5 * math.sqrt(sensor_width_pixels**2 + sensor_height_pixels**2)
    RAD_TO_ARCSEC = 206264.80624709636

    t = (tolerance_pixels * RAD_TO_ARCSEC) / (r * rot_rate)
    return float(t)


def calculate_rule_of_500(
    focal_length_mm: float,
    sensor_width_mm: Optional[float] = None,
    sensor_height_mm: Optional[float] = None,
) -> float:
    """
    Calculates the maximum exposure time to avoid star trailing using the classic Rule of 500.
    Formula: t = 500 / (F_actual * crop_factor)
    """
    if focal_length_mm == 0:
        return 0.0

    if sensor_width_mm is not None and sensor_height_mm is not None:
        diagonal = math.sqrt(sensor_width_mm**2 + sensor_height_mm**2)
        if diagonal == 0:
            return 500.0 / focal_length_mm
        crop_factor = 43.27 / diagonal
        t = 500.0 / (focal_length_mm * crop_factor)
    else:
        t = 500.0 / focal_length_mm

    return float(t)
