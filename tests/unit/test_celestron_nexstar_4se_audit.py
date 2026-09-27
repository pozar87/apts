import unittest

from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope


class TestCelestronNexStar4SEAudit(unittest.TestCase):
    def test_nexstar_4se_specs(self):
        """
        NexStar 4SE Maksutov-Cassegrain specifications audit test.
        Source: https://www.celestron.com/products/nexstar-4se-computerized-telescope
        """
        scope = CelestronTelescope.Celestron_NexStar_4SE()
        self.assertEqual(scope.get_vendor(), "Celestron NexStar 4SE")
        self.assertEqual(scope.aperture.to('mm').magnitude, 102.0)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1325.0)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 1325.0 / 102.0, places=4)
        self.assertEqual(scope.mass.to('gram').magnitude, 2700)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 35.0)


if __name__ == '__main__':
    unittest.main()
