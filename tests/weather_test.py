import pytest
import json
import re
import datetime
import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from apts.weather import Weather
from apts.constants.graphconstants import get_plot_style
from . import setup_place
from requests_mock import ANY
from apts.observations import Observation  # Import Observation
from apts.conditions import Conditions  # Import Conditions
import pytz  # Import pytz


def test_weather_successful_request(requests_mock):
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
                    "ozone": 300,
                }
            ]
        }
    }

    requests_mock.get(ANY, json=mock_response)

    p = setup_place()
    p.get_weather()

    assert p.weather is not None

    weather_data = p.weather.data
    assert not weather_data.empty
    assert weather_data["temperature"].iloc[0] == 20
    assert weather_data["cloudCover"].iloc[0] == 10
    assert weather_data["precipProbability"].iloc[0] == 20


def test_weather_api_error(requests_mock):
    requests_mock.get(ANY, status_code=500)

    p = setup_place()
    with pytest.raises(json.decoder.JSONDecodeError):
        p.get_weather()


@pytest.mark.parametrize(
    "override_value, global_setting, expected_effective_dark_mode",
    [
        (True, False, True),
        (False, True, False),
        (None, True, True),
        (None, False, False),
    ],
)
@patch("apts.weather.Utils.annotate_plot")
@patch("pandas.DataFrame.plot")
@patch("apts.weather.get_dark_mode")
def test_plot_clouds_dark_mode_styles(
    mock_get_dark_mode,
    mock_df_plot,
    mock_annotate_plot,
    requests_mock,
    override_value,
    global_setting,
    expected_effective_dark_mode,
):
    mock_api_response = {
        "hourly": {
            "data": [{"time": 1624000000, "cloudCover": 0.5, "summary": "Cloudy"}]
        }
    }
    requests_mock.get(ANY, json=mock_api_response)
    weather = Weather(lat=0, lon=0, local_timezone=datetime.timezone.utc)

    mock_get_dark_mode.return_value = global_setting
    expected_style = get_plot_style(expected_effective_dark_mode)

    mock_ax = MagicMock()
    mock_fig = MagicMock()
    mock_ax.figure = mock_fig
    mock_fig_patch = MagicMock()
    mock_fig.patch = mock_fig_patch
    mock_df_plot.return_value = mock_ax
    mock_legend = MagicMock()
    mock_ax.get_legend.return_value = mock_legend
    mock_legend_frame = MagicMock()
    mock_legend.get_frame.return_value = mock_legend_frame
    mock_legend_title = MagicMock()
    mock_legend.get_title.return_value = mock_legend_title
    mock_legend_text_item = MagicMock()
    mock_legend.get_texts.return_value = [mock_legend_text_item]
    mock_ax.get_title.return_value = "Clouds"

    ax_returned = weather.plot_clouds(hours=1, dark_mode_override=override_value)

    assert ax_returned == mock_ax
    mock_df_plot.assert_called_once()

    if expected_effective_dark_mode:
        mock_fig_patch.set_facecolor.assert_called_with("#1C1C3A")
        mock_ax.set_facecolor.assert_called_with("#2A004F")
        mock_ax.set_title.assert_any_call("Clouds", color="#FFFFFF")
        if mock_ax.get_legend() is not None and mock_legend_frame is not None:
            mock_legend_frame.set_facecolor.assert_called_with("#2A004F")
            mock_legend_frame.set_edgecolor.assert_called_with("#CCCCCC")
            mock_legend_text_item.set_color.assert_called_with("#FFFFFF")
    else:
        mock_fig_patch.set_facecolor.assert_called_with(
            expected_style["FIGURE_FACE_COLOR"]
        )
        mock_ax.set_facecolor.assert_called_with(expected_style["AXES_FACE_COLOR"])
        mock_ax.set_title.assert_any_call("Clouds", color=expected_style["TEXT_COLOR"])
        if mock_ax.get_legend() is not None and mock_legend_frame is not None:
            mock_legend_frame.set_facecolor.assert_called_with(
                expected_style["AXES_FACE_COLOR"]
            )
            mock_legend_frame.set_edgecolor.assert_called_with(
                expected_style["AXIS_COLOR"]
            )
            mock_legend_text_item.set_color.assert_called_with(
                expected_style["TEXT_COLOR"]
            )

    if mock_ax.get_legend() is not None:
        mock_ax.get_legend.assert_called()

    mock_annotate_plot.assert_called_with(
        mock_ax, "Cloud cover [%]", expected_effective_dark_mode
    )

    mock_df_plot.reset_mock()
    mock_annotate_plot.reset_mock()
    mock_get_dark_mode.reset_mock()


