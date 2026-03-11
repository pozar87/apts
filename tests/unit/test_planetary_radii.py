import pytest
from apts.utils import planetary
from apts.cache import get_timescale

def test_new_planet_radii_lookup():
    assert planetary.get_planet_radius_km("Ceres") == 473.0
    assert planetary.get_planet_radius_km("Haumea") == 816.0
    assert planetary.get_planet_radius_km("Makemake") == 715.0
    assert planetary.get_planet_radius_km("Eris") == 1163.0

def test_new_planet_angular_diameter():
    ts = get_timescale()
    t = ts.utc(2024, 1, 1, 12, 0)

    # Ceres angular diameter should be around 0.7-0.9 arcsec
    ceres_diam = planetary.get_planet_angular_diameter("Ceres", t)
    assert ceres_diam > 0
    assert ceres_diam < 2.0

    # Eris is much further away, should be very small (~0.05 arcsec)
    eris_diam = planetary.get_planet_angular_diameter("Eris", t)
    assert eris_diam > 0
    assert eris_diam < ceres_diam
