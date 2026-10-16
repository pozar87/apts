import unittest

from apts.opticalequipment.telescope.base import TelescopeType
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType, Gender


class TestCelestronRASA8Audit(unittest.TestCase):
    def test_celestron_rasa_8_specs(self):
        """
        Celestron RASA 8" (Rowe-Ackermann Schmidt Astrograph 8") telescope specifications audit test.
        Source: https://www.celestron.com/products/8in-rowe-ackermann-schmidt-astrograph-rasa-8-optical-tube-assembly
        """
        scope = CelestronTelescope.Celestron_RASA_8()
        self.assertEqual(scope.get_vendor(), "Celestron RASA 8\"")
        self.assertEqual(scope.telescope_type, TelescopeType.CATADIOPTRIC)
        self.assertAlmostEqual(scope.aperture.to("mm").magnitude, 203.2, places=1)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 400)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 400.0 / 203.2, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 93)
        self.assertEqual(scope.mass.to("gram").magnitude, 7711)
        self.assertEqual(scope.connection_type, ConnectionType.M48)
        self.assertEqual(scope.connection_gender, Gender.MALE)


if __name__ == "__main__":
    unittest.main()
