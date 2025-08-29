import os
import unittest
import tempfile
import datetime  # Added
from datetime import timedelta
from unittest.mock import patch, mock_open
import pandas as pd
from unittest.mock import MagicMock, call  # Added MagicMock and call
from apts.observations import Observation
from apts.constants.graphconstants import (
    get_plot_style,
    OpticalType,
    GraphConstants,
)  # Added GraphConstants
from apts.constants.objecttablelabels import (
    ObjectTableLabels,
)  # Added ObjectTableLabels
from apts.units import ureg
from tests import setup_observation
from apts.conditions import Conditions  # Import Conditions at the top level
from skyfield.api import Star

# MockPlace and MockEquipment classes are removed


class TestObservationTemplate(unittest.TestCase):
    def setUp(self):
        self.observation = setup_observation()

        # Ensure place.local_timezone is tz-aware for pd.Timestamp construction
        if (
            not hasattr(self.observation.place, "local_timezone")
            or self.observation.place.local_timezone is None
        ):
            obs_local_tz = datetime.timezone.utc
        elif isinstance(self.observation.place.local_timezone, str):
            obs_local_tz = (
                datetime.timezone.utc
                if self.observation.place.local_timezone.upper() == "UTC"
                else self.observation.place.local_timezone
            )
        else:
            obs_local_tz = self.observation.place.local_timezone

        if self.observation.start is None:
            self.observation.start = pd.Timestamp(
                "2025/02/18 18:00:00", tz=obs_local_tz
            )

        if self.observation.stop is None:
            if pd.api.types.is_datetime64_any_dtype(self.observation.start):
                self.observation.stop = self.observation.start + pd.Timedelta(hours=8)
            else:
                self.observation.stop = pd.Timestamp(
                    "2025/02/19 02:00:00", tz=obs_local_tz
                )

        if self.observation.time_limit is None:
            if pd.api.types.is_datetime64_any_dtype(self.observation.start):
                max_return_values = [
                    int(value)
                    for value in self.observation.conditions.max_return.split(":")
                ]
                time_limit_dt = self.observation.start.replace(
                    hour=max_return_values[0],
                    minute=max_return_values[1],
                    second=max_return_values[2],
                )
                self.observation.time_limit = (
                    time_limit_dt
                    if time_limit_dt > self.observation.start
                    else time_limit_dt + pd.Timedelta(days=1)
                )
            else:
                self.observation.time_limit = pd.Timestamp(
                    "2025/02/19 02:00:00", tz=obs_local_tz
                )

        self.default_template_content = """<!doctype html>
<html>
  <head>
    <style>
      body { color: #555; }
    </style>
  </head>
  <body>
    <h1>$title</h1>
    <p>$place_name</p>
  </body>
</html>"""

    @patch("apts.weather.Weather.__init__")
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="<!doctype html><html><head><style>body{color:#555;}</style></head><body><h1>$title</h1><p>$place_name</p></body></html>",
    )
    def test_to_html_default_template(self, mock_file, mock_weather_init):
        """Test that to_html uses the default template when no custom template is provided"""
        mock_weather_init.return_value = None
        self.observation.place.weather = MagicMock()
        self.observation.place.weather.get_critical_data.return_value = pd.DataFrame({
                "time": pd.to_datetime([]).tz_localize('UTC'),
                "cloudCover": [],
                "precipProbability": [],
                "windSpeed": [],
                "temperature": [],
            }
        )
        html = self.observation.to_html()

        # Verify that open was called with the default template path
        mock_file.assert_called_once()
        self.assertEqual(mock_file.call_args[0][0], Observation.NOTIFICATION_TEMPLATE)

        # Verify that the template contains the substituted values
        self.assertIn(self.observation.place.name, html)
        self.assertIn("APTS", html)

    @patch("apts.weather.Weather.__init__")
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="<!doctype html><html><head><style>body{color:#555;}</style></head><body><h1>$title</h1><p>$place_name</p></body></html>",
    )
    def test_to_html_custom_template(self, mock_file, mock_weather_init):
        """Test that to_html uses a custom template when provided"""
        mock_weather_init.return_value = None
        self.observation.place.weather = MagicMock()
        self.observation.place.weather.get_critical_data.return_value = pd.DataFrame({
                "time": pd.to_datetime([]).tz_localize('UTC'),
                "cloudCover": [],
                "precipProbability": [],
                "windSpeed": [],
                "temperature": [],
            }
        )
        custom_template = "/path/to/custom/template.html"
        html = self.observation.to_html(custom_template=custom_template)

        # Verify that open was called with the custom template path
        mock_file.assert_called_once_with(custom_template)

        # Verify that the template contains the substituted values
        self.assertIn(self.observation.place.name, html)
        self.assertIn("APTS", html)

    @patch("apts.weather.Weather.__init__")
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="<!doctype html><html><head><style>body{color:#555;}</style></head><body><h1>$title</h1><p>$place_name</p></body></html>",
    )
    def test_to_html_custom_css(self, mock_file, mock_weather_init):
        """Test that to_html injects custom CSS when provided"""
        mock_weather_init.return_value = None
        self.observation.place.weather = MagicMock()
        self.observation.place.weather.get_critical_data.return_value = pd.DataFrame({
                "time": pd.to_datetime([]).tz_localize('UTC'),
                "cloudCover": [],
                "precipProbability": [],
                "windSpeed": [],
                "temperature": [],
            }
        )
        custom_css = "h1 { color: blue; }"
        html = self.observation.to_html(css=custom_css)

        # Verify that the CSS was properly injected
        self.assertIn(custom_css, html)
        self.assertIn("body{color:#555;}", html)

    @patch("apts.weather.Weather.__init__")
    def test_to_html_with_actual_template_file(self, mock_weather_init):
        """Test to_html with an actual temporary template file"""
        mock_weather_init.return_value = None
        self.observation.place.weather = MagicMock()
        self.observation.place.weather.get_critical_data.return_value = pd.DataFrame({
                "time": pd.to_datetime([]).tz_localize('UTC'),
                "cloudCover": [],
                "precipProbability": [],
                "windSpeed": [],
                "temperature": [],
            }
        )
        # Create a temporary template file
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_file:
            temp_file.write(self.default_template_content)
            temp_path = temp_file.name

        try:
            # Test with the actual file
            custom_css = "h1 { color: blue; }"
            html = self.observation.to_html(custom_template=temp_path, css=custom_css)

            # Verify that the template worked and CSS was injected
            self.assertIn(self.observation.place.name, html)
            self.assertIn("APTS", html)
            self.assertIn(custom_css, html)

        finally:
            # Clean up
            os.unlink(temp_path)


