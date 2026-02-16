import pytest
import datetime
import pytz
import json
import re
from unittest.mock import patch, MagicMock
from requests_mock import ANY
from apts.weather_providers import StormGlass, Meteoblue, VisualCrossing
from datetime import timezone

@pytest.fixture(autouse=True)
def mock_aurora():
    with patch("apts.weather_providers._get_aurora_df") as m:
        m.return_value = MagicMock(empty=True)
        yield m

def test_stormglass_api_url_params(requests_mock):
    api_key = "test_key"
    lat, lon = 52.2297, 21.0122
    local_timezone = pytz.timezone("Europe/Warsaw")
    hours = 24

    # Mock weather response
    requests_mock.get(re.compile("api.stormglass.io"), json={"hours": [{"time": "2024-01-01T00:00:00Z"}]})

    provider = StormGlass(api_key, lat, lon, local_timezone)
    provider.download_data(hours=hours)

    # Find the StormGlass request
    weather_request = next(r for r in requests_mock.request_history if "stormglass.io" in r.url)
    url = weather_request.url

    assert f"lat={lat}" in url
    assert f"lng={lon}" in url
    assert "start=" in url
    assert "end=" in url
    assert f"key={api_key}" in url

def test_meteoblue_api_url_params(requests_mock):
    api_key = "test_key"
    lat, lon = 52.2297, 21.0122
    local_timezone = pytz.timezone("Europe/Warsaw")
    hours = 36 # Should result in 2 days

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
            "sealevelpressure": [1013],
        }
    }

    # Mock weather response
    requests_mock.get(re.compile("my.meteoblue.com"), json=METEOBLUE_MOCK)

    provider = Meteoblue(api_key, lat, lon, local_timezone)
    provider.download_data(hours=hours)

    # Find the Meteoblue request
    weather_request = next(r for r in requests_mock.request_history if "meteoblue.com" in r.url)
    url = weather_request.url

    assert f"lat={lat}" in url
    assert f"lon={lon}" in url
    assert "forecast_days=2" in url

def test_visualcrossing_api_url_params(requests_mock):
    api_key = "test_key"
    lat, lon = 52.2297, 21.0122
    local_timezone = pytz.timezone("Europe/Warsaw")
    hours = 48

    VISUAL_CROSSING_MOCK = {
        "days": [
            {
                "hours": [
                    {
                        "datetimeEpoch": 1624000000,
                        "conditions": "Clear",
                        "preciptype": ["rain"],
                        "precipprob": 0.2,
                        "precip": 0.1,
                        "temp": 20,
                        "feelslike": 21,
                        "dew": 10,
                        "humidity": 0.5,
                        "windspeed": 18,
                        "cloudcover": 10,
                        "visibility": 10,
                        "pressure": 1013,
                        "ozone": 300,
                    }
                ]
            }
        ]
    }

    # Mock weather response
    requests_mock.get(re.compile("weather.visualcrossing.com"), json=VISUAL_CROSSING_MOCK)

    provider = VisualCrossing(api_key, lat, lon, local_timezone)
    provider.download_data(hours=hours)

    # Find the VisualCrossing request
    weather_request = next(r for r in requests_mock.request_history if "visualcrossing.com" in r.url)
    url = weather_request.url

    assert f"next{hours}hours" in url

def test_weather_data_filtering():
    # Mock data with more than 48 hours
    now = datetime.datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
    times = [(now + datetime.timedelta(hours=i)).isoformat() for i in range(72)]

    mock_response = {
        "hours": [{"time": t, "airTemperature": {"sg": 20}} for t in times]
    }

    with (
        patch("apts.weather_providers.get_session") as mock_session
    ):
        mock_resp = MagicMock()
        mock_resp.text = json.dumps(mock_response)
        mock_resp.status_code = 200
        mock_session.return_value.get.return_value.__enter__.return_value = mock_resp

        provider = StormGlass("key", 0, 0, timezone.utc)
        df = provider.download_data(hours=48)

        # Should have around 49 rows (depends on exact current time vs mocked times)
        # But definitely should be limited
        assert len(df) <= 49
        assert df.time.max() <= now + datetime.timedelta(hours=48)
