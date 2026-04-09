import unittest
from apts.opticalequipment.telescope.vendors.askar import AskarTelescope

class TestAskarSpecs(unittest.TestCase):
    def test_fra400_specs(self):
        scope = AskarTelescope.Askar_FRA400()
        self.assertEqual(scope.aperture.to('mm').magnitude, 72)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 400)
        self.assertEqual(scope.mass.to('gram').magnitude, 3200)

if __name__ == '__main__':
    unittest.main()
