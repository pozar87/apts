import math


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
