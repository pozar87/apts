import numpy
from typing import Any, cast
from apts.opticalequipment.camera import Camera
from apts.opticalequipment.telescope import Telescope, TubeMaterial
from apts.optics import OpticalPath

def test_camera_astrophotography_fields():
    c = Camera(sensor_width=36, sensor_height=24, width=6000, height=4000,
               read_noise=1.2, full_well=50000, quantum_efficiency=80, pixel_size=3.76)
    assert c.read_noise == 1.2
    assert c.full_well == 50000
    assert c.quantum_efficiency == 80
    assert cast(Any, c.pixel_size()).to("micrometer").magnitude == 3.76

def test_telescope_astrophotography_fields():
    t = Telescope(aperture=150, focal_length=750, focuser_step_size=1.5, tube_material=TubeMaterial.CARBON_FIBER)
    assert t.focuser_step_size == 1.5
    assert t.tube_material == TubeMaterial.CARBON_FIBER

def test_optical_path_astrophotography():
    t = Telescope(aperture=150, focal_length=750)
    c = Camera(sensor_width=36, sensor_height=24, width=6000, height=4000, pixel_size=3.76, read_noise=1.2, quantum_efficiency=80)
    path = OpticalPath(t, [], [], [], c)

    # Pixel scale: (3.76 / 750) * 206265 = 1.0340752
    scale = path.pixel_scale()
    assert numpy.isclose(cast(Any, scale).to("arcsecond").magnitude, 1.0340752, atol=1e-4)

    # Sampling
    assert path.sampling(seeing=2.0) == "Well-sampled" # 2.0 / 1.03 = 1.94
    assert path.sampling(seeing=0.5) == "Under-sampled" # 0.5 / 1.03 = 0.48
    assert path.sampling(seeing=3.0) == "Over-sampled" # 3.0 / 1.03 = 2.91

    # CFZ
    # 2.44 * 0.55 * (750/150)^2 = 2.44 * 0.55 * 25 = 33.55
    cfz = path.critical_focus_zone(wavelength=550)
    assert numpy.isclose(cast(Any, cfz).to("micrometer").magnitude, 33.55)

    # Thermal drift
    # Aluminum alpha = 23.1e-6. 750 * 23.1e-6 * 1 = 0.017325 mm = 17.325 microns
    t.tube_material = TubeMaterial.ALUMINUM
    drift = path.thermal_drift(delta_t=1.0)
    assert numpy.isclose(cast(Any, drift).to("micrometer").magnitude, 17.325)

    # Sky flux
    # sqm=21. Area = pi * (7.5)^2 = 176.71 cm2. QE=0.8. PixelScale=1.03476.
    # flux = 0.005 * 10^(0.4*(21.83-21)) * 176.71 * 0.8 * (1.03476)^2
    # 10^(0.4*0.83) = 10^0.332 = 2.1478
    # flux = 0.005 * 2.1478 * 176.71 * 0.8 * 1.0707 = 1.626
    flux = path.sky_flux(sqm=21)
    assert numpy.isclose(cast(Any, flux), 1.626, atol=1e-2)

    # Optimum sub-exposure
    # (10 * 1.2^2) / 1.626 = 14.4 / 1.626 = 8.85
    opt_exp = path.optimum_sub_exposure(sqm=21)
    assert numpy.isclose(cast(Any, opt_exp).to("second").magnitude, 8.85, atol=1e-1)

    # Limiting magnitude
    # base = 7.7 + 5*log10(15) = 7.7 + 5*1.176 = 7.7 + 5.88 = 13.58
    # time_factor = 1.25 * log10(60) = 1.25 * 1.778 = 2.22
    # sqm_factor = 21 - 21 = 0
    # expected = 13.58 + 2.22 = 15.8
    lim_mag = path.limiting_magnitude(sqm=21, integration_time=60)
    assert numpy.isclose(lim_mag, 15.8, atol=0.1)
