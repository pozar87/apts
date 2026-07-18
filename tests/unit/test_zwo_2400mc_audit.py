import pytest
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils import ConnectionType, Gender

def test_zwo_2400mc_audit():
    # Instantiate the camera
    camera = ZwoCamera.ZWO_ASI_2400MC_Pro()

    # Assert physical specifications
    assert camera.vendor == "ZWO ASI2400MC Pro"
    # Current value is 1000, corrected should be 730
    assert camera.mass.to("gram").magnitude == 730
    assert camera.optical_length.to("mm").magnitude == 17.5

    # Assert sensor specifications
    assert camera.full_well == 100000
    assert camera.pixel_size().to("micrometer").magnitude == 5.94
    assert camera.quantum_efficiency == 80
    assert camera.read_noise == 1.1
    assert camera.width == 6072
    assert camera.height == 4042
    assert camera.sensor_width.to("mm").magnitude == 36.0
    assert camera.sensor_height.to("mm").magnitude == 24.0

    # Assert connections
    # Current value is M42, corrected should be M54
    assert camera.connection_type == ConnectionType.M54
    assert camera.connection_gender == Gender.FEMALE
