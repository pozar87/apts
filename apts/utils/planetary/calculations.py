import numpy as np
from typing import Union, Any, cast


def calculate_sub_observer_latitude(
    alpha_rad: Union[float, np.ndarray],
    delta_rad: Union[float, np.ndarray],
    alpha0_rad: Union[float, np.ndarray],
    delta0_rad: Union[float, np.ndarray],
) -> Union[float, np.ndarray]:
    """
    Calculates the sub-observer latitude (planetocentric latitude of the Earth) in degrees.
    Formula: sin(De) = -sin(delta0)*sin(delta) - cos(delta0)*cos(delta)*cos(alpha0 - alpha)
    Reference: Explanatory Supplement to the Astronomical Almanac.
    """
    sin_De = -np.sin(delta0_rad) * np.sin(delta_rad) - np.cos(delta0_rad) * np.cos(
        delta_rad
    ) * np.cos(alpha0_rad - alpha_rad)
    De_rad = np.arcsin(np.clip(sin_De, -1.0, 1.0))
    res = np.degrees(De_rad)
    return float(cast(Any, res)) if np.isscalar(res) else res


def calculate_apparent_polar_radius(
    radius_eq: float,
    radius_pol: float,
    De_deg: Union[float, np.ndarray],
) -> Union[float, np.ndarray]:
    """
    Calculates the apparent polar radius in km accounting for planetary tilt De.
    Formula: r_app = r_eq * sqrt(1 - e^2 * cos^2(De)) where e^2 = (r_eq^2 - r_pol^2) / r_eq^2
    """
    De_rad = np.radians(De_deg)
    e_sq = (radius_eq**2 - radius_pol**2) / (radius_eq**2)
    return radius_eq * np.sqrt(1 - e_sq * np.cos(De_rad) ** 2)


def calculate_angular_diameter(
    radius_km: Union[float, np.ndarray],
    distance_km: Union[float, np.ndarray],
) -> Union[float, np.ndarray]:
    """
    Calculates the apparent angular diameter in arcseconds given radius in km and distance in km.
    Formula: alpha_rad = 2 * arcsin(radius / distance)
    """
    alpha_rad = 2 * np.arcsin(radius_km / distance_km)
    res = np.degrees(alpha_rad) * 3600.0
    return float(cast(Any, res)) if np.isscalar(res) else res


def calculate_illuminated_fraction(
    phase_angle_rad: Union[float, np.ndarray],
) -> Union[float, np.ndarray]:
    """
    Calculates the illuminated fraction (0.0 to 1.0) given the phase angle in radians.
    Formula: k = (1 + cos(i)) / 2
    """
    return (1 + np.cos(phase_angle_rad)) / 2


def calculate_illuminated_disk_area(
    angular_diameter_arcsec: Union[float, np.ndarray],
    illuminated_fraction: Union[float, np.ndarray],
) -> Union[float, np.ndarray]:
    """
    Calculates the illuminated area of a disk in square arcseconds.
    Formula: Area = pi * (diameter / 2)^2 * k
    """
    return np.pi * (angular_diameter_arcsec / 2.0) ** 2 * illuminated_fraction


def calculate_surface_brightness(
    magnitude: Union[float, np.ndarray],
    area_arcsec2: Union[float, np.ndarray],
) -> Union[float, np.ndarray]:
    """
    Calculates average surface brightness in mag/arcsec² given visual magnitude and illuminated area.
    Formula: S = V + 2.5 * log10(Area)
    """
    if np.isscalar(area_arcsec2):
        if cast(Any, area_arcsec2) <= 0:
            return float("inf")
        res_scalar = magnitude + 2.5 * np.log10(area_arcsec2)
        return float(cast(Any, res_scalar))
    else:
        res = np.full_like(area_arcsec2, np.inf, dtype=float)
        valid = area_arcsec2 > 0
        np.log10(area_arcsec2, where=valid, out=res)
        res = np.where(valid, magnitude + 2.5 * res, np.inf)
        return cast(np.ndarray, res)


def calculate_sun_magnitude(
    distance_au: Union[float, np.ndarray],
) -> Union[float, np.ndarray]:
    """
    Calculates apparent magnitude of the Sun given distance in AU.
    Formula: M = -26.74 + 5 * log10(dist_au)
    """
    return -26.74 + 5 * np.log10(distance_au)


def calculate_moon_magnitude_krisciunas(
    phase_angle_deg: Union[float, np.ndarray],
    distance_km: Union[float, np.ndarray],
) -> Union[float, np.ndarray]:
    """
    Calculates Moon apparent visual magnitude using Krisciunas & Schaefer (1991) model.
    """
    v_base = -12.73 + 0.026 * np.abs(phase_angle_deg) + 4.0e-9 * (phase_angle_deg**4)
    v_dist = 5 * np.log10(distance_km / 384400.0)
    return v_base + v_dist
