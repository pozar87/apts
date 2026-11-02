import unittest

from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType, Gender


class TestCelestronNexStarEvolution6Audit(unittest.TestCase):
    def test_nexstar_evolution_6_specs(self):
        """
        Audit specs for Celestron NexStar Evolution 6.
        Source: https://www.celestron.com/products/nexstar-evolution-6-telescope
        """
        scope = CelestronTelescope.Celestron_NexStar_Evolution_6()
        self.assertEqual(scope.get_vendor(), "Celestron NexStar Evolution 6")
        self.assertEqual(scope.aperture.to("mm").magnitude, 150)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 1500)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 10.0, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 56)
        self.assertEqual(scope.mass.to("gram").magnitude, 4536)
        self.assertEqual(scope.connection_type, ConnectionType.SC)
        self.assertEqual(scope.connection_gender, Gender.MALE)


if __name__ == "__main__":
    unittest.main()
