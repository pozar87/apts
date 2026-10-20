import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType, Gender

class TestCelestronC8AXLTAudit(unittest.TestCase):
    def test_celestron_c8_a_xlt_ota_specs(self):
        """Audit test for Celestron C8-A XLT (OTA) based on official documentation."""
        scope = CelestronTelescope.Celestron_C8_A_XLT_OTA()

        self.assertEqual(scope.get_vendor(), "Celestron C8-A XLT (OTA)")
        self.assertEqual(scope.aperture.to('mm').magnitude, 203.2)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 2032)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 64)
        self.assertEqual(scope.mass.to('gram').magnitude, 5670)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 10.0, places=2)
        self.assertEqual(scope.connection_type, ConnectionType.SC)
        self.assertEqual(scope.connection_gender, Gender.MALE)

if __name__ == '__main__':
    unittest.main()
