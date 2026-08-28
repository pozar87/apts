import unittest
from apts.opticalequipment.telescope.vendors.william_optics import William_opticsTelescope

class TestWilliamOpticsRedCat51Audit(unittest.TestCase):
    def test_redcat_51_specs(self):
        scope = William_opticsTelescope.William_Optics_RedCat_51()
        self.assertEqual(scope.get_vendor(), "William Optics RedCat 51")
        self.assertEqual(scope.aperture.to('mm').magnitude, 51.0)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 250.0)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 1800.0)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 4.90196, places=4)

if __name__ == '__main__':
    unittest.main()
