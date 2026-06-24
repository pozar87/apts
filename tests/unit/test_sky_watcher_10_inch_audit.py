import unittest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

class TestSkyWatcher10InchAudit(unittest.TestCase):
    def test_traditional_dob_10_audit(self):
        # Verified via Sky-Watcher USA (https://www.skywatcherusa.com/products/sky-watcher-classic-250p)
        scope = Sky_watcherTelescope.Sky_Watcher_Traditional_Dob_10()

        # In current version of apts, vendor is set in from_database as f"{brand} {name}"
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Traditional Dob 10\"")
        self.assertEqual(scope.aperture.to('mm').magnitude, 254)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1200)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 64)
        self.assertEqual(scope.mass.to('gram').magnitude, 12700)

        # Verify focal ratio (1200 / 254 ≈ 4.724)
        # In apts, focal_ratio is a method, not a property
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 4.7244, places=4)

if __name__ == '__main__':
    unittest.main()
