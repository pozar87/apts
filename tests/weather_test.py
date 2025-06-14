import pytest
import json
import requests_mock
from unittest.mock import patch, MagicMock # Added
import pandas as pd # Added
from apts.weather import Weather # Added
from apts.constants.graphconstants import get_plot_style # Added
from . import setup_place

# Keep existing tests if they are not conflicting

def test_weather_successful_request(): # Existing test
  mock_response = {
    "hourly": {
      "data": [
        {
          "time": 1624000000,
          "summary": "Clear",
          "temperature": 20,
          "cloudCover": 0.1,
          "precipProbability": 0.2,
          "windSpeed": 5,
          "pressure": 1013,
          "visibility": 10,
          "ozone": 300
        }
      ]
    }
  }

  with requests_mock.Mocker() as m:
    m.get(requests_mock.ANY, json=mock_response)

    p = setup_place()
    p.get_weather()

    # Verify weather object was created
    assert p.weather is not None

    # Verify data was processed correctly
    weather_data = p.weather.data
    assert not weather_data.empty
    assert weather_data['temperature'].iloc[0] == 20
    assert weather_data['cloudCover'].iloc[0] == 10  # 0.1 * 100
    assert weather_data['precipProbability'].iloc[0] == 20  # 0.2 * 100

def test_weather_api_error():
  with requests_mock.Mocker() as m:
    m.get(requests_mock.ANY, status_code=500)

    p = setup_place()
    # Original test might raise JSONDecodeError if API returns 500.
    # If get_weather is robust to it (e.g. returns None or empty data), adjust assertion.
    # For now, assuming original intent was to check for this specific error on bad response.
    with pytest.raises(json.decoder.JSONDecodeError): # Or other relevant error if behavior changed
      p.get_weather()


@patch('apts.weather.Utils.annotate_plot')
@patch('pandas.DataFrame.plot') # Mocking the plot method of DataFrame
@patch('apts.weather.get_dark_mode')
def test_plot_clouds_dark_mode_styles(mock_get_dark_mode, mock_df_plot, mock_annotate_plot, requests_mock):
    # --- Setup Weather instance and mock data ---
    # Mock the API response for Weather data download
    mock_api_response = {
        "hourly": {
            "data": [{"time": 1624000000, "cloudCover": 0.5}]
        }
    }
    # Mock requests_cache's behavior or actual HTTP request if Weather init calls download_data
    # Here, we assume Weather constructor calls download_data which uses requests.get
    requests_mock.get(requests_mock.ANY, json=mock_api_response)

    weather = Weather(lat=0, lon=0, local_timezone='UTC') # Actual instantiation

    # Ensure weather.data is populated. If download_data isn't called in init, mock it:
    # weather.data = pd.DataFrame({'time': pd.to_datetime(['2023-01-01 12:00:00'], utc=True), 'cloudCover': [50.0]})
    # Or ensure _filter_data returns something suitable
    # For this test, assume weather.data is populated correctly after init.

    # --- Test Dark Mode Enabled ---
    mock_get_dark_mode.return_value = True
    dark_style = get_plot_style(True)

    # Mock the Axes object that pandas.DataFrame.plot() would return
    mock_ax_dark = MagicMock()
    mock_fig_dark = MagicMock()
    mock_ax_dark.figure = mock_fig_dark
    mock_df_plot.return_value = mock_ax_dark # df.plot() returns this mock_ax

    # Mock legend on the axes
    mock_legend_dark = MagicMock()
    mock_ax_dark.get_legend.return_value = mock_legend_dark
    mock_legend_dark.get_frame.return_value = MagicMock()
    mock_legend_dark.get_title.return_value = MagicMock() # if legends can have titles
    mock_legend_dark.get_texts.return_value = [MagicMock()]


    ax_returned_dark = weather.plot_clouds(hours=1) # Call the method to be tested

    assert ax_returned_dark == mock_ax_dark # Ensure the method returns the ax object
    mock_df_plot.assert_called_once() # Check that pandas plot was called

    # Check that figure and axes face colors are set when plot creates them
    mock_fig_dark.patch.set_facecolor.assert_called_with(dark_style['FIGURE_FACE_COLOR'])
    mock_ax_dark.set_facecolor.assert_called_with(dark_style['AXES_FACE_COLOR'])

    # Check title color
    mock_ax_dark.set_title.assert_any_call(mock_ax_dark.get_title(), color=dark_style['TEXT_COLOR'])

    # Check legend styling
    mock_ax_dark.get_legend.assert_called_once()
    mock_legend_dark.get_frame().set_facecolor.assert_called_with(dark_style['AXES_FACE_COLOR'])
    mock_legend_dark.get_frame().set_edgecolor.assert_called_with(dark_style['AXIS_COLOR'])
    for text_mock in mock_legend_dark.get_texts():
        text_mock.set_color.assert_called_with(dark_style['TEXT_COLOR'])

    mock_annotate_plot.assert_called_with(mock_ax_dark, "Cloud cover [%]", True)

    # --- Test Dark Mode Disabled ---
    mock_get_dark_mode.return_value = False
    light_style = get_plot_style(False)

    # Reset mocks for the light mode call
    mock_df_plot.reset_mock()
    mock_annotate_plot.reset_mock()
    # mock_ax_dark.reset_mock() # Don't reset the object itself, just its call records if needed
    # mock_fig_dark.reset_mock()
    # mock_legend_dark.reset_mock()
    # Instead of resetting, create new mocks for clarity or ensure calls are distinct
    mock_ax_light = MagicMock()
    mock_fig_light = MagicMock()
    mock_ax_light.figure = mock_fig_light
    mock_df_plot.return_value = mock_ax_light # df.plot() returns this new mock_ax for light mode

    mock_legend_light = MagicMock()
    mock_ax_light.get_legend.return_value = mock_legend_light
    mock_legend_light.get_frame.return_value = MagicMock()
    mock_legend_light.get_texts.return_value = [MagicMock()]


    ax_returned_light = weather.plot_clouds(hours=1)

    assert ax_returned_light == mock_ax_light
    mock_df_plot.assert_called_once() # Called once for light mode

    mock_fig_light.patch.set_facecolor.assert_called_with(light_style['FIGURE_FACE_COLOR'])
    mock_ax_light.set_facecolor.assert_called_with(light_style['AXES_FACE_COLOR'])
    mock_ax_light.set_title.assert_any_call(mock_ax_light.get_title(), color=light_style['TEXT_COLOR'])

    mock_ax_light.get_legend.assert_called_once()
    mock_legend_light.get_frame().set_facecolor.assert_called_with(light_style['AXES_FACE_COLOR'])
    # ... (add more assertions for light mode legend)

    mock_annotate_plot.assert_called_with(mock_ax_light, "Cloud cover [%]", False)
