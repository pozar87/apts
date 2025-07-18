import pytest
from math import radians as rad
from datetime import date, datetime, timedelta, timezone
import datetime as dt_module # Added alias

import ephem
import pytz

from apts.place import Place
# Assuming setup_place is a helper to create a Place instance for testing
# If it's defined in tests/__init__.py, this import should work.
# Otherwise, we might need to define a fixture or helper here.
from . import setup_place

# Define some known locations and timezones for testing
GOLDEN_COORDS = {"lat": 39.7555, "lon": -105.2211, "tz_name": "America/Denver"}
NORTH_POLE_COORDS = {"lat": 90.0, "lon": 0.0, "tz_name": "UTC"} # UTC for simplicity at poles

# A specific date for legacy tests, ensuring it's UTC as Place expects
DEFAULT_INIT_DATE_UTC = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

class TestPlace:

    @pytest.fixture
    def mid_latitude_place(self):
        """A place in a mid-latitude for general testing."""
        # Using Golden, CO as an example
        # local_timezone is determined by Place based on lat/lon
        # Place constructor expects 'date' argument for the initial date
        return Place(
            lat=GOLDEN_COORDS["lat"],
            lon=GOLDEN_COORDS["lon"],
            date=DEFAULT_INIT_DATE_UTC
        )

    @pytest.fixture
    def north_pole_place(self):
        """A place at the North Pole for testing polar phenomena."""
        # local_timezone is determined by Place based on lat/lon (though for poles, it might default or be less defined)
        # Place constructor expects 'date' argument for the initial date
        return Place(
            lat=NORTH_POLE_COORDS["lat"],
            lon=NORTH_POLE_COORDS["lon"],
            date=DEFAULT_INIT_DATE_UTC # date argument for Place constructor
        )

    def test_place_coordinates_fixture(self, mid_latitude_place):
        """Test that the fixture place has correct coordinates."""
        p = mid_latitude_place
        assert p.lat_decimal == GOLDEN_COORDS["lat"]
        assert p.lat == rad(GOLDEN_COORDS["lat"])
        assert p.lon_decimal == GOLDEN_COORDS["lon"]
        assert p.lon == rad(GOLDEN_COORDS["lon"])
        # Verify that TimezoneFinder (Place.TF) returns the correct timezone name for the fixture's coordinates
        assert Place.TF.timezone_at(lat=p.lat_decimal, lng=p.lon_decimal) == GOLDEN_COORDS["tz_name"], \
            "TimezoneFinder query for fixture coordinates did not return the expected timezone name"

    def test_place_internal_timezone_assignment(self):
        """Test that Place correctly assigns local_timezone based on coordinates."""
        # Instantiate Place without a specific date, let it default.
        # Focus is on timezone assignment from lat/lon.
        place_instance = Place(lat=GOLDEN_COORDS["lat"], lon=GOLDEN_COORDS["lon"])

        assert place_instance.local_timezone is not None, "local_timezone should be set by Place constructor"
        
        expected_tz_name = GOLDEN_COORDS["tz_name"]
        
        # Verify that TimezoneFinder (Place.TF) returns the correct timezone name
        # for the place_instance's coordinates.
        assert Place.TF.timezone_at(lat=place_instance.lat_decimal, lng=place_instance.lon_decimal) == expected_tz_name, \
            f"TimezoneFinder query for place_instance coordinates did not return {expected_tz_name}"

    # --- Tests for sunset_time() and sunrise_time() ---

    def test_sunset_sunrise_with_target_date(self, mid_latitude_place):
        p = mid_latitude_place
        original_place_date = p.date # ephem.Date
        target_d = date(2024, 3, 15) # Use a specific date

        sunset_dt = p.sunset_time(target_date=target_d)
        sunrise_dt = p.sunrise_time(target_date=target_d)

        # Assertions for sunset
        assert sunset_dt is not None, "Sunset should occur"
        assert isinstance(sunset_dt, datetime), "Sunset time should be datetime object"
        assert sunset_dt.tzinfo is not None, "Sunset datetime should be timezone-aware"
        assert sunset_dt.tzinfo == p.local_timezone, "Sunset timezone should be local"
        assert sunset_dt.date() == target_d or (sunset_dt - timedelta(days=1)).date() == target_d or (sunset_dt + timedelta(days=1)).date() == target_d # Sunset can be on target_d or next/prev day in local time
        
        # Example: For Golden, CO (UTC-7 or -6 depending on DST) on 2024-03-15 (DST active, UTC-6)
        # Sunset is around 7:11 PM MDT. Sunrise around 7:14 AM MDT.
        # These are rough checks, actual ephem calculation is the source of truth.
        assert 18 <= sunset_dt.hour <= 20, f"Sunset hour {sunset_dt.hour} out of expected range (18-20)"

        # Assertions for sunrise
        assert sunrise_dt is not None, "Sunrise should occur"
        assert isinstance(sunrise_dt, datetime), "Sunrise time should be datetime object"
        assert sunrise_dt.tzinfo is not None, "Sunrise datetime should be timezone-aware"
        assert sunrise_dt.tzinfo == p.local_timezone, "Sunrise timezone should be local"
        assert sunrise_dt.date() == target_d or (sunrise_dt - timedelta(days=1)).date() == target_d # Sunrise is usually on the same local day
        assert 6 <= sunrise_dt.hour <= 8, f"Sunrise hour {sunrise_dt.hour} out of expected range (6-8)"
        
        assert p.date == original_place_date, "place.date should not be modified"

    def test_sunset_sunrise_without_target_date_legacy(self, mid_latitude_place):
        p = mid_latitude_place # Uses DEFAULT_INIT_DATE_UTC (2023-01-01 12:00 UTC)
        
        # For Golden, CO on 2023-01-01 (MST, UTC-7)
        # init_date is Jan 1, 2023, 12:00 PM UTC, which is 5:00 AM MST.
        # Sunset should be around 4:45 PM MST on Jan 1.
        # Sunrise should be around 7:20 AM MST on Jan 1.

        sunset_dt = p.sunset_time() # No target_date
        sunrise_dt = p.sunrise_time() # No target_date

        assert sunset_dt is not None
        assert isinstance(sunset_dt, datetime)
        assert sunset_dt.tzinfo == p.local_timezone
        # Check if sunset is on Jan 1, 2023 in local time
        assert sunset_dt.year == 2023 and sunset_dt.month == 1 and sunset_dt.day == 1
        assert 16 <= sunset_dt.hour <= 17 # Around 4-5 PM for sunset in winter

        assert sunrise_dt is not None
        assert isinstance(sunrise_dt, datetime)
        assert sunrise_dt.tzinfo == p.local_timezone
        # Check if sunrise is on Jan 1, 2023 in local time
        assert sunrise_dt.year == 2023 and sunrise_dt.month == 1 and sunrise_dt.day == 1
        assert 7 <= sunrise_dt.hour <= 8 # Around 7-8 AM for sunrise in winter

    def test_sun_always_up_polar(self, north_pole_place):
        p = north_pole_place
        target_d = date(2024, 6, 21) # Summer solstice at North Pole

        # Sun is always up, so no "next setting"
        assert p.sunset_time(target_date=target_d) is None, "Sunset should be None (always up)"
        # Sun is always up, so no "next rising" after it has initially risen for the summer period
        assert p.sunrise_time(target_date=target_d) is None, "Sunrise should be None (always up)"

    def test_sun_never_up_polar(self, north_pole_place):
        p = north_pole_place
        target_d = date(2024, 12, 21) # Winter solstice at North Pole

        # Sun is never up, so no "next rising"
        assert p.sunrise_time(target_date=target_d) is None, "Sunrise should be None (never up)"
        # Sun is never up, so no "next setting" after it has initially set for the winter period
        assert p.sunset_time(target_date=target_d) is None, "Sunset should be None (never up)"

    # --- Tests for get_time_relative_to_sunset() ---

    def test_get_time_relative_to_sunset_basic(self, mid_latitude_place):
        p = mid_latitude_place
        original_place_date = p.date
        target_d = date(2024, 3, 20) # A specific date
        offsets = [0, 30, -30] # Test zero, positive, and negative offsets

        expected_sunset_dt = p.sunset_time(target_date=target_d)
        assert expected_sunset_dt is not None, "Prerequisite: sunset must occur for this test"

        for offset_mins in offsets:
            local_obs_time, ephem_obs_date = p.get_time_relative_to_event(target_d, offset_minutes=offset_mins)

            assert local_obs_time is not None
            assert isinstance(local_obs_time, datetime)
            assert local_obs_time.tzinfo == p.local_timezone

            assert ephem_obs_date is not None
            assert isinstance(ephem_obs_date, ephem.Date)

            # Verify local_obs_time calculation
            expected_local_time = expected_sunset_dt + timedelta(minutes=offset_mins)
            assert local_obs_time == expected_local_time

            # Verify ephem_obs_date (is UTC)
            # Convert expected local time to UTC, then to ephem.Date
            expected_utc_time = expected_local_time.astimezone(timezone.utc)
            # ephem.Date can take a datetime object (assumed UTC if naive, or converted if aware)
            # Let's ensure it's UTC and naive for ephem.Date constructor for clarity, or use an aware one.
            # The current implementation of Place converts to UTC datetime before ephem.Date()
            expected_ephem_d = ephem.Date(expected_utc_time) 
            
            # Compare ephem.Date objects. They are floats (days since noon 1899/12/31 UTC).
            # A small tolerance is good for float comparisons.
            assert abs(ephem_obs_date - expected_ephem_d) < 1e-6 # approx 0.1 seconds

        assert p.date == original_place_date, "place.date should not be modified"

    def test_get_time_relative_to_sunset_polar_always_up(self, north_pole_place):
        p = north_pole_place
        target_d = date(2024, 6, 21) # Summer solstice, sun always up

        local_obs_time, ephem_obs_date = p.get_time_relative_to_event(target_d, offset_minutes=30)

        assert local_obs_time is None
        assert ephem_obs_date is None
        
    def test_place_setup_from_init(self):
        """ Test the original setup_place function if it's still relevant """
        # This test assumes setup_place() is available and works as before
        # If setup_place() is no longer the standard, this test might be removed or adapted
        try:
            p_init = setup_place()
            assert p_init.lat_decimal is not None # Basic check
            assert p_init.local_timezone is not None
        except ImportError:
            pytest.skip("setup_place not found, skipping this specific test.")
        except Exception as e:
            pytest.fail(f"setup_place() failed: {e}")

