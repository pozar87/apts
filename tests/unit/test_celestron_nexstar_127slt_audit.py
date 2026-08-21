import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope


class TestCelestronNexStar127SLTAudit(unittest.TestCase):
    def test_nexstar_127slt_specs(self):
        """
        NexStar 127SLT Maksutov-Cassegrain specifications audit test.
        Source: https://www.celestron.com/products/nexstar-127slt-computerized-telescope
        """
        scope = CelestronTelescope.Celestron_NexStar_127SLT()
        self.assertEqual(scope.aperture.to('mm').magnitude, 127.0)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1500.0)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 11.81, places=2)
        self.assertEqual(scope.mass.to('gram').magnitude, 3950)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 40.0)


if __name__ == '__main__':
    unittest.main()
