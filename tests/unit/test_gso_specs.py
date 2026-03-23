import unittest
from apts.opticalequipment.telescope.vendors.gso import GsoTelescope
from apts.units import get_unit_registry

class TestGsoSpecs(unittest.TestCase):
    def test_gso_rc_6(self):
        telescope = GsoTelescope.GSO_RC_6()
        self.assertEqual(telescope.aperture.to(get_unit_registry().mm).magnitude, 152)
        self.assertEqual(telescope.focal_length.to(get_unit_registry().mm).magnitude, 1370)
        self.assertEqual(telescope.mass.to(get_unit_registry().gram).magnitude, 5580)
        self.assertEqual(telescope.central_obstruction.to(get_unit_registry().mm).magnitude, 71)
        self.assertAlmostEqual(telescope.focal_ratio().magnitude, 9.01, places=2)

    def test_gso_newton_8_f_4(self):
        telescope = GsoTelescope.GSO_Newton_8_f_4()
        self.assertEqual(telescope.aperture.to(get_unit_registry().mm).magnitude, 200)
        self.assertEqual(telescope.focal_length.to(get_unit_registry().mm).magnitude, 800)
        self.assertEqual(telescope.mass.to(get_unit_registry().gram).magnitude, 8900)
        self.assertEqual(telescope.central_obstruction.to(get_unit_registry().mm).magnitude, 70)
        self.assertEqual(telescope.focal_ratio().magnitude, 4.0)

    def test_gso_dobson_10(self):
        telescope = GsoTelescope.GSO_Dobson_10()
        self.assertEqual(telescope.aperture.to(get_unit_registry().mm).magnitude, 254)
        self.assertEqual(telescope.focal_length.to(get_unit_registry().mm).magnitude, 1250)
        self.assertEqual(telescope.mass.to(get_unit_registry().gram).magnitude, 18000)
        self.assertEqual(telescope.central_obstruction.to(get_unit_registry().mm).magnitude, 64)
        self.assertAlmostEqual(telescope.focal_ratio().magnitude, 4.92, places=2)

if __name__ == "__main__":
    unittest.main()