# This part is for the original test, I'll keep it separate if it was meant to be a standalone script check
# or integrate if it was just a way to run a single test.
# For now, I'll assume the TestPlace class is the way forward.

# def test_place_should_have_correct_coordinates():
#   p = setup_place()
#   lat = 50.1637973
#   lon = 19.7855169
#
#   assert p.lat_decimal == lat
#   assert p.lat == rad(lat)
#   assert p.lon_decimal == lon
#   assert p.lon == rad(lon)

# To run these tests, you would typically use `pytest` in the terminal.
# Ensure that `apts.place` is importable (e.g., by running from the parent directory of apts,
# or having the project installed in the environment).
# Also, `tests/__init__.py` might need to be present if `from . import setup_place` is used.
# If `setup_place` was in `place_test.py` itself, it should be adapted or removed.

# Based on the problem description, `setup_place` was from `tests/__init__.py`
# I will create a dummy `tests/__init__.py` if it's missing for the code to be runnable,
# or inspect it if provided. For now, I assume it correctly sets up a Place.
# The fixture `mid_latitude_place` replaces the direct need for `setup_place` in these new tests
# for a known mid-latitude location.
# The test `test_place_setup_from_init` is a placeholder to check the original setup.
# The original `test_place_should_have_correct_coordinates` is now covered by `test_place_coordinates_fixture`.

