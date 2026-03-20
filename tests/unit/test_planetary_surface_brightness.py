import pytest
import numpy as np
from datetime import datetime, timezone
from apts.utils import planetary
from apts.cache import get_timescale
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.vendors.zwo import ZwoTelescope

def test_get_planet_surface_brightness():
    ts = get_timescale()
    # March 18, 2026 - Jupiter around opposition
    t = ts.utc(2026, 3, 18, 12, 0, 0)

    # Integrated magnitude V for Jupiter is ~ -2.4
    # Angular diameter d is ~ 45 arcsec
    # Area A = pi * (45/2)^2 * k (where k is ~1.0 for opposition)
    # Area A ~ 1590 arcsec^2
    # S = -2.4 + 2.5 * log10(1590) ~ -2.4 + 2.5 * 3.2 ~ 5.6 mag/arcsec^2

    sb_jupiter = planetary.get_planet_surface_brightness("jupiter", t)
    assert 5.0 <= sb_jupiter <= 6.0

    # Sun surface brightness
    # V = -26.74, d = 1920 arcsec (approx 32 arcmin)
    # Area A = pi * (1920/2)^2 ~ 2,895,000 arcsec^2
    # S = -26.74 + 2.5 * log10(2,895,000) ~ -26.74 + 2.5 * 6.46 ~ -10.6 mag/arcsec^2
    sb_sun = planetary.get_planet_surface_brightness("sun", t)
    assert -11.0 <= sb_sun <= -10.0

    # Moon (Full)
    # V ~ -12.7, d ~ 1800 arcsec
    # Area A = pi * (1800/2)^2 ~ 2,544,000 arcsec^2
    # S = -12.7 + 2.5 * log10(2,544,000) ~ -12.7 + 2.5 * 6.4 ~ 3.3 mag/arcsec^2
    # Full moon occurs near March 3, 2026
    t_full_moon = ts.utc(2026, 3, 3, 12, 0, 0)
    sb_moon = planetary.get_planet_surface_brightness("moon", t_full_moon)
    assert 3.0 <= sb_moon <= 4.0

def test_optical_path_planetary_surface_brightness():
    ts = get_timescale()
    t = ts.utc(2026, 3, 18, 12, 0, 0)

    # Using Seestar S50 as a convenient setup
    seestar = ZwoTelescope.ZWO_Seestar_S50()
    path = OpticalPath.from_path([seestar])

    sb = path.planetary_surface_brightness("jupiter", t)
    assert isinstance(sb, float)
    assert 5.0 <= sb <= 6.0
