import pytest
import datetime
import unittest
from unittest.mock import patch, MagicMock
from apts.weather import Weather
from apts.constants.graphconstants import get_plot_style
from . import setup_place
from requests_mock import ANY
from apts.observations import Observation
from apts.conditions import Conditions
import pytz

# MOCK DATA
PIRATE_WEATHER_MOCK = {
    "hourly": {
        "data": [
            {
                "time": 1624000000, "summary": "Clear", "precipType": "rain", "precipProbability": 0.2,
                "precipIntensity": 0.1, "temperature": 20, "apparentTemperature": 21, "dewPoint": 10,
                "humidity": 0.5, "windSpeed": 5, "cloudCover": 0.1, "visibility": 10,
                "pressure": 1013, "ozone": 300,
            }
        ]
    }
}

VISUAL_CROSSING_MOCK = {
    "days": [
        {
            "hours": [
                {
                    "datetimeEpoch": 1624000000, "conditions": "Clear", "preciptype": ["rain"], "precipprob": 0.2,
                    "precip": 0.1, "temp": 20, "feelslike": 21, "dew": 10,
                    "humidity": 0.5, "windspeed": 18, "cloudcover": 10, "visibility": 10,
                    "pressure": 1013, "ozone": 300,
                }
            ]
        }
    ]
}

OPEN_WEATHER_MAP_MOCK = {
    "hourly": [
        {
            "dt": 1624000000, "temp": 20, "feels_like": 21, "pressure": 1013, "humidity": 50,
            "dew_point": 10, "clouds": 10, "visibility": 10000, "wind_speed": 5,
            "weather": [{"main": "Rain", "description": "light rain"}], "pop": 0.2,
            "rain": {"1h": 0.1}
        }
    ]
}

METEOBLUE_MOCK = {
    "data_1h": {
        "time": ["2022-08-26 12:00"],
        "pictocode": [3],
        "snowfraction": [0],
        "precipitation_probability": [20],
        "precipitation": [0.1],
        "temperature": [20],
        "felttemperature": [21],
        "dewpointtemperature": [10],
        "relativehumidity": [50],
        "windspeed": [5],
        "totalcloudcover": [10],
        "visibility": [10000],
        "sealevelpressure": [1013]
    }
}


@pytest.mark.parametrize(
    "provider_name, mock_response",
    [
        ("pirateweather", PIRATE_WEATHER_MOCK),
        ("visualcrossing", VISUAL_CROSSING_MOCK),
        ("openweathermap", OPEN_WEATHER_MAP_MOCK),
        ("meteoblue", METEOBLUE_MOCK),
    ],
)
@patch('apts.weather.get_weather_settings')
@pytest.mark.xfail(reason="Caching interferes with requests-mock")
def test_weather_providers(mock_get_weather_settings, requests_mock, provider_name, mock_response):
    mock_get_weather_settings.return_value = (provider_name, "dummy_key")
    requests_mock.get(ANY, json=mock_response)

    weather = Weather(lat=0, lon=0, local_timezone=pytz.utc)

    assert weather.data is not None
    assert not weather.data.empty

    data = weather.data.iloc[0]

    assert data['temperature'] == 20
    assert data['apparentTemperature'] == 21
    assert data['dewPoint'] == 10
    assert data['pressure'] == 1013
    assert data['cloudCover'] == 10
    assert data['visibility'] == 10
    assert data['precipProbability'] == 20
    assert data['precipIntensity'] == 0.1

    if provider_name == 'pirateweather':
        assert data['windSpeed'] == 5
        assert data['ozone'] == 300
    elif provider_name == 'visualcrossing':
        assert round(data['windSpeed']) == 18 # It's already in km/h
        assert data['ozone'] == 300
    elif provider_name == 'openweathermap':
        assert data['windSpeed'] == 18.0 # 5 m/s * 3.6 = 18 km/h
        assert data['ozone'] == 'none' # Not provided by OWM
    elif provider_name == 'meteoblue':
        assert data['windSpeed'] == 5
        assert data['ozone'] == 'none'


