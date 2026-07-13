import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope

class TestCelestronC5Audit(unittest.TestCase):
    def test_c5_ota_xlt_specs(self):
        """
        The C5 Spotting Scope variant is officially 127mm.
        Source: https://www.celestron.com/products/c5-spotting-scope
        """
        scope = CelestronTelescope.Celestron_C5_OTA_XLT()
        self.assertEqual(scope.aperture.to('mm').magnitude, 127.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2722)
        # 1250 / 127 = 9.84...
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 9.84, places=2)

    def test_c5_sct_specs(self):
        """
        Standard C5 SCT is officially 125mm.
        Source: https://www.celestron.com/products/nexstar-5se-computerized-telescope
        """
        scope = CelestronTelescope.Celestron_C5_SCT()
        self.assertEqual(scope.aperture.to('mm').magnitude, 125.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2722)
        self.assertEqual(scope.focal_ratio().magnitude, 10.0)

    def test_nexstar_5se_specs(self):
        """
        NexStar 5SE is officially 125mm.
        Source: https://www.celestron.com/products/nexstar-5se-computerized-telescope
        """
        scope = CelestronTelescope.Celestron_NexStar_5SE()
        self.assertEqual(scope.aperture.to('mm').magnitude, 125.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2722)
        self.assertEqual(scope.focal_ratio().magnitude, 10.0)

    def test_astro_fi_5_sct_specs(self):
        """
        Astro-Fi 5 SCT is officially 125mm.
        Source: https://www.celestron.com/products/astro-fi-5-schmidt-cassegrain-telescope
        """
        scope = CelestronTelescope.Celestron_Astro_Fi_5_SCT()
        self.assertEqual(scope.aperture.to('mm').magnitude, 125.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2722)
        self.assertEqual(scope.focal_ratio().magnitude, 10.0)

if __name__ == '__main__':
    unittest.main()
