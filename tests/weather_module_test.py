import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from datetime import datetime, timezone
from apts.weather import Weather
import matplotlib.pyplot as plt

class TestWeatherModule(unittest.TestCase):
    @patch("apts.weather.get_weather_settings")
    @patch("apts.weather.PirateWeather")
    def setUp(self, mock_pirate_weather, mock_get_weather_settings):
        # Mock weather provider
        self.mock_provider = MagicMock()
        self.mock_provider.download_data.return_value = pd.DataFrame({
            'time': pd.to_datetime([datetime(2023, 1, 1, 1, tzinfo=timezone.utc), datetime(2023, 1, 1, 2, tzinfo=timezone.utc)]),
            'cloudCover': [10, 20],
            'precipIntensity': [0.1, 0.2],
            'precipProbability': [0.5, 0.6],
            'precipType': ['rain', 'rain'],
            'summary': ['cloudy', 'cloudy'],
            'temperature': [5, 6],
            'apparentTemperature': [4, 5],
            'dewPoint': [3, 4],
            'windSpeed': [15, 20],
            'pressure': [1010, 1012],
            'ozone': [300, 301],
            'visibility': [10, 12],
            'fog': [5, 10]
        })
        mock_pirate_weather.return_value = self.mock_provider

        # Mock settings
        mock_get_weather_settings.return_value = ("pirateweather", "dummy_key")

        # Initialize Weather class
        self.weather = Weather(lat=52.2, lon=21.0, local_timezone='UTC')

    def test_initialization(self):
        self.assertIsNotNone(self.weather.data)
        self.assertTrue("moonIllumination" in self.weather.data.columns)
        self.assertTrue("moonWaxing" in self.weather.data.columns)

    def test_filter_data(self):
        filtered_data = self.weather._filter_data(["cloudCover"])
        self.assertEqual(list(filtered_data.columns), ["time", "cloudCover"])
        self.assertEqual(len(filtered_data), 2)

    def test_get_critical_data(self):
        start = datetime(2023, 1, 1, 0, tzinfo=timezone.utc)
        stop = datetime(2023, 1, 1, 1, 30, tzinfo=timezone.utc)
        critical_data = self.weather.get_critical_data(start, stop)
        self.assertEqual(len(critical_data), 1)
        self.assertEqual(critical_data.iloc[0]['cloudCover'], 10)

    def test_plot_clouds(self):
        ax = self.weather.plot_clouds()
        self.assertIsNotNone(ax)
        plt.close(ax.figure)

    def test_plot_precipitation(self):
        ax = self.weather.plot_precipitation()
        self.assertIsNotNone(ax)
        plt.close(ax.figure)

    def test_plot_temperature(self):
        ax = self.weather.plot_temperature()
        self.assertIsNotNone(ax)
        plt.close(ax.figure)

    def test_plot_wind(self):
        ax = self.weather.plot_wind()
        self.assertIsNotNone(ax)
        plt.close(ax.figure)

    def test_plot_pressure_and_ozone(self):
        ax = self.weather.plot_pressure_and_ozone()
        self.assertIsNotNone(ax)
        plt.close(ax.figure)

    def test_plot_visibility(self):
        ax = self.weather.plot_visibility()
        self.assertIsNotNone(ax)
        plt.close(ax.figure)

    def test_plot_fog(self):
        ax = self.weather.plot_fog()
        self.assertIsNotNone(ax)
        plt.close(ax.figure)

    def test_plot_moon_illumination(self):
        ax = self.weather.plot_moon_illumination()
        self.assertIsNotNone(ax)
        plt.close(ax.figure)

    def test_plot_clouds_summary(self):
        fig, ax = plt.subplots()
        returned_ax = self.weather.plot_clouds_summary(ax=ax)
        self.assertIsNotNone(returned_ax)
        plt.close(fig)

    def test_plot_precipitation_type_summary(self):
        fig, ax = plt.subplots()
        returned_ax = self.weather.plot_precipitation_type_summary(ax=ax)
        self.assertIsNotNone(returned_ax)
        plt.close(fig)


if __name__ == "__main__":
    unittest.main()
