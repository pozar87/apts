import pytest
import datetime
from unittest.mock import patch, MagicMock
import pytz
import pandas as pd
from apts.observations import Observation
from apts.conditions import Conditions
from apts.weather import Weather
from tests import setup_place


@pytest.fixture
def mock_weather_data(mock_provider):
    mock_data = pd.DataFrame(
        {
            "time": [
                datetime.datetime(2023, 6, 1, 12 + i, tzinfo=pytz.utc) for i in range(5)
            ],
            "cloudCover": [10.0, 30.0, 10.0, 50.0, 10.0],
            "precipProbability": [0.0, 0.0, 0.0, 0.0, 0.0],
            "windSpeed": [5.0, 5.0, 5.0, 5.0, 5.0],
            "temperature": [15.0, 15.0, 15.0, 15.0, 15.0],
            "visibility": [20.0, 20.0, 20.0, 20.0, 20.0],
            "moonIllumination": [10.0, 10.0, 10.0, 10.0, 10.0],
            "fog": [0.0, 0.0, 0.0, 0.0, 0.0],
            "aurora": [0.0, 0.0, 0.0, 0.0, 0.0],
            "precipIntensity": [0.0, 0.0, 0.0, 0.0, 0.0],
        }
    )
    mock_provider.download_data.return_value = mock_data
    weather = Weather(lat=0, lon=0, local_timezone=pytz.utc)
    # Weather init might have recalculated moonIllumination, so we re-set it to our desired test value
    weather.data = mock_data.copy()
    weather.data["moonIllumination"] = 10.0
    return weather


@pytest.fixture
def mock_provider():
    with patch("apts.weather_providers.Meteoblue") as mock:
        yield mock.return_value


def test_get_weather_analysis_with_custom_conditions(mock_weather_data):
    place = setup_place()
    place.weather = mock_weather_data

    # Standard conditions: max_clouds = 20
    standard_conditions = Conditions(max_clouds=20)
    obs = Observation(
        place=place, equipment=MagicMock(), conditions=standard_conditions
    )
    # Mocking observation window for simplicity
    obs.start = datetime.datetime(2023, 6, 1, 12, tzinfo=pytz.utc)
    obs.stop = datetime.datetime(2023, 6, 1, 16, tzinfo=pytz.utc)
    obs.time_limit = obs.stop

    analysis = obs.get_weather_analysis()
    # 2nd and 4th entries have clouds 30 and 50, so they should be "bad"
    assert analysis[0]["is_good_hour"] is True
    assert analysis[1]["is_good_hour"] is False  # clouds 30 > 20
    assert analysis[2]["is_good_hour"] is True
    assert analysis[3]["is_good_hour"] is False  # clouds 50 > 20

    # Custom conditions: max_clouds = 40
    custom_conditions = Conditions(max_clouds=40)
    analysis_custom = obs.get_weather_analysis(conditions=custom_conditions)

    assert analysis_custom[0]["is_good_hour"] is True
    assert analysis_custom[1]["is_good_hour"] is True  # clouds 30 < 40
    assert analysis_custom[2]["is_good_hour"] is True
    assert analysis_custom[3]["is_good_hour"] is False  # clouds 50 > 40


def test_is_weather_good_with_custom_conditions(mock_weather_data):
    place = setup_place()
    place.weather = mock_weather_data

    # Standard: min_weather_goodness = 80
    # In 5 hours, if 3 are good, that's 60%, which is < 80.
    standard_conditions = Conditions(max_clouds=20, min_weather_goodness=80)
    obs = Observation(
        place=place, equipment=MagicMock(), conditions=standard_conditions
    )
    obs.start = datetime.datetime(2023, 6, 1, 12, tzinfo=pytz.utc)
    obs.stop = datetime.datetime(2023, 6, 1, 16, tzinfo=pytz.utc)
    obs.time_limit = obs.stop

    assert obs.is_weather_good() is False

    # Custom: max_clouds = 60 -> all 5 hours good -> 100% > 80
    custom_conditions = Conditions(max_clouds=60, min_weather_goodness=80)
    assert obs.is_weather_good(conditions=custom_conditions) is True
