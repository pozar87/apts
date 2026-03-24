import unittest
from datetime import datetime
from unittest.mock import MagicMock, patch
from apts.optics import OpticalPath
from apts.units import get_unit_registry
from apts.constants import astronomy

class TestPlanetaryRotation(unittest.TestCase):
    @patch("apts.utils.planetary.get_planet_angular_diameter")
    @patch("apts.utils.planetary.get_planet_rotation_period")
    @patch("apts.utils.planetary.get_sub_observer_latitude")
    def test_max_planetary_rotation_duration_jupiter(self, mock_lat, mock_period, mock_diameter):
        # Setup mocks for Jupiter
        # Typical opposition diameter ~48 arcsec => radius 24 arcsec
        mock_diameter.return_value = 48.0
        # Sidereal period ~9h 55m
        mock_period.return_value = astronomy.JUPITER_ROTATION_PERIOD_S
        # Zero tilt for simplicity
        mock_lat.return_value = 0.0

        # Mock OpticalPath setup
        t = MagicMock()
        c = MagicMock()
        path = OpticalPath(t, [], [], [], [], c)

        # Case 1: High resolution setup (0.1 arcsec/pixel)
        # scale = 0.1 "/px
        # r_eq = 24.0 "
        # T = 35729.7 s
        # omega = (2 * pi * 24.0) / 35729.7 = 0.150796 / 35729.7 * 10^3 (approx)
        # omega = 0.004218 "/s
        # t_max = (1.0 * 0.1) / 0.004218 = 23.7 s
        with MagicMock() as mock_scale:
            mock_scale.to.return_value.magnitude = 0.1
            path.pixel_scale = MagicMock(return_value=mock_scale)

            duration = path.max_planetary_rotation_duration("jupiter", datetime(2025, 1, 1))
            self.assertAlmostEqual(duration.magnitude, 23.7, places=1)
            self.assertEqual(duration.units, get_unit_registry().second)

        # Case 2: Lower resolution setup (0.3 arcsec/pixel)
        # t_max = (1.0 * 0.3) / 0.004218 = 71.1 s
        with MagicMock() as mock_scale:
            mock_scale.to.return_value.magnitude = 0.3
            path.pixel_scale = MagicMock(return_value=mock_scale)

            duration = path.max_planetary_rotation_duration("jupiter", datetime(2025, 1, 1))
            self.assertAlmostEqual(duration.magnitude, 71.1, places=1)

    @patch("apts.utils.planetary.get_planet_angular_diameter")
    @patch("apts.utils.planetary.get_planet_rotation_period")
    @patch("apts.utils.planetary.get_sub_observer_latitude")
    def test_max_planetary_rotation_duration_mars(self, mock_lat, mock_period, mock_diameter):
        # Setup mocks for Mars
        # Typical opposition diameter ~15 arcsec => radius 7.5 arcsec
        mock_diameter.return_value = 15.0
        # Sidereal period ~24.6h
        mock_period.return_value = astronomy.MARS_ROTATION_PERIOD_S
        mock_lat.return_value = 20.0 # Significant tilt

        # Mock OpticalPath setup
        t = MagicMock()
        c = MagicMock()
        path = OpticalPath(t, [], [], [], [], c)

        # scale = 0.1 "/px
        # r_eq = 7.5 "
        # T = 88642.7 s
        # cos(20) = 0.9397
        # omega = (2 * pi * 7.5 * 0.9397) / 88642.7 = 44.28 / 88642.7 = 0.0004995 "/s
        # t_max = (1.0 * 0.1) / 0.0004995 = 200.2 s
        with MagicMock() as mock_scale:
            mock_scale.to.return_value.magnitude = 0.1
            path.pixel_scale = MagicMock(return_value=mock_scale)

            duration = path.max_planetary_rotation_duration("mars", datetime(2025, 1, 1))
            self.assertAlmostEqual(duration.magnitude, 200.2, places=1)

    def test_max_planetary_rotation_duration_none_scale(self):
        t = MagicMock()
        c = MagicMock()
        path = OpticalPath(t, [], [], [], [], c)
        path.pixel_scale = MagicMock(return_value=None)

        self.assertIsNone(path.max_planetary_rotation_duration("jupiter", datetime(2025, 1, 1)))

if __name__ == "__main__":
    unittest.main()
