import numpy
from apts.opticalequipment.telescope.vendors.zwo import ZwoTelescope
from apts.optics import OpticalPath

def test_seestar_s50_optics():
    seestar = ZwoTelescope.ZWO_Seestar_S50()
    # Seestar S50: 50mm aperture, 250mm focal length
    # Sensor: 1920x1080, 5.6x3.2mm, 2.9um pixel
    # QE: 80%, RN: 1.0e-

    path = OpticalPath.from_path([seestar])

    # 1. Pixel Scale
    # (2.9 / 250) * 206265 = 2.392674 arcsec/pixel
    scale = path.pixel_scale()
    assert scale is not None
    assert numpy.isclose(scale.magnitude, 2.392674, atol=1e-4)

    # 2. Field of View (Height)
    # 2 * atan(3.2 / (2 * 250)) = 2 * atan(0.0064) = 2 * 0.36668 degrees = 0.73336 degrees
    fov_h = path.fov_height()
    assert numpy.isclose(fov_h.to("deg").magnitude, 0.73336, atol=1e-4)

    # 3. SNR Calculation
    # Should not be None now that SmartTelescope has sensor props and OpticalPath is refactored
    snr = path.snr(magnitude=10, sqm=21, exposure_time=10)
    assert snr is not None
    assert snr > 0

    # 4. Sampling
    # Rayleigh limit is ~2.768", Pixel scale is ~2.393"
    # For seeing = 2.0: R = max(2.0, 2.768) = 2.768. Ratio = 2.768 / 2.393 = 1.157 -> Well-sampled
    assert path.sampling(2.0) == "Well-sampled"
    # For seeing = 8.0: R = max(8.0, 2.768) = 8.0. Ratio = 8.0 / 2.393 = 3.34 -> Over-sampled
    assert path.sampling(8.0) == "Over-sampled"

def test_seestar_s50_flux():
    seestar = ZwoTelescope.ZWO_Seestar_S50()
    path = OpticalPath.from_path([seestar])

    s_flux = path.sky_flux(sqm=21)
    o_flux = path.object_flux(magnitude=15)

    assert s_flux is not None
    assert o_flux is not None
    assert s_flux > 0
    assert o_flux > 0
