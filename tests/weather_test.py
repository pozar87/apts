import pytest
import json
import requests_mock
import datetime # Added
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


@pytest.mark.parametrize(
    "override_value, global_setting, expected_effective_dark_mode",
    [
        (True, False, True),  # Override True, Global False -> Dark
        (False, True, False), # Override False, Global True -> Light
        (None, True, True),   # Override None, Global True -> Dark
        (None, False, False), # Override None, Global False -> Light
    ]
)
@patch('apts.weather.Utils.annotate_plot')
@patch('pandas.DataFrame.plot') # Mocking the plot method of DataFrame
@patch('apts.weather.get_dark_mode')
def test_plot_clouds_dark_mode_styles(
    mock_get_dark_mode,
    mock_df_plot,
    mock_annotate_plot,
    requests_mock, # pytest fixture
    override_value,
    global_setting,
    expected_effective_dark_mode
):
    # --- Setup Weather instance and mock data ---
    mock_api_response = {
        "hourly": {
            "data": [{"time": 1624000000, "cloudCover": 0.5, "summary": "Cloudy"}] # Added summary for potential pie chart
        }
    }
    requests_mock.get(requests_mock.ANY, json=mock_api_response)
    weather = Weather(lat=0, lon=0, local_timezone=datetime.timezone.utc) # Changed

    # Set global dark mode mock based on scenario
    mock_get_dark_mode.return_value = global_setting
    expected_style = get_plot_style(expected_effective_dark_mode)

    # Mock the Axes object that pandas.DataFrame.plot() would return
    # A new mock_ax is implicitly created for each parametrized run by pytest if it were a fixture.
    # Here, we create it manually to ensure it's fresh.
    mock_ax = MagicMock()
    mock_fig = MagicMock()
    mock_ax.figure = mock_fig
    mock_df_plot.return_value = mock_ax

    # Mock legend on the axes
    mock_legend = MagicMock()
    mock_ax.get_legend.return_value = mock_legend
    mock_legend.get_frame.return_value = MagicMock()
    mock_legend.get_title.return_value = MagicMock()
    mock_legend.get_texts.return_value = [MagicMock()]

    # Call the method to be tested with the override value
    ax_returned = weather.plot_clouds(hours=1, dark_mode_override=override_value)

    assert ax_returned == mock_ax
    mock_df_plot.assert_called_once()

    # Check that figure and axes face colors are set when plot creates them
    # (plot_clouds creates the fig/ax if not passed in)
    mock_fig.patch.set_facecolor.assert_called_with(expected_style['FIGURE_FACE_COLOR'])
    mock_ax.set_facecolor.assert_called_with(expected_style['AXES_FACE_COLOR'])

    # Configure mock_ax.get_title before the call to plot_clouds
    # The title is set by data.plot(title="Clouds")
    mock_ax.get_title.return_value = "Clouds"
    mock_ax.set_title.assert_any_call("Clouds", color=expected_style['TEXT_COLOR'])

    if mock_ax.get_legend() is not None : # Check if legend was actually created by the plot
        mock_ax.get_legend.assert_called() # Should be called if legend exists
        mock_legend.get_frame().set_facecolor.assert_called_with(expected_style['AXES_FACE_COLOR'])
        mock_legend.get_frame().set_edgecolor.assert_called_with(expected_style['AXIS_COLOR'])
        for text_mock in mock_legend.get_texts():
            text_mock.set_color.assert_called_with(expected_style['TEXT_COLOR'])

    mock_annotate_plot.assert_called_with(mock_ax, "Cloud cover [%]", expected_effective_dark_mode)

    # Important: Reset mocks if they are reused across parameterize iterations in a way that accumulates calls.
    # Pytest typically isolates test runs, but explicit mock_df_plot.reset_mock() might be needed if issues arise.
    # For this structure, mock_df_plot is patched at function level, so it's reset for each parameter set.
    mock_df_plot.reset_mock() # Reset for the next iteration of parametrize
    mock_annotate_plot.reset_mock() # Reset for the next iteration
    mock_get_dark_mode.reset_mock() # Reset for the next iteration
