import pytest
import pytz
import re
from unittest.mock import patch, MagicMock
from apts.weather_providers import StormGlass


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
    requests_mock.get(
        re.compile("api.stormglass.io"),
        json={"hours": [{"time": "2024-01-01T00:00:00Z"}]},
    )

    provider = StormGlass(api_key, lat, lon, local_timezone)
    provider.download_data(hours=hours)

    # Find the StormGlass request
    weather_request = next(
        r for r in requests_mock.request_history if "stormglass.io" in r.url
    )
    url = weather_request.url

    assert f"lat={lat}" in url
    assert f"lng={lon}" in url
    assert "start=" in url
    assert "end=" in url
    assert f"key={api_key}" in url
