import os
import unittest
import tempfile
import datetime # Added
from unittest.mock import patch, mock_open
import pandas as pd
from unittest.mock import MagicMock, call # Added MagicMock and call
from apts.observations import Observation
from apts.constants.graphconstants import get_plot_style, OpticalType # Added get_plot_style, OpticalType
from apts.utils import ureg # Added ureg for Quantity
from tests import setup_observation


# Mock place and equipment for Observation instantiation if setup_observation isn't sufficient
class MockPlace:
    def __init__(self):
        self.name = "MockPlace"
        self.lat = 0 * ureg.deg
        self.lon = 0 * ureg.deg
        self.local_timezone = datetime.timezone.utc # Changed to datetime.timezone.utc
        self.date = pd.Timestamp('2023-01-01 00:00:00', tz='UTC') # dummy date

    def sunset_time(self, target_date=None):
        return pd.Timestamp('2023-01-01 18:00:00', tz='UTC')

    def sunrise_time(self, target_date=None):
        return pd.Timestamp('2023-01-02 06:00:00', tz='UTC')

    def moonrise_time(self):
        return pd.Timestamp('2023-01-01 20:00:00', tz='UTC')

    def moonset_time(self):
        return pd.Timestamp('2023-01-02 04:00:00', tz='UTC')

class MockEquipment:
    def data(self): # Add a data method if Observation init or other methods need it
        return pd.DataFrame()


class TestObservationTemplate(unittest.TestCase):
    def setUp(self):
        # self.observation = setup_observation() # This might be too complex, use simpler mocks for plotting
        # Simpler setup for plotting tests to avoid deep dependencies of setup_observation
        self.mock_place = MockPlace()
        self.mock_equipment = MockEquipment()
        # Mock conditions if necessary, or use default
        from apts.conditions import Conditions
        self.conditions = Conditions()
        self.observation = Observation(self.mock_place, self.mock_equipment, self.conditions)

        # Ensure self.start and self.time_limit are set for plotting methods
        # These would normally be set by Observation.__init__ based on place.sunset/sunrise
        # Forcing them here if not set by the simplified Observation init
        if self.observation.start is None:
            self.observation.start = pd.Timestamp('2023-01-01 18:00:00', tz='UTC')
        if self.observation.time_limit is None:
            self.observation.time_limit = pd.Timestamp('2023-01-02 02:00:00', tz='UTC')

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
        self.mock_place = MockPlace()
        self.mock_equipment = MockEquipment()
        from apts.conditions import Conditions
        self.conditions = Conditions(min_object_altitude=10*ureg.deg) # Ensure min_object_altitude is a Quantity
        self.observation = Observation(self.mock_place, self.mock_equipment, self.conditions)

        # Ensure self.start and self.time_limit are set.
        if self.observation.start is None:
             self.observation.start = pd.Timestamp('2023-01-01 18:00:00', tz='UTC')
        if self.observation.time_limit is None:
            self.observation.time_limit = pd.Timestamp('2023-01-02 02:00:00', tz='UTC')

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
        # Mock get_visible_planets to return some dummy data
        mock_planets_data = {
            'Name': ['Jupiter'],
            'Size': [40 * ureg.arcsec],
            'Phase': [99.0 * ureg.percent]
        }
        mock_planets_df = pd.DataFrame(mock_planets_data)
        self.observation.get_visible_planets = MagicMock(return_value=mock_planets_df)

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

                if scenario_data["expected_effective_dark_mode"]:
                    mock_svg_drawing.assert_called_with(style={'background-color': '#1C1C3A'})
                    if not mock_planets_df.empty:
                        mock_dwg_instance.circle.assert_any_call(center=(unittest.mock.ANY, unittest.mock.ANY), r=unittest.mock.ANY,
                                                                 stroke='#CCCCCC', fill='#2A004F', stroke_width="1")
                        mock_dwg_instance.text.assert_any_call(unittest.mock.ANY, insert=(unittest.mock.ANY, unittest.mock.ANY),
                                                               text_anchor="middle", fill='#FFFFFF')
                else: # Light mode assertions
                    mock_svg_drawing.assert_called_with(style={'background-color': expected_style['BACKGROUND_COLOR']})
                    if not mock_planets_df.empty:
                        mock_dwg_instance.circle.assert_any_call(center=(unittest.mock.ANY, unittest.mock.ANY), r=unittest.mock.ANY,
                                                                 stroke=expected_style['AXIS_COLOR'], fill=expected_style['AXES_FACE_COLOR'], stroke_width="1")
                        mock_dwg_instance.text.assert_any_call(unittest.mock.ANY, insert=(unittest.mock.ANY, unittest.mock.ANY),
                                                               text_anchor="middle", fill=expected_style['TEXT_COLOR'])


if __name__ == '__main__':
    unittest.main()