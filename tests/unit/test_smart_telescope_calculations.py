import math

import pytest

from apts.opticalequipment.smart_telescope import (
    SmartTelescope,
    calculate_smart_telescope_dynamic_range,
    calculate_smart_telescope_fov_diagonal,
    calculate_smart_telescope_fov_height,
    calculate_smart_telescope_fov_width,
    calculate_smart_telescope_pixel_size,
    normalize_smart_telescope_database_entry,
)


def test_normalize_smart_telescope_database_entry():
    raw_entry = {
        "aperture": 50,
        "focal_length": 250,
        "sensor_width": 6.4,
        "sensor_height": 4.5,
        "width": 1920,
        "height": 1080,
    }
    normalized = normalize_smart_telescope_database_entry(raw_entry)
    assert normalized["brand"] == "Unknown"
    assert normalized["name"] == "Unknown"
    assert normalized["mass"] == 0
    assert normalized["vendor"] == "Unknown Unknown"
    assert normalized["aperture"] == 50
    assert normalized["focal_length"] == 250


def test_smart_telescope_from_database_normalization():
    raw_entry = {
        "brand": "DWARFLAB",
        "name": "DWARF 3",
        "aperture": 35,
        "focal_length": 150,
        "sensor_width": 5.6,
        "sensor_height": 3.1,
        "width": 3840,
        "height": 2160,
        "pixel_size_um": 1.4,
        "mass": 1350,
    }
    scope = SmartTelescope.from_database(raw_entry)
    assert scope.vendor == "DWARFLAB DWARF 3"
    assert scope.aperture.to("mm").magnitude == 35
    assert scope.focal_length.to("mm").magnitude == 150
    assert scope.sensor_width.to("mm").magnitude == 5.6
    assert scope.sensor_height.to("mm").magnitude == 3.1
    assert scope.width == 3840
    assert scope.height == 2160
    assert scope.pixel_size().to("micrometer").magnitude == 1.4


def test_calculate_smart_telescope_pixel_size():
    # Explicit pixel size
    assert calculate_smart_telescope_pixel_size(5.6, 3.1, 3840, 2160, pixel_size_um=1.4) == 1.4

    # Derived pixel size
    derived = calculate_smart_telescope_pixel_size(5.6, 3.1, 3840, 2160)
    expected_mm = math.sqrt(5.6**2 + 3.1**2) / math.sqrt(3840**2 + 2160**2)
    assert derived == pytest.approx(expected_mm * 1000.0)


def test_calculate_smart_telescope_dynamic_range():
    assert calculate_smart_telescope_dynamic_range(None, 1.5) is None
    assert calculate_smart_telescope_dynamic_range(12000, None) is None
    assert calculate_smart_telescope_dynamic_range(12000, 0) is None
    assert calculate_smart_telescope_dynamic_range(16384, 1.0) == pytest.approx(14.0)


def test_calculate_smart_telescope_fov():
    focal_length = 250.0
    sw = 6.4
    sh = 4.5

    fov_w = calculate_smart_telescope_fov_width(focal_length, sw)
    expected_w = 2.0 * math.degrees(math.atan(sw / (2.0 * focal_length)))
    assert fov_w == pytest.approx(expected_w)

    fov_h = calculate_smart_telescope_fov_height(focal_length, sh)
    expected_h = 2.0 * math.degrees(math.atan(sh / (2.0 * focal_length)))
    assert fov_h == pytest.approx(expected_h)

    fov_diag = calculate_smart_telescope_fov_diagonal(focal_length, sw, sh)
    diag = math.sqrt(sw**2 + sh**2)
    expected_diag = 2.0 * math.degrees(math.atan(diag / (2.0 * focal_length)))
    assert fov_diag == pytest.approx(expected_diag)

    # With Barlow/reducer
    fov_w_barlow = calculate_smart_telescope_fov_width(focal_length, sw, barlow_magnification=2.0)
    expected_w_barlow = 2.0 * math.degrees(math.atan(sw / (2.0 * (focal_length * 2.0))))
    assert fov_w_barlow == pytest.approx(expected_w_barlow)
