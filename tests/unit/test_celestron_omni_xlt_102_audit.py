import unittest

from apts.opticalequipment.telescope.base import TelescopeType
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType, Gender


class TestCelestronOmniXLT102Audit(unittest.TestCase):
    def test_omni_xlt_102_specs(self):
        """
        Omni XLT 102 Refractor Telescope specifications audit test.
        Source: https://www.celestron.com/products/omni-xlt-102-telescope
        """
        scope = CelestronTelescope.Celestron_Omni_XLT_102()
        self.assertEqual(scope.get_vendor(), "Celestron Omni XLT 102")
        self.assertEqual(scope.telescope_type, TelescopeType.REFRACTOR)
        self.assertEqual(scope.aperture.to("mm").magnitude, 102.0)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 1000.0)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 1000.0 / 102.0, places=2)
        self.assertEqual(scope.mass.to("gram").magnitude, 4310.0)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 0.0)
        self.assertEqual(scope.connection_type, ConnectionType.F_2)
        self.assertEqual(scope.connection_gender, Gender.FEMALE)


if __name__ == "__main__":
    unittest.main()
