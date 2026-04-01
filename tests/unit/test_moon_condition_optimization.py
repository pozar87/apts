
import unittest
import datetime
from unittest.mock import MagicMock, patch
import pandas as pd
from apts.observations import Observation
from apts.conditions import Conditions
from tests import setup_observation

class TestMoonConditionOptimization(unittest.TestCase):
    def setUp(self):
        # Start patcher to avoid Redis connection errors
        self.get_cache_settings_patcher = patch("apts.config.get_cache_settings")
        self.mock_get_cache_settings = self.get_cache_settings_patcher.start()
        self.mock_get_cache_settings.return_value = {
            "backend": "memory",
            "expire_after": 300,
            "redis_location": None,
        }
        self.addCleanup(self.get_cache_settings_patcher.stop)

        self.obs = setup_observation()
        self.test_tz = datetime.timezone.utc
        self.base_date = pd.Timestamp("2024-01-01", tz=self.test_tz)
        
        # Mock place
        self.mock_place = MagicMock()
        self.mock_place.local_timezone = self.test_tz
        self.mock_place.ts = self.obs.place.ts # Keep real timescale for linspace
        self.mock_place.date = self.base_date
        
        # Mock observer
        self.mock_observer = MagicMock()
        self.mock_place.observer = self.mock_observer
        
        # Mock moon
        self.mock_place.moon = MagicMock()
        
        self.obs.place = self.mock_place
        self.obs.start = self.base_date.replace(hour=18, minute=0)
        self.obs.stop = self.base_date.replace(hour=22, minute=0)
        
        self.obs.conditions = Conditions()
        self.obs.conditions.max_moon_illumination = 50

        # Mock weather
        self.mock_place.weather = None
        self.mock_place.get_weather = MagicMock()

        # Default altaz return value
        self.mock_altaz = MagicMock()
        self.mock_observer.at.return_value.observe.return_value.apparent.return_value.altaz.return_value = (self.mock_altaz, None, None)
        self.mock_altaz.degrees = [10.0] * 10

    @patch("apts.observations.get_moon_illumination")
    def test_weather_analysis_skipped_when_moon_too_bright(self, mock_get_illumination):
        # Arrange: Moon is 80% illuminated (> 50% limit)
        mock_get_illumination.return_value = 80.0
        
        # Act
        results = self.obs.get_weather_analysis()
        
        # Assert
        self.assertEqual(results, [])
        self.mock_place.get_weather.assert_not_called()

    @patch("apts.observations.get_moon_illumination")
    def test_weather_analysis_not_skipped_when_moon_is_dim(self, mock_get_illumination):
        # Arrange: Moon is 20% illuminated (< 50% limit)
        mock_get_illumination.return_value = 20.0
        
        # Mock weather data
        mock_df = pd.DataFrame([{
            "time": self.obs.start,
            "cloudCover": 0,
            "precipIntensity": 0,
            "precipProbability": 0,
            "windSpeed": 0,
            "temperature": 15,
            "visibility": 100,
            "moonIllumination": 20,
            "fog": 0,
            "seeing": 1.0,
            "sqm": 21.0
        }])
        
        # Mock get_weather to set weather
        def set_weather(*args, **kwargs):
            self.mock_place.weather = MagicMock()
            self.mock_place.weather.get_critical_data.return_value = mock_df
        self.mock_place.get_weather.side_effect = set_weather
        
        # Adjust altaz degrees to match mock_df length (1)
        self.mock_altaz.degrees = [10.0]
        
        # Act
        results = self.obs.get_weather_analysis()
        
        # Assert
        self.assertNotEqual(results, [])
        self.mock_place.get_weather.assert_called()

    @patch("apts.observations.get_moon_illumination")
    def test_weather_analysis_forced_when_moon_too_bright(self, mock_get_illumination):
        # Arrange: Moon is 80% illuminated (> 50% limit)
        mock_get_illumination.return_value = 80.0
        
        # Mock weather data
        mock_df = pd.DataFrame([{
            "time": self.obs.start,
            "cloudCover": 0,
            "precipIntensity": 0,
            "precipProbability": 0,
            "windSpeed": 0,
            "temperature": 15,
            "visibility": 100,
            "moonIllumination": 80,
            "fog": 0,
            "seeing": 1.0,
            "sqm": 21.0
        }])
        
        # Mock get_weather to set weather
        def set_weather(*args, **kwargs):
            self.mock_place.weather = MagicMock()
            self.mock_place.weather.get_critical_data.return_value = mock_df
        self.mock_place.get_weather.side_effect = set_weather
        
        # Adjust altaz degrees to match mock_df length (1)
        self.mock_altaz.degrees = [10.0]
        
        # Act
        results = self.obs.get_weather_analysis(force=True)
        
        # Assert
        self.assertNotEqual(results, [])
        self.mock_place.get_weather.assert_called()

    @patch("apts.observations.get_moon_illumination")
    def test_is_weather_good_returns_false_when_moon_too_bright(self, mock_get_illumination):
        # Arrange: Moon is 80% illuminated (> 50% limit)
        mock_get_illumination.return_value = 80.0
        
        # Act
        result = self.obs.is_weather_good()
        
        # Assert
        self.assertFalse(result)
        self.mock_place.get_weather.assert_not_called()
