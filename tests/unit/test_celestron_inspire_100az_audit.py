import unittest

from apts.opticalequipment.telescope.enums import TelescopeType
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType, Gender


class TestCelestronInspire100AZAudit(unittest.TestCase):
    def test_inspire_100az_specs(self):
        scope = CelestronTelescope.Celestron_Inspire_100AZ()
        self.assertEqual(scope.get_vendor(), "Celestron Inspire 100AZ")
        self.assertEqual(scope.aperture.to('mm').magnitude, 100)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 660)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 6.6, places=2)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 0)
        self.assertEqual(scope.mass.to('gram').magnitude, 2223)
        self.assertEqual(scope.connection_type, ConnectionType.F_1_25)
        self.assertEqual(scope.connection_gender, Gender.FEMALE)
        self.assertEqual(scope.telescope_type, TelescopeType.REFRACTOR)


if __name__ == '__main__':
    unittest.main()