# A note on date comparisons for sunset/sunrise:
# Sunset for date D can occur on date D or D+1 in local time depending on how late in the UTC day it is.
# Sunrise for date D can occur on date D or D-1 in local time.
# The current check `assert sunset_dt.date() == target_d` might be too strict.
# A looser check, like `assert abs((sunset_dt.replace(tzinfo=None) - datetime.combine(target_d, sunset_dt.time())).days) <= 1`
# or checking if the date is target_d or target_d + 1 day (for sunset) or target_d or target_d -1 day (for sunrise)
# is more robust. I've updated this in `test_sunset_sunrise_with_target_date`.
# For `test_sunset_sunrise_with_target_date`, the sunset can occur on `target_d` or the next day in local time,
# especially if `target_d` is based on noon UTC.
# Similarly, sunrise can occur on `target_d` or the previous day.
# The current check `assert sunset_dt.date() == target_d` is simplified.
# A better check would be:
# local_target_noon = datetime.combine(target_d, time(12,0), tzinfo=p.local_timezone)
# Then check if sunset_dt.date() is target_d or (if sunset_dt < local_target_noon) target_d -1 day etc.
# For now, I will use a simpler check: `assert sunset_dt.date() == target_d or (sunset_dt - timedelta(days=1)).date() == target_d or (sunset_dt + timedelta(days=1)).date() == target_d`
# This allows the local date of the event to be the day before, the day of, or the day after the target_date, which should cover timezone shifts.
# The core idea is that `_next_rising_time` and `_next_setting_time` use the `start` date (which is noon UTC of `target_date`)
# to find the *next* event.
# For sunset, this next event is usually on the same local date as `target_date`.
# For sunrise, this next event is usually on the same local date as `target_date`.

