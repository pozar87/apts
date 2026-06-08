import unittest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.utils import ConnectionType

class TestSkyWatcherAudit(unittest.TestCase):
    def test_traditional_dob_6_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Traditional_Dob_6()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Traditional Dob 6\"")
        self.assertEqual(scope.aperture.to('mm').magnitude, 153)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1200)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 34.5)
        self.assertEqual(scope.mass.to('gram').magnitude, 5900)

    def test_traditional_dob_8_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Traditional_Dob_8()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Traditional Dob 8\"")
        self.assertEqual(scope.aperture.to('mm').magnitude, 203)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1200)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 47)
        self.assertEqual(scope.mass.to('gram').magnitude, 11000)

    def test_skyliner_300p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Skyliner_300P()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Skyliner 300P")
        self.assertEqual(scope.aperture.to('mm').magnitude, 305)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1500)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 70)
        self.assertEqual(scope.mass.to('gram').magnitude, 21000)

    def test_virtuoso_gti_150p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Virtuoso_GTi_150P()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Virtuoso GTi 150P")
        self.assertEqual(scope.aperture.to('mm').magnitude, 150)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 750)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 48)
        self.assertEqual(scope.mass.to('gram').magnitude, 4800)
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)

if __name__ == '__main__':
    unittest.main()