def test_get_critical_data_all_hours(requests_mock):
    mock_api_response = {
        "hourly": {
            "data": [
                {
                    "time": 1624000000 + i * 3600,
                    "cloudCover": 0.5,
                    "precipProbability": 0.1,
                    "windSpeed": 10,
                    "temperature": 20,
                }
                for i in range(48)
            ]
        }
    }
    requests_mock.get(ANY, json=mock_api_response)
    weather = Weather(lat=0, lon=0, local_timezone=datetime.timezone.utc)

    start_time = datetime.datetime.fromtimestamp(1624000000, tz=datetime.timezone.utc)
    stop_time = start_time + datetime.timedelta(hours=36)

    critical_data = weather.get_critical_data(start_time, stop_time)

    assert not critical_data.empty
    assert critical_data.time.min() >= start_time
    assert critical_data.time.max() <= stop_time
    assert len(critical_data) == 37


def test_download_data_key_error_handling(requests_mock):
    mock_response_missing_key = {"hourly": {"no_data_here": []}}
    requests_mock.get(ANY, json=mock_response_missing_key)
    weather = Weather(lat=0, lon=0, local_timezone=datetime.timezone.utc)
    df = weather.download_data()
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert all(
        col in df.columns
        for col in [
            "time",
            "summary",
            "precipType",
            "precipProbability",
            "precipIntensity",
            "temperature",
            "apparentTemperature",
            "dewPoint",
            "humidity",
            "windSpeed",
            "cloudCover",
            "visibility",
            "pressure",
            "ozone",
        ]
    )


def test_plot_weather_calls_sub_plots(requests_mock):
    mock_api_response = {
        "hourly": {
            "data": [
                {
                    "time": 1624000000 + i * 3600,
                    "cloudCover": 0.1,
                    "precipProbability": 0.05,
                    "windSpeed": 5,
                    "temperature": 15,
                    "summary": "Clear",
                    "precipType": "none",
                    "apparentTemperature": 14,
                    "dewPoint": 10,
                    "humidity": 0.7,
                    "visibility": 10,
                    "pressure": 1012,
                    "ozone": 300,
                }
                for i in range(24)
            ]
        }
    }

    requests_mock.get(ANY, json=mock_api_response)

    mock_weather_instance = Weather(lat=0, lon=0, local_timezone=datetime.timezone.utc)

    # Use setup_place to get a real Place object, then mock its weather attribute and get_weather method
    real_place = setup_place()  # This creates a Place object
    real_place.weather = mock_weather_instance
    real_place.get_weather = MagicMock(return_value=None)  # Mock the method

    mock_equipment = MagicMock()
    mock_conditions = Conditions()

    # Pass the real_place to the Observation constructor
    obs = Observation(
        place=real_place, equipment=mock_equipment, conditions=mock_conditions
    )

    # Set up start and time_limit for the observation
    obs.start = datetime.datetime.fromtimestamp(1624000000, tz=datetime.timezone.utc)
    obs.time_limit = obs.start + datetime.timedelta(hours=24)
    obs.stop = obs.time_limit

    with (
        patch.object(mock_weather_instance, "plot_clouds") as mock_plot_clouds,
        patch.object(
            mock_weather_instance, "plot_clouds_summary"
        ) as mock_plot_clouds_summary,
        patch.object(
            mock_weather_instance, "plot_precipitation"
        ) as mock_plot_precipitation,
        patch.object(
            mock_weather_instance, "plot_precipitation_type_summary"
        ) as mock_plot_precipitation_type_summary,
        patch.object(
            mock_weather_instance, "plot_temperature"
        ) as mock_plot_temperature,
        patch.object(mock_weather_instance, "plot_wind") as mock_plot_wind,
        patch.object(
            mock_weather_instance, "plot_pressure_and_ozone"
        ) as mock_plot_pressure_and_ozone,
        patch.object(mock_weather_instance, "plot_visibility") as mock_plot_visibility,
        patch(
            "apts.observations.pyplot.subplots",
            return_value=(MagicMock(), MagicMock(shape=(4, 2))),
        ) as mock_subplots,
        patch(
            "apts.observations.Observation._mark_observation"
        ) as mock_mark_observation,
        patch(
            "apts.observations.Observation._mark_good_conditions"
        ) as mock_mark_good_conditions,
        patch(
            "apts.observations.Observation.plot_sun_and_moon_path"
        ) as mock_plot_sun_and_moon_path,
    ):
        fig = obs.plot_weather()

        mock_subplots.assert_called_once_with(nrows=4, ncols=2, figsize=(13, 18))

        mock_plot_clouds.assert_called_once()
        mock_plot_clouds_summary.assert_called_once()
        mock_plot_precipitation.assert_called_once()
        mock_plot_precipitation_type_summary.assert_called_once()
        mock_plot_temperature.assert_called_once()
        mock_plot_wind.assert_called_once()
        mock_plot_pressure_and_ozone.assert_called_once()
        mock_plot_visibility.assert_called_once()

        assert mock_mark_observation.call_count >= 1
        assert mock_mark_good_conditions.call_count >= 1

        assert fig is not None
        assert isinstance(fig, MagicMock)


if __name__ == "__main__":
    unittest.main()
