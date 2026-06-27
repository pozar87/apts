import unittest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

class TestSkyWatcherClassic200PAudit(unittest.TestCase):
    def test_traditional_dob_8_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Traditional_Dob_8()
        # Verify basic attributes
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Traditional Dob 8\"")
        self.assertEqual(scope.aperture.to('mm').magnitude, 203.2)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1200)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 48)
        self.assertEqual(scope.mass.to('gram').magnitude, 9072)

        # Verify calculated focal ratio
        # 1200 / 203.2 = 5.9055118...
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 5.9055, places=4)

if __name__ == '__main__':
    unittest.main()
