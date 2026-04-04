import unittest
from apts.opticalequipment.telescope.vendors.william_optics import William_opticsTelescope

class TestRedCat61Specs(unittest.TestCase):
    def test_redcat61_specs(self):
        # Instantiate RedCat 61
        scope = William_opticsTelescope.William_Optics_RedCat_61()

        # Verify basic properties
        self.assertEqual(scope.get_vendor(), "William Optics RedCat 61")
        self.assertEqual(scope.aperture.magnitude, 61)
        self.assertEqual(scope.focal_length.magnitude, 300)
        self.assertEqual(scope.mass.magnitude, 2470)
        self.assertEqual(scope.central_obstruction.magnitude, 0)

        # Verify focal ratio
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 4.918, places=3)

        # Verify connections
        from apts.utils import ConnectionType, Gender
        self.assertEqual(scope.connection_type, ConnectionType.M48)
        self.assertEqual(scope.connection_gender, Gender.MALE)

if __name__ == '__main__':
    unittest.main()
