import unittest

from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType, Gender


class TestCelestronOmniXLT150Audit(unittest.TestCase):
    def test_celestron_omni_xlt_150_specs(self):
        """Audit test for Celestron Omni XLT 150 based on official documentation."""
        scope = CelestronTelescope.Celestron_Omni_XLT_150()

        self.assertEqual(scope.get_vendor(), "Celestron Omni XLT 150")
        self.assertEqual(scope.aperture.to("mm").magnitude, 150)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 750)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 47)
        self.assertEqual(scope.mass.to("gram").magnitude, 5443)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 750 / 150, places=2)
        self.assertEqual(scope.connection_type, ConnectionType.F_2)
        self.assertEqual(scope.connection_gender, Gender.FEMALE)


if __name__ == "__main__":
    unittest.main()
