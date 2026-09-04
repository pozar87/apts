import unittest
from apts.opticalequipment.telescope.vendors.svbony import SvbonyTelescope
from apts.opticalequipment.telescope.enums import TelescopeType
from apts.utils import ConnectionType, Gender


class TestSVBonySV55080EDAudit(unittest.TestCase):
    def test_sv550_80ed_specs(self):
        scope = SvbonyTelescope.SVBony_SV550_80ED()
        self.assertEqual(scope.get_vendor(), "SVBony SV550 80ED")
        self.assertEqual(scope.aperture.to('mm').magnitude, 80)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 480)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 6.0)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2450)
        self.assertEqual(scope.optical_length.to('mm').magnitude, 90)
        self.assertEqual(scope.backfocus.to('mm').magnitude, 90)
        self.assertEqual(scope.connection_type, ConnectionType.F_2)
        self.assertEqual(scope.connection_gender, Gender.FEMALE)
        self.assertEqual(scope.telescope_type, TelescopeType.REFRACTOR)


if __name__ == '__main__':
    unittest.main()
