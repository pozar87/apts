import unittest

from apts.opticalequipment.binoculars import (
    Binoculars,
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


if __name__ == "__main__":
    unittest.main()