class TestObservationPlottingStyles(unittest.TestCase):
    def setUp(self):
        self.observation = setup_observation()
        # If specific conditions are needed for these tests, set them here:
        self.observation.conditions.min_object_altitude = 10 * ureg.deg

        # Ensure place.local_timezone is tz-aware
        if (
            not hasattr(self.observation.place, "local_timezone")
            or self.observation.place.local_timezone is None
        ):
            obs_local_tz = datetime.timezone.utc
        elif isinstance(self.observation.place.local_timezone, str):
            obs_local_tz = (
                datetime.timezone.utc
                if self.observation.place.local_timezone.upper() == "UTC"
                else self.observation.place.local_timezone
            )
        else:
            obs_local_tz = self.observation.place.local_timezone

        if self.observation.start is None:
            self.observation.start = pd.Timestamp(
                "2025/02/18 18:00:00", tz=obs_local_tz
            )

        if self.observation.stop is None:
            if pd.api.types.is_datetime64_any_dtype(self.observation.start):
                self.observation.stop = self.observation.start + pd.Timedelta(hours=8)
            else:
                self.observation.stop = pd.Timestamp(
                    "2025/02/19 02:00:00", tz=obs_local_tz
                )

        if self.observation.time_limit is None:
            if pd.api.types.is_datetime64_any_dtype(self.observation.start):
                max_return_values = [
                    int(value)
                    for value in self.observation.conditions.max_return.split(":")
                ]
                time_limit_dt = self.observation.start.replace(
                    hour=max_return_values[0],
                    minute=max_return_values[1],
                    second=max_return_values[2],
                )
                self.observation.time_limit = (
                    time_limit_dt
                    if time_limit_dt > self.observation.start
                    else time_limit_dt + pd.Timedelta(days=1)
                )
            else:
                self.observation.time_limit = pd.Timestamp(
                    "2025/02/19 02:00:00", tz=obs_local_tz
                )

        # Mock the get_visible_messier to return a non-empty DataFrame
        # to avoid early exit from _generate_plot_messier
        mock_messier_data = {
            "Messier": ["M1"],
            "Type": ["Nebula"],
            "RA": ["05h 34m 31.94s"],
            "Dec": ["+22° 00′ 52.2″"],
            "Magnitude": [8.4 * ureg.mag],
            "Constellation": ["Tau"],
            "Size": [ureg.arcmin * 6],  # Using Quantity for size
            "Distance": [6.523 * 1000 * ureg.light_year],
            "Altitude": [45 * ureg.deg],  # Using Quantity
            "Azimuth": [180 * ureg.deg],  # Using Quantity
            "Transit": [pd.Timestamp("2023-01-01 22:00:00", tz="UTC")],
            "Width": [6.0 * ureg.arcmin],  # Using Quantity
            "Height": [4.0 * ureg.arcmin],  # Using Quantity
        }
        self.mock_messier_df = pd.DataFrame(mock_messier_data)
        # Ensure DataFrame columns with pint Quantities are correctly typed if needed by the method
        # For _generate_plot_messier, it seems to handle .magnitude internally.

        # Mock data for planet color tests
        self.mock_planets_data_for_color_test = pd.DataFrame(
            {
                ObjectTableLabels.NAME: ["Mars", "Jupiter"],
                "TechnicalName": ["mars", "jupiter barycenter"],
                ObjectTableLabels.TRANSIT: [
                    pd.Timestamp("2023-01-01 22:00:00", tz="UTC")
                ]
                * 2,
                ObjectTableLabels.ALTITUDE: [45 * ureg.deg] * 2,
                ObjectTableLabels.SIZE: [10 * ureg.arcsec] * 2,
                ObjectTableLabels.PHASE: [90.0 * ureg.percent] * 2,
                ObjectTableLabels.RISING: [
                    pd.Timestamp("2023-01-01 18:00:00", tz="UTC")
                ]
                * 2,
                ObjectTableLabels.SETTING: [
                    pd.Timestamp("2023-01-02 02:00:00", tz="UTC")
                ]
                * 2,
            }
        )

    @patch("apts.observations.Utils.annotate_plot")
    @patch("apts.observations.pyplot")
    @patch("apts.observations.get_dark_mode")
    def test_generate_plot_messier_dark_mode_styles(
        self, mock_get_dark_mode, mock_pyplot, mock_annotate_plot
    ):
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

        # Mock get_visible_messier to control its output (already in setUp)
        self.observation.get_visible_messier = MagicMock(
            return_value=self.mock_messier_df
        )

        for i, scenario_data in enumerate(scenarios):
            with self.subTest(msg=scenario_data["desc"], i=i):
                mock_get_dark_mode.return_value = scenario_data["global_dark_mode"]
                expected_style = get_plot_style(
                    scenario_data["expected_effective_dark_mode"]
                )

                # Reset mocks that accumulate calls for each subtest
                mock_pyplot.reset_mock()
                mock_annotate_plot.reset_mock()

                # Mock the subplots call and the returned axes object for this subtest run
                mock_ax = MagicMock()
                mock_fig = MagicMock()
                mock_ax.figure = mock_fig
                mock_pyplot.subplots.return_value = (mock_fig, mock_ax)

                # Mock legend calls for this subtest run
                mock_legend = MagicMock()
                mock_ax.legend.return_value = mock_legend
                mock_legend.get_frame.return_value = MagicMock()
                mock_legend.get_title.return_value = MagicMock()
                mock_legend.get_texts.return_value = [
                    MagicMock()
                ]  # Assume at least one text item for simplicity

                returned_fig = self.observation._generate_plot_messier(
                    dark_mode_override=scenario_data["override"]
                )

                self.assertEqual(returned_fig, mock_fig)
                mock_pyplot.subplots.assert_called_once()
                if scenario_data["expected_effective_dark_mode"]:
                    mock_fig.patch.set_facecolor.assert_called_with("#1C1C3A")
                    mock_ax.set_facecolor.assert_called_with("#2A004F")
                    mock_ax.set_title.assert_any_call(
                        "Messier Objects Altitude", color="#FFFFFF"
                    )
                    if not self.mock_messier_df.empty:
                        mock_legend.get_frame().set_facecolor.assert_called_with(
                            "#2A004F"
                        )
                        mock_legend.get_frame().set_edgecolor.assert_called_with(
                            "#CCCCCC"
                        )
                        mock_legend.get_title().set_color.assert_called_with("#FFFFFF")
                        for text_mock in mock_legend.get_texts():
                            text_mock.set_color.assert_called_with("#FFFFFF")
                else:  # Light mode assertions remain using expected_style from get_plot_style(False)
                    mock_fig.patch.set_facecolor.assert_called_with(
                        expected_style["FIGURE_FACE_COLOR"]
                    )
                    mock_ax.set_facecolor.assert_called_with(
                        expected_style["AXES_FACE_COLOR"]
                    )
                    mock_ax.set_title.assert_any_call(
                        "Messier Objects Altitude", color=expected_style["TEXT_COLOR"]
                    )
                    if not self.mock_messier_df.empty:
                        mock_legend.get_frame().set_facecolor.assert_called_with(
                            expected_style["AXES_FACE_COLOR"]
                        )
                        mock_legend.get_frame().set_edgecolor.assert_called_with(
                            expected_style["AXIS_COLOR"]
                        )
                        mock_legend.get_title().set_color.assert_called_with(
                            expected_style["TEXT_COLOR"]
                        )
                        for text_mock in mock_legend.get_texts():
                            text_mock.set_color.assert_called_with(
                                expected_style["TEXT_COLOR"]
                            )

                mock_annotate_plot.assert_called_with(
                    mock_ax,
                    "Altitude [°]",
                    scenario_data["expected_effective_dark_mode"],
                )
                if not self.mock_messier_df.empty:
                    mock_ax.legend.assert_called_once()

    @patch("apts.observations.svg.Drawing")
    @patch("apts.observations.get_dark_mode")
    def test_plot_visible_planets_svg_dark_mode_styles(
        self, mock_get_dark_mode, mock_svg_drawing
    ):
        # Use the more detailed mock_planets_data_for_color_test
        self.observation.get_visible_planets = MagicMock(
            return_value=self.mock_planets_data_for_color_test
        )

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
                mock_get_dark_mode.return_value = scenario_data["global_dark_mode"]
                expected_style = get_plot_style(
                    scenario_data["expected_effective_dark_mode"]
                )

                # Reset svg.Drawing mock and prepare its return value for this subtest
                mock_svg_drawing.reset_mock()
                mock_dwg_instance = MagicMock()
                mock_svg_drawing.return_value = mock_dwg_instance

                self.observation.plot_visible_planets_svg(
                    dark_mode_override=scenario_data["override"]
                )

                fills_called = [
                    call.kwargs["fill"]
                    for call in mock_dwg_instance.circle.call_args_list
                ]
                self.assertEqual(mock_dwg_instance.circle.call_count, 2)

                if scenario_data["expected_effective_dark_mode"]:
                    mock_svg_drawing.assert_called_with(
                        style={"background-color": "#1C1C3A"}
                    )
                    self.assertIn(
                        GraphConstants.PLANET_COLORS_DARK["Mars"], fills_called
                    )
                    self.assertIn(
                        GraphConstants.PLANET_COLORS_DARK["Jupiter"],
                        fills_called,
                    )
                    # Check one text call for color
                    mock_dwg_instance.text.assert_any_call(
                        unittest.mock.ANY,
                        insert=(unittest.mock.ANY, unittest.mock.ANY),
                        text_anchor="middle",
                        fill="#FFFFFF",
                    )
                else:  # Light mode assertions
                    mock_svg_drawing.assert_called_with(
                        style={"background-color": expected_style["BACKGROUND_COLOR"]}
                    )
                    self.assertIn(
                        GraphConstants.PLANET_COLORS_LIGHT["Mars"], fills_called
                    )
                    self.assertIn(
                        GraphConstants.PLANET_COLORS_LIGHT["Jupiter"],
                        fills_called,
                    )
                    mock_dwg_instance.text.assert_any_call(
                        unittest.mock.ANY,
                        insert=(unittest.mock.ANY, unittest.mock.ANY),
                        text_anchor="middle",
                        fill=expected_style["TEXT_COLOR"],
                    )

    @patch("apts.observations.Utils.annotate_plot")
    @patch("apts.observations.pyplot")
    @patch("apts.observations.get_dark_mode")
    @patch("apts.place.Place.get_altaz_curve")
    def test_generate_plot_planets_specific_colors(
        self, mock_get_altitude_curve, mock_get_dark_mode, mock_pyplot, mock_annotate_plot
    ):
        self.observation.get_visible_planets = MagicMock(
            return_value=self.mock_planets_data_for_color_test
        )

        t0 = self.observation.place.ts.utc(self.observation.start)
        t1 = self.observation.place.ts.utc(self.observation.stop)
        mock_curve_df = pd.DataFrame({
            'Time': self.observation.place.ts.linspace(t0, t1, 10),
            'Altitude': [10, 20, 30, 40, 50, 40, 30, 20, 10, 0]
        })
        mock_get_altitude_curve.return_value = mock_curve_df

        self.observation.local_planets.get_skyfield_object = MagicMock(return_value=MagicMock())

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
                mock_get_dark_mode.return_value = scenario_data["global_dark_mode"]
                effective_dark_mode = scenario_data["expected_effective_dark_mode"]

                mock_pyplot.reset_mock()
                mock_annotate_plot.reset_mock()
                mock_ax = MagicMock()
                mock_fig = MagicMock()
                mock_ax.figure = mock_fig
                mock_pyplot.subplots.return_value = (mock_fig, mock_ax)

                self.observation._generate_plot_planets(
                    dark_mode_override=scenario_data["override"]
                )

                mock_ax.plot.assert_called()
                self.assertEqual(mock_ax.plot.call_count, 2)

                mock_ax.scatter.assert_called()
                self.assertEqual(mock_ax.scatter.call_count, 4)

                plot_colors_called = [
                    call.kwargs["color"] for call in mock_ax.plot.call_args_list
                ]
                scatter_colors_called = [
                    call.kwargs["color"] for call in mock_ax.scatter.call_args_list
                ]

                if effective_dark_mode:
                    expected_mars_color = GraphConstants.PLANET_COLORS_DARK["Mars"]
                    expected_jupiter_color = GraphConstants.PLANET_COLORS_DARK[
                        "Jupiter"
                    ]
                else:
                    expected_mars_color = GraphConstants.PLANET_COLORS_LIGHT["Mars"]
                    expected_jupiter_color = GraphConstants.PLANET_COLORS_LIGHT[
                        "Jupiter"
                    ]

                self.assertIn(expected_mars_color, plot_colors_called)
                self.assertIn(expected_jupiter_color, plot_colors_called)

                self.assertEqual(scatter_colors_called.count(expected_mars_color), 2)
                self.assertEqual(scatter_colors_called.count(expected_jupiter_color), 2)


