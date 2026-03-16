import numpy
from apts.opticalequipment.camera import Camera
from apts.opticalequipment.smart_telescope import SmartTelescope
from apts.opticalequipment.telescope import Telescope
from apts.optics import OpticalPath

def test_camera_dynamic_range():
    # ZWO ASI2600MC Pro: Full well 50,000e-, Read noise 1.0e- (at high gain)
    c = Camera(23.5, 15.7, 6248, 4176, full_well=50000, read_noise=1.0)
    # DR = log2(50000 / 1.0) = log2(50000) ~ 15.61 stops
    dr = c.dynamic_range()
    assert dr is not None
    assert numpy.isclose(dr, numpy.log2(50000))

def test_smart_telescope_dynamic_range():
    # Seestar S50: Full well ~12000e-, Read noise ~1.5e-
    s = SmartTelescope(50, 250, 5.6, 3.2, 1920, 1080, full_well=12000, read_noise=1.5)
    # DR = log2(12000 / 1.5) = log2(8000) ~ 12.96 stops
    dr = s.dynamic_range()
    assert dr is not None
    assert numpy.isclose(dr, numpy.log2(8000))

def test_optical_path_dynamic_range():
    t = Telescope(150, 750)
    c = Camera(23.5, 15.7, 6248, 4176, full_well=50000, read_noise=1.0)
    path = OpticalPath(t, [], [], [], [], c)

    dr = path.dynamic_range()
    assert dr is not None
    assert numpy.isclose(dr, numpy.log2(50000))

def test_nyquist_focal_ratio():
    t = Telescope(150, 750)
    # Pixel size 3.76um
    c = Camera(23.5, 15.7, 6248, 4176, pixel_size=3.76)
    path = OpticalPath(t, [], [], [], [], c)

    # λ = 550nm = 0.55um
    # s = 3.0
    # f/D = (3.76 * 3.0) / (1.22 * 0.55) = 11.28 / 0.671 = 16.81
    nfr = path.nyquist_focal_ratio(wavelength_nm=550, sampling_factor=3.0)
    assert nfr is not None
    assert numpy.isclose(nfr, (3.76 * 3.0) / (1.22 * 0.55))

def test_dynamic_range_none_cases():
    # Camera with missing data
    c_none = Camera(23.5, 15.7, 6248, 4176)
    assert c_none.dynamic_range() is None

    # Camera with zero read noise (edge case)
    c_zero = Camera(23.5, 15.7, 6248, 4176, full_well=50000, read_noise=0)
    assert c_zero.dynamic_range() is None

    # Optical path with visual output
    t = Telescope(150, 750)
    path_visual = OpticalPath(t, [], [], [], [], t)
    assert path_visual.dynamic_range() is None
