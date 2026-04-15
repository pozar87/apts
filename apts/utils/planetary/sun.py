import numpy as np
from typing import Any, cast

from apts.cache import get_ephemeris


def get_sun_physical_details(time: Any) -> dict:
    """
    Calculates the physical details of the Sun for a given time.
    - P_degrees: Position angle of the Sun's North Pole (degrees).
    - B0_degrees: Heliographic latitude of the Earth (degrees).
    - L0_degrees: Carrington longitude of the central meridian (degrees).

    Source: Jean Meeus, Astronomical Algorithms, Chapter 29.
    """
    jd = time.tt
    # Time in Julian centuries from J2000.0
    T = (jd - 2451545.0) / 36525.0

    # Solar elements:
    # Longitude of the ascending node of the solar equator on the ecliptic (Omega)
    # Using Meeus formula (accuracy ~0.01 deg)
    omega = np.radians(73.6667 + 1.395833 * (jd - 2396758.0) / 36525.0)
    inclination = np.radians(7.25)

    # Solar Apparent Longitude (lambda) and Obliquity (epsilon) from Skyfield
    eph = get_ephemeris()
    sun = eph["sun"]
    earth = eph["earth"]
    astrometric = cast(Any, earth).at(time).observe(sun).apparent()

    # Solar Ecliptic Longitude (lambda) and Obliquity (epsilon)
    # For physical ephemeris, we need the geometric longitude, not apparent.
    # However, Meeus uses the apparent longitude corrected for aberration
    # and nutation for P, but for B0 and L0 he uses the longitude corrected
    # ONLY for aberration (mean equinox of date).
    _, lon, _ = astrometric.ecliptic_latlon()
    lam = lon.radians

    # Obliquity of the ecliptic (epsilon)
    # Simplified high-accuracy formula from Meeus
    eps = np.radians(
        23.4392911 - (46.8150 * T + 0.00059 * T**2 - 0.001813 * T**3) / 3600.0
    )

    # 1. Calculate P (Position Angle)
    # P = arctan(-cos(lam_app) * tan(eps)) + arctan(-cos(lam - omega) * tan(inclination))
    theta = lam - omega
    x = np.arctan(-np.cos(lam) * np.tan(eps))
    y = np.arctan(-np.cos(theta) * np.tan(inclination))
    p_rad = x + y

    # 2. Calculate B0 (Heliographic latitude of Earth)
    # sin(B0) = sin(lam - omega) * sin(inclination)
    sin_b0 = np.sin(theta) * np.sin(inclination)
    b0_rad = np.arcsin(sin_b0)

    # 3. Calculate L0 (Carrington longitude)
    # Correct formulas from Meeus (Chapter 29):
    # L = λ - 0.00569° - Ω
    # m = 360° - (360° / 25.38) * (JD - 2398220.0)
    # L0 = m - arctan2(sin(L) * cos(I), -cos(L))
    l_meeus = lam - omega
    l0_corr_rad = np.arctan2(np.sin(l_meeus) * np.cos(inclination), -np.cos(l_meeus))
    m_deg = 360.0 - (360.0 / 25.38) * (jd - 2398220.0)
    l0_deg = (m_deg - np.degrees(l0_corr_rad)) % 360

    return {
        "P_degrees": float(np.degrees(p_rad)),
        "B0_degrees": float(np.degrees(b0_rad)),
        "L0_degrees": float(l0_deg),
    }
