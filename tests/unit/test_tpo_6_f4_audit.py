import unittest
from apts.opticalequipment.telescope.vendors.tpo import TpoTelescope
from apts.utils import ConnectionType

class TestTpo6F4Audit(unittest.TestCase):
    def test_tpo_6_f4_specs(self):
        """
        Audit for TPO 6" f/4 Newtonian reflecting OTA telescope.
        Source: https://optcorp.com/products/tpo-6-f-4-newtonian-reflecting-ota-telescope
        """
        scope = TpoTelescope.TPO_TPO_6_f_4_Newton()
        self.assertEqual(scope.get_vendor(), "TPO TPO 6\" f/4 Newton")
        self.assertEqual(scope.aperture.to('mm').magnitude, 154)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 610)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 63)
        self.assertEqual(scope.mass.to('gram').magnitude, 4354)
        self.assertEqual(scope.connection_type, ConnectionType.F_2)

        # Stated focal ratio: f/4, calculated: 610 / 154 = 3.96103896
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 3.9610, places=4)

if __name__ == '__main__':
    unittest.main()
