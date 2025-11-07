import pytest
from math import radians as rad
from datetime import date, datetime, timedelta, timezone
import datetime as dt_module  # Added alias
import unittest
from unittest.mock import patch, MagicMock, ANY
import pandas as pd

# from apts.config import config # Not directly used if get_dark_mode is mocked
from apts.constants.graphconstants import get_plot_style
from apts.constants.twilight import Twilight


from apts.place import Place

# Assuming setup_place is a helper to create a Place instance for testing
# If it's defined in tests/__init__.py, this import should work.
# Otherwise, we might need to define a fixture or helper here.
from . import setup_place

# Define some known locations and timezones for testing
GOLDEN_COORDS = {"lat": 39.7555, "lon": -105.2211, "tz_name": "America/Denver"}
NORTH_POLE_COORDS = {
    "lat": 90.0,
    "lon": 0.0,
    "tz_name": "UTC",
}  # UTC for simplicity at poles

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
            date=DEFAULT_INIT_DATE_UTC,
        )

    @pytest.fixture
    def north_pole_place(self):
        """A place at the North Pole for testing polar phenomena."""
        # local_timezone is determined by Place based on lat/lon (though for poles, it might default or be less defined)
        # Place constructor expects 'date' argument for the initial date
        return Place(
            lat=NORTH_POLE_COORDS["lat"],
            lon=NORTH_POLE_COORDS["lon"],
            date=DEFAULT_INIT_DATE_UTC,  # date argument for Place constructor
        )

    def test_place_coordinates_fixture(self, mid_latitude_place):
        """Test that the fixture place has correct coordinates."""
        p = mid_latitude_place
        assert p.lat_decimal == GOLDEN_COORDS["lat"]
        assert p.lat == rad(GOLDEN_COORDS["lat"])
        assert p.lon_decimal == GOLDEN_COORDS["lon"]
        assert p.lon == rad(GOLDEN_COORDS["lon"])
        # Verify that TimezoneFinder (Place.TF) returns the correct timezone name for the fixture's coordinates
        assert (
            Place.TF.timezone_at(lat=p.lat_decimal, lng=p.lon_decimal)
            == GOLDEN_COORDS["tz_name"]
        ), (
            "TimezoneFinder query for fixture coordinates did not return the expected timezone name"
        )

    def test_place_internal_timezone_assignment(self):
        """Test that Place correctly assigns local_timezone based on coordinates."""
        # Instantiate Place without a specific date, let it default.
        # Focus is on timezone assignment from lat/lon.
        place_instance = Place(lat=GOLDEN_COORDS["lat"], lon=GOLDEN_COORDS["lon"])

        assert place_instance.local_timezone is not None, (
            "local_timezone should be set by Place constructor"
        )

        expected_tz_name = GOLDEN_COORDS["tz_name"]

        # Verify that TimezoneFinder (Place.TF) returns the correct timezone name
        # for the place_instance's coordinates.
        assert (
            Place.TF.timezone_at(
                lat=place_instance.lat_decimal, lng=place_instance.lon_decimal
            )
            == expected_tz_name
        ), (
            f"TimezoneFinder query for place_instance coordinates did not return {expected_tz_name}"
        )

    # --- Tests for sunset_time() and sunrise_time() ---

    def test_sunset_sunrise_with_target_date(self, mid_latitude_place):
        p = mid_latitude_place
        original_place_date = p.date  # Date
        target_d = date(2024, 3, 15)  # Use a specific date

        sunset_dt = p.sunset_time(target_date=target_d)
        sunrise_dt = p.sunrise_time(target_date=target_d)

        # Assertions for sunset
        assert sunset_dt is not None, "Sunset should occur"
        assert isinstance(sunset_dt, datetime), "Sunset time should be datetime object"
        assert sunset_dt.tzinfo is not None, "Sunset datetime should be timezone-aware"
        assert sunset_dt.tzinfo == p.local_timezone, "Sunset timezone should be local"
        assert (
            sunset_dt.date() == target_d
            or (sunset_dt - timedelta(days=1)).date() == target_d
            or (sunset_dt + timedelta(days=1)).date() == target_d
        )  # Sunset can be on target_d or next/prev day in local time

        # Example: For Golden, CO (UTC-7 or -6 depending on DST) on 2024-03-15 (DST active, UTC-6)
        # Sunset is around 7:11 PM MDT. Sunrise around 7:14 AM MDT.
        # These are rough checks, actual calculation is the source of truth.
        assert 18 <= sunset_dt.hour <= 20, (
            f"Sunset hour {sunset_dt.hour} out of expected range (18-20)"
        )

        # Assertions for sunrise
        assert sunrise_dt is not None, "Sunrise should occur"
        assert isinstance(sunrise_dt, datetime), (
            "Sunrise time should be datetime object"
        )
        assert sunrise_dt.tzinfo is not None, (
            "Sunrise datetime should be timezone-aware"
        )
        assert sunrise_dt.tzinfo == p.local_timezone, "Sunrise timezone should be local"
        assert (
            sunrise_dt.date() == target_d
            or (sunrise_dt - timedelta(days=1)).date() == target_d
        )  # Sunrise is usually on the same local day
        assert 6 <= sunrise_dt.hour <= 8, (
            f"Sunrise hour {sunrise_dt.hour} out of expected range (6-8)"
        )

        assert p.date == original_place_date, "place.date should not be modified"

    def test_sunset_sunrise_without_target_date_legacy(self, mid_latitude_place):
        p = mid_latitude_place  # Uses DEFAULT_INIT_DATE_UTC (2023-01-01 12:00 UTC)

        # For Golden, CO on 2023-01-01 (MST, UTC-7)
        # init_date is Jan 1, 2023, 12:00 PM UTC, which is 5:00 AM MST.
        # Sunset should be around 4:45 PM MST on Jan 1.
        # Sunrise should be around 7:20 AM MST on Jan 1.

        sunset_dt = p.sunset_time()  # No target_date
        sunrise_dt = p.sunrise_time()  # No target_date

        assert sunset_dt is not None
        assert isinstance(sunset_dt, datetime)
        assert sunset_dt.tzinfo == p.local_timezone
        # Check if sunset is on Jan 1, 2023 in local time
        assert sunset_dt.year == 2023 and sunset_dt.month == 1 and sunset_dt.day == 1
        assert 16 <= sunset_dt.hour <= 17  # Around 4-5 PM for sunset in winter

        assert sunrise_dt is not None
        assert isinstance(sunrise_dt, datetime)
        assert sunrise_dt.tzinfo == p.local_timezone
        # Check if sunrise is on Jan 1, 2023 in local time
        assert sunrise_dt.year == 2023 and sunrise_dt.month == 1 and sunrise_dt.day == 1
        assert 7 <= sunrise_dt.hour <= 8  # Around 7-8 AM for sunrise in winter

    def test_sun_always_up_polar(self, north_pole_place):
        p = north_pole_place
        target_d = date(2024, 6, 21)  # Summer solstice at North Pole

        # Sun is always up, so no "next setting"
        assert p.sunset_time(target_date=target_d) is None, (
            "Sunset should be None (always up)"
        )
        # Sun is always up, so no "next rising" after it has initially risen for the summer period
        assert p.sunrise_time(target_date=target_d) is None, (
            "Sunrise should be None (always up)"
        )

    def test_sun_never_up_polar(self, north_pole_place):
        p = north_pole_place
        target_d = date(2024, 12, 21)  # Winter solstice at North Pole

        # Sun is never up, so no "next rising"
        assert p.sunrise_time(target_date=target_d) is None, (
            "Sunrise should be None (never up)"
        )
        # Sun is never up, so no "next setting" after it has initially set for the winter period
        assert p.sunset_time(target_date=target_d) is None, (
            "Sunset should be None (never up)"
        )

    def test_twilight_times_order(self, mid_latitude_place):
        p = mid_latitude_place
        target_d = date(2024, 3, 15)

        # Evening times
        sunset = p.sunset_time(target_date=target_d)
        civil_dusk = p.sunset_time(target_date=target_d, twilight=Twilight.CIVIL)
        nautical_dusk = p.sunset_time(target_date=target_d, twilight=Twilight.NAUTICAL)
        astronomical_dusk = p.sunset_time(
            target_date=target_d, twilight=Twilight.ASTRONOMICAL
        )

        # Morning times
        sunrise = p.sunrise_time(target_date=target_d)
        civil_dawn = p.sunrise_time(target_date=target_d, twilight=Twilight.CIVIL)
        nautical_dawn = p.sunrise_time(
            target_date=target_d, twilight=Twilight.NAUTICAL
        )
        astronomical_dawn = p.sunrise_time(
            target_date=target_d, twilight=Twilight.ASTRONOMICAL
        )

        # Assertions for evening
        assert all([sunset, civil_dusk, nautical_dusk, astronomical_dusk])
        assert sunset < civil_dusk < nautical_dusk < astronomical_dusk

        # Assertions for morning
        assert all([astronomical_dawn, nautical_dawn, civil_dawn, sunrise])
        assert astronomical_dawn < nautical_dawn < civil_dawn < sunrise

    def test_twilight_polar_summer(self, north_pole_place):
        p = north_pole_place
        target_d = date(2024, 6, 21)  # Summer solstice

        # At the North Pole in summer, the sun is always up, so there should be no twilight.
        assert p.sunset_time(target_date=target_d, twilight=Twilight.ASTRONOMICAL) is None
        assert p.sunrise_time(target_date=target_d, twilight=Twilight.ASTRONOMICAL) is None

    def test_twilight_polar_winter(self, north_pole_place):
        p = north_pole_place
        target_d = date(2024, 12, 21)  # Winter solstice

        # At the North Pole in winter, the sun is always down, so there should be no twilight.
        assert p.sunset_time(target_date=target_d, twilight=Twilight.ASTRONOMICAL) is None
        assert p.sunrise_time(target_date=target_d, twilight=Twilight.ASTRONOMICAL) is None

    def test_place_setup_from_init(self):
        """Test the original setup_place function if it's still relevant"""
        # This test assumes setup_place() is available and works as before
        # If setup_place() is no longer the standard, this test might be removed or adapted
        try:
            p_init = setup_place()
            assert p_init.lat_decimal is not None  # Basic check
            assert p_init.local_timezone is not None
        except ImportError:
            pytest.skip("setup_place not found, skipping this specific test.")
        except Exception as e:
            pytest.fail(f"setup_place() failed: {e}")

    def test_sun_and_moon_path_data(self, mid_latitude_place):
        """Test that sun_path and moon_path return valid DataFrames."""
        p = mid_latitude_place

        sun_df = p.sun_path()
        assert isinstance(sun_df, pd.DataFrame)
        assert not sun_df.empty
        assert "Sun altitude" in sun_df.columns
        assert "Azimuth" in sun_df.columns
        assert "Local_time" in sun_df.columns

        moon_df = p.moon_path()
        assert isinstance(moon_df, pd.DataFrame)
        assert not moon_df.empty
        assert "Moon altitude" in moon_df.columns
        assert "Azimuth" in moon_df.columns
        assert "Local_time" in moon_df.columns


