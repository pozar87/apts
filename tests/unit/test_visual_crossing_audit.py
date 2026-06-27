import pytest
import pytz
import pandas as pd
from datetime import datetime, timezone
from unittest.mock import patch
from apts.weather.providers import VisualCrossing

@pytest.fixture
def visual_crossing_response():
    return {
        "days": [
            {
                "hours": [
                    {
                        "datetimeEpoch": 1624000000,
                        "conditions": "Clear",
                        "preciptype": ["rain", "snow"],
                        "precipprob": 20.5,
                        "precip": 0.1,
                        "temp": 20.0,
                        "feelslike": 21.0,
                        "dew": 10.0,
                        "humidity": 50.0,
                        "windspeed": 18.0,
                        "cloudcover": 10.0,
                        "visibility": 15.0,
                        "pressure": 1013.0,
                        "ozone": 300.0,
                    }
                ]
            }
        ]
    }

@patch("apts.weather.providers.base._get_aurora_df")
def test_visual_crossing_unit_conversions(mock_aurora, visual_crossing_response, requests_mock):
    mock_aurora.return_value = pd.DataFrame([[datetime.now(timezone.utc), 0]], columns=["time", "aurora"])

    api_key = "test_key"
    lat, lon = 52.2297, 21.0122
    local_timezone = pytz.timezone("Europe/Warsaw")

    requests_mock.get(
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/52.2297,21.0122/next48hours?unitGroup=metric&key=test_key&include=hours",
        json=visual_crossing_response
    )

    provider = VisualCrossing(api_key, lat, lon, local_timezone)
    df = provider.download_data(hours=48)

    assert len(df) == 1
    # precipProbability should stay 20.5 (Visual Crossing returns it in percent)
    assert df.iloc[0]["precipProbability"] == 20.5
    # humidity should be 0.5 (Visual Crossing returns it in percent, we want 0-1)
    assert df.iloc[0]["humidity"] == 0.5
    # cloudCover should stay 10.0 (Visual Crossing returns it in percent)
    assert df.iloc[0]["cloudCover"] == 10.0
    # precipType should be a joined string
    assert df.iloc[0]["precipType"] == "rain, snow"
    # fog should be calculated from visibility
    # visibility is 15.0, so fog should be (10 - 10) * 10 = 0
    assert df.iloc[0]["fog"] == 0.0

def test_visual_crossing_empty_response(requests_mock):
    api_key = "test_key"
    lat, lon = 52.2297, 21.0122
    local_timezone = pytz.timezone("Europe/Warsaw")

    requests_mock.get(
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/52.2297,21.0122/next48hours?unitGroup=metric&key=test_key&include=hours",
        json={"days": []}
    )

    provider = VisualCrossing(api_key, lat, lon, local_timezone)
    df = provider.download_data(hours=48)

    assert df.empty
    assert list(df.columns) == provider.REQUIRED_COLUMNS

def test_visual_crossing_missing_hours(requests_mock):
    api_key = "test_key"
    lat, lon = 52.2297, 21.0122
    local_timezone = pytz.timezone("Europe/Warsaw")

    requests_mock.get(
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/52.2297,21.0122/next48hours?unitGroup=metric&key=test_key&include=hours",
        json={"days": [{"temp": 20}]} # Missing 'hours'
    )

    provider = VisualCrossing(api_key, lat, lon, local_timezone)
    df = provider.download_data(hours=48)

    assert df.empty

def test_visual_crossing_error_response(requests_mock):
    api_key = "test_key"
    lat, lon = 52.2297, 21.0122
    local_timezone = pytz.timezone("Europe/Warsaw")

    requests_mock.get(
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/52.2297,21.0122/next48hours?unitGroup=metric&key=test_key&include=hours",
        status_code=401,
        text="Unauthorized"
    )

    provider = VisualCrossing(api_key, lat, lon, local_timezone)
    df = provider.download_data(hours=48)

    assert df.empty
