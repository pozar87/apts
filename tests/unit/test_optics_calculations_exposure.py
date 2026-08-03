import pytest
import math
from apts.optics.calculations.exposure import (
    calculate_estimated_star_trailing,
    calculate_max_exposure_alt_az,
    calculate_rule_of_500,
)


def test_calculate_estimated_star_trailing():
    # Base cases: zero pixel scale
    assert calculate_estimated_star_trailing(exposure_time=10.0, declination_deg=0.0, pixel_scale=0.0) == 0.0

    # Normal case: dec = 0, scale = 1.0, exposure = 10.0
    # expected = 15.041067 * 10 * cos(0) / 1.0 = 150.41067
    res = calculate_estimated_star_trailing(exposure_time=10.0, declination_deg=0.0, pixel_scale=1.0)
    assert pytest.approx(res, abs=1e-5) == 150.41067

    # Declination case: dec = 60, scale = 2.0, exposure = 20.0
    # expected = 15.041067 * 20 * cos(60) / 2.0 = 15.041067 * 20 * 0.5 / 2.0 = 75.205335
    res_dec = calculate_estimated_star_trailing(exposure_time=20.0, declination_deg=60.0, pixel_scale=2.0)
    assert pytest.approx(res_dec, abs=1e-5) == 75.205335


def test_calculate_max_exposure_alt_az():
    # Low rotation rate: rot_rate < 1e-10 should cap at 3600.0
    assert calculate_max_exposure_alt_az(rot_rate=0.0, sensor_width_pixels=1000, sensor_height_pixels=1000) == 3600.0
    assert calculate_max_exposure_alt_az(rot_rate=1e-11, sensor_width_pixels=1000, sensor_height_pixels=1000) == 3600.0

    # Normal case
    # rot_rate = 10.0 arcsec/s, width = 4000, height = 3000, tolerance = 1.0
    # r = 0.5 * sqrt(4000^2 + 3000^2) = 0.5 * 5000 = 2500
    # RAD_TO_ARCSEC = 206264.80624709636
    # expected = (1.0 * RAD_TO_ARCSEC) / (2500 * 10.0) = 206264.80624709636 / 25000 = 8.25059
    res = calculate_max_exposure_alt_az(rot_rate=10.0, sensor_width_pixels=4000.0, sensor_height_pixels=3000.0, tolerance_pixels=1.0)
    assert pytest.approx(res, abs=1e-5) == 8.25059


def test_calculate_rule_of_500():
    # Zero focal length
    assert calculate_rule_of_500(focal_length_mm=0.0) == 0.0

    # Simple case (no sensor dimensions, falls back to t = 500 / f_actual)
    # expected = 500 / 50 = 10.0
    assert calculate_rule_of_500(focal_length_mm=50.0) == 10.0

    # Normal sensor case: f_actual = 50.0, Full-frame (36x24), diagonal = sqrt(36^2 + 24^2) = 43.266615...
    # crop_factor = 43.27 / 43.266615 = 1.000078...
    # t = 500 / (50.0 * 1.000078) = 9.9992
    res = calculate_rule_of_500(focal_length_mm=50.0, sensor_width_mm=36.0, sensor_height_mm=24.0)
    diagonal = math.sqrt(36.0**2 + 24.0**2)
    crop_factor = 43.27 / diagonal
    expected = 500.0 / (50.0 * crop_factor)
    assert pytest.approx(res, abs=1e-5) == expected

    # Zero sensor diagonal case
    assert calculate_rule_of_500(focal_length_mm=50.0, sensor_width_mm=0.0, sensor_height_mm=0.0) == 10.0
