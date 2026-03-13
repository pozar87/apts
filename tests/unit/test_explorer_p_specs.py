import unittest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

class TestExplorerPSpecs(unittest.TestCase):
    def test_explorer_150p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Explorer_150P()
        self.assertEqual(scope.aperture.to('mm').magnitude, 150)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 750)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 47)
        self.assertEqual(scope.mass.to('gram').magnitude, 5900)

    def test_explorer_200p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Explorer_200P()
        self.assertEqual(scope.aperture.to('mm').magnitude, 200)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 52)
        self.assertEqual(scope.mass.to('gram').magnitude, 8800)

    def test_explorer_250p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Explorer_250P()
        self.assertEqual(scope.aperture.to('mm').magnitude, 254)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1200)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 58)
        self.assertEqual(scope.mass.to('gram').magnitude, 14000)

    def test_explorer_300p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Explorer_300P()
        self.assertEqual(scope.aperture.to('mm').magnitude, 305)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1500)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 70)
        self.assertEqual(scope.mass.to('gram').magnitude, 20000)

if __name__ == '__main__':
    unittest.main()
