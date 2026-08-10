import unittest
import numpy as np
from apts.optics.calculations.atmospheric import (
    calculate_atmospheric_dispersion_in_pixels,
)


class TestOpticsCalculationsAtmospheric(unittest.TestCase):
    def test_calculate_atmospheric_dispersion_in_pixels_scalar(self):
        # dispersion = 1.5, scale = 2.0 -> 0.75
        res = calculate_atmospheric_dispersion_in_pixels(1.5, 2.0)
        self.assertEqual(res, 0.75)

    def test_calculate_atmospheric_dispersion_in_pixels_none_scale(self):
        res = calculate_atmospheric_dispersion_in_pixels(1.5, None)
        self.assertIsNone(res)

    def test_calculate_atmospheric_dispersion_in_pixels_zero_scale(self):
        res = calculate_atmospheric_dispersion_in_pixels(1.5, 0)
        self.assertIsNone(res)

    def test_calculate_atmospheric_dispersion_in_pixels_array(self):
        disp = np.array([1.5, 3.0, 4.5])
        scale = np.array([2.0, 1.5, 3.0])
        res = calculate_atmospheric_dispersion_in_pixels(disp, scale)
        np.testing.assert_array_equal(res, np.array([0.75, 2.0, 1.5]))

    def test_calculate_atmospheric_dispersion_in_pixels_array_with_zero(self):
        disp = np.array([1.5, 3.0])
        scale = np.array([2.0, 0.0])
        res = calculate_atmospheric_dispersion_in_pixels(disp, scale)
        np.testing.assert_array_equal(res, np.array([0.75, 0.0]))

    def test_calculate_atmospheric_dispersion_in_pixels_array_all_zeros(self):
        disp = np.array([1.5, 3.0])
        scale = np.array([0.0, 0.0])
        res = calculate_atmospheric_dispersion_in_pixels(disp, scale)
        self.assertIsNone(res)


if __name__ == "__main__":
    unittest.main()
