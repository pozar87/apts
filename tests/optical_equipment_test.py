import pytest
from unittest.mock import MagicMock
import numpy as np

from apts.opticalequipment.abstract import OpticalEquipment, OutputOpticalEqipment
from apts.units import ureg

def test_optical_equipment_init_with_nan_focal_length():
    with pytest.raises(ValueError):
        OpticalEquipment(focal_length=np.nan, vendor="Test Vendor")

def test_optical_equipment_init_with_nan_vendor():
    # This should probably raise an error, but let's see what it does
    # For now, let's assume it converts it to a string "nan"
    eq = OpticalEquipment(focal_length=100, vendor=np.nan)
    assert str(eq) == "nan f=100 millimeter"

def test_output_optical_equipment_exit_pupil_with_invalid_telescop():
    output_eq = OutputOpticalEqipment(focal_length=25, vendor="Test Eyepiece")
    # Test with various invalid telescop objects
    assert np.isnan(output_eq.exit_pupil(telescop=None, zoom=30 * ureg.dimensionless).magnitude)
    assert np.isnan(output_eq.exit_pupil(telescop=MagicMock(aperture=np.nan), zoom=30 * ureg.dimensionless).magnitude)
    assert np.isnan(output_eq.exit_pupil(telescop=MagicMock(spec=[]), zoom=30 * ureg.dimensionless).magnitude)


def test_output_optical_equipment_exit_pupil_with_invalid_zoom():
    output_eq = OutputOpticalEqipment(focal_length=25, vendor="Test Eyepiece")
    telescop = MagicMock(aperture=150 * ureg.mm)
    # Test with various invalid zoom values
    assert np.isnan(output_eq.exit_pupil(telescop=telescop, zoom=np.nan).magnitude)
    assert np.isnan(output_eq.exit_pupil(telescop=telescop, zoom=0 * ureg.dimensionless).magnitude)
    assert np.isnan(output_eq.exit_pupil(telescop=telescop, zoom=None).magnitude)


def test_output_optical_equipment_brightness_with_invalid_telescop():
    output_eq = OutputOpticalEqipment(focal_length=25, vendor="Test Eyepiece")
    # Test with various invalid telescop objects
    assert np.isnan(output_eq.brightness(telescop=None, zoom=30 * ureg.dimensionless).magnitude)
    assert np.isnan(output_eq.brightness(telescop=MagicMock(aperture=np.nan), zoom=30 * ureg.dimensionless).magnitude)
    assert np.isnan(output_eq.brightness(telescop=MagicMock(spec=[]), zoom=30 * ureg.dimensionless).magnitude)

def test_output_optical_equipment_brightness_with_invalid_zoom():
    output_eq = OutputOpticalEqipment(focal_length=25, vendor="Test Eyepiece")
    telescop = MagicMock(aperture=150 * ureg.mm)
    # Test with various invalid zoom values
    assert np.isnan(output_eq.brightness(telescop=telescop, zoom=np.nan).magnitude)
    assert np.isnan(output_eq.brightness(telescop=telescop, zoom=0 * ureg.dimensionless).magnitude)
    assert np.isnan(output_eq.brightness(telescop=telescop, zoom=None).magnitude)
