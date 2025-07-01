import unittest
import pandas as pd
import pytz
from matplotlib import pyplot
from matplotlib import dates as mdates

# Ensure apts is discoverable, assuming tests are run from project root or similar
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from apts.utils import Utils
from apts.constants.graphconstants import get_plot_style # Needed by annotate_plot

class TestUtils(unittest.TestCase):

    def test_annotate_plot_timezone(self):
        # 1. Create a sample timezone-aware Pandas Series
        dates = pd.to_datetime([
            '2023-01-01 10:00:00',
            '2023-01-01 12:00:00',
            '2023-01-01 14:00:00'
        ])
        test_timezone_str = 'Europe/Berlin'
        test_timezone = pytz.timezone(test_timezone_str)

        # Localize to UTC first, then convert to the target timezone, common practice
        series = pd.Series(index=dates).tz_localize('UTC').tz_convert(test_timezone_str)

        # 2. Create a Matplotlib figure and axes
        fig, ax = pyplot.subplots()

        # 3. Plot the sample data on the axes
        # Plotting the series index if series itself has no values or for simplicity
        # For actual date plotting, pandas uses the index if it's a DatetimeIndex
        # We need to ensure that x-axis has dates.
        # A simple way is to plot series against itself if values are not important
        # or plot series.index against some dummy values.
        dummy_values = range(len(series.index))
        ax.plot(series.index, dummy_values)


        # 4. Call Utils.annotate_plot
        Utils.annotate_plot(ax, "Test Y Label", False, local_tz=test_timezone)

        # 5. Assertions
        formatter = ax.xaxis.get_major_formatter()
        self.assertIsInstance(formatter, mdates.DateFormatter, "Formatter should be a DateFormatter instance.")

        # Check the 'tz' attribute of the formatter
        # Note: mdates.DateFormatter stores the tzinfo object directly.
        self.assertEqual(formatter.tz, test_timezone,
                         f"DateFormatter's timezone ({formatter.tz}) does not match expected ({test_timezone}).")

        # 6. Cleanup
        pyplot.close(fig)

    def test_annotate_plot_no_timezone(self):
        # Test behavior when no timezone is explicitly passed (should default to None in formatter.tz, meaning rcParams['timezone'])
        dates = pd.to_datetime([
            '2023-01-01 10:00:00',
            '2023-01-01 12:00:00',
        ])
        series = pd.Series(index=dates) # Timezone-naive data

        fig, ax = pyplot.subplots()
        dummy_values = range(len(series.index))
        ax.plot(series.index, dummy_values)

        Utils.annotate_plot(ax, "Test Y Label No TZ", False, local_tz=None) # Explicitly pass None

        formatter = ax.xaxis.get_major_formatter()
        self.assertIsInstance(formatter, mdates.DateFormatter)
        self.assertIsNone(formatter.tz,
                          "DateFormatter's timezone should be None when no local_tz is passed and data is naive.")

        pyplot.close(fig)

if __name__ == '__main__':
    unittest.main()
