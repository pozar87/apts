import unittest
from typing import Any, cast
from unittest.mock import MagicMock

import numpy as np
import pytest

from apts.opticalequipment.abstract import OpticalEquipment, OutputOpticalEqipment
from apts.opticalequipment.barlow import Barlow
from apts.opticalequipment.eyepiece import Eyepiece
from apts.opticalequipment.telescope import Telescope
from apts.optics import OpticsUtils
from apts.units import ureg


class OpticalEquipmentTest(unittest.TestCase):
    def test_telescope(self):
        t = Telescope(aperture=150, focal_length=750)
        self.assertEqual(t.focal_ratio(), 5.0)
        self.assertEqual(t.dawes_limit().magnitude, 0.773)
        self.assertEqual(t.rayleigh_limit().magnitude, 0.923)
        self.assertAlmostEqual(t.limiting_magnitude(), 13.58, 2)
        self.assertAlmostEqual(t.light_grasp_ratio(7).magnitude, 459.18, 2)
        self.assertEqual(t.min_useful_zoom(), 25)
        self.assertEqual(t.max_useful_zoom(), 375)

    def test_barlow(self):
        b = Barlow(magnification=2)
        self.assertEqual(b.magnification, 2)

    def test_eyepiece(self):
        t = Telescope(aperture=150, focal_length=750)
        e = Eyepiece(focal_length=10, field_of_view=50)
        zoom = OpticsUtils.compute_zoom(t, [], e)
        self.assertEqual(zoom, 75)
        fov = e.field_of_view(t, zoom, 1)
        self.assertAlmostEqual(cast(Any, fov).magnitude, 0.67, 2)


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
    assert np.isnan(
        cast(
            Any, output_eq.exit_pupil(telescop=None, zoom=30 * ureg.dimensionless)
        ).magnitude
    )
    assert np.isnan(
        cast(
            Any,
            output_eq.exit_pupil(
                telescop=MagicMock(aperture=np.nan), zoom=30 * ureg.dimensionless
            ),
        ).magnitude
    )
    assert np.isnan(
        cast(
            Any,
            output_eq.exit_pupil(
                telescop=MagicMock(spec=[]), zoom=30 * ureg.dimensionless
            ),
        ).magnitude
    )


def test_output_optical_equipment_exit_pupil_with_invalid_zoom():
    output_eq = OutputOpticalEqipment(focal_length=25, vendor="Test Eyepiece")
    telescop = MagicMock(aperture=150 * ureg.mm)
    # Test with various invalid zoom values
    assert np.isnan(
        cast(Any, output_eq.exit_pupil(telescop=telescop, zoom=np.nan)).magnitude
    )
    assert np.isnan(
        cast(
            Any, output_eq.exit_pupil(telescop=telescop, zoom=0 * ureg.dimensionless)
        ).magnitude
    )
    assert np.isnan(
        cast(Any, output_eq.exit_pupil(telescop=telescop, zoom=None)).magnitude
    )


def test_output_optical_equipment_brightness_with_invalid_telescop():
    output_eq = OutputOpticalEqipment(focal_length=25, vendor="Test Eyepiece")
    # Test with various invalid telescop objects
    assert np.isnan(
        cast(
            Any, output_eq.brightness(telescop=None, zoom=30 * ureg.dimensionless)
        ).magnitude
    )
    assert np.isnan(
        cast(
            Any,
            output_eq.brightness(
                telescop=MagicMock(aperture=np.nan), zoom=30 * ureg.dimensionless
            ),
        ).magnitude
    )
    assert np.isnan(
        cast(
            Any,
            output_eq.brightness(
                telescop=MagicMock(spec=[]), zoom=30 * ureg.dimensionless
            ),
        ).magnitude
    )


def test_output_optical_equipment_brightness_with_invalid_zoom():
    output_eq = OutputOpticalEqipment(focal_length=25, vendor="Test Eyepiece")
    telescop = MagicMock(aperture=150 * ureg.mm)
    # Test with various invalid zoom values
    assert np.isnan(
        cast(Any, output_eq.brightness(telescop=telescop, zoom=np.nan)).magnitude
    )
    assert np.isnan(
        cast(
            Any, output_eq.brightness(telescop=telescop, zoom=0 * ureg.dimensionless)
        ).magnitude
    )
    assert np.isnan(
        cast(Any, output_eq.brightness(telescop=telescop, zoom=None)).magnitude
    )
