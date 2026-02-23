import unittest
from unittest.mock import patch
from apts.cache import get_timescale
from apts.utils.planetary import (
    get_moon_illumination,
    get_moon_illumination_details,
    get_moon_age,
)

# Ensure apts is discoverable, assuming tests are run from project root or similar
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestUtils(unittest.TestCase):
    # test_annotate_plot_timezone and test_annotate_plot_no_timezone were removed
    # as the line they were testing (plot.xaxis.set_major_formatter)
    # has been removed from Utils.annotate_plot.
    # Other tests for Utils methods would go here if they existed.
    def test_get_moon_illumination(self):
        ts = get_timescale()
        # Full moon on 2023-11-27 09:16 UTC
        # A day after, it should still be almost full
        time = ts.utc(2023, 11, 28, 9, 16)
        illumination = get_moon_illumination(time)
        self.assertAlmostEqual(illumination, 99, delta=1)

    def test_get_moon_illumination_details(self):
        ts = get_timescale()
        # Waxing crescent on 2023-11-15
        time_waxing = ts.utc(2023, 11, 15)
        _, is_waxing = get_moon_illumination_details(time_waxing)
        self.assertTrue(is_waxing)

        # Waning gibbous on 2023-11-30
        time_waning = ts.utc(2023, 11, 30)
        _, is_waxing = get_moon_illumination_details(time_waning)
        self.assertFalse(is_waxing)

    def test_get_moon_age(self):
        ts = get_timescale()
        # New Moon was on 2024-02-09 around 22:59 UTC
        time = ts.utc(2024, 2, 10, 22, 59)
        age = get_moon_age(time)
        # It should be around 1.0 day
        self.assertAlmostEqual(age, 1.0, delta=0.1)

    @patch("apts.utils.planetary.almanac.find_discrete")
    def test_get_moon_age_fallback(self, mock_find_discrete):
        # Force fallback by returning empty lists
        mock_find_discrete.return_value = ([], [])
        ts = get_timescale()
        # Full moon roughly
        time = ts.utc(2024, 2, 24)
        age = get_moon_age(time)
        # Lunar month is ~29.5 days. Full moon is ~14.7 days.
        self.assertAlmostEqual(age, 14.7, delta=1.0)


if __name__ == "__main__":
    unittest.main()
