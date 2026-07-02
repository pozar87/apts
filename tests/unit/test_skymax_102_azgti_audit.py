import unittest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.utils.equipment import ConnectionType

class TestSkyMax102AZGTiAudit(unittest.TestCase):
    def test_skymax_102_azgti_connection(self):
        scope = Sky_watcherTelescope.Sky_Watcher_SkyMax_102_AZ_GTi()
        # Verify that the connection type is 1.25"
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)

if __name__ == '__main__':
    unittest.main()
