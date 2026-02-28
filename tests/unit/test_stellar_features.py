import pytest
from typing import Any, cast
from apts.opticalequipment.telescope.base import Telescope
from apts.opticalequipment.camera.base import Camera
from apts.optics import OpticalPath

def test_skywatcher_quattro_database():
    # Verify Quattro 150P
    telescope = cast(Any, Telescope).Sky_Watcher_Quattro_150P()
    assert telescope.aperture.magnitude == 150
    assert telescope.focal_length.magnitude == 600
    assert telescope.central_obstruction.magnitude == 52
    assert telescope.mass.magnitude == 5700

    # Verify Quattro 200P
    telescope_200 = cast(Any, Telescope).Sky_Watcher_Quattro_200P()
    assert telescope_200.aperture.magnitude == 200
    assert telescope_200.focal_length.magnitude == 800
    assert telescope_200.mass.magnitude == 9500

def test_zwo_duo_cameras():
    # Verify MC Duo
    camera_mc = cast(Any, Camera).ZWO_ASI_2600MC_Duo()
    assert camera_mc.sensor_width.magnitude == 23.5
    assert camera_mc.pixel_size().to("micrometer").magnitude == pytest.approx(3.76)
    assert camera_mc.mass.magnitude == 800

    # Verify MM Duo
    camera_mm = cast(Any, Camera).ZWO_ASI_2600MM_Duo()
    assert camera_mm.quantum_efficiency == 91
    assert camera_mm.mass.magnitude == 800

def test_atmospheric_dispersion():
    telescope = Telescope(100, 500)
    camera = Camera(23.5, 15.7, 6000, 4000)
    path = OpticalPath(telescope, [], [], [], [], camera)

    # At zenith (90 deg altitude), dispersion should be 0
    disp_zenith = path.atmospheric_dispersion(90)
    assert disp_zenith.magnitude == 0

    # At 45 degrees
    disp_45 = path.atmospheric_dispersion(45)
    assert disp_45.magnitude > 0
    assert disp_45.magnitude < 5

def test_quattro_npf_rule():
    telescope = cast(Any, Telescope).Sky_Watcher_Quattro_200P() # 200/800 f/4
    camera = cast(Any, Camera).ZWO_ASI2600MM_PRO() # 3.76um
    path = OpticalPath(telescope, [], [], [], [], camera)

    # t = (35*4 + 30*3.76) / 800 = (140 + 112.8) / 800 = 252.8 / 800 = 0.316
    t = path.npf_rule(declination=0)
    assert cast(Any, t).magnitude == pytest.approx(0.316)
