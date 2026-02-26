from typing import Any, cast

import numpy
import pytest

from apts.opticalequipment.camera import Camera
from apts.opticalequipment.filter import Filter
from apts.opticalequipment.telescope import Telescope
from apts.optics import OpticalPath
from apts.units import get_unit_registry


def test_new_cameras():
    mc = cast(Any, Camera).ZWO_ASI294MC_PRO()
    assert mc.vendor == "ZWO ASI294MC Pro"
    assert mc.sensor_width.magnitude == 19.1
    assert mc.sensor_height.magnitude == 13.0
    assert mc.width == 4144
    assert mc.height == 2822
    assert mc.read_noise == 1.2
    assert mc.full_well == 63700
    assert mc.quantum_efficiency == 75
    assert cast(Any, mc._pixel_size).to("micrometer").magnitude == 4.63

    mm = cast(Any, Camera).ZWO_ASI294MM_PRO()
    assert mm.vendor == "ZWO ASI294MM Pro"
    assert mm.quantum_efficiency == 90
    assert mm.full_well == 66000


def test_sky_flux_with_filters():
    t = Telescope(aperture=150, focal_length=750)
    c = Camera(
        sensor_width=36,
        sensor_height=24,
        width=6000,
        height=4000,
        pixel_size=3.76,
        read_noise=1.2,
        quantum_efficiency=80,
    )
    f1 = Filter(name="L-Pro", transmission=0.9)
    f2 = Filter(name="Some Filter", transmission=0.8)

    path_no_filter = OpticalPath(t, [], [], [], [], c)
    path_with_filters = OpticalPath(t, [], [], [f1, f2], [], c)

    flux_no_filter = path_no_filter.sky_flux(sqm=21)
    flux_with_filters = path_with_filters.sky_flux(sqm=21)

    # Ensure fluxes are not None before calculation
    assert flux_no_filter is not None
    assert flux_with_filters is not None

    # Flux with filters should be 0.9 * 0.8 = 0.72 of flux without filters
    assert numpy.isclose(flux_with_filters, flux_no_filter * 0.72)


def test_object_flux():
    t = Telescope(aperture=150, focal_length=750)
    c = Camera(
        sensor_width=36,
        sensor_height=24,
        width=6000,
        height=4000,
        pixel_size=3.76,
        read_noise=1.2,
        quantum_efficiency=80,
    )
    path = OpticalPath(t, [], [], [], [], c)

    # If sqm == magnitude, object_flux should be sky_flux / pixel_area_arcsec2
    sqm = 21
    mag = 21
    s_flux = path.sky_flux(sqm=sqm)
    o_flux = path.object_flux(magnitude=mag)
    p_scale = path.pixel_scale()

    assert s_flux is not None
    assert o_flux is not None
    assert p_scale is not None

    scale = cast(Any, path.pixel_scale()).magnitude

    assert numpy.isclose(o_flux, s_flux / (scale**2))


def test_snr():
    t = Telescope(aperture=150, focal_length=750)
    c = Camera(
        sensor_width=36,
        sensor_height=24,
        width=6000,
        height=4000,
        pixel_size=3.76,
        read_noise=1.2,
        quantum_efficiency=80,
    )
    path = OpticalPath(t, [], [], [], [], c)

    # High SNR case: bright star, dark sky, long exposure
    snr_high = path.snr(magnitude=10, sqm=21, exposure_time=60)
    # Low SNR case: faint star, bright sky, short exposure
    snr_low = path.snr(magnitude=18, sqm=18, exposure_time=1)

    assert snr_high is not None
    assert snr_low is not None

    assert snr_high > snr_low
    assert snr_high > 0
    assert snr_low > 0

    # Stacking subs should increase SNR by sqrt(N) approximately (if not dominated by shot noise)
    snr_1 = path.snr(magnitude=15, sqm=21, exposure_time=30, n_subs=1)
    snr_4 = path.snr(magnitude=15, sqm=21, exposure_time=30, n_subs=4)

    assert snr_1 is not None
    assert snr_4 is not None

    assert numpy.isclose(snr_4, snr_1 * 2, rtol=0.1)


def test_stellar_limits_and_helpers():
    # 8-inch SCT (203.2 mm aperture, 2032 mm focal length)
    telescope = Telescope(203.2, 2032, vendor="Celestron C8")
    # ZWO ASI2600MM Pro (3.76 micron pixels)
    camera = Camera(23.5, 15.7, 6248, 4176, vendor="ZWO ASI2600MM Pro", pixel_size=3.76)

    path = OpticalPath(telescope, [], [], [], [], camera)

    # Dawes' Limit: 11.6 / 20.32 cm = 0.57086...
    assert cast(Any, path.dawes_limit()).magnitude == pytest.approx(0.571, abs=1e-3)

    # Rayleigh Limit: 1.22 * 550e-9 / 0.2032 * 206265 = 0.6808...
    assert cast(Any, path.rayleigh_limit()).magnitude == pytest.approx(0.681, abs=1e-3)

    # Ideal Planetary Focal Ratio: 5 * 3.76 = 18.8
    assert path.ideal_planetary_focal_ratio(k=5.0) == pytest.approx(18.8)
    # With k=3.0: 3 * 3.76 = 11.28
    assert path.ideal_planetary_focal_ratio(k=3.0) == pytest.approx(11.28)


def test_limits_without_telescope_support():
    # Create a mock-like object that doesn't have the methods
    class FakeOptic:
        def __init__(self):
            self.focal_length = 500 * get_unit_registry().mm

    path = OpticalPath(FakeOptic(), [], [], [], [], None)
    assert path.dawes_limit() is None
    assert path.rayleigh_limit() is None
    assert path.ideal_planetary_focal_ratio() is None
