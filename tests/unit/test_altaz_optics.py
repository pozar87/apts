import pytest
import numpy as np
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.vendors.zwo import ZwoTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.units import get_unit_registry

def test_field_rotation_rate():
    # Setup a simple optical path
    # Use a generic telescope and camera
    telescope = ZwoTelescope.ZWO_Seestar_S50() # SmartTelescope
    path = OpticalPath.from_path([telescope])

    # Earth sidereal rate ~15.041 "/s
    # Case 1: Equator (lat=0), Horizon (alt=0), Meridian (az=0)
    # rate = 15.041 * cos(0) * cos(0) / cos(0) = 15.041
    rate = path.field_rotation_rate(0, 0, 0)
    assert rate.magnitude == pytest.approx(15.041067, rel=1e-5)

    # Case 2: Pole (lat=90), any direction
    # rate = 15.041 * cos(90) * cos(az) / cos(alt) = 0
    rate = path.field_rotation_rate(90, 0, 45)
    assert rate.magnitude == pytest.approx(0, abs=1e-10)

    # Case 3: North latitude (lat=45), East (az=90), at altitude 30
    # cos(90) = 0, so rate should be 0
    rate = path.field_rotation_rate(45, 30, 90)
    assert rate.magnitude == pytest.approx(0, abs=1e-10)

def test_max_exposure_alt_az():
    # Use Seestar S50 specs: 250mm FL, IMX462 (5.6x3.2mm, 1920x1080, 2.9um)
    telescope = ZwoTelescope.ZWO_Seestar_S50()
    path = OpticalPath.from_path([telescope])

    # Calculate for lat=45, alt=45, az=0 (South/North)
    # rate = 15.041 * cos(45) * cos(0) / cos(45) = 15.041 "/s
    # Pixel scale for 250mm, 2.9um = (2.9/250)*206265 = 2.392674 "/px
    # Diagonal radius in px = 0.5 * sqrt(1920^2 + 1080^2) = 0.5 * 2202.9 = 1101.45 px
    # max_exposure = (1.0 * 206265) / (1101.45 * 15.041) = 206265 / 16566.9 = 12.45 s

    max_exp = path.max_exposure_alt_az(45, 45, 0, tolerance_px=1.0)
    assert max_exp.magnitude == pytest.approx(12.45, rel=1e-2)
