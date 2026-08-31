import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType, Gender


class TestCelestronNexStar6SEAudit(unittest.TestCase):
    def test_nexstar_6se_audited_specs(self):
        """Verify the audited hardware specifications for Celestron NexStar 6SE."""
        scope = CelestronTelescope.Celestron_NexStar_6SE()
        self.assertEqual(scope.get_vendor(), "Celestron NexStar 6SE")
        self.assertEqual(scope.aperture.to("mm").magnitude, 150)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 1500)
        self.assertAlmostEqual(scope.focal_ratio(), 10.0, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 56)
        self.assertEqual(scope.mass.to("gram").magnitude, 3629)
        self.assertEqual(scope.connection_type, ConnectionType.SC)
        self.assertEqual(scope.connection_gender, Gender.MALE)


if __name__ == "__main__":
    unittest.main()
