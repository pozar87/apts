import unittest

from apts.opticalequipment.filter_wheel.base import FilterHolder, FilterWheel
from apts.opticalequipment.filter_wheel.calculations import (
    normalize_filter_wheel_database_entry,
)
from apts.utils import ConnectionType, Gender


class TestFilterWheelCalculations(unittest.TestCase):
    def test_normalize_filter_wheel_database_entry_defaults(self):
        entry = {
            "brand": "ZWO",
            "name": "EFW 8x1.25",
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
        }
        normalized = normalize_filter_wheel_database_entry(entry)

        self.assertEqual(normalized["vendor"], "ZWO EFW 8x1.25")
        self.assertEqual(normalized["optical_length"], 0)
        self.assertEqual(normalized["mass"], 0)
        self.assertEqual(
            normalized["inputs"], [(ConnectionType.M42, Gender.FEMALE)]
        )
        self.assertEqual(
            normalized["outputs"], [(ConnectionType.M42, Gender.MALE)]
        )

    def test_normalize_filter_wheel_database_entry_custom_inputs_outputs(self):
        entry = {
            "brand": "Player One",
            "name": "Phoenix Wheel",
            "optical_length": 20,
            "mass": 350,
            "inputs": [("M48", "Female"), ("M54", "Female")],
            "outputs": [("M48", "Male"), ("M54", "Male")],
        }
        normalized = normalize_filter_wheel_database_entry(entry)

        self.assertEqual(normalized["vendor"], "Player One Phoenix Wheel")
        self.assertEqual(normalized["optical_length"], 20)
        self.assertEqual(normalized["mass"], 350)
        self.assertEqual(
            normalized["inputs"],
            [
                (ConnectionType.M48, Gender.FEMALE),
                (ConnectionType.M54, Gender.FEMALE),
            ],
        )
        self.assertEqual(
            normalized["outputs"],
            [
                (ConnectionType.M48, Gender.MALE),
                (ConnectionType.M54, Gender.MALE),
            ],
        )

    def test_from_database_creation(self):
        raw_entry = {
            "brand": "ZWO",
            "name": "Filter Drawer M48",
            "optical_length": 21,
            "mass": 180,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
        }
        fw = FilterWheel.from_database(raw_entry)
        self.assertEqual(fw.vendor, "ZWO Filter Drawer M48")
        self.assertEqual(fw.optical_length.magnitude, 21)
        self.assertEqual(fw.mass.magnitude, 180)

        fh = FilterHolder.from_database(raw_entry)
        self.assertEqual(fh.vendor, "ZWO Filter Drawer M48")
        self.assertEqual(fh.optical_length.magnitude, 21)
        self.assertEqual(fh.mass.magnitude, 180)


if __name__ == "__main__":
    unittest.main()
