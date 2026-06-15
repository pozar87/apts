import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope

class TestCelestronC6Audit(unittest.TestCase):
    def test_nexstar_6se_mass(self):
        scope = CelestronTelescope.Celestron_NexStar_6SE()
        self.assertEqual(scope.mass.to('gram').magnitude, 3629)

    def test_advanced_vx_6_sct_mass(self):
        scope = CelestronTelescope.Celestron_Advanced_VX_6_SCT()
        self.assertEqual(scope.mass.to('gram').magnitude, 4536)

    def test_astro_fi_6_sct_mass(self):
        scope = CelestronTelescope.Celestron_Astro_Fi_6_SCT()
        self.assertEqual(scope.mass.to('gram').magnitude, 4536)

    def test_nexstar_evolution_6_mass(self):
        scope = CelestronTelescope.Celestron_NexStar_Evolution_6()
        self.assertEqual(scope.mass.to('gram').magnitude, 4536)

    def test_c6_sct_mass(self):
        scope = CelestronTelescope.Celestron_C6_SCT()
        self.assertEqual(scope.mass.to('gram').magnitude, 4536)

if __name__ == '__main__':
    unittest.main()
