import os
import unittest
import tempfile
import datetime # Added
import ephem
from unittest.mock import patch, mock_open
import pandas as pd
from unittest.mock import MagicMock, call # Added MagicMock and call
from apts.observations import Observation
from apts.constants.graphconstants import get_plot_style, OpticalType, GraphConstants # Added GraphConstants
from apts.constants.objecttablelabels import ObjectTableLabels # Added ObjectTableLabels
from apts.utils import ureg # Added ureg for Quantity
from tests import setup_observation
from apts.conditions import Conditions # Import Conditions at the top level


# MockPlace and MockEquipment classes are removed

class TestObservationTemplate(unittest.TestCase):
    def setUp(self):
        self.observation = setup_observation()

        # Ensure place.local_timezone is tz-aware for pd.Timestamp construction
        if not hasattr(self.observation.place, 'local_timezone') or self.observation.place.local_timezone is None:
            obs_local_tz = datetime.timezone.utc
        elif isinstance(self.observation.place.local_timezone, str):
            obs_local_tz = datetime.timezone.utc if self.observation.place.local_timezone.upper() == 'UTC' else self.observation.place.local_timezone
        else:
            obs_local_tz = self.observation.place.local_timezone

        if self.observation.start is None:
            self.observation.start = pd.Timestamp('2025/02/18 18:00:00', tz=obs_local_tz)

        if self.observation.stop is None:
            if pd.api.types.is_datetime64_any_dtype(self.observation.start):
                self.observation.stop = self.observation.start + pd.Timedelta(hours=8)
            else:
                self.observation.stop = pd.Timestamp('2025/02/19 02:00:00', tz=obs_local_tz)

        if self.observation.time_limit is None:
            if pd.api.types.is_datetime64_any_dtype(self.observation.start):
                max_return_values = [int(value) for value in self.observation.conditions.max_return.split(":")]
                time_limit_dt = self.observation.start.replace(
                    hour=max_return_values[0], minute=max_return_values[1], second=max_return_values[2]
                )
                self.observation.time_limit = (
                    time_limit_dt if time_limit_dt > self.observation.start else time_limit_dt + pd.Timedelta(days=1)
                )
            else:
                self.observation.time_limit = pd.Timestamp('2025/02/19 02:00:00', tz=obs_local_tz)

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
    
    @patch('builtins.open', new_callable=mock_open, read_data="<!doctype html><html><head><style>body{color:#555;}</style></head><body><h1>$title</h1><p>$place_name</p></body></html>")
    def test_to_html_default_template(self, mock_file):
        """Test that to_html uses the default template when no custom template is provided"""
        html = self.observation.to_html()
        
        # Verify that open was called with the default template path
        mock_file.assert_called_once()
        self.assertEqual(mock_file.call_args[0][0], Observation.NOTIFICATION_TEMPLATE)
        
        # Verify that the template contains the substituted values
        self.assertIn(self.observation.place.name, html)
        self.assertIn("APTS", html)
        
    @patch('builtins.open', new_callable=mock_open, read_data="<!doctype html><html><head><style>body{color:#555;}</style></head><body><h1>$title</h1><p>$place_name</p></body></html>")
    def test_to_html_custom_template(self, mock_file):
        """Test that to_html uses a custom template when provided"""
        custom_template = "/path/to/custom/template.html"
        html = self.observation.to_html(custom_template=custom_template)
        
        # Verify that open was called with the custom template path
        mock_file.assert_called_once_with(custom_template)
        
        # Verify that the template contains the substituted values
        self.assertIn(self.observation.place.name, html)
        self.assertIn("APTS", html)
    
    @patch('builtins.open', new_callable=mock_open, read_data="<!doctype html><html><head><style>body{color:#555;}</style></head><body><h1>$title</h1><p>$place_name</p></body></html>")
    def test_to_html_custom_css(self, mock_file):
        """Test that to_html injects custom CSS when provided"""
        custom_css = "h1 { color: blue; }"
        html = self.observation.to_html(css=custom_css)
        
        # Verify that the CSS was properly injected
        self.assertIn(custom_css, html)
        self.assertIn("body{color:#555;}", html)
        
    def test_to_html_with_actual_template_file(self):
        """Test to_html with an actual temporary template file"""
        # Create a temporary template file
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
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
        if not hasattr(self.observation.place, 'local_timezone') or self.observation.place.local_timezone is None:
            obs_local_tz = datetime.timezone.utc
        elif isinstance(self.observation.place.local_timezone, str):
            obs_local_tz = datetime.timezone.utc if self.observation.place.local_timezone.upper() == 'UTC' else self.observation.place.local_timezone
        else:
            obs_local_tz = self.observation.place.local_timezone

        if self.observation.start is None:
             self.observation.start = pd.Timestamp('2025/02/18 18:00:00', tz=obs_local_tz)

        if self.observation.stop is None:
            if pd.api.types.is_datetime64_any_dtype(self.observation.start):
                self.observation.stop = self.observation.start + pd.Timedelta(hours=8)
            else:
                self.observation.stop = pd.Timestamp('2025/02/19 02:00:00', tz=obs_local_tz)

        if self.observation.time_limit is None:
            if pd.api.types.is_datetime64_any_dtype(self.observation.start):
                max_return_values = [int(value) for value in self.observation.conditions.max_return.split(":")]
                time_limit_dt = self.observation.start.replace(
                    hour=max_return_values[0], minute=max_return_values[1], second=max_return_values[2]
                )
                self.observation.time_limit = (
                    time_limit_dt if time_limit_dt > self.observation.start else time_limit_dt + pd.Timedelta(days=1)
                )
            else:
                self.observation.time_limit = pd.Timestamp('2025/02/19 02:00:00', tz=obs_local_tz)

        # Mock the get_visible_messier to return a non-empty DataFrame
        # to avoid early exit from _generate_plot_messier
        mock_messier_data = {
            'Messier': ['M1'],
            'Type': ['Nebula'],
            'RA': ['05h 34m 31.94s'],
            'Dec': ['+22° 00′ 52.2″'],
            'Magnitude': [8.4 * ureg.mag],
            'Constellation': ['Tau'],
            'Size': [ureg.arcmin * 6], # Using Quantity for size
            'Distance': [6.523 * 1000 * ureg.light_year],
            'Altitude': [45 * ureg.deg], # Using Quantity
            'Azimuth': [180 * ureg.deg], # Using Quantity
            'Transit': [pd.Timestamp('2023-01-01 22:00:00', tz='UTC')],
            'Width': [6.0 * ureg.arcmin], # Using Quantity
            'Height': [4.0 * ureg.arcmin] # Using Quantity
        }
        self.mock_messier_df = pd.DataFrame(mock_messier_data)
        # Ensure DataFrame columns with pint Quantities are correctly typed if needed by the method
        # For _generate_plot_messier, it seems to handle .magnitude internally.

        # Mock data for planet color tests
        self.mock_planets_data_for_color_test = pd.DataFrame({
            ObjectTableLabels.NAME: ['Mars', 'Jupiter', 'UnknownPlanet'],
            ObjectTableLabels.TRANSIT: [pd.Timestamp('2023-01-01 22:00:00', tz='UTC')] * 3,
            ObjectTableLabels.ALTITUDE: [45 * ureg.deg] * 3,
            ObjectTableLabels.SIZE: [10 * ureg.arcsec] * 3,
            ObjectTableLabels.PHASE: [90.0 * ureg.percent] * 3 # For SVG plot
        })

    @patch('apts.observations.Utils.annotate_plot')
    @patch('apts.observations.pyplot')
    @patch('apts.observations.get_dark_mode')
    def test_generate_plot_messier_dark_mode_styles(self, mock_get_dark_mode, mock_pyplot, mock_annotate_plot):
        scenarios = [
            {"override": True, "global_dark_mode": False, "expected_effective_dark_mode": True, "desc": "Override True"},
            {"override": False, "global_dark_mode": True, "expected_effective_dark_mode": False, "desc": "Override False"},
            {"override": None, "global_dark_mode": True,  "expected_effective_dark_mode": True, "desc": "Override None, Global True"},
            {"override": None, "global_dark_mode": False, "expected_effective_dark_mode": False, "desc": "Override None, Global False"},
        ]

        # Mock get_visible_messier to control its output (already in setUp)
        self.observation.get_visible_messier = MagicMock(return_value=self.mock_messier_df)

        for i, scenario_data in enumerate(scenarios):
            with self.subTest(msg=scenario_data["desc"], i=i):
                mock_get_dark_mode.return_value = scenario_data["global_dark_mode"]
                expected_style = get_plot_style(scenario_data["expected_effective_dark_mode"])

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
                mock_legend.get_texts.return_value = [MagicMock()] # Assume at least one text item for simplicity

                returned_fig = self.observation._generate_plot_messier(dark_mode_override=scenario_data["override"])

                self.assertEqual(returned_fig, mock_fig)
                mock_pyplot.subplots.assert_called_once()
                if scenario_data["expected_effective_dark_mode"]:
                    mock_fig.patch.set_facecolor.assert_called_with('#1C1C3A')
                    mock_ax.set_facecolor.assert_called_with('#2A004F')
                    mock_ax.set_title.assert_any_call("Messier Objects Altitude", color='#FFFFFF')
                    if not self.mock_messier_df.empty:
                        mock_legend.get_frame().set_facecolor.assert_called_with('#2A004F')
                        mock_legend.get_frame().set_edgecolor.assert_called_with('#CCCCCC')
                        mock_legend.get_title().set_color.assert_called_with('#FFFFFF')
                        for text_mock in mock_legend.get_texts():
                            text_mock.set_color.assert_called_with('#FFFFFF')
                else: # Light mode assertions remain using expected_style from get_plot_style(False)
                    mock_fig.patch.set_facecolor.assert_called_with(expected_style['FIGURE_FACE_COLOR'])
                    mock_ax.set_facecolor.assert_called_with(expected_style['AXES_FACE_COLOR'])
                    mock_ax.set_title.assert_any_call("Messier Objects Altitude", color=expected_style['TEXT_COLOR'])
                    if not self.mock_messier_df.empty:
                        mock_legend.get_frame().set_facecolor.assert_called_with(expected_style['AXES_FACE_COLOR'])
                        mock_legend.get_frame().set_edgecolor.assert_called_with(expected_style['AXIS_COLOR'])
                        mock_legend.get_title().set_color.assert_called_with(expected_style['TEXT_COLOR'])
                        for text_mock in mock_legend.get_texts():
                            text_mock.set_color.assert_called_with(expected_style['TEXT_COLOR'])

                mock_annotate_plot.assert_called_with(mock_ax, "Altitude [°]", scenario_data["expected_effective_dark_mode"])
                if not self.mock_messier_df.empty:
                    mock_ax.legend.assert_called_once()

    @patch('apts.observations.svg.Drawing')
    @patch('apts.observations.get_dark_mode')
    def test_plot_visible_planets_svg_dark_mode_styles(self, mock_get_dark_mode, mock_svg_drawing):
        # Use the more detailed mock_planets_data_for_color_test
        self.observation.get_visible_planets = MagicMock(return_value=self.mock_planets_data_for_color_test)

        scenarios = [
            {"override": True, "global_dark_mode": False, "expected_effective_dark_mode": True, "desc": "Override True"},
            {"override": False, "global_dark_mode": True, "expected_effective_dark_mode": False, "desc": "Override False"},
            {"override": None, "global_dark_mode": True,  "expected_effective_dark_mode": True, "desc": "Override None, Global True"},
            {"override": None, "global_dark_mode": False, "expected_effective_dark_mode": False, "desc": "Override None, Global False"},
        ]

        for i, scenario_data in enumerate(scenarios):
            with self.subTest(msg=scenario_data["desc"], i=i):
                mock_get_dark_mode.return_value = scenario_data["global_dark_mode"]
                expected_style = get_plot_style(scenario_data["expected_effective_dark_mode"])

                # Reset svg.Drawing mock and prepare its return value for this subtest
                mock_svg_drawing.reset_mock()
                mock_dwg_instance = MagicMock()
                mock_svg_drawing.return_value = mock_dwg_instance

                self.observation.plot_visible_planets_svg(dark_mode_override=scenario_data["override"])

                fills_called = [call.kwargs['fill'] for call in mock_dwg_instance.circle.call_args_list]
                self.assertEqual(mock_dwg_instance.circle.call_count, 3)

                if scenario_data["expected_effective_dark_mode"]:
                    mock_svg_drawing.assert_called_with(style={'background-color': '#1C1C3A'})
                    self.assertIn(GraphConstants.PLANET_COLORS_DARK['Mars'], fills_called)
                    self.assertIn(GraphConstants.PLANET_COLORS_DARK['Jupiter'], fills_called)
                    self.assertIn(expected_style['AXES_FACE_COLOR'], fills_called) # Default for UnknownPlanet
                    # Check one text call for color
                    mock_dwg_instance.text.assert_any_call(unittest.mock.ANY, insert=(unittest.mock.ANY, unittest.mock.ANY),
                                                           text_anchor="middle", fill='#FFFFFF')
                else: # Light mode assertions
                    mock_svg_drawing.assert_called_with(style={'background-color': expected_style['BACKGROUND_COLOR']})
                    self.assertIn(GraphConstants.PLANET_COLORS_LIGHT['Mars'], fills_called)
                    self.assertIn(GraphConstants.PLANET_COLORS_LIGHT['Jupiter'], fills_called)
                    self.assertIn(expected_style['AXES_FACE_COLOR'], fills_called) # Default for UnknownPlanet
                    mock_dwg_instance.text.assert_any_call(unittest.mock.ANY, insert=(unittest.mock.ANY, unittest.mock.ANY),
                                                           text_anchor="middle", fill=expected_style['TEXT_COLOR'])

    @patch('apts.observations.Utils.annotate_plot')
    @patch('apts.observations.pyplot')
    @patch('apts.observations.get_dark_mode')
    def test_generate_plot_planets_specific_colors(self, mock_get_dark_mode, mock_pyplot, mock_annotate_plot):
        self.observation.get_visible_planets = MagicMock(return_value=self.mock_planets_data_for_color_test)

        scenarios = [
            {"override": True, "global_dark_mode": False, "expected_effective_dark_mode": True, "desc": "Override True"},
            {"override": False, "global_dark_mode": True, "expected_effective_dark_mode": False, "desc": "Override False"},
            {"override": None, "global_dark_mode": True,  "expected_effective_dark_mode": True, "desc": "Override None, Global True"},
            {"override": None, "global_dark_mode": False, "expected_effective_dark_mode": False, "desc": "Override None, Global False"},
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

                self.observation._generate_plot_planets(dark_mode_override=scenario_data["override"])

                mock_ax.scatter.assert_called()
                self.assertEqual(mock_ax.scatter.call_count, 3)

                colors_called = [call.kwargs['color'] for call in mock_ax.scatter.call_args_list] # Changed 'c' to 'color'

                if effective_dark_mode:
                    expected_mars_color = GraphConstants.PLANET_COLORS_DARK['Mars']
                    expected_jupiter_color = GraphConstants.PLANET_COLORS_DARK['Jupiter']
                    default_color = GraphConstants.DARK_COLORS[OpticalType.GENERIC]
                else:
                    expected_mars_color = GraphConstants.PLANET_COLORS_LIGHT['Mars']
                    expected_jupiter_color = GraphConstants.PLANET_COLORS_LIGHT['Jupiter']
                    default_color = GraphConstants.COLORS[OpticalType.GENERIC]

                self.assertIn(expected_mars_color, colors_called)
                self.assertIn(expected_jupiter_color, colors_called)
                self.assertIn(default_color, colors_called) # For 'UnknownPlanet'


class TestObservationWeatherAnalysis(unittest.TestCase):
    def setUp(self):
        # Basic setup, will be customized in each test
        self.obs = setup_observation()

        # Ensure place.local_timezone is tz-aware for pd.Timestamp construction
        # Using a fixed timezone for consistency in tests
        self.test_tz = datetime.timezone(datetime.timedelta(hours=-5), 'EST') # Example: EST

        self.obs.place.local_timezone = self.test_tz
        self.obs.start = pd.Timestamp('2024-01-01 18:00:00', tz=self.test_tz)
        self.obs.stop = pd.Timestamp('2024-01-02 06:00:00', tz=self.test_tz) # Next day
        self.obs.time_limit = pd.Timestamp('2024-01-02 02:00:00', tz=self.test_tz)

        # Mock conditions
        self.obs.conditions = Conditions() # Use default conditions or mock as needed
        self.obs.conditions.max_clouds = 20.0
        self.obs.conditions.max_precipitation_probability = 10.0
        self.obs.conditions.max_wind = 15.0
        self.obs.conditions.min_temperature = 0.0
        self.obs.conditions.max_temperature = 25.0

        # Mock place.weather and its methods
        self.obs.place.weather = MagicMock()


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
            if hour_time > self.obs.time_limit : # Ensure we don't generate data beyond time_limit
                break

            # Good weather by default
            cloud = self.obs.conditions.max_clouds - 1
            precip = self.obs.conditions.max_precipitation_probability -1
            wind = self.obs.conditions.max_wind -1
            temp = (self.obs.conditions.min_temperature + self.obs.conditions.max_temperature) / 2

            if i < len(conditions_met_flags) and not conditions_met_flags[i]: # If flag is False, make weather bad
                # Example: make cloud cover too high. More sophisticated logic can be added.
                cloud = self.obs.conditions.max_clouds + 10

            data.append({
                'time': hour_time,
                'cloudCover': cloud,
                'precipProbability': precip,
                'windSpeed': wind,
                'temperature': temp
            })
        return pd.DataFrame(data)

    def test_get_hourly_weather_analysis_all_good(self):
        """Test when all hours have good weather."""
        num_hours = 3
        mock_weather_df = self._generate_weather_data(num_hours, [True] * num_hours)
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df

        results = self.obs.get_hourly_weather_analysis()

        self.assertEqual(len(results), num_hours)
        for i in range(num_hours):
            self.assertTrue(results[i]['is_good'])
            self.assertEqual(len(results[i]['reasons']), 0)
            self.assertEqual(results[i]['time'], mock_weather_df['time'].iloc[i])

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
            temp = (self.obs.conditions.min_temperature + self.obs.conditions.max_temperature) / 2

            if i == 1: # Second hour
                cloud = self.obs.conditions.max_clouds + 5 # Exceeds limit

            data_rows.append({
                'time': hour_time, 'cloudCover': cloud, 'precipProbability': precip,
                'windSpeed': wind, 'temperature': temp
            })
        mock_weather_df = pd.DataFrame(data_rows)
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df

        results = self.obs.get_hourly_weather_analysis()

        self.assertEqual(len(results), num_hours)
        self.assertTrue(results[0]['is_good'])
        self.assertFalse(results[1]['is_good'])
        self.assertEqual(len(results[1]['reasons']), 1)
        self.assertIn("Cloud cover", results[1]['reasons'][0])
        self.assertTrue(results[2]['is_good'])

    def test_get_hourly_weather_analysis_one_hour_multiple_reasons(self):
        """Test one hour bad due to multiple reasons."""
        num_hours = 2
        # First hour bad (clouds and wind)
        data_rows = []
        base_time = self.obs.start
        # Hour 0: Bad
        data_rows.append({
            'time': base_time,
            'cloudCover': self.obs.conditions.max_clouds + 5, # Bad
            'precipProbability': self.obs.conditions.max_precipitation_probability - 1, # Good
            'windSpeed': self.obs.conditions.max_wind + 5, # Bad
            'temperature': (self.obs.conditions.min_temperature + self.obs.conditions.max_temperature) / 2 # Good
        })
        # Hour 1: Good
        data_rows.append({
            'time': base_time + datetime.timedelta(hours=1),
            'cloudCover': self.obs.conditions.max_clouds - 1,
            'precipProbability': self.obs.conditions.max_precipitation_probability - 1,
            'windSpeed': self.obs.conditions.max_wind - 1,
            'temperature': (self.obs.conditions.min_temperature + self.obs.conditions.max_temperature) / 2
        })
        mock_weather_df = pd.DataFrame(data_rows)
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df

        results = self.obs.get_hourly_weather_analysis()

        self.assertEqual(len(results), num_hours)
        self.assertFalse(results[0]['is_good'])
        self.assertEqual(len(results[0]['reasons']), 2)
        self.assertTrue(any("Cloud cover" in reason for reason in results[0]['reasons']))
        self.assertTrue(any("Wind speed" in reason for reason in results[0]['reasons']))
        self.assertTrue(results[1]['is_good'])

    def test_get_hourly_weather_analysis_respects_time_limit(self):
        """Test that analysis stops at self.time_limit."""
        # time_limit is 02:00, start is 18:00. So 18, 19, 20, 21, 22, 23, 00, 01 (8 hours)
        # Let's provide 10 hours of data, but only 8 should be processed.
        num_hours_data = 10
        expected_processed_hours = 8

        mock_weather_df = self._generate_weather_data(num_hours_data, [True] * num_hours_data)
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df

        results = self.obs.get_hourly_weather_analysis()

        self.assertEqual(len(results), expected_processed_hours)
        for i in range(expected_processed_hours):
            self.assertTrue(results[i]['is_good'])

    def test_get_hourly_weather_analysis_no_weather_data_initially(self):
        """Test when weather data needs to be fetched."""
        self.obs.place.weather = None # Simulate no weather data initially

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
        self.assertTrue(results[0]['is_good'])

    def test_get_hourly_weather_analysis_bad_temperature_low(self):
        """Test bad weather due to low temperature."""
        num_hours = 1
        data_rows = [{
            'time': self.obs.start,
            'cloudCover': self.obs.conditions.max_clouds - 1,
            'precipProbability': self.obs.conditions.max_precipitation_probability - 1,
            'windSpeed': self.obs.conditions.max_wind - 1,
            'temperature': self.obs.conditions.min_temperature - 5 # Too cold
        }]
        mock_weather_df = pd.DataFrame(data_rows)
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df
        results = self.obs.get_hourly_weather_analysis()
        self.assertFalse(results[0]['is_good'])
        self.assertIn("Temperature", results[0]['reasons'][0])
        self.assertIn("below limit", results[0]['reasons'][0])

    def test_get_hourly_weather_analysis_bad_temperature_high(self):
        """Test bad weather due to high temperature."""
        num_hours = 1
        data_rows = [{
            'time': self.obs.start,
            'cloudCover': self.obs.conditions.max_clouds - 1,
            'precipProbability': self.obs.conditions.max_precipitation_probability - 1,
            'windSpeed': self.obs.conditions.max_wind - 1,
            'temperature': self.obs.conditions.max_temperature + 5 # Too hot
        }]
        mock_weather_df = pd.DataFrame(data_rows)
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df
        results = self.obs.get_hourly_weather_analysis()
        self.assertFalse(results[0]['is_good'])
        self.assertIn("Temperature", results[0]['reasons'][0])
        self.assertIn("exceeds limit", results[0]['reasons'][0])

    def test_get_hourly_weather_analysis_bad_precipitation(self):
        """Test bad weather due to high precipitation probability."""
        num_hours = 1
        data_rows = [{
            'time': self.obs.start,
            'cloudCover': self.obs.conditions.max_clouds - 1,
            'precipProbability': self.obs.conditions.max_precipitation_probability + 5, # Too high
            'windSpeed': self.obs.conditions.max_wind - 1,
            'temperature': (self.obs.conditions.min_temperature + self.obs.conditions.max_temperature) / 2
        }]
        mock_weather_df = pd.DataFrame(data_rows)
        self.obs.place.weather.get_critical_data.return_value = mock_weather_df
        results = self.obs.get_hourly_weather_analysis()
        self.assertFalse(results[0]['is_good'])
        self.assertIn("Precipitation probability", results[0]['reasons'][0])

    def test_get_hourly_weather_analysis_empty_data_from_critical(self):
        """Test when get_critical_data returns an empty DataFrame."""
        self.obs.place.weather.get_critical_data.return_value = pd.DataFrame(
            columns=['time', 'cloudCover', 'precipProbability', 'windSpeed', 'temperature']
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
        self.obs.start = pd.Timestamp('2024-01-01 18:00:00', tz=self.test_tz)
        self.obs.stop = None
        results = self.obs.get_hourly_weather_analysis()
        self.assertEqual(results, [])
        self.obs.place.weather.get_critical_data.assert_not_called()

        # Restore stop and test with time_limit = None
        self.obs.stop = pd.Timestamp('2024-01-02 06:00:00', tz=self.test_tz)
        self.obs.time_limit = None
        results = self.obs.get_hourly_weather_analysis()
        self.assertEqual(results, [])
        self.obs.place.weather.get_critical_data.assert_not_called()


class TestSunObservation(unittest.TestCase):
    def test_sun_observation_window(self):
        """Test that the observation window is set correctly for sun observations."""
        # Arrange
        place = MagicMock()
        place.local_timezone = datetime.timezone.utc
        place.sunrise_time.return_value = pd.Timestamp('2025-02-18 06:00:00', tz='UTC')
        place.sunset_time.return_value = pd.Timestamp('2025-02-18 18:00:00', tz='UTC')
        place.get_time_relative_to_event.return_value = (pd.Timestamp('2025-02-18 06:00:00', tz='UTC'), ephem.Date('2025/2/18 06:00:00'))

        equipment = MagicMock()
        conditions = MagicMock()
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
        self.assertEqual(observation.start_time_for_observation_window, place.sunrise_time.return_value)
        self.assertEqual(observation.stop_time_for_observation_window, place.sunset_time.return_value)

if __name__ == '__main__':
    unittest.main()