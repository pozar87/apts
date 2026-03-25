import pytest
import numpy as np
from apts.light_pollution import LightPollution
from apts.place import Place
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

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
    import datetime
    # Krakow (roughly)
    # Use a fixed date/time at night to avoid Sun/Moon brightness hitting the caps
    # On 2024-01-11 00:00 UTC, both Sun and Moon are below horizon in Krakow.
    date = datetime.datetime(2024, 1, 11, 0, 0, 0, tzinfo=datetime.timezone.utc)
    place = Place(50.06, 19.94, "Krakow", date=date)
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
    assert n_subs is not None
    assert n_subs > 0
    assert isinstance(n_subs, float)

    total_time = path.required_integration_time(target_snr, magnitude, sqm, exposure_time)
    assert total_time is not None
    assert total_time.magnitude == n_subs * exposure_time

    # Verify SNR at the calculated N is close to target
    calculated_snr = path.snr(magnitude, sqm, exposure_time, n_subs=int(n_subs))
    assert calculated_snr is not None
    assert abs(calculated_snr - target_snr) < 1.0 # Should be >= target_snr because of ceil

def test_camera_limiting_magnitude():
    telescope = Sky_watcherTelescope.Sky_Watcher_Esprit_100ED()
    camera = ZwoCamera.ZWO_ASI2600MC_PRO()
    path = OpticalPath.from_path([telescope, camera])

    sqm = 21.0
    total_time = 3600 # 1 hour
    sub_time = 300

    limit_mag = path.camera_limiting_magnitude(sqm, total_time, sub_time, target_snr=5.0)
    assert limit_mag is not None
    assert 15.0 < limit_mag < 25.0 # Reasonable range for 100mm scope

    # Verify SNR at limit is approx 5.0
    n_subs = np.ceil(total_time / sub_time)
    snr_at_limit = path.snr(limit_mag, sqm, sub_time, n_subs=int(n_subs))
    assert snr_at_limit is not None
    assert abs(snr_at_limit - 5.0) < 0.1

def test_snr_db_conversion():
    telescope = Sky_watcherTelescope.Sky_Watcher_Esprit_100ED()
    camera = ZwoCamera.ZWO_ASI2600MC_PRO()
    path = OpticalPath.from_path([telescope, camera])

    magnitude = 15.0
    sqm = 21.0
    exposure_time = 60

    snr_linear = path.snr(magnitude, sqm, exposure_time, in_db=False)
    snr_db = path.snr(magnitude, sqm, exposure_time, in_db=True)

    assert snr_linear is not None
    assert snr_db is not None
    # SNR in dB should be 20 * log10(SNR_linear)
    assert snr_db == pytest.approx(20.0 * np.log10(snr_linear))

    # Test edge case: SNR <= 0
    # Zero exposure time ensures zero signal and thus zero SNR
    snr_zero_linear = path.snr(magnitude, sqm, exposure_time=0.0)
    snr_zero_db = path.snr(magnitude, sqm, exposure_time=0.0, in_db=True)
    assert snr_zero_linear == 0.0
    assert snr_zero_db == -np.inf

def test_snr_extinction_verification():
    # Verify that SNR calculation accounts for atmospheric extinction
    telescope = Sky_watcherTelescope.Sky_Watcher_Esprit_100ED()
    camera = ZwoCamera.ZWO_ASI2600MC_PRO()
    path = OpticalPath.from_path([telescope, camera])

    magnitude = 10.0
    sqm = 21.0
    exposure_time = 60

    # Zenith (altitude 90, airmass 1.0)
    snr_zenith = path.snr(magnitude, sqm, exposure_time, altitude=90.0, extinction_k=0.2)
    # Near horizon (altitude 10, airmass ~5.6)
    snr_low = path.snr(magnitude, sqm, exposure_time, altitude=10.0, extinction_k=0.2)

    assert snr_zenith is not None
    assert snr_low is not None
    # Extinction should make the star fainter at lower altitudes, thus lower SNR
    assert snr_zenith > snr_low
