import pytest
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.optics import OpticalPath
from apts.utils import planetary
from apts.cache import get_timescale

def test_asi664mc_specs():
    camera = ZwoCamera.ZWO_ASI_664MC()
    assert camera.get_vendor() == 'ZWO ASI664MC'
    assert camera.pixel_size().magnitude == 2.0
    assert camera.sensor_width.magnitude == 7.68
    assert camera.sensor_height.magnitude == 4.32
    assert camera.width == 3840
    assert camera.height == 2160
    assert camera.quantum_efficiency == 91
    assert camera.read_noise == 1.0

def test_nyquist_focal_ratio():
    camera = ZwoCamera.ZWO_ASI_664MC() # 2.0um
    telescope = Sky_watcherTelescope.Sky_Watcher_Explorer_150P()
    path = OpticalPath.from_path([telescope, camera])

    # Nyquist FR = (p * s) / (1.22 * lambda)
    # For p=2.0um, s=3.0, lambda=0.550um:
    # (2.0 * 3.0) / (1.22 * 0.550) = 6.0 / 0.671 = 8.9418...
    expected_fr = (2.0 * 3.0) / (1.22 * 0.550)
    assert path.nyquist_focal_ratio() == pytest.approx(expected_fr, rel=1e-4)

    # Test with different sampling factor
    # (2.0 * 2.0) / (1.22 * 0.550) = 4.0 / 0.671 = 5.9612...
    expected_fr_2 = (2.0 * 2.0) / (1.22 * 0.550)
    assert path.nyquist_focal_ratio(sampling_factor=2.0) == pytest.approx(expected_fr_2, rel=1e-4)

def test_planet_fraction_illuminated():
    ts = get_timescale()
    t = ts.utc(2024, 1, 1)

    # For Venus, it varies. Let's just check it returns a float between 0 and 1.
    fraction = planetary.get_planet_fraction_illuminated('venus', t)
    assert isinstance(fraction, float)
    assert 0.0 <= fraction <= 1.0

    # For Moon
    fraction_moon = planetary.get_planet_fraction_illuminated('moon', t)
    assert isinstance(fraction_moon, float)
    assert 0.0 <= fraction_moon <= 1.0

    # Verify it matches get_moon_illumination approximately
    # get_moon_illumination returns percentage
    perc_moon = planetary.get_moon_illumination(t)
    assert fraction_moon * 100 == pytest.approx(perc_moon, abs=0.1)
