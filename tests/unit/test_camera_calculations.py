import math

import pytest

from apts.opticalequipment.camera import (
    Camera,
    calculate_camera_fov_diagonal,
    calculate_camera_fov_height,
    calculate_camera_fov_width,
    calculate_sensor_diagonal,
    normalize_camera_database_entry,
)
from apts.utils import ConnectionType, Gender


def test_normalize_camera_database_entry_complete():
    entry = {
        "brand": "ZWO",
        "name": "ASI533MC Pro",
        "sensor_width_mm": 11.31,
        "sensor_height_mm": 11.31,
        "width": 3008,
        "height": 3008,
        "inputs": [(ConnectionType.M42, Gender.FEMALE)],
    }
    normalized = normalize_camera_database_entry(entry)
    assert normalized["sensor_width_mm"] == 11.31
    assert normalized["sensor_height_mm"] == 11.31
    assert normalized["width"] == 3008
    assert normalized["height"] == 3008
    assert normalized["inputs"] == [(ConnectionType.M42, Gender.FEMALE)]


def test_normalize_camera_database_entry_default_heuristics():
    entry = {
        "brand": "Generic",
        "name": "ApsC Camera",
        "tside_thread": "T2",
        "tside_gender": "Female",
    }
    normalized = normalize_camera_database_entry(entry)
    assert normalized["sensor_width_mm"] == 23.5
    assert normalized["sensor_height_mm"] == 15.7
    assert normalized["width"] == 6000
    assert normalized["height"] == 4000
    assert normalized["inputs"] == [(ConnectionType.T2, Gender.FEMALE)]


def test_normalize_camera_database_entry_full_frame_heuristics():
    entry = {
        "brand": "Canon",
        "name": "EOS Full Frame 36x24",
    }
    normalized = normalize_camera_database_entry(entry)
    assert normalized["sensor_width_mm"] == 35.9
    assert normalized["sensor_height_mm"] == 23.9
    assert normalized["width"] == 8256
    assert normalized["height"] == 5504


def test_normalize_camera_database_entry_mft_heuristics():
    entry = {
        "brand": "ZWO",
        "name": "ASI Micro Four Thirds",
    }
    normalized = normalize_camera_database_entry(entry)
    assert normalized["sensor_width_mm"] == 17.3
    assert normalized["sensor_height_mm"] == 13.0
    assert normalized["width"] == 4656
    assert normalized["height"] == 3520


def test_camera_class_normalize_and_from_database():
    raw_entry = {
        "brand": "ZWO",
        "name": "ASI533MC Pro",
        "sensor_width_mm": 11.31,
        "sensor_height_mm": 11.31,
        "width": 3008,
        "height": 3008,
        "tside_thread": "M42",
        "tside_gender": "Female",
    }
    normalized = Camera.normalize_database_entry(raw_entry)
    assert normalized["inputs"] == [(ConnectionType.M42, Gender.FEMALE)]

    cam = Camera.from_database(raw_entry)
    assert cam.sensor_width.magnitude == 11.31
    assert cam.sensor_height.magnitude == 11.31
    assert cam.width == 3008
    assert cam.height == 3008
    assert cam.vendor == "ZWO ASI533MC Pro"


def test_calculate_sensor_diagonal():
    diag = calculate_sensor_diagonal(36.0, 24.0)
    expected = math.sqrt(36.0**2 + 24.0**2)
    assert pytest.approx(diag, rel=1e-6) == expected


def test_calculate_camera_fov_calculations():
    # Full-frame sensor: 36mm x 24mm on a 1000mm focal length telescope
    fov_w = calculate_camera_fov_width(36.0, 1000.0, 1.0)
    fov_h = calculate_camera_fov_height(24.0, 1000.0, 1.0)
    fov_d = calculate_camera_fov_diagonal(36.0, 24.0, 1000.0, 1.0)

    # 2 * arctan(36 / 2000) in deg = 2 * arctan(0.018) ~ 2.0626 deg
    assert pytest.approx(fov_w.magnitude, rel=1e-4) == 2.0626
    # 2 * arctan(24 / 2000) in deg = 2 * arctan(0.012) ~ 1.3751 deg
    assert pytest.approx(fov_h.magnitude, rel=1e-4) == 1.3751

    # fov_d corresponds to diagonal sqrt(36^2 + 24^2) ~ 43.2666mm
    diag = math.sqrt(36.0**2 + 24.0**2)
    expected_d = math.degrees(2.0 * math.atan(diag / 2000.0))
    assert pytest.approx(fov_d.magnitude, rel=1e-4) == expected_d


def test_calculate_camera_fov_with_barlow():
    # Same sensor on a 1000mm scope with 2x Barlow (2000mm effective focal length)
    fov_w = calculate_camera_fov_width(36.0, 1000.0, 2.0)
    expected_w = math.degrees(2.0 * math.atan(36.0 / 4000.0))
    assert pytest.approx(fov_w.magnitude, rel=1e-4) == expected_w
