import pandas as pd
from apts.weather_providers import _get_aurora_df, PirateWeather
from unittest.mock import patch, MagicMock
import json
import pytz


@patch("apts.weather_providers.get_session")
def test_get_aurora_df(mock_get_session):
    # Mock the session and its get method
    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.text = json.dumps(
        {
            "Forecast Time": "2024-01-01T12:00:00Z",
            "coordinates": [
                [-120, 30, 10],
                [-118.24, 34.05, 50],
                [-110, 40, 20],
            ],
        }
    )
    mock_response.raise_for_status.return_value = None
    mock_session.get.return_value.__enter__.return_value = mock_response
    mock_get_session.return_value = mock_session

    # Call the function
    lat = 34.05
    lon = -118.24
    local_timezone = "America/Los_Angeles"
    aurora_df = _get_aurora_df(lat, lon, local_timezone)

    # Assertions
    assert not aurora_df.empty
    assert "aurora" in aurora_df.columns
    assert aurora_df["aurora"].iloc[0] == 50
    assert aurora_df["time"].iloc[0].strftime(
        "%Y-%m-%d %H:%M:%S"
    ) == "2024-01-01 04:00:00"  # Check timezone conversion


def test_enrich_with_aurora_data_handles_dtype_mismatch():
    # Create a sample weather DataFrame with second precision, which mimics the original bug scenario
    weather_data = {
        "time": pd.to_datetime(["2024-01-01 12:00:00", "2024-01-01 13:00:00"]).tz_localize("UTC")
    }
    weather_df = pd.DataFrame(weather_data)
    weather_df['time'] = weather_df['time'].astype("datetime64[s, UTC]")

    # Create a mock aurora DataFrame, which defaults to nanosecond precision
    aurora_data = {
        "time": pd.to_datetime(["2024-01-01 12:30:00"]).tz_localize("UTC"),
        "aurora": [75],
    }
    aurora_df_mock = pd.DataFrame(aurora_data)

    # Patch the function that fetches aurora data to return our mock DataFrame
    with patch("apts.weather_providers._get_aurora_df", return_value=aurora_df_mock):
        # Instantiate a concrete WeatherProvider
        provider = PirateWeather(api_key="dummy", lat=0, lon=0, local_timezone=pytz.utc)

        # Call the method that performs the merge
        enriched_df = provider._enrich_with_aurora_data(weather_df)

        # Assert that the 'aurora' column was successfully added and filled
        assert "aurora" in enriched_df.columns
        assert not enriched_df["aurora"].isna().all()
        assert enriched_df["aurora"].iloc[0] == 75
        assert enriched_df["aurora"].iloc[1] == 75
