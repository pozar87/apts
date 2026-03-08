import unittest
from typing import Any, cast
from unittest.mock import MagicMock
import numpy as np
from apts.optics import OpticalPath
from apts.units import get_unit_registry
from apts.opticalequipment.telescope import Telescope
from apts.opticalequipment.camera import Camera

class TestFieldRotation(unittest.TestCase):
    def setUp(self):
        self.ureg = get_unit_registry()

    def test_field_rotation_rate(self):
        t = MagicMock(spec=Telescope)
        path = OpticalPath(t, [], [], [], [], MagicMock())

        # Test at equator (lat 0), North (az 0), 45 deg altitude
        # rate = 15.041067 * cos(0) * cos(0) / cos(45) = 15.041067 / (1/sqrt(2)) = 15.041067 * sqrt(2) approx 21.271
        rate = path.field_rotation_rate(0, 0, 45)
        self.assertAlmostEqual(cast(Any, rate).magnitude, 15.041067 * np.sqrt(2), places=3)
        self.assertEqual(cast(Any, rate).units, self.ureg.arcsecond / self.ureg.second)

        # Test at Pole (lat 90)
        # rate = 15.041067 * cos(90) * cos(0) / cos(45) = 0
        rate_pole = path.field_rotation_rate(90, 0, 45)
        self.assertAlmostEqual(cast(Any, rate_pole).magnitude, 0.0, places=3)

        # Test at zenith (alt 90) - should be capped by 89.99
        # rate approx 15.041067 * cos(lat) * cos(az) / cos(89.99)
        rate_zenith = path.field_rotation_rate(45, 0, 90)
        # cos(89.99) is very small, so rate should be large but finite
        self.assertTrue(cast(Any, rate_zenith).magnitude > 1000)

    def test_max_exposure_alt_az(self):
        t = MagicMock(spec=Telescope)

        c = MagicMock(spec=Camera)
        # ZWO ASI1600: 4656 x 3520
        c.width = 4656
        c.height = 3520

        path = OpticalPath(t, [], [], [], [], c)

        # Distance to corner: sqrt((4656/2)^2 + (3520/2)^2) = sqrt(2328^2 + 1760^2) approx 2918.4 pixels
        # At lat 45, az 0, alt 45:
        # rate = 15.041067 * cos(45) * cos(0) / cos(45) = 15.041067 arcsec/s
        # rate_rad_s = 15.041067 / 206265 approx 7.292e-5 rad/s
        # max_exp = 1.0 / (2918.4 * 7.292e-5) approx 4.70 seconds

        max_exp = path.max_exposure_alt_az(45, 0, 45, tolerance_pixels=1.0)

        r_pixels = np.sqrt((4656/2.0)**2 + (3520/2.0)**2)
        rate_arcsec_s = 15.041067 * np.cos(np.radians(45)) * np.cos(np.radians(0)) / np.cos(np.radians(45))
        rate_rad_s = rate_arcsec_s / 206265.0
        expected = 1.0 / (r_pixels * rate_rad_s)

        self.assertAlmostEqual(cast(Any, max_exp).magnitude, expected, places=2)
        self.assertEqual(cast(Any, max_exp).units, self.ureg.second)

    def test_max_exposure_non_camera(self):
        t = MagicMock(spec=Telescope)
        path = OpticalPath(t, [], [], [], [], MagicMock()) # Not a Camera
        self.assertIsNone(path.max_exposure_alt_az(45, 0, 45))

if __name__ == "__main__":
    unittest.main()
