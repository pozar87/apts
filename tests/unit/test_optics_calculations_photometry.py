import numpy as np
import pytest
from apts.optics.calculations.photometry import (
    calculate_required_subs,
    calculate_optimum_sub_exposure,
    calculate_limiting_magnitude_simple,
    calculate_saturation_magnitude_analytical,
    calculate_saturation_magnitude,
    calculate_camera_limiting_magnitude,
    calculate_saturation_time
)

def test_calculate_required_subs():
    # Simple case: high signal, low noise
    # S=100, B=10, R=5, exp=1, target_snr=10
    # s=100, b=10*4=40, r=25*4=100
    # n = 100 * (100 + 40 + 100) / 10000 = 100 * 240 / 10000 = 2.4 -> ceil = 3
    n = calculate_required_subs(
        target_snr=10.0,
        obj_flux=100.0,
        sky_flux=10.0,
        read_noise=5.0,
        exposure_time=1.0,
        n_pix=4
    )
    assert n == 3.0

    # Zero flux case
    assert calculate_required_subs(10.0, 0.0, 10.0, 5.0, 1.0) == np.inf

def test_calculate_optimum_sub_exposure():
    # sky_flux=2, read_noise=4, swamp=10
    # t = 10 * 16 / 2 = 80
    t = calculate_optimum_sub_exposure(sky_flux=2.0, read_noise=4.0, swamp_factor=10.0)
    assert t == 80.0

    # Zero flux case
    assert calculate_optimum_sub_exposure(0.0, 4.0) == np.inf

def test_calculate_limiting_magnitude_simple():
    # aperture=10cm, sqm=21, integration=1s
    # base = 7.7 + 5 * log10(10) = 7.7 + 5 = 12.7
    # time_factor = 1.25 * log10(1) = 0
    # sqm_factor = 21 - 21 = 0
    # total = 12.7
    m = calculate_limiting_magnitude_simple(aperture_cm=10.0, sqm=21.0, integration_time=1.0)
    assert pytest.approx(m) == 12.7

    # aperture=10cm, sqm=19, integration=100s
    # base = 12.7
    # time_factor = 1.25 * log10(100) = 1.25 * 2 = 2.5
    # sqm_factor = 19 - 21 = -2.0
    # total = 12.7 + 2.5 - 2.0 = 13.2
    m = calculate_limiting_magnitude_simple(aperture_cm=10.0, sqm=19.0, integration_time=100.0)
    assert pytest.approx(m) == 13.2

def test_calculate_saturation_magnitude_analytical():
    # full_well=10000, flux_at_zero=1000000, exp=1, f=1
    # target_flux = 10000 / (1 * 1) = 10000
    # m_eff = -2.5 * log10(10000 / 1000000) = -2.5 * log10(0.01) = -2.5 * -2 = 5.0
    m = calculate_saturation_magnitude_analytical(
        full_well=10000.0,
        flux_at_zero_mag=1000000.0,
        exposure_time=1.0,
        psf_peak_fraction=1.0
    )
    assert pytest.approx(m) == 5.0

    # Invalid cases
    assert np.isnan(calculate_saturation_magnitude_analytical(10000, 1000000, 0, 1))
    assert np.isnan(calculate_saturation_magnitude_analytical(10000, 1000000, 1, 0))
    assert np.isnan(calculate_saturation_magnitude_analytical(10000, 0, 1, 1))


def test_calculate_saturation_magnitude():
    # Base analytical saturation magnitude = 5.0
    m_no_airmass = calculate_saturation_magnitude(
        full_well=10000.0,
        flux_at_zero_mag=1000000.0,
        exposure_time=1.0,
        psf_peak_fraction=1.0,
        airmass_val=None,
    )
    assert pytest.approx(m_no_airmass) == 5.0

    # With airmass = 2.0 and extinction_k = 0.2
    # m = 5.0 - 0.2 * 2.0 = 4.6
    m_with_airmass = calculate_saturation_magnitude(
        full_well=10000.0,
        flux_at_zero_mag=1000000.0,
        exposure_time=1.0,
        psf_peak_fraction=1.0,
        airmass_val=2.0,
        extinction_k=0.2,
    )
    assert pytest.approx(m_with_airmass) == 4.6

    # Invalid inputs -> None
    assert calculate_saturation_magnitude(10000, 1000000, 0, 1) is None


def test_calculate_camera_limiting_magnitude():
    # Setup a mock/dummy snr function:
    # Let's say SNR is: 5.0 when magnitude is 15.0,
    # SNR > 5.0 when mag < 15.0, and SNR < 5.0 when mag > 15.0.
    # Specifically, snr = 5.0 * (2.0 ** (15.0 - mag))
    def mock_snr(mag):
        return 5.0 * (2.0 ** (15.0 - mag))

    limit_mag = calculate_camera_limiting_magnitude(mock_snr, target_snr=5.0)
    assert limit_mag is not None
    # Since snr = 5.0 at mag = 15.0, binary search should converge to 15.0.
    assert pytest.approx(limit_mag, abs=0.02) == 15.0

    # Test when SNR function returns None (e.g. invalid inputs)
    def none_snr(mag):
        return None
    assert calculate_camera_limiting_magnitude(none_snr) is None


def test_calculate_saturation_time():
    # full_well = 10000, obj_flux = 100, psf_peak_fraction = 0.5
    # expected t = 10000 / (100 * 0.5) = 10000 / 50 = 200
    t = calculate_saturation_time(
        full_well=10000.0,
        obj_flux=100.0,
        psf_peak_fraction=0.5
    )
    assert t == 200.0

    # Invalid obj_flux <= 0 or psf_peak_fraction <= 0
    assert calculate_saturation_time(10000.0, 0.0, 0.5) is None
    assert calculate_saturation_time(10000.0, 100.0, -0.1) is None
