import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.opticalequipment.telescope.base import TelescopeType
from apts.utils import ConnectionType

class TestCelestronStarSenseExplorerLT127Audit(unittest.TestCase):
    def test_starsense_lt127_specs(self):
        """
        Verify physical specifications for Celestron StarSense Explorer LT 127AZ
        against official manufacturer technical specs.
        Source: https://www.celestron.com/products/starsense-explorer-lt-127az
        """
        scope = CelestronTelescope.Celestron_StarSense_Explorer_LT_127()

        # Vendor name string
        self.assertEqual(scope.get_vendor(), "Celestron StarSense Explorer LT 127AZ")

        # Telescope Type
        self.assertEqual(scope.telescope_type, TelescopeType.NEWTONIAN_REFLECTOR)

        # Physical specs (Pint quantities)
        self.assertEqual(scope.aperture.to('mm').magnitude, 127)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 41)
        self.assertEqual(scope.mass.to('gram').magnitude, 3440)
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)
        self.assertEqual(scope.connection_type.value, '1.25')

        # Calculated focal ratio check: 1000 / 127 = 7.8740...
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 1000 / 127, places=2)

if __name__ == '__main__':
    unittest.main()
