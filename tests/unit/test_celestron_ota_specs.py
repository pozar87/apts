import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope

class TestCelestronOTASpecs(unittest.TestCase):
    def test_c11_ota_specs(self):
        scope = CelestronTelescope.Celestron_C11_OTA()
        self.assertEqual(scope.get_vendor(), "Celestron C11 OTA")
        self.assertEqual(scope.aperture.to('mm').magnitude, 279.4)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 2800)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 95)
        self.assertEqual(scope.mass.to('gram').magnitude, 12470)

    def test_c14_ota_specs(self):
        scope = CelestronTelescope.Celestron_C14_OTA()
        self.assertEqual(scope.get_vendor(), "Celestron C14 OTA")
        self.assertEqual(scope.aperture.to('mm').magnitude, 355.6)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 3910)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 114)
        self.assertEqual(scope.mass.to('gram').magnitude, 20410)

    def test_nexstar_4se_specs(self):
        scope = CelestronTelescope.Celestron_NexStar_4SE()
        self.assertEqual(scope.get_vendor(), "Celestron NexStar 4SE")
        self.assertEqual(scope.aperture.to('mm').magnitude, 102)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1325)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 35)
        self.assertEqual(scope.mass.to('gram').magnitude, 2722)

    def test_nexstar_5se_specs(self):
        scope = CelestronTelescope.Celestron_NexStar_5SE()
        self.assertEqual(scope.get_vendor(), "Celestron NexStar 5SE")
        self.assertEqual(scope.aperture.to('mm').magnitude, 125)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1250)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 51)
        self.assertEqual(scope.mass.to('gram').magnitude, 2722)

    def test_c6_ota_specs(self):
        scope = CelestronTelescope.Celestron_C6_OTA()
        self.assertEqual(scope.get_vendor(), "Celestron C6 OTA")
        self.assertEqual(scope.aperture.to('mm').magnitude, 150)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1500)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 56)
        self.assertEqual(scope.mass.to('gram').magnitude, 4536)

    def test_c8_ota_specs(self):
        scope = CelestronTelescope.Celestron_C8_OTA()
        self.assertEqual(scope.get_vendor(), "Celestron C8 OTA")
        self.assertEqual(scope.aperture.to('mm').magnitude, 203.2)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 2032)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 64)
        self.assertEqual(scope.mass.to('gram').magnitude, 5670)

    def test_c9_25_ota_specs(self):
        scope = CelestronTelescope.Celestron_C9_25_OTA()
        self.assertEqual(scope.get_vendor(), "Celestron C9.25 OTA")
        self.assertEqual(scope.aperture.to('mm').magnitude, 234.95)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 2350)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 85)
        self.assertEqual(scope.mass.to('gram').magnitude, 9070)

    def test_firstscope_76_specs(self):
        scope = CelestronTelescope.Celestron_FirstScope_76()
        self.assertEqual(scope.get_vendor(), "Celestron FirstScope 76")
        self.assertEqual(scope.aperture.to('mm').magnitude, 76)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 300)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 28)
        self.assertEqual(scope.mass.to('gram').magnitude, 640)

    def test_inspire_100az_specs(self):
        scope = CelestronTelescope.Celestron_Inspire_100AZ()
        self.assertEqual(scope.get_vendor(), "Celestron Inspire 100AZ")
        self.assertEqual(scope.aperture.to('mm').magnitude, 100)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 660)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2200)

if __name__ == '__main__':
    unittest.main()
