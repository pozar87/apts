import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType, Gender


class TestCelestronAstroMaster70AZAudit(unittest.TestCase):
    def test_astromaster_70az_audited_specs(self):
        """Verify the audited hardware specifications for Celestron AstroMaster 70AZ."""
        scope = CelestronTelescope.Celestron_AstroMaster_70AZ()
        self.assertEqual(scope.get_vendor(), "Celestron AstroMaster 70AZ")
        self.assertEqual(scope.aperture.to("mm").magnitude, 70)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 900)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 12.857, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 0)
        self.assertEqual(scope.mass.to("gram").magnitude, 1315)
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)
        self.assertEqual(scope.connection_gender, Gender.FEMALE)


if __name__ == "__main__":
    unittest.main()
