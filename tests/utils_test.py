import unittest
from apts.cache import get_timescale
from apts.utils.planetary import get_moon_phase

# Ensure apts is discoverable, assuming tests are run from project root or similar
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestUtils(unittest.TestCase):
    # test_annotate_plot_timezone and test_annotate_plot_no_timezone were removed
    # as the line they were testing (plot.xaxis.set_major_formatter)
    # has been removed from Utils.annotate_plot.
    # Other tests for Utils methods would go here if they existed.
    def test_get_moon_phase(self):
        ts = get_timescale()
        # Full moon on 2023-11-27 09:16 UTC
        # A day after, it should still be almost full
        time = ts.utc(2023, 11, 28, 9, 16)
        illumination = get_moon_phase(time)
        self.assertAlmostEqual(illumination, 99, delta=1)


if __name__ == '__main__':
    unittest.main()
