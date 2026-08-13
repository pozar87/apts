import pytest
import numpy as np

from apts.optics.calculations.eyepiece import calculate_eyepiece_field_of_view
from apts.optics.calculations.camera import (
    calculate_pixel_size,
    calculate_dynamic_range,
    calculate_camera_field_of_view,
)


def test_calculate_eyepiece_field_of_view():
    # 1. With field stop
    # Formula: 2 * degrees(arctan(field_stop / (2 * focal_length_eff)))
    # TFoV = 2 * atan(20 / 2000) = 2 * atan(0.01) rad approx 1.145762838175103 deg
    fov = calculate_eyepiece_field_of_view(
        field_stop_mm=20.0,
        apparent_fov_deg=70.0,
        focal_length_eff_mm=1000.0,
        zoom_magnitude=50.0,
    )
    expected = 2.0 * np.degrees(np.arctan(20.0 / 2000.0))
    assert fov == pytest.approx(expected, rel=1e-5)

    # 2. Without field stop (fallback to apparent fov / zoom)
    fov_fallback = calculate_eyepiece_field_of_view(
        field_stop_mm=None,
        apparent_fov_deg=70.0,
        focal_length_eff_mm=1000.0,
        zoom_magnitude=50.0,
    )
    assert fov_fallback == pytest.approx(70.0 / 50.0, rel=1e-5)

    # 3. Zoom is 0 fallback
    fov_zero_zoom = calculate_eyepiece_field_of_view(
        field_stop_mm=None,
        apparent_fov_deg=70.0,
        focal_length_eff_mm=1000.0,
        zoom_magnitude=0.0,
    )
    assert fov_zero_zoom == 0.0


def test_calculate_pixel_size():
    # 1. Explicit pixel size is returned directly
    pixel_size = calculate_pixel_size(
        pixel_size_um=3.76,
        sensor_width_mm=36.0,
        sensor_height_mm=24.0,
        width=6000,
        height=4000,
    )
    assert pixel_size == 3.76

    # 2. Calculated from sensor dimensions and resolution
    calculated_pixel_size = calculate_pixel_size(
        pixel_size_um=None,
        sensor_width_mm=36.0,
        sensor_height_mm=24.0,
        width=6000,
        height=4000,
    )
    expected_mm = np.sqrt(36.0**2 + 24.0**2) / np.sqrt(6000**2 + 4000**2)
    expected_um = expected_mm * 1000.0
    assert calculated_pixel_size == pytest.approx(expected_um, rel=1e-5)

    # 3. Resolution is 0
    zero_res = calculate_pixel_size(
        pixel_size_um=None,
        sensor_width_mm=36.0,
        sensor_height_mm=24.0,
        width=0,
        height=0,
    )
    assert zero_res == 0.0


def test_calculate_dynamic_range():
    # 1. Valid inputs
    # Full well: 50000, Read noise: 2 -> log2(25000) approx 15.60964
    dr = calculate_dynamic_range(full_well=50000.0, read_noise=2.0)
    assert dr == pytest.approx(np.log2(25000.0), rel=1e-5)

    # 2. Missing inputs / invalid read noise
    assert calculate_dynamic_range(full_well=None, read_noise=2.0) is None
    assert calculate_dynamic_range(full_well=50000.0, read_noise=None) is None
    assert calculate_dynamic_range(full_well=50000.0, read_noise=0.0) is None
    assert calculate_dynamic_range(full_well=50000.0, read_noise=-1.0) is None


def test_calculate_camera_field_of_view():
    # 1. Valid inputs
    # sensor width: 36, focal length: 750
    fov = calculate_camera_field_of_view(
        sensor_dimension_mm=36.0,
        focal_length_eff_mm=750.0,
    )
    expected = 2.0 * np.degrees(np.arctan(36.0 / (2.0 * 750.0)))
    assert fov == pytest.approx(expected, rel=1e-5)

    # 2. Focal length is 0 or negative
    assert calculate_camera_field_of_view(36.0, 0.0) == 0.0
    assert calculate_camera_field_of_view(36.0, -100.0) == 0.0
