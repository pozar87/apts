import unittest

from apts.opticalequipment.telescope.base import TelescopeType
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType


class TestCelestronAstroMaster130EQAudit(unittest.TestCase):
    def test_astromaster_130eq_specs(self):
        """
        AstroMaster 130EQ Newtonian Reflector specifications audit test.
        Source: https://www.celestron.com/products/astromaster-130eq-telescope
        """
        scope = CelestronTelescope.Celestron_AstroMaster_130EQ()
        self.assertEqual(scope.get_vendor(), "Celestron AstroMaster 130EQ")
        self.assertEqual(scope.telescope_type, TelescopeType.NEWTONIAN_REFLECTOR)
        self.assertEqual(scope.aperture.to("mm").magnitude, 130.0)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 650.0)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 5.0, places=2)
        self.assertEqual(scope.mass.to("gram").magnitude, 3500)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 44.0)
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)


if __name__ == "__main__":
    unittest.main()
