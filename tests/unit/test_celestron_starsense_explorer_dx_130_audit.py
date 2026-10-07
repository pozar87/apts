import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.opticalequipment.telescope.base import TelescopeType
from apts.utils import ConnectionType

class TestCelestronStarSenseExplorerDX130Audit(unittest.TestCase):
    def test_starsense_dx130_specs(self):
        """
        Verify physical specifications for Celestron StarSense Explorer DX 130
        against official manufacturer technical specs.
        Source: https://www.celestron.com/products/starsense-explorer-dx-130az
        """
        scope = CelestronTelescope.Celestron_StarSense_Explorer_DX_130()

        # Vendor name string
        self.assertEqual(scope.get_vendor(), "Celestron StarSense Explorer DX 130")

        # Telescope Type
        self.assertEqual(scope.telescope_type, TelescopeType.NEWTONIAN_REFLECTOR)

        # Physical specs (Pint quantities)
        self.assertEqual(scope.aperture.to('mm').magnitude, 130)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 650)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 45)
        self.assertEqual(scope.mass.to('gram').magnitude, 3990)
        self.assertEqual(scope.connection_type, ConnectionType.F_2)
        self.assertEqual(scope.connection_type.value, '2')

        # Calculated focal ratio check: 650 / 130 = 5.0
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 5.0, places=2)

if __name__ == '__main__':
    unittest.main()
