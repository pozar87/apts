import pandas as pd
from apts.weather_providers import _get_aurora_df
from unittest.mock import patch, MagicMock
import json


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
