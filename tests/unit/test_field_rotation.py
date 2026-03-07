import pytest
import numpy as np
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.vendors.zwo import ZwoTelescope
from apts.units import get_unit_registry

def test_field_rotation_rate():
    # Setup: Seestar S50
    telescope = ZwoTelescope.ZWO_Seestar_S50()
    path = OpticalPath.from_path([telescope])

    omega_e = 15.041067 # arcsec/s

    # 1. At latitude 45, looking North (Az=0) at altitude 45
    # rate = omega_e * cos(45) * cos(0) / cos(45) = omega_e
    rate = path.field_rotation_rate(45.0, 45.0, 0.0)
    assert pytest.approx(rate.magnitude, 1e-6) == omega_e

    # 2. At Equator (lat=0), looking East (Az=90)
    # rate = omega_e * cos(0) * cos(90) / cos(alt) = 0
    rate = path.field_rotation_rate(0.0, 30.0, 90.0)
    assert pytest.approx(rate.magnitude, 1e-6) == 0.0

    # 3. At North Pole (lat=90)
    # rate = omega_e * cos(90) * ... = 0
    rate = path.field_rotation_rate(90.0, 45.0, 180.0)
    assert pytest.approx(rate.magnitude, 1e-6) == 0.0

def test_max_exposure_alt_az():
    # Setup: Seestar S50
    # Aperture 50, FL 250, 1920x1080, 2.9um pixel
    telescope = ZwoTelescope.ZWO_Seestar_S50()
    path = OpticalPath.from_path([telescope])

    # Diagonal pixels = sqrt(1920^2 + 1080^2) approx 2202.9
    # r_pixels approx 1101.45
    # max_theta_rad = 1.0 / 1101.45 approx 0.0009078 rad
    # max_theta_arcsec = deg(0.0009078) * 3600 approx 187.25"

    # At lat 45, az 0, alt 45, rate = 15.041 "/s
    # T = 187.25 / 15.041 approx 12.45s

    t_max = path.max_exposure_alt_az(45.0, 45.0, 0.0, tolerance_px=1.0)
    assert t_max is not None
    assert pytest.approx(t_max.magnitude, 0.1) == 12.45

    # Very low rate should give high exposure cap
    t_max_low = path.max_exposure_alt_az(0.0, 30.0, 90.0)
    assert t_max_low.magnitude == 3600.0
