import logging
import pytz
from unittest.mock import patch
from apts.weather import Weather
from requests.exceptions import ConnectionError

def test_weather_provider_leak_on_connection_error(requests_mock, caplog):
    # Set up the mock to raise a ConnectionError
    # The URL contains the API key
    api_key = "SECRET_API_KEY_12345"
    provider_name = "pirateweather"

    # We need to mock get_weather_settings to return our provider and secret key
    with patch("apts.weather.get_weather_settings", return_value=(provider_name, api_key)):
        # Configure requests_mock to raise ConnectionError for the PirateWeather URL
        url = f"https://api.pirateweather.net/forecast/{api_key}/0,0?units=si"
        requests_mock.get(url, exc=ConnectionError(f"Connection failed for {url}"))

        with caplog.at_level(logging.ERROR):
            Weather(lat=0, lon=0, local_timezone=pytz.utc, provider_name=provider_name, api_key=api_key)

            # The exception should be caught and logged by apts now
            # And it should be masked.

            # Check that the secret is NOT in any log record
            for record in caplog.records:
                assert api_key not in record.message

            # Check that the masked version IS in the logs
            # PirateWeather uses _log_download_error which uses mask_text
            # mask_text("...SECRET_API_KEY_12345...", "SECRET_API_KEY_12345")
            # -> "...SECR...2345..." (from mask_secret)
            assert "SECR...2345" in caplog.text
