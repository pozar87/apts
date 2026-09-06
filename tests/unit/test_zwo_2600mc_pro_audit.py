from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.utils import ConnectionType, Gender


def test_zwo_2600mc_pro_audit():
    # Instantiate the camera
    camera = ZwoCamera.ZWO_ASI_2600MC_Pro()

    # Assert vendor name and physical specifications
    assert camera.vendor == "ZWO ASI2600MC Pro"
    assert camera.mass.to("gram").magnitude == 700
    assert camera.optical_length.to("mm").magnitude == 17.5

    # Assert sensor and optical specifications
    assert camera.full_well == 50000
    assert camera.pixel_size().to("micrometer").magnitude == 3.76
    assert camera.quantum_efficiency == 80
    assert camera.read_noise == 1.0
    assert camera.width == 6248
    assert camera.height == 4176
    assert camera.sensor_width.to("mm").magnitude == 23.5
    assert camera.sensor_height.to("mm").magnitude == 15.7

    # Assert connections
    assert camera.connection_type == ConnectionType.M42
    assert camera.connection_gender == Gender.FEMALE
