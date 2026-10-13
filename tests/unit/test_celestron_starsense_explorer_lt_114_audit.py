import unittest

from apts.opticalequipment.telescope.base import TelescopeType
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType


class TestCelestronStarSenseExplorerLT114Audit(unittest.TestCase):
    def test_starsense_lt114_specs(self):
        """
        Verify physical specifications for Celestron StarSense Explorer LT 114AZ
        against official manufacturer technical specs.
        Source: https://www.celestron.com/products/starsense-explorer-lt-114az
        """
        scope = CelestronTelescope.Celestron_StarSense_Explorer_LT_114()

        # Vendor name string
        self.assertEqual(scope.get_vendor(), "Celestron StarSense Explorer LT 114AZ")

        # Telescope Type
        self.assertEqual(scope.telescope_type, TelescopeType.NEWTONIAN_REFLECTOR)

        # Physical specs (Pint quantities)
        self.assertEqual(scope.aperture.to('mm').magnitude, 114)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 44)
        self.assertEqual(scope.mass.to('gram').magnitude, 2990)
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)
        self.assertEqual(scope.connection_type.value, '1.25')

        # Calculated focal ratio check: 1000 / 114 = 8.77
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 8.77, places=2)


if __name__ == '__main__':
    unittest.main()
