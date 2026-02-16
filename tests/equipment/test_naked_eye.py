import unittest
from typing import Any, cast
import numpy as np

from apts.constants import EquipmentTableLabels, GraphConstants, OpticalType
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
        self.assertEqual(ne._type, OpticalType.VISUAL)

    def test_naked_eye_str(self):
        ne = NakedEye()
        self.assertEqual(str(ne), "Naked Eye 1x7")

    def test_naked_eye_fov(self):
        ne = NakedEye()
        self.assertEqual(ne.fov().magnitude, 180)

    def test_naked_eye_exit_pupil(self):
        ne = NakedEye()
        self.assertEqual(ne.exit_pupil().magnitude, 7.0)

    def test_naked_eye_limits(self):
        ne = NakedEye()
        self.assertEqual(ne.dawes_limit().magnitude, 16.571)
        self.assertEqual(ne.rayleigh_limit().magnitude, 19.714)

    def test_naked_eye_limiting_magnitude(self):
        ne = NakedEye()
        self.assertTrue(np.isclose(ne.limiting_magnitude(), 6.92, atol=0.01))

    def test_naked_eye_brightness(self):
        ne = NakedEye()
        self.assertEqual(ne.brightness(), 100.0)

    def test_naked_eye_register(self):
        eq = Equipment()
        ne = NakedEye()
        ne.register(eq)
        self.assertIn(ne.id(), eq.connection_garph.nodes())
        self.assertTrue(eq.connection_garph.has_edge(GraphConstants.SPACE_ID, ne.id()))
        self.assertTrue(eq.connection_garph.has_edge(ne.id(), GraphConstants.EYE_ID))

    def test_naked_eye_output_type(self):
        ne = NakedEye()
        self.assertEqual(ne.output_type(), OpticalType.VISUAL)

    def test_naked_eye_max_useful_zoom(self):
        ne = NakedEye()
        self.assertEqual(ne.max_useful_zoom(), 1)

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
