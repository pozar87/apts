import pytest
import datetime
from unittest.mock import patch, MagicMock
import pytz
import pandas as pd
from apts.observations import Observation
from apts.weather import Weather
from tests import setup_place


@pytest.fixture
def mock_weather_instance():
    with patch("apts.weather.get_weather_settings") as mock_settings:
        mock_settings.return_value = ("pirateweather", "dummy_key")
        with patch("apts.weather.PirateWeather") as mock_pw:
            mock_provider = mock_pw.return_value
            mock_data = pd.DataFrame(
                {
                    "time": [
                        datetime.datetime(2023, 6, 1, 12, tzinfo=pytz.utc),
                        datetime.datetime(2023, 6, 1, 13, tzinfo=pytz.utc),
                    ],
                    "cloudCover": [10.0, 20.0],
                    "precipProbability": [0.0, 0.0],
                    "windSpeed": [5.0, 6.0],
                    "temperature": [15.0, 16.0],
                    "visibility": [20.0, 20.0],
                    "moonIllumination": [10.0, 11.0],
                    "fog": [0.0, 0.0],
                    "aurora": [0.0, 0.0],
                    "precipIntensity": [0.0, 0.0],
                }
            )
            mock_provider.download_data.return_value = mock_data
            weather = Weather(lat=0, lon=0, local_timezone=pytz.utc)
            weather.data = mock_data
            return weather


@pytest.mark.parametrize(
    "plot_method, weather_method",
    [
        ("plot_clouds", "plot_clouds"),
        ("plot_precipitation", "plot_precipitation"),
        ("plot_temperature", "plot_temperature"),
        ("plot_wind", "plot_wind"),
        ("plot_visibility", "plot_visibility"),
        ("plot_moon_illumination", "plot_moon_illumination"),
        ("plot_fog", "plot_fog"),
        ("plot_aurora", "plot_aurora"),
    ],
)
def test_individual_weather_plots(mock_weather_instance, plot_method, weather_method):
    place = setup_place()
    place.weather = mock_weather_instance
    obs = Observation(place=place, equipment=MagicMock())

    with patch.object(mock_weather_instance, weather_method) as mock_method:
        mock_ax = MagicMock()
        mock_method.return_value = mock_ax

        with (
            patch("apts.plotting.weather.mark_observation") as mock_mark_obs,
            patch("apts.plotting.weather.mark_good_conditions") as mock_mark_good,
        ):
            getattr(obs, plot_method)()

            mock_method.assert_called_once()
            mock_mark_obs.assert_called_once()
            mock_mark_good.assert_called_once()

    with (
        patch.object(mock_weather_instance, "plot_clouds_summary") as mock_clouds_sum,
        patch.object(
            mock_weather_instance, "plot_precipitation_type_summary"
        ) as mock_precip_sum,
        patch.object(
            mock_weather_instance, "plot_pressure_and_ozone"
        ) as mock_press_ozone,
    ):
        obs.plot_clouds_summary()
        mock_clouds_sum.assert_called_once()

        obs.plot_precipitation_type_summary()
        mock_precip_sum.assert_called_once()

        obs.plot_pressure_and_ozone()
        mock_press_ozone.assert_called_once()
