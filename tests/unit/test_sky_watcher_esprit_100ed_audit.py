import unittest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.utils import ConnectionType, Gender


class TestSkyWatcherEsprit100EDAudit(unittest.TestCase):
    def test_esprit_100ed_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Esprit_100ED()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Esprit 100ED")
        self.assertEqual(scope.aperture.to("mm").magnitude, 100)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 550)
        self.assertAlmostEqual(scope.focal_ratio(), 5.5, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 0)
        self.assertEqual(scope.mass.to("gram").magnitude, 6300)
        self.assertEqual(scope.connection_type, ConnectionType.M74)
        self.assertEqual(scope.connection_gender, Gender.FEMALE)


if __name__ == "__main__":
    unittest.main()
