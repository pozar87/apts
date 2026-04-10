import unittest
from apts.opticalequipment.telescope.vendors.askar import AskarTelescope

class TestAskarSpecs(unittest.TestCase):
    def test_fra400_specs(self):
        scope = AskarTelescope.Askar_FRA400()
        self.assertEqual(scope.aperture.to('mm').magnitude, 72)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 400)
        self.assertEqual(scope.mass.to('gram').magnitude, 2560)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)

    def test_203apo_specs(self):
        scope = AskarTelescope.Askar_203APO()
        self.assertEqual(scope.aperture.to('mm').magnitude, 203)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1421)
        self.assertEqual(scope.mass.to('gram').magnitude, 14900)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)

if __name__ == '__main__':
    unittest.main()
