import pytest
import numpy as np
from apts.opticalequipment.eyepiece.base import Eyepiece
from apts.opticalequipment.telescope.base import Telescope
from apts.units import get_unit_registry

def test_eyepiece_fov_calculation_field_stop():
    # Setup a telescope: 100mm aperture, 1000mm focal length
    telescope = Telescope(100, 1000, vendor="Test Scope")

    # Setup an eyepiece with 20mm field stop
    # Formula: TFoV = 2 * atan(field_stop / (2 * focal_length))
    # TFoV = 2 * atan(20 / 2000) = 2 * atan(0.01) rad
    # TFoV approx 1.14576 deg
    eyepiece = Eyepiece(20, vendor="Test Eyepiece", field_stop=20)

    # Magnification = 1000 / 20 = 50x
    zoom = 50.0
    barlow = 1.0

    fov = eyepiece.field_of_view(telescope, zoom, barlow)

    expected_fov = 2 * np.degrees(np.arctan(20 / (2 * 1000)))

    assert fov.units == get_unit_registry().deg
    assert fov.magnitude == pytest.approx(expected_fov, rel=1e-5)

def test_eyepiece_fov_calculation_fallback():
    # Setup a telescope: 100mm aperture, 1000mm focal length
    telescope = Telescope(100, 1000, vendor="Test Scope")

    # Setup an eyepiece without field stop, AFoV = 70 deg
    eyepiece = Eyepiece(20, vendor="Test Eyepiece", field_of_view=70)

    # Magnification = 1000 / 20 = 50x
    zoom = 50.0
    barlow = 1.0

    fov = eyepiece.field_of_view(telescope, zoom, barlow)

    # Fallback formula: TFoV = AFoV / zoom = 70 / 50 = 1.4 deg
    expected_fov = 1.4

    assert fov.units == get_unit_registry().deg
    assert fov.magnitude == pytest.approx(expected_fov, rel=1e-5)

def test_eyepiece_fov_calculation_with_barlow():
    # Setup a telescope: 100mm aperture, 1000mm focal length
    telescope = Telescope(100, 1000, vendor="Test Scope")

    # Setup an eyepiece with 20mm field stop
    eyepiece = Eyepiece(20, vendor="Test Eyepiece", field_stop=20)

    # Use a 2x Barlow
    barlow = 2.0
    # Magnification = (1000 * 2) / 20 = 100x
    zoom = 100.0

    fov = eyepiece.field_of_view(telescope, zoom, barlow)

    # f_eff = 1000 * 2 = 2000
    expected_fov = 2 * np.degrees(np.arctan(20 / (2 * 2000)))

    assert fov.units == get_unit_registry().deg
    assert fov.magnitude == pytest.approx(expected_fov, rel=1e-5)

def test_eyepiece_from_database_field_stop():
    entry = {
        'brand': 'TestBrand',
        'name': 'TestEyepiece',
        'focal_length_mm': 20,
        'field_of_view_deg': 70,
        'field_stop_mm': 25.4,
        'tside_thread': '1.25"',
        'tside_gender': 'Male'
    }

    eyepiece = Eyepiece.from_database(entry)

    assert eyepiece.focal_length.magnitude == 20
    assert eyepiece.field_stop.magnitude == 25.4
    assert eyepiece._field_of_view.magnitude == 70
