import unittest

from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope


class TestCelestronNexStar130SLTAudit(unittest.TestCase):
    def test_nexstar_130slt_specs(self):
        """
        NexStar 130SLT Newtonian Reflector specifications audit test.
        Source: https://www.celestron.com/products/nexstar-130slt-computerized-telescope
        """
        scope = CelestronTelescope.Celestron_NexStar_130SLT()
        self.assertEqual(scope.aperture.to('mm').magnitude, 130.0)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 650.0)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 5.0, places=2)
        self.assertEqual(scope.mass.to('gram').magnitude, 3990)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 38.0)


if __name__ == '__main__':
    unittest.main()
