import sys
from unittest.mock import MagicMock

# Mock problematic dependencies
sys.modules['seaborn'] = MagicMock()
sys.modules['matplotlib'] = MagicMock()
sys.modules['matplotlib.pyplot'] = MagicMock()
sys.modules['pycairo'] = MagicMock()
sys.modules['cairo'] = MagicMock()
sys.modules['networkx'] = MagicMock()
sys.modules['requests_cache'] = MagicMock()
sys.modules['requests_mock'] = MagicMock()
sys.modules['timezonefinder'] = MagicMock()
sys.modules['Babel'] = MagicMock()
sys.modules['svgwrite'] = MagicMock()

import pytest
import numpy
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.vendors.celestron import Celestron_AstroMaster_70AZ
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.units import get_unit_registry

def test_field_rotation_rate():
    telescope = Celestron_AstroMaster_70AZ()
    camera = ZwoCamera.ZWO_ASI_220MM_Mini()
    path = OpticalPath(telescope, [], [], [], [], camera)

    # At latitude 45, Az 0 (North), Alt 45
    # ω = 15.041067 * cos(45) * cos(0) / cos(45) = 15.041067
    rate = path.field_rotation_rate(45, 0, 45)
    assert pytest.approx(rate.magnitude, 1e-5) == 15.041067
    assert rate.units == get_unit_registry().arcsecond / get_unit_registry().second

    # At zenith (capped at 89.99)
    rate_zenith = path.field_rotation_rate(90, 0, 45)
    # ω = 15.041067 * cos(45) * cos(0) / cos(89.99)
    # cos(45) approx 0.7071
    # cos(89.99) approx 0.0001745
    # ω approx 15.041 * 0.7071 / 0.0001745 approx 60945
    assert rate_zenith.magnitude > 60000

def test_max_exposure_alt_az():
    telescope = Celestron_AstroMaster_70AZ()
    camera = ZwoCamera.ZWO_ASI_220MM_Mini() # 1920x1080
    path = OpticalPath(telescope, [], [], [], [], camera)

    # Distance from center = sqrt(1920^2 + 1080^2) / 2 = 2202.9 / 2 = 1101.45 pixels
    # Rate at (45, 0, 45) = 15.041067 arcsec/s
    # t = (1.0 * 206265) / (15.041067 * 1101.45) = 206265 / 16566.9 = 12.45s
    max_exp = path.max_exposure_alt_az(45, 0, 45, tolerance_pixels=1.0)
    assert pytest.approx(max_exp.magnitude, 0.1) == 12.45
    assert max_exp.units == get_unit_registry().second

    # Zero rotation at Az 90 (East) or 270 (West)
    # ω = cos(90) = 0
    max_exp_zero = path.max_exposure_alt_az(45, 90, 45)
    assert max_exp_zero.magnitude == 3600
