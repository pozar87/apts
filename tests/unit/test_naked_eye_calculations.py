import unittest
from apts.opticalequipment.naked_eye import NakedEye, normalize_naked_eye_database_entry


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


if __name__ == "__main__":
    unittest.main()
