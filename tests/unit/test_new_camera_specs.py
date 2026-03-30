import pytest
from apts.opticalequipment.camera.vendors.nikon import NikonCamera
from apts.opticalequipment.camera.vendors.sony import SonyCamera

def test_nikon_z50ii_specs():
    cam = NikonCamera.Nikon_Z50II()
    assert cam.vendor == "Nikon Z50II"
    assert cam.width == 5568
    assert cam.height == 3712
    assert pytest.approx(cam.sensor_width.magnitude) == 23.5
    assert pytest.approx(cam.sensor_height.magnitude) == 15.7
    assert pytest.approx(cam.pixel_size().magnitude) == 4.22
    assert pytest.approx(cam.mass.magnitude) == 495
    assert pytest.approx(cam.optical_length.magnitude) == 16

def test_sony_a1ii_specs():
    cam = SonyCamera.Sony_A1_II()
    assert cam.vendor == "Sony A1 II"
    assert cam.width == 8640
    assert cam.height == 5760
    assert pytest.approx(cam.sensor_width.magnitude) == 35.9
    assert pytest.approx(cam.sensor_height.magnitude) == 24.0
    assert pytest.approx(cam.pixel_size().magnitude) == 4.16
    assert pytest.approx(cam.mass.magnitude) == 743
    assert pytest.approx(cam.optical_length.magnitude) == 18
