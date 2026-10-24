import unittest

from apts.opticalequipment.binoculars import (
    Binoculars,
    calculate_binoculars_brightness,
    calculate_binoculars_dawes_limit,
    calculate_binoculars_exit_pupil,
    calculate_binoculars_fov,
    calculate_binoculars_limiting_magnitude,
    calculate_binoculars_rayleigh_limit,
    normalize_binoculars_database_entry,
)
from apts.utils import ConnectionType, Gender


class TestBinocularsCalculations(unittest.TestCase):
    def test_normalize_binoculars_database_entry_basic(self):
        entry = {
            "brand": "Nikon",
            "name": "Action EX 10x50",
            "mass": 1020,
            "cside_thread": '2"',
            "cside_gender": "Male",
        }
        normalized = normalize_binoculars_database_entry(entry)
        self.assertEqual(normalized["vendor"], "Nikon Action EX 10x50")
        self.assertEqual(normalized["mass"], 1020)
        self.assertEqual(normalized["magnification"], 10)
        self.assertEqual(normalized["objective_diameter"], 50)
        self.assertEqual(normalized["apparent_fov_deg"], 60)
        self.assertEqual(
            normalized["outputs"], [(ConnectionType.F_2, Gender.MALE)]
        )

    def test_normalize_binoculars_database_entry_with_explicit_fov_and_outputs(self):
        entry = {
            "brand": "Celestron",
            "name": "SkyMaster 15x70",
            "mass": 1360,
            "magnification": 15,
            "objective_diameter": 70,
            "apparent_fov_deg": 65,
            "outputs": [(ConnectionType.F_1_25, Gender.FEMALE)],
        }
        normalized = normalize_binoculars_database_entry(entry)
        self.assertEqual(normalized["vendor"], "Celestron SkyMaster 15x70")
        self.assertEqual(normalized["mass"], 1360)
        self.assertEqual(normalized["magnification"], 15)
        self.assertEqual(normalized["objective_diameter"], 70)
        self.assertEqual(normalized["apparent_fov_deg"], 65)
        self.assertEqual(
            normalized["outputs"], [(ConnectionType.F_1_25, Gender.FEMALE)]
        )

    def test_binoculars_from_database(self):
        entry = {
            "brand": "Orion",
            "name": "GiantView 25x100 Binocular",
            "mass": 2500,
            "cside_thread": '2"',
            "cside_gender": "Male",
        }
        bino = Binoculars.from_database(entry)
        self.assertEqual(bino.get_vendor(), "Orion GiantView 25x100 Binocular")
        self.assertEqual(bino.magnification, 25)
        self.assertEqual(bino.objective_diameter.magnitude, 100)
        self.assertEqual(bino.mass.magnitude, 2500)

    def test_calculate_binoculars_fov(self):
        fov = calculate_binoculars_fov(65.0, 10.0)
        self.assertAlmostEqual(fov, 6.5)

    def test_calculate_binoculars_exit_pupil(self):
        exit_pupil = calculate_binoculars_exit_pupil(50.0, 10.0)
        self.assertAlmostEqual(exit_pupil, 5.0)

    def test_calculate_binoculars_dawes_limit(self):
        dawes = calculate_binoculars_dawes_limit(5.0)  # 50mm = 5cm
        self.assertEqual(dawes, 2.32)

    def test_calculate_binoculars_rayleigh_limit(self):
        rayleigh = calculate_binoculars_rayleigh_limit(0.05)  # 50mm = 0.05m
        self.assertAlmostEqual(rayleigh, 2.768, places=3)

    def test_calculate_binoculars_limiting_magnitude(self):
        mag = calculate_binoculars_limiting_magnitude(5.0)  # 50mm = 5cm
        self.assertAlmostEqual(mag, 11.195, places=3)

    def test_calculate_binoculars_brightness(self):
        brightness = calculate_binoculars_brightness(5.0)  # 5mm exit pupil
        self.assertAlmostEqual(brightness, 51.02, places=2)


if __name__ == "__main__":
    unittest.main()
