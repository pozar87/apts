import unittest
from apts.opticalequipment.telescope.vendors.gso import GsoTelescope
from apts.units import get_unit_registry

class TestGsoSpecs(unittest.TestCase):
    def test_gso_rc_6(self):
        telescope = GsoTelescope.GSO_RC_6()
        self.assertEqual(telescope.aperture.to(get_unit_registry().mm).magnitude, 152.4)
        self.assertEqual(telescope.focal_length.to(get_unit_registry().mm).magnitude, 1370)
        self.assertEqual(telescope.mass.to(get_unit_registry().gram).magnitude, 5400)
        self.assertEqual(telescope.central_obstruction.to(get_unit_registry().mm).magnitude, 77)
        self.assertAlmostEqual(telescope.focal_ratio().magnitude, 8.99, places=2)

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

    def test_gso_rc_8(self):
        telescope = GsoTelescope.GSO_RC_8()
        self.assertEqual(telescope.aperture.to(get_unit_registry().mm).magnitude, 203)
        self.assertEqual(telescope.focal_length.to(get_unit_registry().mm).magnitude, 1624)
        self.assertEqual(telescope.mass.to(get_unit_registry().gram).magnitude, 7500)
        self.assertEqual(telescope.central_obstruction.to(get_unit_registry().mm).magnitude, 85)
        self.assertAlmostEqual(telescope.focal_ratio().magnitude, 8.0, places=2)

    def test_gso_rc_10(self):
        telescope = GsoTelescope.GSO_RC_10()
        self.assertEqual(telescope.aperture.to(get_unit_registry().mm).magnitude, 254)
        self.assertEqual(telescope.focal_length.to(get_unit_registry().mm).magnitude, 2000)
        self.assertEqual(telescope.mass.to(get_unit_registry().gram).magnitude, 15700)
        self.assertEqual(telescope.central_obstruction.to(get_unit_registry().mm).magnitude, 112)
        self.assertAlmostEqual(telescope.focal_ratio().magnitude, 7.87, places=2)

    def test_gso_rc_12(self):
        telescope = GsoTelescope.GSO_RC_12()
        self.assertEqual(telescope.aperture.to(get_unit_registry().mm).magnitude, 304)
        self.assertEqual(telescope.focal_length.to(get_unit_registry().mm).magnitude, 2432)
        self.assertEqual(telescope.mass.to(get_unit_registry().gram).magnitude, 20500)
        self.assertEqual(telescope.central_obstruction.to(get_unit_registry().mm).magnitude, 150)
        self.assertAlmostEqual(telescope.focal_ratio().magnitude, 8.0, places=2)

if __name__ == "__main__":
    unittest.main()
