import unittest

from apts.opticalequipment.telescope.base import TelescopeType
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.utils import ConnectionType, Gender


class TestCelestronNexStar4SEAudit(unittest.TestCase):
    def test_nexstar_4se_specs(self):
        """
        Celestron NexStar 4SE Maksutov-Cassegrain Telescope specifications audit test.
        Source: https://www.celestron.com/products/nexstar-4se-computerized-telescope
        """
        scope = CelestronTelescope.Celestron_NexStar_4SE()
        self.assertEqual(scope.get_vendor(), "Celestron NexStar 4SE")
        self.assertEqual(scope.telescope_type, TelescopeType.MAKSUTOV_CASSEGRAIN)
        self.assertEqual(scope.aperture.to("mm").magnitude, 102)
        self.assertEqual(scope.focal_length.to("mm").magnitude, 1325)
        self.assertAlmostEqual(scope.focal_ratio().magnitude, 1325.0 / 102.0, places=2)
        self.assertEqual(scope.central_obstruction.to("mm").magnitude, 35)
        self.assertEqual(scope.mass.to("gram").magnitude, 2722)
        self.assertEqual(scope.connection_type, ConnectionType.NX4)
        self.assertEqual(scope.connection_gender, Gender.MALE)


if __name__ == "__main__":
    unittest.main()
