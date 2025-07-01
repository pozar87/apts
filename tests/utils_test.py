import unittest
import pandas as pd
import pytz
from matplotlib import pyplot
from matplotlib import dates as mdates
import datetime # Added for datetime.timezone.utc

# Ensure apts is discoverable, assuming tests are run from project root or similar
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from apts.utils import Utils
from apts.constants.graphconstants import get_plot_style # Needed by annotate_plot

class TestUtils(unittest.TestCase):
    # test_annotate_plot_timezone and test_annotate_plot_no_timezone were removed
    # as the line they were testing (plot.xaxis.set_major_formatter)
    # has been removed from Utils.annotate_plot.
    # Other tests for Utils methods would go here if they existed.
    pass

if __name__ == '__main__':
    unittest.main()
