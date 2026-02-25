import pytz
from unittest.mock import patch
from requests_mock import ANY
from apts.weather import Weather

STORMGLASS_MOCK = {
    "hours": [
        {
            "time": "2022-08-26T12:00:00+00:00",
            "airTemperature": {"sg": 20},
            "pressure": {"sg": 1013},
            "cloudCover": {"sg": 10},
            "dewPointTemperature": {"sg": 10},
            "humidity": {"sg": 50},
            "precipitation": {"sg": 0.1},
            "visibility": {"sg": 10},
            "windSpeed": {"sg": 5},
            "gust": {"sg": 7},
            "rain": {"sg": 0.1},
            "snow": {"sg": 0},
        }
    ],
    "meta": {"dailyQuota": 50, "lat": 0, "lng": 0, "requestCount": 1},
}


@patch("apts.weather.get_weather_settings")
def test_stormglass_provider(mock_get_weather_settings, requests_mock):
    mock_get_weather_settings.return_value = ("stormglass", "dummy_key")
    requests_mock.get(ANY, json=STORMGLASS_MOCK)

    weather = Weather(lat=0, lon=0, local_timezone=pytz.utc)

    assert weather.data is not None
    assert not weather.data.empty

    data = weather.data.iloc[0]

    assert data["temperature"] == 20
    assert data["apparentTemperature"] == 20
    assert data["dewPoint"] == 10
    assert data["pressure"] == 1013
    assert data["cloudCover"] == 10
    assert data["visibility"] == 10
    assert data["precipIntensity"] == 0.1
    assert data["windSpeed"] == 18.0  # 5 m/s * 3.6 = 18 km/h
    assert data["precipType"] == "rain"
    assert data["fog"] == 0.0


def test_stormglass_precip_type_snow(requests_mock):
    mock_response = {
        "hours": [
            {
                "time": "2022-08-26T12:00:00+00:00",
                "precipitation": {"sg": 0.5},
                "rain": {"sg": 0.1},
                "snow": {"sg": 0.4},
            }
        ]
    }
    with patch(
        "apts.weather.get_weather_settings", return_value=("stormglass", "dummy_key")
    ):
        requests_mock.get(ANY, json=mock_response)
        weather = Weather(lat=0, lon=0, local_timezone=pytz.utc)
        assert weather.data.iloc[0]["precipType"] == "snow"


def test_stormglass_precip_type_none(requests_mock):
    mock_response = {
        "hours": [
            {
                "time": "2022-08-26T12:00:00+00:00",
                "precipitation": {"sg": 0},
                "rain": {"sg": 0},
                "snow": {"sg": 0},
            }
        ]
    }
    with patch(
        "apts.weather.get_weather_settings", return_value=("stormglass", "dummy_key")
    ):
        requests_mock.get(ANY, json=mock_response)
        weather = Weather(lat=0, lon=0, local_timezone=pytz.utc)
        assert weather.data.iloc[0]["precipType"] == "none"