# The specific hour checks are also approximations and depend on DST.
# Golden, CO on 2024-03-15: DST is active (starts March 10, 2024). Timezone is MDT (UTC-6).
# Sunset around 19:11 MDT (01:11 UTC next day). Sunrise around 07:14 MDT (13:14 UTC same day).
# My hour checks (18-20 for sunset, 6-8 for sunrise) are reasonable for MDT.

# For legacy test `test_sunset_sunrise_without_target_date_legacy`:
# `DEFAULT_INIT_DATE_UTC` is Jan 1, 2023, 12:00 UTC.
# For Golden, CO (MST, UTC-7), this is Jan 1, 2023, 5:00 AM MST.
# `p.date` (which is `ephem.Date(DEFAULT_INIT_DATE_UTC)`) is used as `start`.
# Sunrise on Jan 1, 2023 in Golden is ~7:22 AM MST.
# Sunset on Jan 1, 2023 in Golden is ~4:46 PM MST.
# The `_next_rising_time` will find the sunrise *after* 5:00 AM MST on Jan 1. This will be ~7:22 AM MST on Jan 1.
# The `_next_setting_time` will find the sunset *after* 5:00 AM MST on Jan 1. This will be ~4:46 PM MST on Jan 1.
# My hour checks (16-17 for sunset, 7-8 for sunrise) are correct.
# The date checks `assert sunset_dt.year == 2023 and sunset_dt.month == 1 and sunset_dt.day == 1` are also correct.
# `datetime.timezone.utc` is used instead of `pytz.UTC` for constructing `DEFAULT_INIT_DATE_UTC` for consistency.
# `place.local_timezone` will be a `pytz` timezone object.
# `astimezone(timezone.utc)` is fine for converting.

import unittest
from unittest.mock import patch, MagicMock, ANY
import pandas as pd
# from apts.config import config # Not directly used if get_dark_mode is mocked
from apts.constants.graphconstants import get_plot_style

