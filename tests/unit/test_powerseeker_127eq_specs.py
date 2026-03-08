import unittest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope

class TestPowerSeeker127EQ(unittest.TestCase):
    def test_powerseeker_127eq_specs(self):
        scope = CelestronTelescope.Celestron_PowerSeeker_127EQ()
        self.assertEqual(scope.get_vendor(), "Celestron PowerSeeker 127EQ")
        self.assertEqual(scope.aperture.to('mm').magnitude, 127)
        self.assertEqual(scope.focal_length.to('mm').magnitude, 1000)
        self.assertEqual(scope.central_obstruction.to('mm').magnitude, 41)
        self.assertEqual(scope.mass.to('gram').magnitude, 3230)
        self.assertEqual(scope.focal_ratio().magnitude, 1000/127)
        from apts.opticalequipment.telescope.base import TelescopeType
        self.assertEqual(scope.telescope_type, TelescopeType.NEWTONIAN_REFLECTOR)

if __name__ == '__main__':
    unittest.main()
