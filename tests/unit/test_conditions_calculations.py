import unittest
from unittest.mock import MagicMock

import numpy as np

from apts.conditions import Conditions, check_simple_visibility, check_visibility


class QuantityMock:
    def __init__(self, magnitude):
        self.magnitude = magnitude


class TestConditionsCalculations(unittest.TestCase):
    def test_check_simple_visibility_scalar(self):
        # Normal azimuth range [0, 360]
        self.assertTrue(check_simple_visibility(azimuth=180, altitude=20, min_altitude=15, min_azimuth=0, max_azimuth=360))
        self.assertFalse(check_simple_visibility(azimuth=180, altitude=10, min_altitude=15, min_azimuth=0, max_azimuth=360))

        # Constrained azimuth range [90, 270]
        self.assertTrue(check_simple_visibility(azimuth=180, altitude=20, min_altitude=15, min_azimuth=90, max_azimuth=270))
        self.assertFalse(check_simple_visibility(azimuth=45, altitude=20, min_altitude=15, min_azimuth=90, max_azimuth=270))

        # Wrapped azimuth range [270, 90] (crosses 0/360 degrees)
        self.assertTrue(check_simple_visibility(azimuth=350, altitude=20, min_altitude=15, min_azimuth=270, max_azimuth=90))
        self.assertTrue(check_simple_visibility(azimuth=45, altitude=20, min_altitude=15, min_azimuth=270, max_azimuth=90))
        self.assertFalse(check_simple_visibility(azimuth=180, altitude=20, min_altitude=15, min_azimuth=270, max_azimuth=90))

    def test_check_simple_visibility_with_magnitude_attribute(self):
        min_alt = QuantityMock(15)
        min_az = QuantityMock(90)
        max_az = QuantityMock(270)

        self.assertTrue(check_simple_visibility(azimuth=180, altitude=20, min_altitude=min_alt, min_azimuth=min_az, max_azimuth=max_az))
        self.assertFalse(check_simple_visibility(azimuth=45, altitude=20, min_altitude=min_alt, min_azimuth=min_az, max_azimuth=max_az))

    def test_check_simple_visibility_numpy_array(self):
        azimuths = np.array([45, 180, 300])
        altitudes = np.array([20, 20, 10])

        result = check_simple_visibility(
            azimuth=azimuths,
            altitude=altitudes,
            min_altitude=15,
            min_azimuth=90,
            max_azimuth=270,
        )
        np.testing.assert_array_equal(result, np.array([False, True, False]))

    def test_check_visibility_horizon_delegation(self):
        mock_horizon = MagicMock()
        mock_horizon.is_visible.return_value = True

        res = check_visibility(
            azimuth=180,
            altitude=20,
            min_altitude=15,
            min_azimuth=0,
            max_azimuth=360,
            horizon=mock_horizon,
        )

        self.assertTrue(res)
        mock_horizon.is_visible.assert_called_once_with(180, 20)

    def test_conditions_is_visible_delegation(self):
        cond = Conditions(min_object_altitude=15, min_object_azimuth=0, max_object_azimuth=360)
        self.assertTrue(cond.is_visible(180, 20))
        self.assertFalse(cond.is_visible(180, 10))


if __name__ == "__main__":
    unittest.main()
