import unittest

from apts.opticalequipment.telescope.base import TelescopeType
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType, Gender


class TestCelestronC11EdgeHDAudit(unittest.TestCase):
    def test_c11_edgehd_specs(self):
        """Audit test for Celestron C11 EdgeHD based on official manufacturer documentation."""
        scope = CelestronTelescope.Celestron_C11_EdgeHD()
        self.assertEqual(scope.get_vendor(), "Celestron C11 EdgeHD")
        self.assertEqual(scope.aperture.to('mm').magnitude, 279.4)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 2800)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 95)
        self.assertEqual(scope.mass.to('gram').magnitude, 12701)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 2800 / 279.4, places=4)
        self.assertEqual(scope.telescope_type, TelescopeType.CATADIOPTRIC)
        self.assertEqual(scope.connection_type, ConnectionType.F_2)
        self.assertEqual(scope.connection_gender, Gender.FEMALE)

    def test_c11_edgehd_ota_specs(self):
        """Audit test for Celestron C11 EdgeHD OTA based on official manufacturer documentation."""
        scope = CelestronTelescope.Celestron_C11_EdgeHD_OTA()
        self.assertEqual(scope.get_vendor(), "Celestron C11 EdgeHD OTA")
        self.assertEqual(scope.aperture.to('mm').magnitude, 279.4)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 2800)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 95)
        self.assertEqual(scope.mass.to('gram').magnitude, 12701)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 2800 / 279.4, places=4)
        self.assertEqual(scope.telescope_type, TelescopeType.CATADIOPTRIC)
        self.assertEqual(scope.connection_type, ConnectionType.F_2)
        self.assertEqual(scope.connection_gender, Gender.FEMALE)

if __name__ == '__main__':
    unittest.main()
