import unittest
import requests_mock
import pandas as pd
from datetime import datetime, timezone
from apts.weather.providers.open_weather_map import OpenWeatherMap

class TestOpenWeatherMap(unittest.TestCase):
    def setUp(self):
        self.api_key = "test_api_key"
        self.lat = 52.2
        self.lon = 21.0
        self.tz = timezone.utc
        self.provider = OpenWeatherMap(self.api_key, self.lat, self.lon, self.tz)

    @requests_mock.Mocker()
    def test_download_data_success(self, m):
        # Mock response data for OpenWeatherMap
        mock_json = {
            "lat": 52.2,
            "lon": 21.0,
            "timezone": "UTC",
            "timezone_offset": 0,
            "hourly": [
                {
                    "dt": int(datetime.now(timezone.utc).timestamp()),
                    "temp": 20.5,
                    "feels_like": 19.8,
                    "pressure": 1015,
                    "humidity": 60,
                    "dew_point": 12.5,
                    "clouds": 20,
                    "visibility": 10000,
                    "wind_speed": 3.5,
                    "pop": 0.1,
                    "weather": [
                        {
                            "id": 801,
                            "main": "Clouds",
                            "description": "few clouds",
                            "icon": "02d"
                        }
                    ],
                    "rain": { "1h": 0.5 }
                }
            ]
        }

        url = self.provider.API_URL.format(apikey=self.api_key, lat=self.lat, lon=self.lon)
        m.get(url, json=mock_json)

        # Mock aurora data
        m.get("https://services.swpc.noaa.gov/json/ovation_aurora_latest.json",
              json={"Forecast Time": "2023-06-05T12:00:00Z", "coordinates": [[21.0, 52.2, 5.0]]})

        df = self.provider.download_data(hours=48)

        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty, "DataFrame should not be empty")
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["summary"], "few clouds")
        self.assertEqual(df.iloc[0]["precipType"], "Clouds")
        self.assertEqual(df.iloc[0]["precipIntensity"], 0.5)
        self.assertEqual(df.iloc[0]["temperature"], 20.5)
        self.assertEqual(df.iloc[0]["humidity"], 0.6) # 60 / 100
        self.assertEqual(df.iloc[0]["windSpeed"], 3.5 * 3.6) # 3.5 m/s to km/h
        self.assertEqual(df.iloc[0]["visibility"], 10.0) # 10000 m to km
        self.assertEqual(df.iloc[0]["precipProbability"], 10.0) # 0.1 * 100

    @requests_mock.Mocker()
    def test_download_data_error(self, m):
        url = self.provider.API_URL.format(apikey=self.api_key, lat=self.lat, lon=self.lon)
        m.get(url, status_code=401)

        df = self.provider.download_data(hours=48)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.empty)

if __name__ == "__main__":
    unittest.main()
