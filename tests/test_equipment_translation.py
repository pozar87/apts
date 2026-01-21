import unittest

import apts
from apts.constants import EquipmentTableLabels
from apts.equipment import Equipment


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
        # Using case-insensitive check to be robust
        self.assertTrue(
            any(t.upper() == "WIZUALNE" for t in types),
            f"Polish translation 'WIZUALNE' (case-insensitive) not found in types: {types}",
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

    def test_naked_eye_filtering_pl(self):
        """Test that Naked Eye is correctly filtered out in Polish context when include_naked_eye=False."""
        eq = Equipment()
        from apts.i18n import language_context

        with language_context("pl"):
            # _filter_and_merge returns (result_df, columns_enums)
            # We check the index of result_df which contains the labels
            df, _ = eq._filter_and_merge("Zoom", True, include_naked_eye=False)
            self.assertFalse(any("Gołe oko" in str(label) for label in df.index))

            # Now check that it IS included when requested
            df_with, _ = eq._filter_and_merge("Zoom", True, include_naked_eye=True)
            self.assertTrue(any("Gołe oko" in str(label) for label in df_with.index))


if __name__ == "__main__":
    unittest.main()
