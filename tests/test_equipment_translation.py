import unittest

import apts
from apts.constants import EquipmentTableLabels
from apts.equipment import Equipment
from apts.i18n import language_context


class TestEquipmentTranslation(unittest.TestCase):
    def test_naked_eye_translation_pl(self):
        """Test that Naked Eye is correctly translated to Polish in the equipment table."""
        eq = Equipment()
        # Test with explicit language parameter
        df_pl = eq.data(language="pl")
        labels = df_pl[EquipmentTableLabels.LABEL].tolist()
        self.assertTrue(
            any("Gołe oko" in label for label in labels),
            f"Polish translation 'Gołe oko' not found in labels: {labels}",
        )
        self.assertFalse(
            any("Naked Eye" in label for label in labels),
            f"English 'Naked Eye' still found in labels: {labels}",
        )

    def test_naked_eye_translation_global_pl(self):
        """Test that Naked Eye is correctly translated when global language is set to Polish."""
        apts.set_language("pl")
        try:
            eq = Equipment()
            df = eq.data()
            labels = df[EquipmentTableLabels.LABEL].tolist()
            self.assertTrue(
                any("Gołe oko" in label for label in labels),
                f"Polish translation 'Gołe oko' not found in labels: {labels}",
            )
        finally:
            apts.set_language("en")

    def test_optical_type_translation_pl(self):
        """Test that the 'Type' column is correctly translated in Polish."""
        eq = Equipment()
        df_pl = eq.data(language="pl")
        types = df_pl[EquipmentTableLabels.TYPE].unique().tolist()
        # Based on .po file, VISUAL is translated to WIZUALNE
        self.assertIn(
            "WIZUALNE",
            types,
            f"Polish translation 'WIZUALNE' not found in types: {types}",
        )
        # Ensure 'VISUAL' (raw enum name) is not there
        self.assertNotIn("VISUAL", types)

    def test_naked_eye_translation_dynamic(self):
        """Test that Naked Eye translation changes dynamically based on context."""
        eq = Equipment()
        # First check English
        df_en = eq.data(language="en")
        labels_en = df_en[EquipmentTableLabels.LABEL].tolist()
        self.assertTrue(any("Naked Eye" in label for label in labels_en))

        # Then check Polish
        df_pl = eq.data(language="pl")
        labels_pl = df_pl[EquipmentTableLabels.LABEL].tolist()
        self.assertTrue(any("Gołe oko" in label for label in labels_pl))

    def test_plot_zoom_filtering_translation_pl(self):
        """Test that plot_zoom correctly filters out Naked Eye in Polish."""
        eq = Equipment()
        # Default eq has only Naked Eye
        data, _ = eq._filter_and_merge(EquipmentTableLabels.ZOOM, False, include_naked_eye=False)
        self.assertTrue(data.empty, "Naked eye should be filtered out in English")

        # Test in Polish
        with language_context("pl"):
            data_pl, _ = eq._filter_and_merge(EquipmentTableLabels.ZOOM, False, include_naked_eye=False)
            self.assertTrue(data_pl.empty, f"Naked eye should be filtered out in Polish, but got: {data_pl}")


if __name__ == "__main__":
    unittest.main()
