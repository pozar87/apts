import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.opticalequipment.telescope.base import TelescopeType
from apts.utils import ConnectionType, Gender

class TestCelestronC925AXLTAudit(unittest.TestCase):
    def test_celestron_c9_25_a_xlt_ota_specs(self):
        """Audit test for Celestron C9.25-A XLT (OTA) based on official manufacturer documentation."""
        scope = CelestronTelescope.Celestron_C9_25_A_XLT_OTA()

        self.assertEqual(scope.get_vendor(), "Celestron C9.25-A XLT (OTA)")
        self.assertEqual(scope.aperture.to('mm').magnitude, 234.95)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 2350)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 85)
        self.assertEqual(scope.mass.to('gram').magnitude, 9070)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 2350 / 234.95, places=2)
        self.assertEqual(scope.telescope_type, TelescopeType.SCHMIDT_CASSEGRAIN)
        self.assertEqual(scope.connection_type, ConnectionType.SC)
        self.assertEqual(scope.connection_gender, Gender.MALE)

if __name__ == '__main__':
    unittest.main()
