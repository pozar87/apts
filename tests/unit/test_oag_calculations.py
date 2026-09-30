import unittest
from apts.opticalequipment.oag.calculations import normalize_oag_database_entry
from apts.utils import ConnectionType, Gender


class TestOAGCalculations(unittest.TestCase):
    def test_normalize_oag_database_entry_basic(self):
        entry = {
            "brand": "ZWO",
            "name": "OAG",
            "optical_length": 17.5,
            "mass": 200,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
        }
        normalized = normalize_oag_database_entry(entry)
        self.assertEqual(normalized["vendor"], "ZWO OAG")
        self.assertEqual(normalized["optical_length"], 17.5)
        self.assertEqual(normalized["mass"], 200)
        self.assertEqual(normalized["inputs"], [(ConnectionType.M48, Gender.FEMALE)])
        self.assertEqual(normalized["outputs"], [(ConnectionType.M42, Gender.MALE)])

    def test_normalize_oag_database_entry_fallback_vendor(self):
        entry = {
            "vendor": "Custom OAG",
            "optical_length": 15,
        }
        normalized = normalize_oag_database_entry(entry)
        self.assertEqual(normalized["vendor"], "Custom OAG")
        self.assertEqual(normalized["optical_length"], 15)

    def test_normalize_oag_database_entry_custom_inputs_outputs(self):
        entry = {
            "brand": "Askar",
            "name": "OAG-L",
            "inputs": [("M48", "Female"), (ConnectionType.M54, Gender.FEMALE)],
            "outputs": [("M42", "Male")],
        }
        normalized = normalize_oag_database_entry(entry)
        self.assertEqual(normalized["vendor"], "Askar OAG-L")
        self.assertEqual(
            normalized["inputs"],
            [(ConnectionType.M48, Gender.FEMALE), (ConnectionType.M54, Gender.FEMALE)],
        )
        self.assertEqual(normalized["outputs"], [(ConnectionType.M42, Gender.MALE)])


if __name__ == "__main__":
    unittest.main()
