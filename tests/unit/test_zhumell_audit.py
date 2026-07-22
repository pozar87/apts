import unittest
from apts.opticalequipment.telescope.vendors.zhumell import ZhumellTelescope


class TestZhumellAudit(unittest.TestCase):
    def test_zhumell_z6_specs(self):
        scope = ZhumellTelescope.Zhumell_Z6_Dobsonian()
        self.assertEqual(scope.get_vendor(), "Zhumell Z6 Dobsonian")
        self.assertEqual(scope.aperture.to('mm').magnitude, 152.4)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1200)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 31.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 8255)

    def test_zhumell_z8_specs(self):
        scope = ZhumellTelescope.Zhumell_Z8_Dobsonian()
        self.assertEqual(scope.get_vendor(), "Zhumell Z8 Dobsonian")
        self.assertEqual(scope.aperture.to('mm').magnitude, 203.2)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1200)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 50.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 11113)

    def test_zhumell_z10_specs(self):
        scope = ZhumellTelescope.Zhumell_Z10_Dobsonian()
        self.assertEqual(scope.get_vendor(), "Zhumell Z10 Dobsonian")
        self.assertEqual(scope.aperture.to('mm').magnitude, 254)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1250)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 63.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 15785)

    def test_zhumell_z12_specs(self):
        scope = ZhumellTelescope.Zhumell_Z12_Dobsonian()
        self.assertEqual(scope.get_vendor(), "Zhumell Z12 Dobsonian")
        self.assertEqual(scope.aperture.to('mm').magnitude, 304.8)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1520)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 70.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 21682)

    def test_zhumell_z16_specs(self):
        scope = ZhumellTelescope.Zhumell_Z16_Dobsonian()
        self.assertEqual(scope.get_vendor(), "Zhumell Z16 Dobsonian")
        self.assertEqual(scope.aperture.to('mm').magnitude, 406.4)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1800)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 88.0)
        self.assertEqual(scope.mass.to('gram').magnitude, 34246)


if __name__ == '__main__':
    unittest.main()
