import unittest
from apts.opticalequipment.telescope.vendors.askar import AskarTelescope

class TestAskarSpecs(unittest.TestCase):
    def test_fra400_specs(self):
        scope = AskarTelescope.Askar_FRA400()
        self.assertEqual(scope.aperture.to('mm').magnitude, 72)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 400)
        self.assertEqual(scope.mass.to('gram').magnitude, 2560)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)

    def test_103apo_specs(self):
        scope = AskarTelescope.Askar_103APO()
        self.assertEqual(scope.aperture.to('mm').magnitude, 103)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 700)
        self.assertEqual(scope.mass.to('gram').magnitude, 4750)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)

    def test_v60q_specs(self):
        scope = AskarTelescope.Askar_V_60Q()
        self.assertEqual(scope.aperture.to('mm').magnitude, 60)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 360)
        self.assertEqual(scope.mass.to('gram').magnitude, 2860)

    def test_fma230_specs(self):
        scope = AskarTelescope.Askar_FMA_230()
        self.assertEqual(scope.aperture.to('mm').magnitude, 50)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 275)
        self.assertEqual(scope.mass.to('gram').magnitude, 1200)

    def test_203apo_specs(self):
        scope = AskarTelescope.Askar_203APO()
        self.assertEqual(scope.aperture.to('mm').magnitude, 203)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1421)
        self.assertEqual(scope.mass.to('gram').magnitude, 18000)

if __name__ == '__main__':
    unittest.main()
