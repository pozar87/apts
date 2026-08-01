import pytest
import numpy as np
from apts.optics.calculations.planetary import (
    calculate_planetary_size_in_pixels,
    calculate_saturn_ring_size_in_pixels,
    calculate_max_planetary_rotation_duration,
)


def test_calculate_planetary_size_in_pixels():
    # Test scalar case
    # angular_diameter = 48.0, pixel_scale_magnitude = 0.5 => 96.0
    res = calculate_planetary_size_in_pixels(48.0, 0.5)
    assert res == 96.0

    # Test array case
    # angular_diameter = np.array([48.0, 24.0]), pixel_scale_magnitude = 0.5 => [96.0, 48.0]
    res_arr = calculate_planetary_size_in_pixels(np.array([48.0, 24.0]), 0.5)
    np.testing.assert_array_equal(res_arr, np.array([96.0, 48.0]))

    # Test zero pixel scale magnitude
    assert calculate_planetary_size_in_pixels(48.0, 0.0) is None


def test_calculate_saturn_ring_size_in_pixels():
    # Test scalar case
    res = calculate_saturn_ring_size_in_pixels(44.0, 22.0, 2.0)
    assert res == (22.0, 11.0)

    # Test array case
    majors = np.array([44.0, 88.0])
    minors = np.array([22.0, 44.0])
    res_arr = calculate_saturn_ring_size_in_pixels(majors, minors, 2.0)
    assert res_arr is not None
    np.testing.assert_array_equal(res_arr[0], np.array([22.0, 44.0]))
    np.testing.assert_array_equal(res_arr[1], np.array([11.0, 22.0]))

    # Test zero pixel scale magnitude
    assert calculate_saturn_ring_size_in_pixels(44.0, 22.0, 0.0) is None


def test_calculate_max_planetary_rotation_duration():
    # Test typical case (e.g., mock Jupiter parameters)
    # pixel_scale = 0.1, r_eq = 24.0, period = 35730.0, cos_de = 1.0, tolerance = 1.0
    # omega = 2 * pi * 24 * 1.0 / 35730.0 = 0.004221
    # t_max = 1.0 * 0.1 / 0.004221 = 23.69
    t_max = calculate_max_planetary_rotation_duration(
        pixel_scale_magnitude=0.1,
        r_eq=24.0,
        period=35730.0,
        cos_de=1.0,
        tolerance_pixels=1.0,
    )
    assert pytest.approx(t_max, abs=1e-2) == 23.69

    # Test slow rotator / zero omega limit
    t_max_slow = calculate_max_planetary_rotation_duration(
        pixel_scale_magnitude=0.1,
        r_eq=24.0,
        period=1e16, # extremely long period to make omega <= 1e-12
        cos_de=1.0,
        tolerance_pixels=1.0,
    )
    assert t_max_slow == 3600.0

    # Test invalid parameters
    assert calculate_max_planetary_rotation_duration(0.1, -1.0, 35730.0, 1.0) is None
    assert calculate_max_planetary_rotation_duration(0.1, 24.0, -100.0, 1.0) is None
