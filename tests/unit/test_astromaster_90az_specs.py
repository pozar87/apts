import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope

class TestAstroMaster90AZ(unittest.TestCase):
    def test_astromaster_90az_specs(self):
        scope = CelestronTelescope.Celestron_AstroMaster_90AZ()
        self.assertEqual(scope.get_vendor(), "Celestron AstroMaster 90AZ")
        self.assertEqual(scope.aperture.to('mm').magnitude, 90)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2268)
        self.assertEqual(scope.focal_ratio().magnitude, 1000/90)

if __name__ == '__main__':
    unittest.main()
