import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope

class TestCelestronC8EdgeHDAudit(unittest.TestCase):
    def test_c8_edgehd_specs(self):
        scope = CelestronTelescope.Celestron_C8_EdgeHD()
        self.assertEqual(scope.get_vendor(), "Celestron C8 EdgeHD")
        self.assertEqual(scope.aperture.to('mm').magnitude, 203.2)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 2032)
        # Expected corrected value
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 64)
        self.assertEqual(scope.mass.to('gram').magnitude, 6350)
        self.assertEqual(scope.focal_ratio().magnitude, 10.0)

    def test_c8_edgehd_ota_specs(self):
        scope = CelestronTelescope.Celestron_C8_EdgeHD_OTA()
        self.assertEqual(scope.get_vendor(), "Celestron C8 EdgeHD OTA")
        self.assertEqual(scope.aperture.to('mm').magnitude, 203.2)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 2032)
        # Expected corrected value
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 64)
        self.assertEqual(scope.mass.to('gram').magnitude, 6350)
        self.assertEqual(scope.focal_ratio().magnitude, 10.0)

if __name__ == '__main__':
    unittest.main()
