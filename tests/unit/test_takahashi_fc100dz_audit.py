import unittest
from apts.opticalequipment.telescope.vendors.takahashi import TakahashiTelescope
from apts.units import get_unit_registry

class TestTakahashiFC100DZAudit(unittest.TestCase):
    def test_takahashi_fc100dz_specs(self):
        telescope = TakahashiTelescope.Takahashi_FC_100DZ()

        # Verify physical specs
        self.assertEqual(telescope.aperture.to(get_unit_registry().mm).magnitude, 100)
        self.assertEqual(telescope.focal_length.to(get_unit_registry().mm).magnitude, 800)
        self.assertEqual(telescope.mass.to(get_unit_registry().gram).magnitude, 3900)
        self.assertEqual(telescope.central_obstruction.to(get_unit_registry().mm).magnitude, 0)
        self.assertEqual(telescope.focal_ratio().magnitude, 8.0)

        # Verify back focus role & optical length
        self.assertEqual(telescope.optical_length.to(get_unit_registry().mm).magnitude, 223)
        self.assertEqual(telescope.backfocus.to(get_unit_registry().mm).magnitude, 223)

if __name__ == "__main__":
    unittest.main()
