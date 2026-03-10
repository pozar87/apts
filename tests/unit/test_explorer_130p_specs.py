import unittest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

class TestExplorer130P(unittest.TestCase):
    def test_explorer_130p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Explorer_130P()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Explorer 130P")
        self.assertEqual(scope.aperture.to('mm').magnitude, 130)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 650)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 34.5)
        self.assertEqual(scope.mass.to('gram').magnitude, 3660)
        self.assertEqual(scope.focal_ratio().magnitude, 650/130)

if __name__ == '__main__':
    unittest.main()
