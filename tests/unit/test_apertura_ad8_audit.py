import unittest
from apts.opticalequipment.telescope.vendors.apertura import AperturaTelescope

class TestAperturaAD8Audit(unittest.TestCase):
    def test_apertura_ad8_specs(self):
        scope = AperturaTelescope.Apertura_AD8_Dobsonian()
        self.assertEqual(scope.get_vendor(), "Apertura AD8 Dobsonian")
        self.assertEqual(scope.aperture.to('mm').magnitude, 203.2)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1200)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 50.0)
        # Weight 24.5 lbs (OTA) + 27.7 lbs (Base) = 52.2 lbs.
        # But our database stores OTA mass or total mass?
        # Looking at Apertura file: mass: 11113.
        # 11113 grams is approx 24.5 lbs. So it's OTA mass.
        self.assertEqual(scope.mass.to('gram').magnitude, 11113)

if __name__ == '__main__':
    unittest.main()