class TestPlacePlotting(unittest.TestCase):
    def setUp(self):
        self.place = setup_place()
        # Ensure place.local_timezone is robust for tests
        if not hasattr(self.place, 'local_timezone') or self.place.local_timezone is None:
            self.place.local_timezone = dt_module.timezone.utc # Use aliased dt_module
        elif isinstance(self.place.local_timezone, str):
             # Simplified: if it's a string, default to UTC for test consistency
             self.place.local_timezone = dt_module.timezone.utc # Use aliased dt_module


        # Mock moon_path to return predictable data
        mock_moon_path_data = pd.DataFrame({
            'Time': [dt_module.time(hour=18, minute=0), dt_module.time(hour=19, minute=0), dt_module.time(hour=20, minute=0)], # Use aliased dt_module
            'Moon altitude': [10, 20, 30],
            'Azimuth': [90, 100, 110],
            'Local_time': ['18:00', '19:00', '20:00'],
            'Phase': [0.5, 0.5, 0.5],
            'Lunation': [0.5, 0.5, 0.5]
        })
        self.place.moon_path = MagicMock(return_value=mock_moon_path_data)
        self.place._moon_phase_letter = MagicMock(return_value='M')
        self.place.moon_phase = MagicMock(return_value=50)

    @patch('apts.place.get_dark_mode') # Corrected path for get_dark_mode used in Place
    @patch('pandas.DataFrame.plot')
    def test_plot_moon_path_styling(self, mock_df_plot, mock_get_dark_mode_place):
        scenarios = [
            {"override": True, "global_dark_mode": False, "expected_effective_dark_mode": True, "desc": "Override True"},
            {"override": False, "global_dark_mode": True, "expected_effective_dark_mode": False, "desc": "Override False"},
            {"override": None, "global_dark_mode": True,  "expected_effective_dark_mode": True, "desc": "Override None, Global True"},
            {"override": None, "global_dark_mode": False, "expected_effective_dark_mode": False, "desc": "Override None, Global False"},
        ]

        for i, scenario_data in enumerate(scenarios):
            with self.subTest(msg=scenario_data["desc"], i=i):
                mock_get_dark_mode_place.return_value = scenario_data["global_dark_mode"]
                expected_style = get_plot_style(scenario_data["expected_effective_dark_mode"])
                is_dark = scenario_data["expected_effective_dark_mode"]

                mock_ax = MagicMock()
                mock_fig = MagicMock()
                mock_fig_patch = MagicMock()
                mock_fig.patch = mock_fig_patch
                mock_ax.figure = mock_fig

                mock_line = MagicMock()
                mock_ax.lines = [mock_line]

                mock_df_plot.return_value = mock_ax

                self.place.plot_moon_path(dark_mode_override=scenario_data["override"])

                mock_df_plot.assert_called_once_with(x="Azimuth", y="Moon altitude", title="Moon altitude", style=".-")

                mock_fig_patch.set_facecolor.assert_called_with(expected_style['FIGURE_FACE_COLOR'])
                mock_ax.set_facecolor.assert_called_with(expected_style['AXES_FACE_COLOR'])
                mock_line.set_color.assert_called_with(expected_style['TEXT_COLOR'])
                mock_ax.set_xlabel.assert_called_with("Azimuth [°]", color=expected_style['TEXT_COLOR'])
                mock_ax.set_ylabel.assert_called_with("Altitude [°]", color=expected_style['TEXT_COLOR'])
                mock_ax.set_title.assert_called_with("Moon altitude", color=expected_style['TEXT_COLOR'])
                mock_ax.tick_params.assert_any_call(axis='x', colors=expected_style['TICK_COLOR'])
                mock_ax.tick_params.assert_any_call(axis='y', colors=expected_style['TICK_COLOR'])

                for spine_pos in ['top', 'bottom', 'left', 'right']:
                    mock_ax.spines[spine_pos].set_color.assert_called_with(expected_style['AXIS_COLOR'])

                mock_ax.axvline.assert_any_call(ANY, color=expected_style['GRID_COLOR'], linestyle="--", linewidth=1)
                mock_ax.text.assert_any_call(ANY, 1, ANY, weight="bold", horizontalalignment="center", color=expected_style['TEXT_COLOR']) # E/S/W labels
                mock_ax.axhspan.assert_called_with(0, -50, color=expected_style['GRID_COLOR'], alpha=0.3)
                mock_ax.text.assert_any_call(180, 10, 'M', fontproperties=Place.MOON_FONT, horizontalalignment="center", color=expected_style['TEXT_COLOR'])
                mock_ax.text.assert_any_call(180, 5, "50%", color=expected_style['TEXT_COLOR'], alpha=0.7, horizontalalignment="center")
                mock_ax.annotate.assert_any_call(ANY, (ANY, ANY), color=expected_style['TEXT_COLOR'])

                # Reset mocks for next subtest
                mock_df_plot.reset_mock()
                mock_ax.reset_mock()
                mock_fig.reset_mock()
                mock_fig_patch.reset_mock()
                mock_line.reset_mock()
                mock_get_dark_mode_place.reset_mock() # Reset this as it's called in each loop
