import unittest

from apts.opticalequipment.telescope.base import TelescopeType
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType, Gender


class TestCelestronFirstScope76Audit(unittest.TestCase):
    def test_firstscope_76_specs(self):
        """
        FirstScope 76 Newtonian Reflector specifications audit test.
        Source: https://www.celestron.com/products/firstscope-official-product-of-international-year-of-astronomy-2009
        """
        scope = CelestronTelescope.Celestron_FirstScope_76()
        self.assertEqual(scope.get_vendor(), "Celestron FirstScope 76")
        self.assertEqual(scope.telescope_type, TelescopeType.NEWTONIAN_REFLECTOR)
        self.assertEqual(scope.aperture.to("mm").magnitude, 76.0)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 300.0)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 300.0 / 76.0, places=2)
        self.assertEqual(scope.mass.to("gram").magnitude, 1956)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 28.0)
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)
        self.assertEqual(scope.connection_gender, Gender.FEMALE)


if __name__ == "__main__":
    unittest.main()
