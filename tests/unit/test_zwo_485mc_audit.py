import pytest

from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils import ConnectionType, Gender


def test_zwo_485mc_audit():
    # Instantiate the camera
    camera = ZwoCamera.ZWO_ASI_485MC()

    # Assert physical specifications
    assert camera.vendor == "ZWO ASI485MC"
    assert camera.mass.to("gram").magnitude == 133
    assert camera.optical_length.to("mm").magnitude == 12.5

    # Assert sensor specifications
    assert camera.full_well == 13000
    assert camera.pixel_size().to("micrometer").magnitude == 2.9
    assert camera.quantum_efficiency == 85
    assert camera.read_noise == 1.0
    assert camera.width == 3840
    assert camera.height == 2160
    assert camera.sensor_width.to("mm").magnitude == pytest.approx(11.14, abs=1e-2)
    assert camera.sensor_height.to("mm").magnitude == pytest.approx(6.26, abs=1e-2)

    # Assert connection types
    assert camera.connection_type == ConnectionType.CS
    assert camera.connection_gender == Gender.FEMALE
