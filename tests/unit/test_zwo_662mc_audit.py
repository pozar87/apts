import pytest
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils import ConnectionType, Gender

def test_zwo_662mc_audit():
    # Instantiate the camera
    camera = ZwoCamera.ZWO_ASI_662MC()

    # Assert physical specifications
    assert camera.vendor == "ZWO ASI662MC"
    assert camera.mass.to("gram").magnitude == 126
    assert camera.optical_length.to("mm").magnitude == 12.5

    # Assert sensor specifications
    assert camera.full_well == 37800
    assert camera.pixel_size().to("micrometer").magnitude == 2.9
    assert camera.quantum_efficiency == 91
    assert camera.read_noise == 0.8
    assert camera.width == 1920
    assert camera.height == 1080
    assert camera.sensor_width.to("mm").magnitude == 5.568
    assert camera.sensor_height.to("mm").magnitude == 3.132

    # Assert connections (using centralized enums as per convention)
    assert camera.connection_type == ConnectionType.M42
    assert camera.connection_gender == Gender.FEMALE
