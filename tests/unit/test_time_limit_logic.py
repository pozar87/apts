import unittest
from unittest.mock import MagicMock, patch
import pandas as pd
import datetime
import numpy as np
from apts.observations import Observation
from apts.conditions import Conditions

class TestObservationTimeLimitLogic(unittest.TestCase):
    def setUp(self):
        self.place = MagicMock()
        self.place.local_timezone = datetime.timezone.utc
        self.place.ts = MagicMock()
        # Mock from_datetimes to return something that we can use to match calls if needed
        self.place.ts.from_datetimes.side_effect = lambda args_list: MagicMock(length=len(args_list))

        self.equipment = MagicMock()
        self.conditions = Conditions()

        # Setup observation with fixed start/stop
        self.start = pd.Timestamp("2024-01-01 18:00:00", tz="UTC")
        self.stop = pd.Timestamp("2024-01-02 06:00:00", tz="UTC")

        with patch("apts.observations.Observation._normalize_dates", return_value=(self.start, self.stop)):
            self.obs = Observation(self.place, self.equipment, self.conditions)
            self.obs.start = self.start
            self.obs.stop = self.stop

        # Mock weather data
        self.weather_data = pd.DataFrame({
            "time": [
                pd.Timestamp("2024-01-01 18:00:00", tz="UTC"),
                pd.Timestamp("2024-01-01 21:00:00", tz="UTC"),
                pd.Timestamp("2024-01-02 03:00:00", tz="UTC"),
            ],
            "cloudCover": [0, 0, 0],
            "temperature": [20, 20, 20],
            "windSpeed": [0, 0, 0],
            "precipProbability": [0, 0, 0],
            "visibility": [20, 20, 20],
            "moonIllumination": [0, 0, 0],
            "precipIntensity": [0, 0, 0]
        })
        self.obs.place.weather = MagicMock()
        self.obs.place.weather.get_critical_data.return_value = self.weather_data

    @patch("apts.observations.weather.get_moon_illumination", return_value=0)
    def test_get_hourly_weather_analysis_with_time_limit(self, mock_moon_illum):
        # Set time limit to 22:00
        self.obs.time_limit = pd.Timestamp("2024-01-01 22:00:00", tz="UTC")

        # Mock moon altitude to return correct number of points based on input
        def altaz_side_effect(*args, **kwargs):
            return (MagicMock(degrees=np.array([10, 10])), None, None)

        self.obs.place.observer.at.return_value.observe.return_value.apparent.return_value.altaz.side_effect = altaz_side_effect

        analysis = self.obs.get_hourly_weather_analysis()

        # Should only have 2 points (18:00 and 21:00)
        self.assertEqual(len(analysis), 2)
        self.assertEqual(analysis[0]["time"], pd.Timestamp("2024-01-01 18:00:00", tz="UTC"))
        self.assertEqual(analysis[1]["time"], pd.Timestamp("2024-01-01 21:00:00", tz="UTC"))

    @patch("apts.observations.weather.get_moon_illumination", return_value=0)
    def test_get_hourly_weather_analysis_without_time_limit(self, mock_moon_illum):
        # Set time limit to None
        self.obs.time_limit = None

        # Mock moon altitude to return 3 points
        def altaz_side_effect(*args, **kwargs):
            return (MagicMock(degrees=np.array([10, 10, 10])), None, None)

        self.obs.place.observer.at.return_value.observe.return_value.apparent.return_value.altaz.side_effect = altaz_side_effect

        analysis = self.obs.get_hourly_weather_analysis()

        # Should have all 3 points
        self.assertEqual(len(analysis), 3)

if __name__ == "__main__":
    unittest.main()
