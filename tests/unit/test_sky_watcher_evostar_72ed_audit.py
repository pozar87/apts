import unittest

from apts.opticalequipment.telescope.enums import TelescopeType
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.utils import ConnectionType, Gender


class TestSkyWatcherEvostar72EDAudit(unittest.TestCase):
    def test_evostar_72ed_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Evostar_72ED()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Evostar 72ED")
        self.assertEqual(scope.aperture.to("mm").magnitude, 72)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 420)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 5.833, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 0)
        self.assertEqual(scope.mass.to("gram").magnitude, 2000)
        self.assertEqual(scope.connection_type, ConnectionType.F_2)
        self.assertEqual(scope.connection_gender, Gender.FEMALE)
        self.assertEqual(scope.telescope_type, TelescopeType.REFRACTOR)

    def test_evostar_72ed_ds_pro_specs(self):
        scope = Sky_watcherTelescope.Sky_Watcher_Evostar_72ED_DS_Pro()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Evostar 72ED DS-Pro")
        self.assertEqual(scope.aperture.to("mm").magnitude, 72)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 420)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 5.833, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 0)
        self.assertEqual(scope.mass.to("gram").magnitude, 1955)
        self.assertEqual(scope.connection_type, ConnectionType.F_2)
        self.assertEqual(scope.connection_gender, Gender.FEMALE)
        self.assertEqual(scope.telescope_type, TelescopeType.REFRACTOR)


if __name__ == "__main__":
    unittest.main()
