import numpy as np
from apts.opticalequipment.camera import Camera
from apts.opticalequipment.telescope import Telescope
from apts.optics import OpticalPath, OpticsUtils


def test_rayleigh_limit_wavelength():
    # 100mm aperture telescope
    t = Telescope(aperture=100, focal_length=500)

    # Standard 550nm: 1.22 * 550e-9 / 0.1 * 206265 = 1.384 arcsec
    limit_550 = t.rayleigh_limit(wavelength_nm=550)
    assert np.isclose(limit_550.magnitude, 1.384, atol=0.001)

    # H-alpha 656.3nm: 1.22 * 656.3e-9 / 0.1 * 206265 = 1.652 arcsec
    limit_656 = t.rayleigh_limit(wavelength_nm=656.3)
    assert np.isclose(limit_656.magnitude, 1.652, atol=0.001)

    # UV 350nm: 1.22 * 350e-9 / 0.1 * 206265 = 0.881 arcsec
    limit_350 = t.rayleigh_limit(wavelength_nm=350)
    assert np.isclose(limit_350.magnitude, 0.881, atol=0.001)

def test_airmass_calculation():
    # Zenith: alt=90 -> X=1.0
    assert np.isclose(OpticsUtils.calculate_airmass(90), 1.0, atol=0.001)

    # 30 deg altitude: Kasten-Young formula check
    # 1 / (sin(30) + 0.50572 * (30 + 6.07995)**-1.6364)
    # 1 / (0.5 + 0.50572 * 36.07995**-1.6364)
    # 1 / (0.5 + 0.50572 * 0.00282) = 1 / 0.50143 = 1.9943
    assert np.isclose(OpticsUtils.calculate_airmass(30), 1.994, atol=0.001)

    # 0 deg altitude (horizon):
    # 1 / (0 + 0.50572 * 6.07995**-1.6364)
    # 1 / (0.50572 * 0.0526) = 1 / 0.0266 = 37.59
    assert np.isclose(OpticsUtils.calculate_airmass(0), 37.917, atol=0.1) # Approx 38

def test_atmospheric_extinction():
    t = Telescope(aperture=100, focal_length=500)
    c = Camera(36, 24, 6000, 4000, pixel_size=3.76)
    path = OpticalPath(t, [], [], [], [], c)

    # Mag 10 star at 30 deg altitude, k=0.2
    # X ~ 1.994
    # m_app = 10 + 0.2 * 1.994 = 10.3988
    extinct_mag = path.atmospheric_extinction(10, 30, extinction_k=0.2)
    assert np.isclose(extinct_mag, 10.3988, atol=0.001)

def test_snr_with_altitude():
    t = Telescope(aperture=100, focal_length=500)
    # Give it 100% QE for easy math baseline if needed, but we use ASI6200 factory
    from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
    c = ZwoCamera.ZWO_ASI6200MM_PRO()
    path = OpticalPath(t, [], [], [], [], c)

    # SNR at zenith
    snr_zenith = path.snr(magnitude=10, sqm=21, exposure_time=60, altitude=90)
    # SNR at low altitude (more extinction -> less signal -> lower SNR)
    snr_low = path.snr(magnitude=10, sqm=21, exposure_time=60, altitude=10)

    assert snr_zenith is not None
    assert snr_low is not None
    assert snr_zenith > snr_low

    # Object flux should also be lower
    flux_zenith = path.object_flux(10, altitude=90)
    flux_low = path.object_flux(10, altitude=10)

    assert flux_zenith is not None
    assert flux_low is not None
    assert flux_zenith > flux_low

def test_new_camera_factory_methods():
    from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

    asi6200mm = ZwoCamera.ZWO_ASI6200MM_PRO()
    assert asi6200mm.vendor == "ZWO ASI6200MM Pro"
    assert asi6200mm.quantum_efficiency == 91
    assert asi6200mm.width == 9576

    asi533mm = ZwoCamera.ZWO_ASI533MM_PRO()
    assert asi533mm.vendor == "ZWO ASI533MM Pro"
    assert asi533mm.quantum_efficiency == 91
    assert asi533mm.sensor_width.magnitude == 11.31
