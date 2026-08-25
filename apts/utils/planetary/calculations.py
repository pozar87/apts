import numpy as np
from typing import Union, Any, Tuple, cast
from apts.i18n import gettext_


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


def calculate_moon_orientation_elements(
    time_tt: Union[float, np.ndarray],
) -> Tuple[Union[float, np.ndarray], Union[float, np.ndarray], Union[float, np.ndarray]]:
    """
    Internal helper to calculate Moon orientation elements (alpha0, delta0, W)
    using the IAU 2015 model given Terrestrial Time (TT) Julian Date. Results are in radians.
    """
    d = time_tt - 2451545.0
    T = d / 36525.0

    # IAU 2015 Lunar rotation parameters (Archinal et al. 2018)
    E1 = np.radians((125.045 - 0.0529921 * d) % 360)
    E2 = np.radians((250.089 - 0.1059842 * d) % 360)
    E3 = np.radians((260.008 + 13.0120009 * d) % 360)
    E4 = np.radians((176.625 + 13.3407154 * d) % 360)
    E5 = np.radians((357.529 + 0.9856003 * d) % 360)
    E6 = np.radians((311.589 + 26.4057084 * d) % 360)
    E7 = np.radians((134.963 + 13.0649930 * d) % 360)
    E8 = np.radians((276.617 + 0.3287146 * d) % 360)
    E10 = np.radians((15.134 - 0.1589763 * d) % 360)
    E11 = np.radians((119.743 + 0.0036096 * d) % 360)
    E12 = np.radians((239.961 + 0.1295801 * d) % 360)
    E13 = np.radians((25.053 + 12.5126625 * d) % 360)

    alpha0 = np.radians(
        (
            269.9949
            + 0.0031 * T
            - 3.8787 * np.sin(E1)
            - 0.1204 * np.sin(E2)
            - 0.0700 * np.sin(E3)
            - 0.0172 * np.sin(E4)
            + 0.0072 * np.sin(E6)
            - 0.0052 * np.sin(E10)
            + 0.0043 * np.sin(E13)
        )
        % 360
    )

    delta0 = np.radians(
        (
            66.5392
            + 0.0130 * T
            + 1.5419 * np.cos(E1)
            + 0.0239 * np.cos(E2)
            + 0.0278 * np.cos(E3)
            + 0.0068 * np.cos(E4)
            - 0.0029 * np.cos(E6)
            + 0.0009 * np.cos(E7)
            + 0.0008 * np.cos(E10)
            - 0.0009 * np.cos(E13)
        )
        % 360
    )

    W = np.radians(
        (
            38.3213
            + 13.17635815 * d
            + 3.5610 * np.sin(E1)
            + 0.1108 * np.sin(E2)
            + 0.0642 * np.sin(E3)
            + 0.0158 * np.sin(E4)
            - 0.0252 * np.sin(E5)
            - 0.0066 * np.sin(E6)
            - 0.0047 * np.sin(E7)
            - 0.0027 * np.sin(E8)
            + 0.0048 * np.sin(E10)
            + 0.0028 * np.sin(E11)
            + 0.0052 * np.sin(E12)
            - 0.0040 * np.sin(E13)
        )
        % 360
    )

    return alpha0, delta0, W


def calculate_moon_illumination_and_waxing(
    phase_angle_deg: Union[float, np.ndarray],
) -> Tuple[Union[float, np.ndarray], Any]:
    """
    Calculates Moon illumination percentage and waxing boolean flag given phase angle in degrees.
    """
    if np.isscalar(phase_angle_deg):
        is_waxing = 0 < phase_angle_deg < 180  # type: ignore
    else:
        is_waxing = (0 < phase_angle_deg) & (phase_angle_deg < 180)  # type: ignore

    illumination = (1 - np.cos(np.deg2rad(phase_angle_deg))) / 2 * 100
    return illumination, is_waxing


def calculate_moon_phase_name(
    phase_angle_deg: float,
) -> str:
    """
    Returns translated phase name given Moon phase angle in degrees.
    """
    if phase_angle_deg < 1.0 or phase_angle_deg > 359.0:
        return gettext_("New Moon")
    elif phase_angle_deg < 89.0:
        return gettext_("Waxing Crescent")
    elif phase_angle_deg < 91.0:
        return gettext_("First Quarter")
    elif phase_angle_deg < 179.0:
        return gettext_("Waxing Gibbous")
    elif phase_angle_deg < 181.0:
        return gettext_("Full Moon")
    elif phase_angle_deg < 269.0:
        return gettext_("Waning Gibbous")
    elif phase_angle_deg < 271.0:
        return gettext_("Last Quarter")
    else:
        return gettext_("Waning Crescent")


def calculate_moon_position_angle_bright_limb(
    ra_moon_rad: float,
    dec_moon_rad: float,
    ra_sun_rad: float,
    dec_sun_rad: float,
) -> float:
    """
    Calculates the position angle of the Moon's bright limb in degrees counterclockwise from North
    given RA and Dec in radians for Moon and Sun. Reference: Meeus, Ch. 48.
    """
    num = np.cos(dec_sun_rad) * np.sin(ra_sun_rad - ra_moon_rad)
    den = np.cos(dec_moon_rad) * np.sin(dec_sun_rad) - np.sin(dec_moon_rad) * np.cos(dec_sun_rad) * np.cos(ra_sun_rad - ra_moon_rad)
    pa_rad = np.arctan2(num, den)
    return float(np.degrees(pa_rad) % 360)


def calculate_moon_selenographic_coords(
    v_target_au: np.ndarray,
    alpha0_rad: Union[float, np.ndarray],
    delta0_rad: Union[float, np.ndarray],
    W_rad: Union[float, np.ndarray],
    is_array: bool = False,
) -> Tuple[Union[float, np.ndarray], Union[float, np.ndarray]]:
    """
    Calculates selenographic longitude and latitude in degrees given position vector in AU and orientation parameters.
    """
    if is_array:
        u_v = v_target_au / np.linalg.norm(v_target_au, axis=0)
    else:
        u_v = v_target_au / np.linalg.norm(v_target_au)

    x_node = u_v[0] * (-np.sin(alpha0_rad)) + u_v[1] * np.cos(alpha0_rad)
    y_node = (
        u_v[0] * (-np.sin(delta0_rad) * np.cos(alpha0_rad))
        + u_v[1] * (-np.sin(delta0_rad) * np.sin(alpha0_rad))
        + u_v[2] * np.cos(delta0_rad)
    )
    z = (
        u_v[0] * (np.cos(delta0_rad) * np.cos(alpha0_rad))
        + u_v[1] * (np.cos(delta0_rad) * np.sin(alpha0_rad))
        + u_v[2] * np.sin(delta0_rad)
    )

    lat_deg = np.degrees(np.arcsin(np.clip(z, -1.0, 1.0)))
    phi = np.degrees(np.arctan2(y_node, x_node))
    lon_deg = (phi - np.degrees(W_rad) + 180) % 360 - 180

    def _maybe_float(val):
        return float(cast(Any, val)) if np.isscalar(val) else val

    return _maybe_float(lon_deg), _maybe_float(lat_deg)
