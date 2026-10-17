import unittest

from apts.opticalequipment.telescope.base import TelescopeType
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType


class TestCelestronAstroMaster90AZAudit(unittest.TestCase):
    def test_astromaster_90az_specs(self):
        """
        Verify physical specifications for Celestron AstroMaster 90AZ refractor
        against official manufacturer technical specs.
        Source: https://www.celestron.com/products/astromaster-90az-telescope
        """
        scope = CelestronTelescope.Celestron_AstroMaster_90AZ()

        # Vendor string
        self.assertEqual(scope.get_vendor(), "Celestron AstroMaster 90AZ")

        # Telescope Type
        self.assertEqual(scope.telescope_type, TelescopeType.REFRACTOR)

        # Physical specs
        self.assertEqual(scope.aperture.to('mm').magnitude, 90)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 1996)
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)
        self.assertEqual(scope.connection_type.value, '1.25')

        # Calculated focal ratio check: 1000 / 90 = 11.111...
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 1000 / 90, places=4)


if __name__ == '__main__':
    unittest.main()
