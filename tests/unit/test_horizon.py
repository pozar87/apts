import os
import unittest
import numpy as np
from apts.horizon import Horizon
from apts.conditions import Conditions


class TestHorizon(unittest.TestCase):
    def setUp(self):
        self.hrz_file = "test_horizon.hrz"
        with open(self.hrz_file, "w") as f:
            f.write("0 10\n")
            f.write("90 20\n")
            f.write("180 30\n")
            f.write("270 20\n")
            f.write("360 10\n")

    def tearDown(self):
        if os.path.exists(self.hrz_file):
            os.remove(self.hrz_file)

    def test_horizon_parsing(self):
        h = Horizon(self.hrz_file)
        self.assertEqual(h.get_altitude(0), 10)
        self.assertEqual(h.get_altitude(90), 20)
        self.assertEqual(h.get_altitude(180), 30)
        self.assertEqual(h.get_altitude(45), 15)  # Linear interpolation

    def test_horizon_visibility(self):
        h = Horizon(self.hrz_file)
        # At 90 deg azimuth, horizon is 20 deg
        self.assertTrue(h.is_visible(90, 21))
        self.assertFalse(h.is_visible(90, 19))

        # At 180 deg azimuth, horizon is 30 deg
        self.assertTrue(h.is_visible(180, 31))
        self.assertFalse(h.is_visible(180, 29))

    def test_conditions_with_horizon(self):
        c = Conditions(horizon_file=self.hrz_file)
        # At 180 deg azimuth, horizon is 30 deg
        self.assertTrue(c.is_visible(180, 31))
        self.assertFalse(c.is_visible(180, 29))

        # Test array input
        az = np.array([90, 180])
        alt = np.array([21, 29])
        visible = c.is_visible(az, alt)
        np.testing.assert_array_equal(visible, [True, False])

    def test_landscape_ini_support(self):
        ini_file = "test_landscape.ini"
        with open(ini_file, "w") as f:
            f.write("[landscape]\n")
            f.write(f"polygonal_horizon_list = {os.path.basename(self.hrz_file)}\n")

        try:
            h = Horizon(ini_file)
            # Should have loaded from test_horizon.hrz
            self.assertEqual(h.get_altitude(0), 10)
            self.assertEqual(h.get_altitude(90), 20)
        finally:
            if os.path.exists(ini_file):
                os.remove(ini_file)

    def test_conditions_fallback(self):
        # No horizon file, just min_object_altitude
        c = Conditions(min_object_altitude=15)
        self.assertTrue(c.is_visible(90, 16))
        self.assertFalse(c.is_visible(90, 14))

        # With azimuth limits
        c = Conditions(min_object_altitude=15, min_object_azimuth=170, max_object_azimuth=190)
        self.assertTrue(c.is_visible(180, 16))
        self.assertFalse(c.is_visible(90, 16))

        # With azimuth limits crossing 0 (e.g. 350 to 10)
        c = Conditions(min_object_altitude=15, min_object_azimuth=350, max_object_azimuth=10)
        self.assertTrue(c.is_visible(355, 16))
        self.assertTrue(c.is_visible(5, 16))
        self.assertFalse(c.is_visible(180, 16))


if __name__ == "__main__":
    unittest.main()
