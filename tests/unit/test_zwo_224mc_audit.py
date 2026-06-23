import pytest
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

def test_zwo_224mc_audit():
    # Instantiate the camera
    camera = ZwoCamera.ZWO_ASI_224MC()

    # Assert audited mass
    # The mass in _DATABASE is 120 (grams)
    assert camera.mass.to("gram").magnitude == 120

    # Assert key specifications match official ZWO documentation
    assert camera.vendor == "ZWO ASI224MC"
    assert camera.width == 1304
    assert camera.height == 976
    assert camera.pixel_size().to("micrometer").magnitude == 3.75
    assert camera.sensor_width.to("mm").magnitude == 4.8
    assert camera.sensor_height.to("mm").magnitude == 3.6
    assert camera.full_well == 19200
    assert camera.read_noise == 0.8
    assert camera.quantum_efficiency == 80
    assert camera.optical_length.to("mm").magnitude == 12.5

    # Verify the factory method docstring update
    assert "Mass: 120g" in ZwoCamera.ZWO_ASI_224MC.__doc__
