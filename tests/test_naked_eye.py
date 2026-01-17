import unittest
from typing import Any, cast

from apts.constants import EquipmentTableLabels, GraphConstants
from apts.equipment import Equipment
from apts.opticalequipment import NakedEye
from apts.i18n import language_context


class TestNakedEye(unittest.TestCase):
    def test_naked_eye_init(self):
        """Test that NakedEye is initialized with correct default values."""
        ne = NakedEye()
        self.assertEqual(ne.magnification, 1)
        self.assertEqual(cast(Any, ne.objective_diameter).magnitude, 7)
        self.assertEqual(ne.vendor, "Naked Eye")

    def test_naked_eye_in_equipment(self):
        """Test that NakedEye is always present in the Equipment's graph."""
        eq = Equipment()

        # Check for a path from SPACE to EYE that goes through a NakedEye instance
        paths = eq._get_paths(GraphConstants.EYE_ID)
        naked_eye_path_found = False
        for p in paths:
            if isinstance(p.telescope, NakedEye):
                naked_eye_path_found = True
                break

        self.assertTrue(
            naked_eye_path_found,
            "A direct path for NakedEye should exist in Equipment.",
        )

    def test_naked_eye_data(self):
        """Test that the data() method includes an entry for NakedEye."""
        with language_context('en'):
            eq = Equipment()
            df = eq.data()

            print(f"DEBUG: Labels in dataframe: {df[EquipmentTableLabels.LABEL].tolist()}")

            # Find the row corresponding to NakedEye
            naked_eye_rows = df[
                df[EquipmentTableLabels.LABEL].str.contains("Naked Eye", na=False)
            ]

            self.assertEqual(
                len(naked_eye_rows), 1, "There should be exactly one entry for NakedEye."
            )

            # Verify some properties of the NakedEye entry
            naked_eye_data = naked_eye_rows.iloc[0]
            self.assertEqual(naked_eye_data[EquipmentTableLabels.ZOOM], 1)
            self.assertEqual(naked_eye_data[EquipmentTableLabels.EXIT_PUPIL], 7)
            self.assertTrue(naked_eye_data[EquipmentTableLabels.USEFUL_ZOOM])


if __name__ == "__main__":
    unittest.main()
