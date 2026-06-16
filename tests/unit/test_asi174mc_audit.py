import pytest
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.units import get_unit_registry
from apts.utils import ConnectionType, Gender

def test_asi174mc_audit():
    # Instantiate the audited camera
    cam = ZwoCamera.ZWO_ASI_174MC()
    ureg = get_unit_registry()

    # Verify physical specs
    assert cam.vendor == "ZWO ASI174MC"
    assert cam.mass.to(ureg.g).magnitude == 140

    # Verify sensor dimensions
    assert cam.sensor_width.to(ureg.mm).magnitude == 11.3
    assert cam.sensor_height.to(ureg.mm).magnitude == 7.1

    # Verify resolution
    assert cam.width == 1936
    assert cam.height == 1216

    # Verify pixel size
    assert cam.pixel_size().to(ureg.micrometer).magnitude == pytest.approx(5.86, rel=1e-3)

    # Verify performance specs
    assert cam.full_well == 32000
    assert cam.read_noise == 3.5
    assert cam.quantum_efficiency == 77

    # Verify connection
    assert cam.connection_type == ConnectionType.CS
    assert cam.connection_gender == Gender.FEMALE

    # Verify optical length
    assert cam.optical_length.to(ureg.mm).magnitude == 6.5
