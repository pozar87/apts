import unittest

import numpy as np

from apts.opticalequipment.naked_eye import (
    NakedEye,
    calculate_naked_eye_brightness,
    calculate_naked_eye_dawes_limit,
    calculate_naked_eye_exit_pupil,
    calculate_naked_eye_fov,
    calculate_naked_eye_limiting_magnitude,
    calculate_naked_eye_rayleigh_limit,
    normalize_naked_eye_database_entry,
)


class TestNakedEyeCalculations(unittest.TestCase):
    def test_normalize_naked_eye_database_entry_defaults(self):
        entry = {}
        normalized = normalize_naked_eye_database_entry(entry)
        self.assertEqual(normalized["vendor"], "Naked Eye")
        self.assertEqual(normalized["magnification"], 1)
        self.assertEqual(normalized["objective_diameter"], 7)
        self.assertEqual(normalized["apparent_fov_deg"], 180)
        self.assertEqual(normalized["focal_length"], 1)

    def test_normalize_naked_eye_database_entry_custom(self):
        entry = {
            "brand": "Custom",
            "name": "Eye",
            "magnification": 2,
            "objective_diameter": 8,
            "apparent_fov_deg": 160,
            "focal_length": 2,
        }
        normalized = normalize_naked_eye_database_entry(entry)
        self.assertEqual(normalized["vendor"], "Custom Eye")
        self.assertEqual(normalized["magnification"], 2)
        self.assertEqual(normalized["objective_diameter"], 8)
        self.assertEqual(normalized["apparent_fov_deg"], 160)
        self.assertEqual(normalized["focal_length"], 2)

    def test_naked_eye_from_database(self):
        entry = {
            "brand": "Human",
            "name": "Eye",
            "magnification": 1,
            "objective_diameter": 7,
        }
        naked_eye = NakedEye.from_database(entry)
        self.assertEqual(naked_eye.get_vendor(), "Human Eye")
        self.assertEqual(naked_eye.magnification, 1)

    def test_calculate_naked_eye_fov(self):
        fov = calculate_naked_eye_fov(180.0, 1.0)
        self.assertEqual(fov, 180.0)
        fov_zoomed = calculate_naked_eye_fov(180.0, 2.0)
        self.assertEqual(fov_zoomed, 90.0)

    def test_calculate_naked_eye_exit_pupil(self):
        exit_pupil = calculate_naked_eye_exit_pupil(7.0, 1.0)
        self.assertEqual(exit_pupil, 7.0)

    def test_calculate_naked_eye_dawes_limit(self):
        dawes = calculate_naked_eye_dawes_limit(0.7)  # 7mm = 0.7cm
        self.assertEqual(dawes, 16.571)

    def test_calculate_naked_eye_rayleigh_limit(self):
        rayleigh = calculate_naked_eye_rayleigh_limit(0.7)  # 7mm = 0.7cm
        self.assertAlmostEqual(rayleigh, 19.714, places=3)

    def test_calculate_naked_eye_limiting_magnitude(self):
        mag = calculate_naked_eye_limiting_magnitude(0.7)  # 7mm = 0.7cm
        self.assertTrue(np.isclose(mag, 6.925, atol=0.01))

    def test_calculate_naked_eye_brightness(self):
        brightness = calculate_naked_eye_brightness(7.0)  # 7mm exit pupil
        self.assertEqual(brightness, 100.0)


if __name__ == "__main__":
    unittest.main()
