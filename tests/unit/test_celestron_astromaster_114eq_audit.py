import unittest

from apts.opticalequipment.telescope.base import TelescopeType
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType


class TestCelestronAstroMaster114EQAudit(unittest.TestCase):
    def test_celestron_astromaster_114eq_specs(self):
        """
        Audit test for Celestron AstroMaster 114EQ telescope specifications.
        Specs verified via official Celestron documentation:
        https://www.celestron.com/products/astromaster-114eq-telescope
        """
        scope = CelestronTelescope.Celestron_AstroMaster_114EQ()

        self.assertEqual(scope.get_vendor(), "Celestron AstroMaster 114EQ")
        self.assertEqual(scope.telescope_type, TelescopeType.NEWTONIAN_REFLECTOR)

        # Physical specifications
        self.assertEqual(scope.aperture.to("mm").magnitude, 114)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 44)
        self.assertEqual(scope.mass.to("gram").magnitude, 2676)

        # Connections / visual back
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)
        self.assertEqual(scope.connection_type.value, "1.25")

        # Calculated optical parameters
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 1000 / 114, places=4)


if __name__ == "__main__":
    unittest.main()
