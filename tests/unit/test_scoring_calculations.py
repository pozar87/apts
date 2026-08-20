import unittest
import pandas as pd

from apts.scoring.calculations import (
    calculate_altitude_score,
    calculate_window_score,
    calculate_fov_score,
    calculate_moon_penalty_score,
    calculate_brightness_score,
    calculate_scores_bulk,
)
from apts.constants import ObjectTableLabels


class TestScoringCalculations(unittest.TestCase):
    def test_calculate_altitude_score(self):
        self.assertEqual(calculate_altitude_score(70.0), 30)
        self.assertEqual(calculate_altitude_score(65.0), 30)
        self.assertEqual(calculate_altitude_score(55.0), 25)
        self.assertEqual(calculate_altitude_score(40.0), 18)
        self.assertEqual(calculate_altitude_score(25.0), 10)
        self.assertEqual(calculate_altitude_score(15.0), 0)

    def test_calculate_window_score(self):
        self.assertEqual(calculate_window_score(360.0), 20)  # 6 hrs -> >= 5
        self.assertEqual(calculate_window_score(300.0), 20)  # 5 hrs -> >= 5
        self.assertEqual(calculate_window_score(240.0), 16)  # 4 hrs -> >= 3
        self.assertEqual(calculate_window_score(150.0), 12)  # 2.5 hrs -> >= 2
        self.assertEqual(calculate_window_score(90.0), 8)   # 1.5 hrs -> >= 1
        self.assertEqual(calculate_window_score(30.0), 0)   # 0.5 hrs -> 0

    def test_calculate_fov_score(self):
        self.assertEqual(calculate_fov_score(50.0), 30)   # in range (30, 110)
        self.assertEqual(calculate_fov_score(15.0), 18)   # in range (10, 200)
        self.assertEqual(calculate_fov_score(5.0), 0)     # outside range

    def test_calculate_moon_penalty_score(self):
        # Broadband
        self.assertAlmostEqual(calculate_moon_penalty_score(0.0, is_narrowband=False), 20.0)
        self.assertAlmostEqual(calculate_moon_penalty_score(50.0, is_narrowband=False), 9.0)
        self.assertAlmostEqual(calculate_moon_penalty_score(100.0, is_narrowband=False), 0.0)

        # Narrowband (always max 20 pts)
        self.assertEqual(calculate_moon_penalty_score(0.0, is_narrowband=True), 20.0)
        self.assertEqual(calculate_moon_penalty_score(50.0, is_narrowband=True), 20.0)

    def test_calculate_brightness_score(self):
        self.assertEqual(calculate_brightness_score(4.0), 10)  # < 5
        self.assertEqual(calculate_brightness_score(7.0), 7)   # < 8
        self.assertEqual(calculate_brightness_score(10.0), 4)  # < 11
        self.assertEqual(calculate_brightness_score(12.0), 1)  # default

    def test_calculate_scores_bulk(self):
        df = pd.DataFrame(
            {
                ObjectTableLabels.ALTITUDE: [70.0, 25.0],
                "window_minutes": [360.0, 90.0],
                "fov_ratio": [50.0, 15.0],
                "moon_separation": [50.0, 100.0],
                "Magnitude_float": [4.0, 12.0],
            }
        )

        res_broadband = calculate_scores_bulk(df, is_narrowband=False)
        self.assertEqual(len(res_broadband), 2)
        self.assertIn("total_score", res_broadband.columns)
        self.assertIn("s_alt", res_broadband.columns)
        self.assertIn("s_win", res_broadband.columns)
        self.assertIn("s_fov", res_broadband.columns)
        self.assertIn("s_moon", res_broadband.columns)
        self.assertIn("s_bright", res_broadband.columns)

        # Row 0 broadband: s_alt=30, s_win=20, s_fov=30, s_moon=9.0, s_bright=10 -> total=99.0
        self.assertEqual(res_broadband.iloc[0]["s_alt"], 30)
        self.assertEqual(res_broadband.iloc[0]["s_win"], 20)
        self.assertEqual(res_broadband.iloc[0]["s_fov"], 30)
        self.assertAlmostEqual(res_broadband.iloc[0]["s_moon"], 9.0)
        self.assertEqual(res_broadband.iloc[0]["s_bright"], 10)
        self.assertAlmostEqual(res_broadband.iloc[0]["total_score"], 99.0)

        # Test narrowband bulk
        res_narrowband = calculate_scores_bulk(df, is_narrowband=True)
        self.assertEqual(res_narrowband.iloc[0]["s_moon"], 20.0)
        self.assertAlmostEqual(res_narrowband.iloc[0]["total_score"], 110.0)
