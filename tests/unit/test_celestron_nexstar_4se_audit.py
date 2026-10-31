import unittest

from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import Gender


class TestCelestronNexStar4SEAudit(unittest.TestCase):
    def test_nexstar_4se_audited_specs(self):
        """Verify the audited hardware specifications for Celestron NexStar 4SE."""
        scope = CelestronTelescope.Celestron_NexStar_4SE()
        self.assertEqual(scope.get_vendor(), "Celestron NexStar 4SE")
        self.assertEqual(scope.aperture.to("mm").magnitude, 102.0)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 1325.0)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 12.99, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 35.0)
        self.assertEqual(scope.mass.to("gram").magnitude, 2722)
        self.assertEqual(str(scope.connection_type), "1.375\"-24")
        self.assertEqual(scope.connection_gender, Gender.MALE)


if __name__ == "__main__":
    unittest.main()
