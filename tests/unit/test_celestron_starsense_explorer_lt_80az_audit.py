import unittest

from apts.opticalequipment.telescope.base import TelescopeType
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType


class TestCelestronStarSenseExplorerLT80AZAudit(unittest.TestCase):
    def test_starsense_explorer_lt_80az_specs(self):
        """
        Verify physical specifications for Celestron StarSense Explorer LT 80AZ
        against official manufacturer technical specs.
        Source: https://www.celestron.com/products/starsense-explorer-lt-80az
        """
        scope = CelestronTelescope.Celestron_StarSense_Explorer_LT_80AZ()

        # Vendor name string
        self.assertEqual(scope.get_vendor(), "Celestron StarSense Explorer LT 80AZ")

        # Telescope Type
        self.assertEqual(scope.telescope_type, TelescopeType.REFRACTOR)

        # Physical specs (Pint quantities)
        self.assertEqual(scope.aperture.to('mm').magnitude, 80)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 900)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2450)
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)
        self.assertEqual(scope.connection_type.value, '1.25')

        # Calculated focal ratio check: 900 / 80 = 11.25
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 11.25, places=2)

if __name__ == '__main__':
    unittest.main()
