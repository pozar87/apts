import unittest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.utils import ConnectionType, Gender


class TestSkyWatcherEvostar120EDAudit(unittest.TestCase):
    def test_evostar_120ed_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Evostar_120ED()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Evostar 120ED")
        self.assertEqual(scope.aperture.to("mm").magnitude, 120)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 900)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 7.5, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 0)
        self.assertEqual(scope.mass.to("gram").magnitude, 5130)
        self.assertEqual(scope.connection_type, ConnectionType.F_2)
        self.assertEqual(scope.connection_gender, Gender.FEMALE)


if __name__ == "__main__":
    unittest.main()
