import unittest

from apts.opticalequipment.reducer import (
    Corrector,
    Flattener,
    Reducer,
    normalize_reducer_database_entry,
)
from apts.utils import ConnectionType, Gender


class TestReducerCalculations(unittest.TestCase):
    def test_normalize_reducer_entry_with_parsed_magnification(self):
        raw_entry = {
            "brand": "TS-Optics",
            "name": "0.79x Reducer",
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "optical_length": 45.0,
            "mass": 250,
        }

        normalized = normalize_reducer_database_entry(
            raw_entry, default_magnification=0.8, parse_magnification=True
        )

        self.assertEqual(normalized["vendor"], "TS-Optics 0.79x Reducer")
        self.assertAlmostEqual(normalized["magnification"], 0.79)
        self.assertEqual(normalized["optical_length"], 45.0)
        self.assertEqual(normalized["mass"], 250)
        self.assertEqual(normalized["required_backfocus"], 55)
        self.assertEqual(
            normalized["inputs"], [(ConnectionType.M48, Gender.FEMALE)]
        )
        self.assertEqual(
            normalized["outputs"], [(ConnectionType.M42, Gender.MALE)]
        )

    def test_normalize_flattener_entry_default_magnification(self):
        raw_entry = {
            "brand": "Sky-Watcher",
            "name": "Field Flattener",
            "tside_thread": "M48",
            "tside_gender": "Female",
            "required_backfocus": 55.0,
        }

        normalized = normalize_reducer_database_entry(
            raw_entry, default_magnification=1.0, parse_magnification=False
        )

        self.assertEqual(normalized["vendor"], "Sky-Watcher Field Flattener")
        self.assertEqual(normalized["magnification"], 1.0)
        self.assertEqual(normalized["required_backfocus"], 55.0)

    def test_reducer_classes_from_database(self):
        entry = {
            "brand": "TeleVue",
            "name": "TRF-2008 0.8x Reducer/Flattener",
            "optical_length": 30,
            "mass": 180,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": "T2",
            "cside_gender": "Male",
        }

        reducer = Reducer.from_database(entry)
        self.assertEqual(
            reducer.get_vendor(), "TeleVue TRF-2008 0.8x Reducer/Flattener"
        )
        self.assertAlmostEqual(reducer.magnification, 0.8)

        flattener = Flattener.from_database(entry)
        self.assertEqual(flattener.magnification, 1.0)

        corrector = Corrector.from_database(entry)
        self.assertEqual(corrector.magnification, 1.0)


if __name__ == "__main__":
    unittest.main()
