import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope


class TestCelestronNexStar8SEAudit(unittest.TestCase):
    def test_nexstar_8se_specs(self):
        scope = CelestronTelescope.Celestron_NexStar_8SE()
        self.assertEqual(scope.get_vendor(), "Celestron NexStar 8SE")
        self.assertEqual(scope.aperture.to("mm").magnitude, 203.2)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 2032)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 10.0, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 64)
        self.assertEqual(scope.mass.to("gram").magnitude, 5443)


if __name__ == "__main__":
    unittest.main()