class TestObservationWeatherAnalysis(unittest.TestCase):
    def setUp(self):
        # Basic setup, will be customized in each test
        self.obs = setup_observation()

        # Ensure place.local_timezone is tz-aware for pd.Timestamp construction
        # Using a fixed timezone for consistency in tests
        self.test_tz = datetime.timezone(
            datetime.timedelta(hours=-5), "EST"
        )  # Example: EST
        self.base_date = pd.Timestamp("2024-01-01", tz=self.test_tz)

        self.obs.place.local_timezone = self.test_tz
        self.obs.start = self.base_date.replace(
            hour=18, minute=0, second=0, microsecond=0
        )
        self.obs.stop = (self.base_date + timedelta(days=1)).replace(
            hour=6, minute=0, second=0, microsecond=0
        )  # Next day
        self.obs.time_limit = (self.base_date + timedelta(days=1)).replace(
            hour=2, minute=0, second=0, microsecond=0
        )

        # Mock conditions
        self.obs.conditions = Conditions()  # Use default conditions or mock as needed
        self.obs.conditions.max_clouds = 20.0
        self.obs.conditions.max_precipitation_probability = 10.0
        self.obs.conditions.max_wind = 15.0
        self.obs.conditions.min_temperature = 0.0
        self.obs.conditions.max_temperature = 25.0

        # Mock place.weather and its methods
        self.obs.place.weather = MagicMock()
        self.obs.place.weather.download_data.return_value = {"hourly": {"data": []}}
        # Explicitly mock get_weather method on self.obs.place to ensure it's a mock object
        self.obs.place.get_weather = MagicMock()

    def _generate_weather_data(self, num_hours, conditions_met_flags):
        """
        Helper to generate mock weather data DataFrame.
        conditions_met_flags is a list of booleans, one for each hour.
        If True, the hour will have good weather. If False, one or more conditions will fail.
        """
        data = []
        base_time = self.obs.start
        for i in range(num_hours):
            hour_time = base_time + datetime.timedelta(hours=i)
            if (
                hour_time > self.obs.time_limit
            ):  # Ensure we don't generate data beyond time_limit
                break

            # Good weather by default
            cloud = self.obs.conditions.max_clouds - 1
            precip = self.obs.conditions.max_precipitation_probability - 1
            wind = self.obs.conditions.max_wind - 1
            temp = (
                self.obs.conditions.min_temperature
                + self.obs.conditions.max_temperature
            ) / 2

            if (
                i < len(conditions_met_flags) and not conditions_met_flags[i]
            ):  # If flag is False, make weather bad
                # Example: make cloud cover too high. More sophisticated logic can be added.
                cloud = self.obs.conditions.max_clouds + 10

            data.append(
                {
                    "time": hour_time,
                    "cloudCover": cloud,
                    "precipProbability": precip,
                    "windSpeed": wind,
                    "temperature": temp,
                }
            )
        return pd.DataFrame(data)

    def test_get_hourly_weather_analysis_all_good(self):
        """Test when all hours have good weather."""
        num_hours = 3
        mock_weather_df = self._generate_weather_data(num_hours, [True] * num_hours)
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df

        results = self.obs.get_hourly_weather_analysis()

        self.assertEqual(len(results), num_hours)
        for i in range(num_hours):
            self.assertTrue(results[i]["is_good_hour"])
            self.assertEqual(len(results[i]["reasons"]), 0)
            self.assertEqual(results[i]["time"], mock_weather_df["time"].iloc[i])

    def test_get_hourly_weather_analysis_one_hour_bad_clouds(self):
        """Test one hour bad due to high cloud cover."""
        num_hours = 3
        # Second hour has bad weather (cloud cover)
        conditions_flags = [True, False, True]

        # Explicitly create data that violates cloud cover for the second hour
        data_rows = []
        base_time = self.obs.start
        for i in range(num_hours):
            hour_time = base_time + datetime.timedelta(hours=i)
            cloud = self.obs.conditions.max_clouds - 1
            precip = self.obs.conditions.max_precipitation_probability - 1
            wind = self.obs.conditions.max_wind - 1
            temp = (
                self.obs.conditions.min_temperature
                + self.obs.conditions.max_temperature
            ) / 2

            if i == 1:  # Second hour
                cloud = self.obs.conditions.max_clouds + 5  # Exceeds limit

            data_rows.append(
                {
                    "time": hour_time,
                    "cloudCover": cloud,
                    "precipProbability": precip,
                    "windSpeed": wind,
                    "temperature": temp,
                }
            )
        mock_weather_df = pd.DataFrame(data_rows)
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df

        results = self.obs.get_hourly_weather_analysis()

        self.assertEqual(len(results), num_hours)
        self.assertTrue(results[0]["is_good_hour"])
        self.assertFalse(results[1]["is_good_hour"])
        self.assertEqual(len(results[1]["reasons"]), 1)
        self.assertIn("Cloud cover", results[1]["reasons"][0])
        self.assertTrue(results[2]["is_good_hour"])

    def test_get_hourly_weather_analysis_one_hour_multiple_reasons(self):
        """Test one hour bad due to multiple reasons."""
        num_hours = 2
        # First hour bad (clouds and wind)
        data_rows = []
        base_time = self.obs.start
        # Hour 0: Bad
        data_rows.append(
            {
                "time": base_time,
                "cloudCover": self.obs.conditions.max_clouds + 5,  # Bad
                "precipProbability": self.obs.conditions.max_precipitation_probability
                - 1,  # Good
                "windSpeed": self.obs.conditions.max_wind + 5,  # Bad
                "temperature": (
                    self.obs.conditions.min_temperature
                    + self.obs.conditions.max_temperature
                )
                / 2,  # Good
            }
        )
        # Hour 1: Good
        data_rows.append(
            {
                "time": base_time + datetime.timedelta(hours=1),
                "cloudCover": self.obs.conditions.max_clouds - 1,
                "precipProbability": self.obs.conditions.max_precipitation_probability
                - 1,
                "windSpeed": self.obs.conditions.max_wind - 1,
                "temperature": (
                    self.obs.conditions.min_temperature
                    + self.obs.conditions.max_temperature
                )
                / 2,
            }
        )
        mock_weather_df = pd.DataFrame(data_rows)
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df

        results = self.obs.get_hourly_weather_analysis()

        self.assertEqual(len(results), num_hours)
        self.assertFalse(results[0]["is_good_hour"])
        self.assertEqual(len(results[0]["reasons"]), 2)
        self.assertTrue(
            any("Cloud cover" in reason for reason in results[0]["reasons"])
        )
        self.assertTrue(any("Wind speed" in reason for reason in results[0]["reasons"]))
        self.assertTrue(results[1]["is_good_hour"])

    def test_get_hourly_weather_analysis_respects_time_limit(self):
        """Test that analysis stops at self.time_limit."""
        # time_limit is 02:00, start is 18:00. So 18, 19, 20, 21, 22, 23, 00, 01 (8 hours)
        # Let's provide 10 hours of data, but only 8 should be processed.
        num_hours_data = 10
        expected_processed_hours = 9

        mock_weather_df = self._generate_weather_data(
            num_hours_data, [True] * num_hours_data
        )
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df

        results = self.obs.get_hourly_weather_analysis()

        self.assertEqual(len(results), expected_processed_hours)
        for i in range(expected_processed_hours):
            self.assertTrue(results[i]["is_good_hour"])

    def test_get_hourly_weather_analysis_inclusive_time_limit(self):
        """Test that analysis *includes* the hour at self.time_limit."""
        # Setup: start at 18:00, time_limit at 20:00,
        # so data for 18, 19, 20 should be included (3 hours)
        self.obs.start = self.base_date.replace(
            hour=18, minute=0, second=0, microsecond=0
        )
        self.obs.stop = self.base_date.replace(
            hour=21, minute=0, second=0, microsecond=0
        )  # Beyond time_limit
        self.obs.time_limit = self.base_date.replace(
            hour=20, minute=0, second=0, microsecond=0
        )

        num_hours_data = 5  # Provide more data than needed (18, 19, 20, 21, 22)
        mock_weather_df = self._generate_weather_data(
            num_hours_data, [True] * num_hours_data
        )
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df

        results = self.obs.get_hourly_weather_analysis()

        self.assertEqual(len(results), 3)  # Expect 18:00, 19:00, 20:00

        # Verify the times are correct
        self.assertEqual(results[0]["time"].hour, 18)
        self.assertEqual(results[1]["time"].hour, 19)
        self.assertEqual(results[2]["time"].hour, 20)

    def test_get_hourly_weather_analysis_no_weather_data_initially(self):
        """Test when weather data needs to be fetched."""
        self.obs.place.weather = None  # Simulate no weather data initially

        mock_weather_instance = MagicMock()
        num_hours = 2
        mock_weather_df = self._generate_weather_data(num_hours, [True] * num_hours)
        mock_weather_instance.get_critical_data.return_value = mock_weather_df

        # Mock self.obs.place.get_weather() to set self.obs.place.weather
        def mock_get_weather():
            self.obs.place.weather = mock_weather_instance

        self.obs.place.get_weather = MagicMock(side_effect=mock_get_weather)

        results = self.obs.get_hourly_weather_analysis()

        self.obs.place.get_weather.assert_called_once()
        self.assertEqual(len(results), num_hours)
        self.assertTrue(results[0]["is_good_hour"])

    def test_get_hourly_weather_analysis_bad_temperature_low(self):
        """Test bad weather due to low temperature."""
        num_hours = 1
        data_rows = [
            {
                "time": self.obs.start,
                "cloudCover": self.obs.conditions.max_clouds - 1,
                "precipProbability": self.obs.conditions.max_precipitation_probability
                - 1,
                "windSpeed": self.obs.conditions.max_wind - 1,
                "temperature": self.obs.conditions.min_temperature - 5,  # Too cold
            }
        ]
        mock_weather_df = pd.DataFrame(data_rows)
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df
        results = self.obs.get_hourly_weather_analysis()

        self.assertFalse(results[0]["is_good_hour"])
        self.assertIn("Temperature", results[0]["reasons"][0])
        self.assertIn("below limit", results[0]["reasons"][0])

    def test_get_hourly_weather_analysis_bad_temperature_high(self):
        """Test bad weather due to high temperature."""
        num_hours = 1
        data_rows = [
            {
                "time": self.obs.start,
                "cloudCover": self.obs.conditions.max_clouds - 1,
                "precipProbability": self.obs.conditions.max_precipitation_probability
                - 1,
                "windSpeed": self.obs.conditions.max_wind - 1,
                "temperature": self.obs.conditions.max_temperature + 5,  # Too hot
            }
        ]
        mock_weather_df = pd.DataFrame(data_rows)
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df
        results = self.obs.get_hourly_weather_analysis()

        self.assertFalse(results[0]["is_good_hour"])
        self.assertIn("Temperature", results[0]["reasons"][0])
        self.assertIn("exceeds limit", results[0]["reasons"][0])

    def test_get_hourly_weather_analysis_bad_precipitation(self):
        """Test bad weather due to high precipitation probability."""
        num_hours = 1
        data_rows = [
            {
                "time": self.obs.start,
                "cloudCover": self.obs.conditions.max_clouds - 1,
                "precipProbability": self.obs.conditions.max_precipitation_probability
                + 5,  # Too high
                "windSpeed": self.obs.conditions.max_wind - 1,
                "temperature": (
                    self.obs.conditions.min_temperature
                    + self.obs.conditions.max_temperature
                )
                / 2,
            }
        ]
        mock_weather_df = pd.DataFrame(data_rows)
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df
        results = self.obs.get_hourly_weather_analysis()

        self.assertFalse(results[0]["is_good_hour"])
        self.assertIn("Precipitation probability", results[0]["reasons"][0])

    def test_get_hourly_weather_analysis_empty_data_from_critical(self):
        """Test when get_critical_data returns an empty DataFrame."""
        self.obs.place.weather.get_critical_data.return_value = pd.DataFrame(
            columns=[
                "time",
                "cloudCover",
                "precipProbability",
                "windSpeed",
                "temperature",
            ]
        )
        results = self.obs.get_hourly_weather_analysis()

        self.assertEqual(len(results), 0)

    def test_get_hourly_weather_analysis_start_stop_time_limit_undefined(self):
        """Test behavior when observation window is not fully defined."""
        self.obs.start = None
        # self.obs.stop = None # Keep stop and time_limit for this specific test
        # self.obs.time_limit = None

        results = self.obs.get_hourly_weather_analysis()

        self.assertEqual(results, [])
        self.obs.place.weather.get_critical_data.assert_not_called()

        # Restore start and test with stop = None
        self.obs.start = pd.Timestamp("2024-01-01 18:00:00", tz=self.test_tz)
        self.obs.stop = None
        results = self.obs.get_hourly_weather_analysis()

        self.assertEqual(results, [])
        self.obs.place.weather.get_critical_data.assert_not_called()

        # Restore stop and test with time_limit = None
        self.obs.stop = pd.Timestamp("2024-01-02 06:00:00", tz=self.test_tz)
        self.obs.time_limit = None
        results = self.obs.get_hourly_weather_analysis()

        self.assertEqual(results, [])
        self.obs.place.weather.get_critical_data.assert_not_called()

    def test_is_weather_good(self):
        """Test the is_weather_good method."""
        # Use the self.obs.place and self.obs.place.weather mocks set up in setUp.

        # Test Case 1: All good weather
        # Assign a fresh mock for place.weather to ensure clean state for this case
        self.obs.place.weather = MagicMock()
        num_hours_good = 5
        mock_weather_df_good = self._generate_weather_data(
            num_hours_good, [True] * num_hours_good
        )
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df_good
        self.obs.conditions.min_weather_goodness = 50  # 50% good hours required
        self.assertTrue(self.obs.is_weather_good())
        self.obs.place.weather.get_critical_data.assert_called_once()  # Verify it was called

        # Test Case 2: Some bad weather, but overall good enough
        self.obs.place.weather = MagicMock()  # Assign a fresh mock for this case
        num_hours_mixed = 4
        # 3 good, 1 bad -> 75% good
        mock_weather_df_mixed = self._generate_weather_data(
            num_hours_mixed, [True, True, True, False]
        )
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df_mixed
        self.obs.conditions.min_weather_goodness = 70  # 70% good hours required
        self.assertTrue(self.obs.is_weather_good())
        self.obs.place.weather.get_critical_data.assert_called_once()

        # Test Case 3: Too much bad weather, overall not good enough
        self.obs.place.weather = MagicMock()  # Assign a fresh mock for this case
        num_hours_bad_overall = 4
        # 1 good, 3 bad -> 25% good
        mock_weather_df_bad_overall = self._generate_weather_data(
            num_hours_bad_overall, [True, False, False, False]
        )
        self.obs.place.weather.get_critical_data.return_value = (
            mock_weather_df_bad_overall
        )
        self.obs.conditions.min_weather_goodness = 50  # 50% good hours required
        self.assertFalse(self.obs.is_weather_good())
        self.obs.place.weather.get_critical_data.assert_called_once()

        # Test Case 4: No weather data initially (self.obs.place.weather is None)
        self.obs.place.weather = None  # Simulate no weather data initially
        self.obs.place.get_weather.reset_mock()  # Reset mock to count calls for this specific case

        # Mock get_weather to set weather data when called
        mock_weather_fetched = MagicMock()

        def mock_get_weather_side_effect():
            self.obs.place.weather = (
                mock_weather_fetched  # Set the weather mock when get_weather is called
            )
            mock_weather_fetched.get_critical_data.return_value = (
                self._generate_weather_data(1, [True])
            )

        self.obs.place.get_weather.side_effect = mock_get_weather_side_effect

        # Call is_weather_good, it should trigger get_weather
        self.assertTrue(self.obs.is_weather_good())
        self.obs.place.get_weather.assert_called_once()
        mock_weather_fetched.get_critical_data.assert_called_once()  # Verify critical data was called after fetch


