import unittest

from apts.opticalequipment.telescope.base import TelescopeType
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.utils import ConnectionType, Gender


class TestSkyWatcherEvostar150EDAudit(unittest.TestCase):
    def test_evostar_150ed_specs(self):
        """
        Sky-Watcher Evostar 150ED Refractor Telescope specifications audit test.
        Source: http://skywatcher.com/product/evostar-150ed/
        """
        scope = Sky_watcherTelescope.Sky_Watcher_Evostar_150ED()
        self.assertEqual(scope.get_vendor(), "Sky-Watcher Evostar 150ED")
        self.assertEqual(scope.telescope_type, TelescopeType.REFRACTOR)
        self.assertEqual(scope.aperture.to("mm").magnitude, 150)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 1200)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 1200.0 / 150.0, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 0)
        self.assertEqual(scope.mass.to("gram").magnitude, 9500)
        self.assertEqual(scope.connection_type, ConnectionType.F_2)
        self.assertEqual(scope.connection_gender, Gender.FEMALE)


if __name__ == "__main__":
    unittest.main()
