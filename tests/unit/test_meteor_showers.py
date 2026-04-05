import unittest
from apts.skyfield_searches.meteor_showers import _get_drifted_radiant

class TestMeteorShowers(unittest.TestCase):
    def test_get_drifted_radiant_no_drift(self):
        data = {
            "radiant": (10.0, 20.0),
            "d_ra_h": 0.0,
            "d_dec_d": 0.0
        }
        # Peak at 100, current at 100 -> no drift
        ra, dec = _get_drifted_radiant(data, 100.0, 100.0)
        self.assertEqual(ra, 10.0)
        self.assertEqual(dec, 20.0)

    def test_get_drifted_radiant_with_drift(self):
        data = {
            "radiant": (10.0, 20.0),
            "d_ra_h": 0.1,
            "d_dec_d": 0.5
        }
        # Peak at 100, current at 110 -> 10 deg diff
        # drifted_ra = (10.0 + 10 * 0.1) % 24 = 11.0
        # drifted_dec = 20.0 + 10 * 0.5 = 25.0
        ra, dec = _get_drifted_radiant(data, 100.0, 110.0)
        self.assertAlmostEqual(ra, 11.0)
        self.assertAlmostEqual(dec, 25.0)

    def test_get_drifted_radiant_wrap_around_positive(self):
        data = {
            "radiant": (23.5, 20.0),
            "d_ra_h": 0.1,
            "d_dec_d": 0.0
        }
        # Peak at 100, current at 110 -> 10 deg diff
        # drifted_ra = (23.5 + 10 * 0.1) % 24 = 24.5 % 24 = 0.5
        ra, dec = _get_drifted_radiant(data, 100.0, 110.0)
        self.assertAlmostEqual(ra, 0.5)

    def test_get_drifted_radiant_wrap_around_longitude(self):
        data = {
            "radiant": (10.0, 20.0),
            "d_ra_h": 0.1,
            "d_dec_d": 0.0
        }
        # Peak at 355, current at 5 -> 10 deg diff (355 to 360/0 to 5)
        # diff = (5 - 355 + 180) % 360 - 180 = (10 + 180) % 360 - 180 = 190 - 180 = 10
        ra, dec = _get_drifted_radiant(data, 355.0, 5.0)
        self.assertAlmostEqual(ra, 11.0)

        # Peak at 5, current at 355 -> -10 deg diff
        # diff = (355 - 5 + 180) % 360 - 180 = (350 + 180) % 360 - 180 = 530 % 360 - 180 = 170 - 180 = -10
        ra, dec = _get_drifted_radiant(data, 5.0, 355.0)
        self.assertAlmostEqual(ra, 9.0)

    def test_get_drifted_radiant_default_coefficients(self):
        data = {
            "radiant": (10.0, 20.0)
            # d_ra_h and d_dec_d missing
        }
        ra, dec = _get_drifted_radiant(data, 100.0, 110.0)
        self.assertEqual(ra, 10.0)
        self.assertEqual(dec, 20.0)

if __name__ == '__main__':
    unittest.main()
