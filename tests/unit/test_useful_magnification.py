import pytest
from apts.opticalequipment.telescope import Telescope
from apts.opticalequipment.eyepiece import Eyepiece
from apts.opticalequipment.camera import Camera
from apts.optics import OpticalPath
from apts.units import get_unit_registry

def test_telescope_useful_magnification_limits():
    # 80mm Refractor
    t80 = Telescope(aperture=80, focal_length=600, vendor="80ED")
    assert t80.highest_useful_magnification() == 160.0
    assert t80.lowest_useful_magnification() == pytest.approx(11.428, rel=1e-3)

    # 200mm Newtonian
    t200 = Telescope(aperture=200, focal_length=1000, vendor="200PDS")
    assert t200.highest_useful_magnification() == 400.0
    assert t200.lowest_useful_magnification() == pytest.approx(28.571, rel=1e-3)

def test_optical_path_is_magnification_useful_visual():
    t80 = Telescope(aperture=80, focal_length=600, vendor="80ED")

    # 10mm Eyepiece -> 60x magnification (Useful)
    ep10 = Eyepiece(focal_length=10, vendor="10mm")
    path_ok = OpticalPath(t80, [], [], [], [], ep10)
    assert path_ok.zoom().magnitude == 60.0
    assert path_ok.is_magnification_useful() is True

    # 2mm Eyepiece -> 300x magnification (Too high for 80mm)
    ep2 = Eyepiece(focal_length=2, vendor="2mm")
    path_high = OpticalPath(t80, [], [], [], [], ep2)
    assert path_high.zoom().magnitude == 300.0
    assert path_high.is_magnification_useful() is False

    # 100mm Eyepiece (hypothetical) -> 6x magnification (Too low for 80mm/7mm pupil)
    ep100 = Eyepiece(focal_length=100, vendor="100mm")
    path_low = OpticalPath(t80, [], [], [], [], ep100)
    assert path_low.zoom().magnitude == 6.0
    assert path_low.is_magnification_useful() is False

def test_optical_path_is_magnification_useful_imaging():
    t80 = Telescope(aperture=80, focal_length=600, vendor="80ED")
    # ASI2600MC
    camera = Camera(23.5, 15.7, 6248, 4176, vendor="ASI2600MC")

    # Magnification doesn't matter for imaging in this context, should always be True
    path = OpticalPath(t80, [], [], [], [], camera)
    assert path.is_magnification_useful() is True
