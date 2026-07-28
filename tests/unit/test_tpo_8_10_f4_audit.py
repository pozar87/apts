import unittest
from apts.opticalequipment.telescope.vendors.tpo import TpoTelescope
from apts.utils import ConnectionType
from apts.opticalequipment.telescope.base import TelescopeType

class TestTpo810F4Audit(unittest.TestCase):
    def test_tpo_8_f4_specs(self):
        """
        Audit for TPO 8" f/4 Newtonian reflecting OTA telescope.
        Source: https://optcorp.com/products/tpo-8-f-4-newtonian-reflecting-ota-telescope
        """
        scope = TpoTelescope.TPO_TPO_8_f_4_Newton()
        self.assertEqual(scope.get_vendor(), "TPO TPO 8\" f/4 Newton")
        self.assertEqual(scope.telescope_type, TelescopeType.NEWTONIAN_REFLECTOR)
        self.assertEqual(scope.aperture.to('mm').magnitude, 200)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 800)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 70)
        self.assertEqual(scope.mass.to('gram').magnitude, 8709)
        self.assertEqual(scope.connection_type, ConnectionType.F_2)

        # Derived focal ratio: 800 / 200 = 4.0
        self.assertEqual(scope.focal_ratio().magnitude, 4.0)

    def test_tpo_10_f4_specs(self):
        """
        Audit for TPO 10" f/4 Newtonian reflecting OTA telescope.
        Source: https://optcorp.com/products/tpo-10-f-4-newtonian-reflecting-ota-telescope
        """
        scope = TpoTelescope.TPO_TPO_10_f_4_Newton()
        self.assertEqual(scope.get_vendor(), "TPO TPO 10\" f/4 Newton")
        self.assertEqual(scope.telescope_type, TelescopeType.NEWTONIAN_REFLECTOR)
        self.assertEqual(scope.aperture.to('mm').magnitude, 254)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1016)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 70)
        self.assertEqual(scope.mass.to('gram').magnitude, 13290)
        self.assertEqual(scope.connection_type, ConnectionType.F_2)

        # Derived focal ratio: 1016 / 254 = 4.0
        self.assertEqual(scope.focal_ratio().magnitude, 4.0)

if __name__ == '__main__':
    unittest.main()
