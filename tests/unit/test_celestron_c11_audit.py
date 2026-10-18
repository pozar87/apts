import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.opticalequipment.telescope.base import TelescopeType

class TestCelestronC11Audit(unittest.TestCase):
    def test_c11_a_xlt_ota_specs(self):
        scope = CelestronTelescope.Celestron_C11_A_XLT_OTA()
        self.assertEqual(scope.get_vendor(), "Celestron C11-A XLT (OTA)")
        self.assertEqual(scope.aperture.to('mm').magnitude, 279.4)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 2800)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 95)
        self.assertEqual(scope.mass.to('gram').magnitude, 12470)
        self.assertEqual(scope.focal_ratio().magnitude, 2800 / 279.4)
        self.assertEqual(scope.telescope_type, TelescopeType.SCHMIDT_CASSEGRAIN)
        self.assertEqual(str(scope.connection_type), "SC (Schmidt-Cassegrain)")

    def test_c11_ota_specs(self):
        scope = CelestronTelescope.Celestron_C11_OTA()
        self.assertEqual(scope.get_vendor(), "Celestron C11 OTA")
        self.assertEqual(scope.aperture.to('mm').magnitude, 279.4)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 2800)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 95)
        self.assertEqual(scope.mass.to('gram').magnitude, 12470)
        self.assertEqual(scope.focal_ratio().magnitude, 2800 / 279.4)
        self.assertEqual(scope.telescope_type, TelescopeType.SCHMIDT_CASSEGRAIN)
        self.assertEqual(str(scope.connection_type), "SC (Schmidt-Cassegrain)")

if __name__ == '__main__':
    unittest.main()
