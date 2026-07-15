import numpy as np
import pytest
from apts.optics.calculations.photometry import (
    calculate_required_subs,
    calculate_optimum_sub_exposure,
    calculate_limiting_magnitude_simple,
    calculate_saturation_magnitude_analytical
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
