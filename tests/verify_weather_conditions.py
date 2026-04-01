import unittest
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import pytz
from unittest.mock import MagicMock, patch

from apts.observations import Observation
from apts.conditions import Conditions
from apts.place import Place
from apts.equipment import Equipment

class TestWeatherConditionsVerification(unittest.TestCase):
    def setUp(self):
        # Mock Place
        self.place = MagicMock(spec=Place)
        self.place.name = "Test Place"
        self.place.lat = 0.9  # ~51.5 deg
        self.place.lon = 0.0
        self.place.lat_decimal = 51.5
        self.place.lon_decimal = 0.0
        self.place.local_timezone = pytz.UTC
        self.place.elevation = 100

        from apts.cache import get_timescale
        self.place.ts = get_timescale()
        self.place.date = self.place.ts.utc(2024, 1, 1)

        # Mock Equipment
        self.equipment = MagicMock(spec=Equipment)

        # Default start/stop
        self.start = datetime(2024, 1, 1, 20, 0, tzinfo=pytz.UTC)
        self.stop = datetime(2024, 1, 2, 4, 0, tzinfo=pytz.UTC)

        self.place.sunset_time.return_value = self.start
        self.place.sunrise_time.return_value = self.stop

        # Mock observer for moon condition check
        self.place.observer = MagicMock()
        self.place.moon = MagicMock()

    def _create_observation(self, conditions=None):
        if conditions is None:
            conditions = Conditions()

        with patch('apts.observations.Observation._normalize_dates', side_effect=lambda x, y: (x, y)):
            # Pass target_date to avoid legacy behavior that might use place.date in tricky ways
            obs = Observation(self.place, self.equipment, conditions, target_date=datetime(2024, 1, 1))
            # Re-ensure they are exactly what we want, though constructor should have set them
            obs.start = self.start
            obs.stop = self.stop
            obs.time_limit = self.stop
            return obs

    def _get_mock_weather_data(self, **kwargs):
        # Default good weather
        data = {
            'time': [self.start + timedelta(hours=i) for i in range(5)],
            'cloudCover': [0.0] * 5,
            'precipProbability': [0.0] * 5,
            'precipIntensity': [0.0] * 5,
            'windSpeed': [0.0] * 5,
            'temperature': [15.0] * 5,
            'visibility': [20.0] * 5,
            'fog': [0.0] * 5,
            'aurora': [100.0] * 5, # High aurora as default
            'seeing': [1.0] * 5,
            'sqm': [21.0] * 5,
            'moonIllumination': [0.0] * 5,
            'moon_altitude': [-10.0] * 5 # Moon down
        }
        for key, value in kwargs.items():
            if key in data:
                data[key] = value
        return pd.DataFrame(data)

    @patch('apts.observations.get_moon_illumination', return_value=0)
    def test_all_conditions_checked(self, mock_moon_illum):
        # We want to verify that if ANY condition is violated, the hour is marked as "not good"
        # and a reason is provided.

        test_cases = [
            ('cloudCover', 50, 'max_clouds', 20, "Cloud cover", False),
            ('cloudCover', 20, 'max_clouds', 20, "Cloud cover", True), # Boundary is good
            ('precipProbability', 10, 'max_precipitation_probability', 5, "Precipitation probability", False),
            ('precipProbability', 5, 'max_precipitation_probability', 5, "Precipitation probability", True), # Boundary is good
            ('precipIntensity', 10, 'max_precipitation_intensity', 5, "Precipitation intensity", False),
            ('precipIntensity', 5, 'max_precipitation_intensity', 5, "Precipitation intensity", True), # Boundary is good
            ('windSpeed', 20, 'max_wind', 10, "Wind speed", False),
            ('windSpeed', 10, 'max_wind', 10, "Wind speed", True), # Boundary is good
            ('temperature', -5, 'min_temperature', 0, "Temperature", False),
            ('temperature', 0, 'min_temperature', 0, "Temperature", True), # Boundary is good
            ('temperature', 30, 'max_temperature', 25, "Temperature", False),
            ('temperature', 25, 'max_temperature', 25, "Temperature", True), # Boundary is good
            ('visibility', 5, 'min_visibility', 10, "Visibility", False),
            ('visibility', 10, 'min_visibility', 10, "Visibility", True), # Boundary is good
            ('fog', 10, 'max_fog', 5, "Fog", False),
            ('fog', 5, 'max_fog', 5, "Fog", True), # Boundary is good
            ('seeing', 4.0, 'max_seeing', 2.5, "Seeing", False),
            ('seeing', 2.5, 'max_seeing', 2.5, "Seeing", True), # Boundary is good
            ('sqm', 17.0, 'min_sqm', 19.0, "Sky brightness", False),
            ('sqm', 19.0, 'min_sqm', 19.0, "Sky brightness", True), # Boundary is good
            ('aurora', 10, 'min_aurora', 50, "Aurora", False),
            ('aurora', 50, 'min_aurora', 50, "Aurora", True), # Boundary is good
        ]

        for col, val, cond_attr, cond_val, reason_part, expected_good in test_cases:
            with self.subTest(condition=cond_attr, value=val):
                cond_kwargs = {cond_attr: cond_val}
                conditions = Conditions(**cond_kwargs)
                obs = self._create_observation(conditions)

                # Setup weather data with one test hour
                weather_data = self._get_mock_weather_data()
                weather_data.loc[2, col] = val

                self.place.weather = MagicMock()
                self.place.weather.get_critical_data.return_value = weather_data

                analysis = obs.get_weather_analysis()

                self.assertEqual(len(analysis), 5)
                self.assertTrue(analysis[0]['is_good_hour'], f"Hour 0 should be good for {cond_attr}")

                if expected_good:
                    self.assertTrue(analysis[2]['is_good_hour'], f"Hour 2 with {val} should be good for {cond_attr}. Reasons: {analysis[2]['reasons']}")
                else:
                    self.assertFalse(analysis[2]['is_good_hour'], f"Hour 2 with {val} should be bad for {cond_attr}")
                    reasons = analysis[2]['reasons']
                    self.assertTrue(any(reason_part in r for r in reasons), f"Reason for {cond_attr} not found in {reasons}")

    @patch('apts.observations.get_moon_illumination', return_value=80)
    def test_moon_condition(self, mock_moon_illum):
        # Moon is 80% illuminated
        conditions = Conditions(max_moon_illumination=50)
        obs = self._create_observation(conditions)

        # Weather data with Moon UP in hour 2
        weather_data = self._get_mock_weather_data(moonIllumination=[80.0]*5)
        weather_data.loc[2, 'moon_altitude'] = 30.0

        self.place.weather = MagicMock()
        self.place.weather.get_critical_data.return_value = weather_data

        # Mock the skyfield call in _is_moon_condition_met
        mock_alt = MagicMock()
        mock_alt.degrees = [30.0] * 10
        self.place.observer.at.return_value.observe.return_value.apparent.return_value.altaz.return_value = (mock_alt, None, None)

        # Ensure _is_moon_condition_met returns False
        self.assertFalse(obs._is_moon_condition_met(conditions))

        # Now check get_weather_analysis
        analysis = obs.get_weather_analysis()
        if not analysis:
            # If it returns [], it's because _is_moon_condition_met returned False and get_weather_analysis skips
            self.assertEqual(analysis, [])
        else:
            self.assertFalse(analysis[2]['is_good_hour'], "Hour 2 should be bad due to Moon")
            self.assertTrue(any("Moon illumination" in r for r in analysis[2]['reasons']))

if __name__ == '__main__':
    unittest.main()
