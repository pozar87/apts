import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope


class TestCelestronNexStarEvolution8Audit(unittest.TestCase):
    def test_nexstar_evolution_8_specs(self):
        """
        Audit specs for Celestron NexStar Evolution 8.
        Source: https://www.celestron.com/products/nexstar-evolution-8-computerized-telescope
        """
        scope = CelestronTelescope.Celestron_NexStar_Evolution_8()
        self.assertEqual(scope.get_vendor(), "Celestron NexStar Evolution 8")
        self.assertEqual(scope.aperture.to("mm").magnitude, 203.2)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 2032)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 10.0, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 64)
        self.assertEqual(scope.mass.to("gram").magnitude, 5670)


if __name__ == "__main__":
    unittest.main()
