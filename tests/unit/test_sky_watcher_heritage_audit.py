import unittest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

class TestSkyWatcherHeritageAudit(unittest.TestCase):
    def test_heritage_130p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Heritage_130P()
        self.assertEqual(scope.aperture.to('mm').magnitude, 130)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 650)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 40)
        self.assertEqual(scope.mass.to('gram').magnitude, 2948)

    def test_heritage_130p_flextube_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Heritage_130P_FlexTube()
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 40)
        self.assertEqual(scope.mass.to('gram').magnitude, 2948)

    def test_heritage_p130_flextube_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Heritage_P130_FlexTube()
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 40)
        self.assertEqual(scope.mass.to('gram').magnitude, 2948)

    def test_heritage_150p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Heritage_150P()
        self.assertEqual(scope.aperture.to('mm').magnitude, 150)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 750)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 48)
        self.assertEqual(scope.mass.to('gram').magnitude, 3629)

    def test_heritage_150p_flextube_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Heritage_150P_FlexTube()
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 48)
        self.assertEqual(scope.mass.to('gram').magnitude, 3629)

if __name__ == '__main__':
    unittest.main()
