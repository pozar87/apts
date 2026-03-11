import pytest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.opticalequipment.smart_telescope import SmartTelescope

def test_celestron_origin_instantiation():
    origin = CelestronTelescope.Celestron_Origin()
    assert isinstance(origin, SmartTelescope)
    assert origin.aperture.magnitude == 152
    assert origin.focal_length.magnitude == 335
    assert origin.width == 3096
    assert origin.height == 2080
    assert origin.pixel_size().magnitude == pytest.approx(2.4, abs=0.01)
    assert origin.mass.magnitude == 18870
