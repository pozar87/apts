import unittest

from apts.opticalequipment.telescope.base import TelescopeType
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope


class TestCelestronC14AXLTAudit(unittest.TestCase):
    def test_c14_a_xlt_ota_specs(self):
        scope = CelestronTelescope.Celestron_C14_A_XLT_OTA()
        self.assertEqual(scope.get_vendor(), "Celestron C14-A XLT (OTA)")
        self.assertEqual(scope.aperture.to("mm").magnitude, 355.6)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 3910)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 114)
        self.assertEqual(scope.mass.to("gram").magnitude, 20412)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 3910 / 355.6, places=5)
        self.assertEqual(scope.telescope_type, TelescopeType.SCHMIDT_CASSEGRAIN)
        self.assertEqual(str(scope.connection_type), "SC (Schmidt-Cassegrain)")

    def test_c14_ota_specs(self):
        scope = CelestronTelescope.Celestron_C14_OTA()
        self.assertEqual(scope.get_vendor(), "Celestron C14 OTA")
        self.assertEqual(scope.aperture.to("mm").magnitude, 355.6)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 3910)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 114)
        self.assertEqual(scope.mass.to("gram").magnitude, 20412)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 3910 / 355.6, places=5)
        self.assertEqual(scope.telescope_type, TelescopeType.SCHMIDT_CASSEGRAIN)
        self.assertEqual(str(scope.connection_type), "SC (Schmidt-Cassegrain)")

    def test_c14_sct_specs(self):
        scope = CelestronTelescope.Celestron_C14_SCT()
        self.assertEqual(scope.get_vendor(), "Celestron C14 SCT")
        self.assertEqual(scope.aperture.to("mm").magnitude, 355.6)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 3910)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 114)
        self.assertEqual(scope.mass.to("gram").magnitude, 20412)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 3910 / 355.6, places=5)
        self.assertEqual(scope.telescope_type, TelescopeType.SCHMIDT_CASSEGRAIN)
        self.assertEqual(str(scope.connection_type), "SC (Schmidt-Cassegrain)")


if __name__ == "__main__":
    unittest.main()
