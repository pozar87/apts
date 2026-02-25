from typing import Any, cast

import numpy

from apts.opticalequipment.camera import Camera
from apts.opticalequipment.filter import Filter
from apts.opticalequipment.telescope import Telescope
from apts.optics import OpticalPath


def test_new_cameras():
    mc = Camera.ZWO_ASI294MC_PRO()
    assert mc.vendor == "ZWO ASI294MC Pro"
    assert mc.sensor_width.magnitude == 19.1
    assert mc.sensor_height.magnitude == 13.0
    assert mc.width == 4144
    assert mc.height == 2822
    assert mc.read_noise == 1.2
    assert mc.full_well == 63700
    assert mc.quantum_efficiency == 75
    assert cast(Any, mc._pixel_size).to("micrometer").magnitude == 4.63

    mm = Camera.ZWO_ASI294MM_PRO()
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
