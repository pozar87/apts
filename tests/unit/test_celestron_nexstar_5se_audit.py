import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope


class TestCelestronNexStar5SEAudit(unittest.TestCase):
    def test_nexstar_5se_specs(self):
        """
        NexStar 5SE Schmidt-Cassegrain specifications audit test.
        Source: https://www.celestron.com/products/nexstar-5se-computerized-telescope
        """
        scope = CelestronTelescope.Celestron_NexStar_5SE()
        self.assertEqual(scope.get_vendor(), "Celestron NexStar 5SE")
        self.assertEqual(scope.aperture.to('mm').magnitude, 125.0)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1250.0)
        self.assertEqual(scope.focal_ratio().magnitude, 10.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2722)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 51.0)


if __name__ == '__main__':
    unittest.main()
