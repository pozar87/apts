import unittest

from apts.opticalequipment.telescope.base import TelescopeType
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType, Gender


class TestCelestronRASA11Audit(unittest.TestCase):
    def test_celestron_rasa_11_specs(self):
        """
        Celestron RASA 11" (11" Rowe-Ackermann Schmidt Astrograph) telescope specifications audit test.
        Source: https://www.celestron.com/products/11in-rowe-ackermann-schmidt-astrograph-rasa-11-v2-optical-tube-assembly
        """
        scope = CelestronTelescope.Celestron_RASA_11()
        self.assertEqual(scope.get_vendor(), "Celestron RASA 11\"")
        self.assertEqual(scope.telescope_type, TelescopeType.CATADIOPTRIC)
        self.assertAlmostEqual(scope.aperture.to("mm").magnitude, 279.4, places=1)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 620)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 620.0 / 279.4, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 114)
        self.assertEqual(scope.mass.to("gram").magnitude, 19504)
        self.assertEqual(scope.connection_type, ConnectionType.M48)
        self.assertEqual(scope.connection_gender, Gender.MALE)


if __name__ == "__main__":
    unittest.main()
