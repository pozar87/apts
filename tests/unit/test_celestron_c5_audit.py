import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope

class TestCelestronC5Audit(unittest.TestCase):
    def test_c5_ota_xlt_specs(self):
        scope = CelestronTelescope.Celestron_C5_OTA_XLT()
        self.assertEqual(scope.aperture.to('mm').magnitude, 127.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2722)

    def test_c5_sct_specs(self):
        scope = CelestronTelescope.Celestron_C5_SCT()
        self.assertEqual(scope.aperture.to('mm').magnitude, 127.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2722)

    def test_nexstar_5se_specs(self):
        # Even as part of a SE system, the OTA is a C5
        scope = CelestronTelescope.Celestron_NexStar_5SE()
        self.assertEqual(scope.aperture.to('mm').magnitude, 127.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2722)

    def test_astro_fi_5_sct_specs(self):
        scope = CelestronTelescope.Celestron_Astro_Fi_5_SCT()
        self.assertEqual(scope.aperture.to('mm').magnitude, 127.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2722)

if __name__ == '__main__':
    unittest.main()
