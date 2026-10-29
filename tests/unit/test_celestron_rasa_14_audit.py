import unittest

from apts.opticalequipment.telescope.base import TelescopeType
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType, Gender


class TestCelestronRASA14Audit(unittest.TestCase):
    def test_celestron_rasa_14_specs(self):
        """
        Celestron RASA 14" (36cm Rowe-Ackermann Schmidt Astrograph) telescope specifications audit test.
        Source: https://www.celestron.com/products/36cm-rowe-ackermann-schmidt-astrograph-rasa-36cm-v2-optical-tube-assembly
        """
        scope_14 = CelestronTelescope.Celestron_RASA_14()
        self.assertEqual(scope_14.get_vendor(), "Celestron RASA 14\"")
        self.assertEqual(scope_14.telescope_type, TelescopeType.CATADIOPTRIC)
        self.assertAlmostEqual(scope_14.aperture.to("mm").magnitude, 355.6, places=1)
        self.assertEqual(scope_14.focal_length.to("mm").magnitude, 790)
        self.assertAlmostEqual(scope_14.focal_ratio().magnitude, 790.0 / 355.6, places=2)
        self.assertEqual(scope_14.central_obstruction.to("mm").magnitude, 158)
        self.assertEqual(scope_14.mass.to("gram").magnitude, 34019)
        self.assertEqual(scope_14.connection_type, ConnectionType.M48)
        self.assertEqual(scope_14.connection_gender, Gender.MALE)

        scope_36cm = CelestronTelescope.Celestron_RASA_36cm()
        self.assertEqual(scope_36cm.get_vendor(), "Celestron RASA 36cm")
        self.assertEqual(scope_36cm.telescope_type, TelescopeType.CATADIOPTRIC)
        self.assertAlmostEqual(scope_36cm.aperture.to("mm").magnitude, 355.6, places=1)
        self.assertEqual(scope_36cm.focal_length.to("mm").magnitude, 790)
        self.assertAlmostEqual(scope_36cm.focal_ratio().magnitude, 790.0 / 355.6, places=2)
        self.assertEqual(scope_36cm.central_obstruction.to("mm").magnitude, 158)
        self.assertEqual(scope_36cm.mass.to("gram").magnitude, 34019)
        self.assertEqual(scope_36cm.connection_type, ConnectionType.M48)
        self.assertEqual(scope_36cm.connection_gender, Gender.MALE)


if __name__ == "__main__":
    unittest.main()
