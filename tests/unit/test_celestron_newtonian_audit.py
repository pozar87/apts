import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils.equipment import ConnectionType

class TestCelestronNewtonianAudit(unittest.TestCase):
    def test_astromaster_130eq_specs(self):
        scope = CelestronTelescope.Celestron_AstroMaster_130EQ()
        self.assertEqual(scope.get_vendor(), "Celestron AstroMaster 130EQ")
        self.assertEqual(scope.aperture.to('mm').magnitude, 130)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 650)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 44)
        self.assertEqual(scope.mass.to('gram').magnitude, 3500)
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)

    def test_astromaster_114eq_specs(self):
        scope = CelestronTelescope.Celestron_AstroMaster_114EQ()
        self.assertEqual(scope.get_vendor(), "Celestron AstroMaster 114EQ")
        self.assertEqual(scope.aperture.to('mm').magnitude, 114)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 44)
        self.assertEqual(scope.mass.to('gram').magnitude, 2676)
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)

    def test_astrofi_130_specs(self):
        scope = CelestronTelescope.Celestron_AstroFi_130()
        self.assertEqual(scope.get_vendor(), "Celestron AstroFi 130")
        self.assertEqual(scope.aperture.to('mm').magnitude, 130)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 650)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 38)
        self.assertEqual(scope.mass.to('gram').magnitude, 3628)
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)

    def test_powerseeker_127eq_specs(self):
        scope = CelestronTelescope.Celestron_PowerSeeker_127EQ()
        self.assertEqual(scope.get_vendor(), "Celestron PowerSeeker 127EQ")
        self.assertEqual(scope.aperture.to('mm').magnitude, 127)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 41)
        self.assertEqual(scope.mass.to('gram').magnitude, 3230)
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)

if __name__ == '__main__':
    unittest.main()