class TestSunObservation(unittest.TestCase):
    @patch("apts.observations.Messier")
    @patch("apts.observations.SolarObjects")
    def test_sun_observation_window(self, mock_planets, mock_messier):
        """Test that the observation window is set correctly for sun observations."""
        # Arrange
        place = MagicMock()
        place.local_timezone = datetime.timezone.utc
        place.sunrise_time.return_value = pd.Timestamp("2025-02-18 06:00:00", tz="UTC")
        place.sunset_time.return_value = pd.Timestamp("2025-02-18 18:00:00", tz="UTC")

        ts = pd.Timestamp("2025-02-18 06:00:00", tz="UTC")
        place.get_time_relative_to_event.return_value = (ts, ts.to_pydatetime())

        equipment = MagicMock()
        conditions = MagicMock()
        conditions.max_return = "02:00:00"
        target_date = datetime.date(2025, 2, 18)

        # Act
        observation = Observation(
            place=place,
            equipment=equipment,
            conditions=conditions,
            target_date=target_date,
            sun_observation=True,
        )

        # Assert
        self.assertEqual(observation.start, place.sunrise_time.return_value)
        self.assertEqual(observation.stop, place.sunset_time.return_value)


class TestObservationSkymap(unittest.TestCase):
    def setUp(self):
        self.observation = setup_observation()

    @patch("apts.observations.pyplot")
    def test_plot_skymap_messier(self, mock_pyplot):
        """Test that plot_skymap generates a plot for a Messier object without errors."""
        fig = self.observation.plot_skymap(target_name="M31")
        self.assertIsNotNone(fig)
        mock_pyplot.subplots.assert_called_once()
        ax = mock_pyplot.subplots.return_value[1]
        ax.set_title.assert_called_with("Skymap centered on M31", color=unittest.mock.ANY)

    @patch("apts.observations.pyplot")
    def test_plot_skymap_planet(self, mock_pyplot):
        """Test that plot_skymap generates a plot for a planet without errors."""
        fig = self.observation.plot_skymap(target_name="Mars")
        self.assertIsNotNone(fig)
        mock_pyplot.subplots.assert_called_once()
        ax = mock_pyplot.subplots.return_value[1]
        ax.set_title.assert_called_with("Skymap centered on Mars", color=unittest.mock.ANY)

    @patch("apts.observations.pyplot")
    def test_plot_skymap_object_not_found(self, mock_pyplot):
        """Test that plot_skymap handles object not found gracefully."""
        fig = self.observation.plot_skymap(target_name="Not an object")
        self.assertIsNotNone(fig)
        mock_pyplot.subplots.assert_called_once()
        ax = mock_pyplot.subplots.return_value[1]
        ax.text.assert_called_with(0.5, 0.5, "Object 'Not an object' not found.",
                                   horizontalalignment='center', verticalalignment='center',
                                   transform=ax.transAxes, color=unittest.mock.ANY)