class TestPlacePlotting(unittest.TestCase):
    def setUp(self):
        self.place = setup_place()
        # Ensure place.local_timezone is robust for tests
        if (
            not hasattr(self.place, "local_timezone")
            or self.place.local_timezone is None
        ):
            self.place.local_timezone = dt_module.timezone.utc  # Use aliased dt_module
        elif isinstance(self.place.local_timezone, str):
            # Simplified: if it's a string, default to UTC for test consistency
            self.place.local_timezone = dt_module.timezone.utc  # Use aliased dt_module

        # Mock moon_path to return predictable data
        mock_moon_path_data = pd.DataFrame(
            {
                "Time": [
                    dt_module.time(hour=18, minute=0),
                    dt_module.time(hour=19, minute=0),
                    dt_module.time(hour=20, minute=0),
                ],  # Use aliased dt_module
                "Moon altitude": [10, 20, 30],
                "Azimuth": [90, 100, 110],
                "Local_time": ["18:00", "19:00", "20:00"],
                "Phase": [0.5, 0.5, 0.5],
                "Lunation": [0.5, 0.5, 0.5],
            }
        )
        self.place.moon_path = MagicMock(return_value=mock_moon_path_data)
        self.place._moon_phase_letter = MagicMock(return_value="M")
        self.place.moon_phase = MagicMock(return_value=50)

    @patch("apts.place.get_dark_mode")  # Corrected path for get_dark_mode used in Place
    @patch("pandas.DataFrame.plot")
    def test_plot_moon_path_styling(self, mock_df_plot, mock_get_dark_mode_place):
        scenarios = [
            {
                "override": True,
                "global_dark_mode": False,
                "expected_effective_dark_mode": True,
                "desc": "Override True",
            },
            {
                "override": False,
                "global_dark_mode": True,
                "expected_effective_dark_mode": False,
                "desc": "Override False",
            },
            {
                "override": None,
                "global_dark_mode": True,
                "expected_effective_dark_mode": True,
                "desc": "Override None, Global True",
            },
            {
                "override": None,
                "global_dark_mode": False,
                "expected_effective_dark_mode": False,
                "desc": "Override None, Global False",
            },
        ]

        for i, scenario_data in enumerate(scenarios):
            with self.subTest(msg=scenario_data["desc"], i=i):
                mock_get_dark_mode_place.return_value = scenario_data[
                    "global_dark_mode"
                ]
                expected_style = get_plot_style(
                    scenario_data["expected_effective_dark_mode"]
                )
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

                mock_df_plot.assert_called_once_with(
                    x="Azimuth", y="Moon altitude", title="Moon altitude", style=".-"
                )

                mock_fig_patch.set_facecolor.assert_called_with(
                    expected_style["FIGURE_FACE_COLOR"]
                )
                mock_ax.set_facecolor.assert_called_with(
                    expected_style["AXES_FACE_COLOR"]
                )
                mock_line.set_color.assert_called_with(expected_style["TEXT_COLOR"])
                mock_ax.set_xlabel.assert_called_with(
                    "Azimuth [°]", color=expected_style["TEXT_COLOR"]
                )
                mock_ax.set_ylabel.assert_called_with(
                    "Altitude [°]", color=expected_style["TEXT_COLOR"]
                )
                mock_ax.set_title.assert_called_with(
                    "Moon altitude", color=expected_style["TEXT_COLOR"]
                )
                mock_ax.tick_params.assert_any_call(
                    axis="x", colors=expected_style["TICK_COLOR"]
                )
                mock_ax.tick_params.assert_any_call(
                    axis="y", colors=expected_style["TICK_COLOR"]
                )

                for spine_pos in ["top", "bottom", "left", "right"]:
                    mock_ax.spines[spine_pos].set_color.assert_called_with(
                        expected_style["AXIS_COLOR"]
                    )

                mock_ax.axvline.assert_any_call(
                    ANY, color=expected_style["GRID_COLOR"], linestyle="--", linewidth=1
                )
                mock_ax.text.assert_any_call(
                    ANY,
                    1,
                    ANY,
                    weight="bold",
                    horizontalalignment="center",
                    color=expected_style["TEXT_COLOR"],
                )  # E/S/W labels
                mock_ax.axhspan.assert_called_with(
                    0, -50, color=expected_style["GRID_COLOR"], alpha=0.3
                )
                if is_dark:
                    mock_ax.plot.assert_any_call(
                        180,
                        10,
                        marker="o",
                        markersize=45,
                        color=expected_style["TEXT_COLOR"],
                        linestyle="None",
                    )
                    mock_ax.text.assert_any_call(
                        180,
                        10,
                        "M",
                        fontproperties=Place.MOON_FONT,
                        horizontalalignment="center",
                        verticalalignment="center",
                        color=expected_style["AXES_FACE_COLOR"],
                    )
                else:
                    mock_ax.text.assert_any_call(
                        180,
                        10,
                        "M",
                        fontproperties=Place.MOON_FONT,
                        horizontalalignment="center",
                        verticalalignment="center",
                        color=expected_style["TEXT_COLOR"],
                    )
                mock_ax.text.assert_any_call(
                    180,
                    -3,
                    "50%",
                    color=expected_style["TEXT_COLOR"],
                    alpha=0.7,
                    horizontalalignment="center",
                )
                mock_ax.annotate.assert_any_call(
                    ANY, (ANY, ANY), color=expected_style["TEXT_COLOR"]
                )

                # Reset mocks for next subtest
                mock_df_plot.reset_mock()
                mock_ax.reset_mock()
                mock_fig.reset_mock()
                mock_fig_patch.reset_mock()
                mock_line.reset_mock()
                mock_get_dark_mode_place.reset_mock()  # Reset this as it's called in each loop
