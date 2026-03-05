import pytest
from apts.light_pollution import LightPollution
from apts.place import Place
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
import numpy as np

def test_bortle_to_sqm():
    # Test midpoints
    assert LightPollution.bortle_to_sqm(1.0) == 21.88
    assert LightPollution.bortle_to_sqm(5.0) == 19.77
    assert LightPollution.bortle_to_sqm(9.0) == 16.0

    # Test interpolation
    # Between 1.0 (21.88) and 2.0 (21.67)
    sqm_1_5 = LightPollution.bortle_to_sqm(1.5)
    assert 21.67 < sqm_1_5 < 21.88

    # Test boundaries
    assert LightPollution.bortle_to_sqm(0.5) == 21.88
    assert LightPollution.bortle_to_sqm(10.0) == 16.0

def test_place_get_sqm():
    # Krakow (roughly)
    place = Place(50.06, 19.94, "Krakow")
    # This should trigger light pollution calculation
    sqm = place.get_sqm()
    assert 16.0 <= sqm <= 22.0

def test_snr_solvers():
    telescope = Sky_watcherTelescope.Sky_Watcher_Esprit_100ED()
    camera = ZwoCamera.ZWO_ASI2600MC_PRO()
    path = OpticalPath.from_path([telescope, camera])

    target_snr = 10.0
    magnitude = 22.0
    sqm = 21.0
    exposure_time = 300 # seconds

    n_subs = path.required_subs_for_snr(target_snr, magnitude, sqm, exposure_time)
    assert n_subs > 0
    assert isinstance(n_subs, float)

    total_time = path.required_integration_time(target_snr, magnitude, sqm, exposure_time)
    assert total_time.magnitude == n_subs * exposure_time

    # Verify SNR at the calculated N is close to target
    calculated_snr = path.snr(magnitude, sqm, exposure_time, n_subs=n_subs)
    assert abs(calculated_snr - target_snr) < 1.0 # Should be >= target_snr because of ceil

def test_camera_limiting_magnitude():
    telescope = Sky_watcherTelescope.Sky_Watcher_Esprit_100ED()
    camera = ZwoCamera.ZWO_ASI2600MC_PRO()
    path = OpticalPath.from_path([telescope, camera])

    sqm = 21.0
    total_time = 3600 # 1 hour
    sub_time = 300

    limit_mag = path.camera_limiting_magnitude(sqm, total_time, sub_time, target_snr=5.0)
    assert 15.0 < limit_mag < 25.0 # Reasonable range for 100mm scope

    # Verify SNR at limit is approx 5.0
    n_subs = np.ceil(total_time / sub_time)
    snr_at_limit = path.snr(limit_mag, sqm, sub_time, n_subs=n_subs)
    assert abs(snr_at_limit - 5.0) < 0.1