if __name__ == "__main__":
    unittest.main()


class TestPathBasedAzimuthFiltering(unittest.TestCase):
    def setUp(self):
        self.observation = setup_observation()
        self.observation.start = pd.Timestamp("2025-02-18 18:00:00", tz="UTC")
        self.observation.stop = pd.Timestamp("2025-02-19 02:00:00", tz="UTC")
        self.observation.time_limit = pd.Timestamp("2025-02-19 02:00:00", tz="UTC")

        messier_data = {
            "Messier": ["M1", "M42", "M31"],
            "Type": ["Nebula", "Nebula", "Galaxy"],
            "RA": [5.575538888888889, 5.588138888888889, 0.7123055555555556],
            "Dec": [22.0145, -5.391111111111111, 41.26916666666666],
            "Magnitude": [8.4, 4.0, 3.4],
            "Altitude": [45, 60, 20],
            "Transit": [
                pd.Timestamp("2025-02-18 20:00:00", tz="UTC"),
                pd.Timestamp("2025-02-18 22:00:00", tz="UTC"),
                pd.Timestamp("2025-02-18 19:00:00", tz="UTC"),
            ],
            "ID": [0,1,2]
        }
        self.messier_df = pd.DataFrame(messier_data)

        planets_data = {
            "Name": ["mars", "jupiter barycenter", "saturn barycenter"],
            "Magnitude": [1.0, -2.0, 0.5],
            "Altitude": [30, 50, 40],
            "Rising": [
                pd.Timestamp("2025-02-18 18:00:00", tz="UTC"),
                pd.Timestamp("2025-02-18 19:00:00", tz="UTC"),
                pd.Timestamp("2025-02-18 17:00:00", tz="UTC"),
            ],
            "Setting": [
                pd.Timestamp("2025-02-19 01:00:00", tz="UTC"),
                pd.Timestamp("2025-02-19 03:00:00", tz="UTC"),
                pd.Timestamp("2025-02-18 23:00:00", tz="UTC"),
            ],
            "Transit": [
                pd.Timestamp("2025-02-18 21:00:00", tz="UTC"),
                pd.Timestamp("2025-02-18 23:00:00", tz="UTC"),
                pd.Timestamp("2025-02-18 20:00:00", tz="UTC"),
            ],
             "ID": [0,1,2]
        }
        self.planets_df = pd.DataFrame(planets_data)

        self.observation.local_messier.objects = self.messier_df
        self.observation.local_planets.objects = self.planets_df

        # Mock get_altaz_curve
        def mock_get_altaz_curve(skyfield_object, start, stop):
            if isinstance(skyfield_object, Star):
                if skyfield_object.ra.hours == 5.575538888888889: # M1
                    return pd.DataFrame({
                        'Altitude': [10, 20, 30, 20, 10],
                        'Azimuth': [170, 180, 190, 200, 210]
                    })
                elif skyfield_object.ra.hours == 5.588138888888889: # M42
                    return pd.DataFrame({
                        'Altitude': [40, 50, 60, 50, 40],
                        'Azimuth': [190, 200, 210, 220, 230]
                    })
                elif skyfield_object.ra.hours == 0.7123055555555556: # M31
                    return pd.DataFrame({
                        'Altitude': [10, 15, 20, 15, 10],
                        'Azimuth': [350, 355, 0, 5, 10]
                    })
            else: # It's a planet
                if 'MARS' in str(skyfield_object):
                    return pd.DataFrame({
                        'Altitude': [20, 30, 40, 30, 20],
                        'Azimuth': [80, 90, 100, 110, 120]
                    })
                elif 'JUPITER' in str(skyfield_object):
                    return pd.DataFrame({
                        'Altitude': [40, 50, 60, 50, 40],
                        'Azimuth': [140, 150, 160, 170, 180]
                    })
                elif 'SATURN' in str(skyfield_object):
                    return pd.DataFrame({
                        'Altitude': [30, 40, 50, 40, 30],
                        'Azimuth': [355, 0, 5, 10, 15]
                    })

        self.observation.place.get_altaz_curve = mock_get_altaz_curve


    def test_messier_azimuth_filter(self):
        # Test with a simple azimuth range
        self.observation.conditions = Conditions(min_object_azimuth=170, max_object_azimuth=210, min_object_altitude=15)
        visible_messier = self.observation.get_visible_messier()
        self.assertEqual(len(visible_messier), 2)
        self.assertIn("M1", visible_messier["Messier"].values)
        self.assertIn("M42", visible_messier["Messier"].values)

        # Test with a wrap-around azimuth range
        self.observation.conditions = Conditions(min_object_azimuth=350, max_object_azimuth=10, min_object_altitude=15)
        visible_messier = self.observation.get_visible_messier()
        self.assertEqual(len(visible_messier), 1)
        self.assertIn("M31", visible_messier["Messier"].values)

    def test_planets_azimuth_filter(self):
        # Test with a simple azimuth range
        self.observation.conditions = Conditions(min_object_azimuth=80, max_object_azimuth=160, min_object_altitude=25)
        visible_planets = self.observation.get_visible_planets()
        self.assertEqual(len(visible_planets), 2)
        self.assertIn("Mars", visible_planets["Name"].values)
        self.assertIn("Jupiter", visible_planets["Name"].values)

        # Test with a wrap-around azimuth range
        self.observation.conditions = Conditions(min_object_azimuth=350, max_object_azimuth=100, min_object_altitude=35)
        visible_planets = self.observation.get_visible_planets()
        self.assertEqual(len(visible_planets), 2)
        self.assertIn("Saturn", visible_planets["Name"].values)
        self.assertIn("Mars", visible_planets["Name"].values)
