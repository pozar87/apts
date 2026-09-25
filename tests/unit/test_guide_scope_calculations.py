import unittest

from apts.opticalequipment.guide_scope.base import GuideScope
from apts.opticalequipment.guide_scope.calculations import (
    normalize_guide_scope_database_entry,
)
from apts.utils import ConnectionType, Gender


class TestGuideScopeCalculations(unittest.TestCase):
    def test_normalize_guide_scope_database_entry_defaults(self):
        entry = {
            "brand": "ZWO",
            "name": "30mm F4 Guide Scope",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "bf_role": "start",
            "optical_length": 25,
            "mass": 250,
        }
        normalized = normalize_guide_scope_database_entry(entry)

        self.assertEqual(normalized["vendor"], "ZWO 30mm F4 Guide Scope")
        self.assertEqual(normalized["aperture"], 30)
        self.assertEqual(normalized["focal_length"], 120)
        self.assertEqual(normalized["optical_length"], 25)
        self.assertEqual(normalized["mass"], 250)
        self.assertEqual(normalized["backfocus"], 25)
        self.assertEqual(
            normalized["outputs"], [(ConnectionType.M42, Gender.FEMALE)]
        )

    def test_normalize_guide_scope_database_entry_custom_outputs(self):
        entry = {
            "brand": "SVBONY",
            "name": "SV105 50mm",
            "outputs": [("1.25\"", "Female")],
        }
        normalized = normalize_guide_scope_database_entry(entry)

        self.assertEqual(normalized["vendor"], "SVBONY SV105 50mm")
        self.assertEqual(normalized["aperture"], 50)
        self.assertEqual(
            normalized["outputs"], [(ConnectionType.F_1_25, Gender.FEMALE)]
        )
        self.assertIsNone(normalized["backfocus"])

    def test_from_database_creation(self):
        raw_entry = {
            "brand": "Askar",
            "name": "FMA180 40mm",
            "optical_length": 180,
            "mass": 395,
            "cside_thread": "M42",
            "cside_gender": "Male",
            "bf_role": "start",
        }
        gs = GuideScope.from_database(raw_entry)
        self.assertEqual(gs.vendor, "Askar FMA180 40mm")
        self.assertEqual(gs.aperture.magnitude, 40)
        self.assertEqual(gs.optical_length.magnitude, 180)
        self.assertEqual(gs.mass.magnitude, 395)
        self.assertEqual(gs.backfocus.magnitude, 180)


if __name__ == "__main__":
    unittest.main()
