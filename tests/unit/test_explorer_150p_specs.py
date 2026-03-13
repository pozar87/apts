import unittest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

class TestExplorer150P(unittest.TestCase):
    def test_explorer_150p_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Explorer_150P()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Explorer 150P")
        self.assertEqual(scope.aperture.to('mm').magnitude, 150)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 750)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 47)
        self.assertEqual(scope.mass.to('gram').magnitude, 5900)
        self.assertEqual(scope.focal_ratio().magnitude, 750/150)

if __name__ == '__main__':
    unittest.main()