@pytest.mark.parametrize(
    "provider_name, mock_response",
    [
        ("pirateweather", {"hourly": {"data": [{"time": 1624000000, "cloudCover": 50, "summary": "Cloudy"}]}}),
        ("visualcrossing", {"days": [{"hours": [{"datetimeEpoch": 1624000000, "cloudcover": 50, "conditions": "Cloudy"}]}]}),
        ("openweathermap", {"hourly": [{"dt": 1624000000, "clouds": 50, "weather": [{"main": "Clouds", "description": "Cloudy"}]}]}),
    ],
)
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
@patch("apts.weather.get_weather_settings")
@pytest.mark.xfail(reason="Caching interferes with requests-mock")
def test_plot_clouds_dark_mode_styles(
    mock_get_weather_settings,
    mock_get_dark_mode,
    mock_df_plot,
    mock_annotate_plot,
    requests_mock,
    provider_name,
    mock_response,
    override_value,
    global_setting,
    expected_effective_dark_mode,
):
    mock_get_weather_settings.return_value = (provider_name, "dummy_key")
    requests_mock.get(ANY, json=mock_response)
    weather = Weather(lat=0, lon=0, local_timezone=pytz.utc)

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


@pytest.mark.xfail(reason="Caching interferes with requests-mock")
@patch("apts.weather.get_weather_settings")
def test_get_critical_data_all_hours(mock_get_weather_settings, requests_mock):
    mock_get_weather_settings.return_value = ("pirateweather", "dummy_key")
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
    weather = Weather(lat=0, lon=0, local_timezone=pytz.utc)

    start_time = datetime.datetime.fromtimestamp(1624000000, tz=pytz.utc)
    stop_time = start_time + datetime.timedelta(hours=36)

    critical_data = weather.get_critical_data(start_time, stop_time)

    assert not critical_data.empty
    assert critical_data.time.min() >= start_time
    assert critical_data.time.max() <= stop_time
    assert len(critical_data) == 37


@pytest.mark.xfail(reason="Caching interferes with requests-mock")
def test_weather_provider_key_error(requests_mock):
    # This test checks if a malformed response from a provider is handled gracefully.
    # It assumes the provider's `download_data` will return an empty DataFrame.
    mock_response_missing_key = {"wrong_key": {}}

    with patch('apts.weather.get_weather_settings', return_value=('pirateweather', 'dummy_key')):
        requests_mock.get(ANY, json=mock_response_missing_key)
        weather = Weather(lat=0, lon=0, local_timezone=pytz.utc)
        assert weather.data.empty


@patch("apts.weather.get_weather_settings")
def test_plot_weather_calls_sub_plots(mock_get_weather_settings, requests_mock):
    mock_get_weather_settings.return_value = ("pirateweather", "dummy_key")
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

    mock_weather_instance = Weather(lat=0, lon=0, local_timezone=pytz.utc)

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
            "apts.plot.pyplot.subplots",
            return_value=(MagicMock(), MagicMock(shape=(4, 2))),
        ) as mock_subplots,
        patch(
            "apts.plot._mark_observation"
        ) as mock_mark_observation,
        patch(
            "apts.plot._mark_good_conditions"
        ) as mock_mark_good_conditions,
        patch(
            "apts.plot.plot_sun_and_moon_path"
        ),
        patch.object(mock_weather_instance, "plot_moon_phase") as mock_plot_moon_phase,
    ):
        fig = obs.plot_weather()

        mock_subplots.assert_called_once_with(nrows=5, ncols=2, figsize=(13, 22))

        mock_plot_clouds.assert_called_once()
        mock_plot_clouds_summary.assert_called_once()
        mock_plot_precipitation.assert_called_once()
        mock_plot_precipitation_type_summary.assert_called_once()
        mock_plot_temperature.assert_called_once()
        mock_plot_wind.assert_called_once()
        mock_plot_pressure_and_ozone.assert_called_once()
        mock_plot_visibility.assert_called_once()
        mock_plot_moon_phase.assert_called_once()

        assert mock_mark_observation.call_count >= 1
        assert mock_mark_good_conditions.call_count >= 1

        assert fig is not None
        assert isinstance(fig, MagicMock)


@pytest.mark.xfail(reason="Caching interferes with requests-mock")
@patch("apts.weather.get_weather_settings")
def test_plot_moon_phase(mock_get_weather_settings, requests_mock):
    mock_get_weather_settings.return_value = ("pirateweather", "dummy_key")
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

    weather = Weather(lat=0, lon=0, local_timezone=pytz.utc)
    with patch("apts.weather.Utils.annotate_plot") as mock_annotate_plot:
        ax = weather.plot_moon_phase()
        assert ax is not None
        mock_annotate_plot.assert_called_once_with(
            ax, "Moon Phase [%]", False
        )


if __name__ == "__main__":
    unittest.main()