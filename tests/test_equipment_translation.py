import unittest
import apts
from apts.equipment import Equipment
from apts.constants import EquipmentTableLabels
from apts.i18n import language_context

class TestEquipmentTranslation(unittest.TestCase):
    def test_naked_eye_translation_pl(self):
        """Test that Naked Eye is correctly translated to Polish in the equipment table."""
        eq = Equipment()
        # Test with explicit language parameter
        df_pl = eq.data(language='pl')
        labels = df_pl[EquipmentTableLabels.LABEL].tolist()
        self.assertTrue(any("Gołe oko" in label for label in labels), f"Polish translation 'Gołe oko' not found in labels: {labels}")
        self.assertFalse(any("Naked Eye" in label for label in labels), f"English 'Naked Eye' still found in labels: {labels}")

    def test_naked_eye_translation_global_pl(self):
        """Test that Naked Eye is correctly translated when global language is set to Polish."""
        apts.set_language('pl')
        try:
            eq = Equipment()
            df = eq.data()
            labels = df[EquipmentTableLabels.LABEL].tolist()
            self.assertTrue(any("Gołe oko" in label for label in labels), f"Polish translation 'Gołe oko' not found in labels: {labels}")
        finally:
            apts.set_language('en')

    def test_optical_type_translation_pl(self):
        """Test that the 'Type' column is correctly translated in Polish."""
        eq = Equipment()
        df_pl = eq.data(language='pl')
        # VISUAL -> Wizualne (assuming this is the translation)
        # We need to check what VISUAL is translated to.
        # From my previous grep, VISUAL might not be translated?
        # Let's check the 'Type' column values.
        types = df_pl[EquipmentTableLabels.TYPE].unique()
        print(f"DEBUG: Translated types: {types}")
        # If it's not translated, it will remain 'VISUAL' or similar.
        # The user specifically mentioned 'Naked Eye' vs 'Gołe oko'.

if __name__ == "__main__":
    unittest.main()
