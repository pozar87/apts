import unittest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.utils import ConnectionType, Gender


class TestSkyWatcherEsprit80EDAudit(unittest.TestCase):
    def test_esprit_80ed_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Esprit_80ED()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Esprit 80ED")
        self.assertEqual(scope.aperture.to("mm").magnitude, 80)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 400)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 5.0, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 0)
        self.assertEqual(scope.mass.to("gram").magnitude, 3970)
        self.assertEqual(scope.connection_type, ConnectionType.M66)
        self.assertEqual(scope.connection_gender, Gender.FEMALE)


if __name__ == "__main__":
    unittest.main()
