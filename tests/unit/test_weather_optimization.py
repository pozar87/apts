import unittest
from unittest.mock import MagicMock, patch
import pandas as pd
import datetime
from apts.observations import Observation
from apts.place import Place
from apts.conditions import Conditions
from apts.weather_providers import Meteoblue

class TestWeatherOptimization(unittest.TestCase):
    def setUp(self):
        # Mock Place
        self.place = MagicMock(spec=Place)
        self.place.lat_decimal = 52.0
        self.place.lon_decimal = 21.0
        self.place.local_timezone = datetime.timezone.utc
        self.place.ts = MagicMock()
        self.place.ts.utc.side_effect = lambda dt: dt
        self.place.ts.from_datetime.side_effect = lambda dt: MagicMock()
        self.place.observer = MagicMock()
        self.place.moon = MagicMock()
        self.place.date = datetime.datetime(2025, 1, 1, 12, 0, tzinfo=datetime.timezone.utc)
        self.place.weather = None

        # Avoid TypeError in Observation.__init__
        self.place.sunset_time.return_value = datetime.datetime(2025, 1, 1, 18, 0, tzinfo=datetime.timezone.utc)
        self.place.sunrise_time.return_value = datetime.datetime(2025, 1, 2, 6, 0, tzinfo=datetime.timezone.utc)

        # Mock Equipment
        self.equipment = MagicMock()

    @patch("apts.observations.get_moon_illumination")
    def test_moon_pre_check_skips_fetch(self, mock_illum):
        # Setup: Moon is too bright and always up
        mock_illum.return_value = 90.0
        conditions = Conditions(max_moon_illumination=50, min_weather_goodness=80)

        obs = Observation(self.place, self.equipment, conditions=conditions)
        obs.start = datetime.datetime(2025, 1, 1, 20, 0, tzinfo=datetime.timezone.utc)
        obs.stop = datetime.datetime(2025, 1, 1, 23, 0, tzinfo=datetime.timezone.utc)
        obs.effective_date = MagicMock()

        # Mock moon altitude to be always positive (e.g., 10 degrees)
        mock_alt = MagicMock()
        mock_alt.degrees = [10.0] * 10
        self.place.observer.at.return_value.observe.return_value.apparent.return_value.altaz.return_value = (mock_alt, None, None)

        # is_weather_good should return False and NOT call get_weather
        result = obs.is_weather_good()

        self.assertFalse(result)
        self.place.get_weather.assert_not_called()

    @patch("apts.observations.get_moon_illumination")
    def test_moon_pre_check_allows_fetch_if_moon_is_down(self, mock_illum):
        # Setup: Moon is bright but always down
        mock_illum.return_value = 90.0
        conditions = Conditions(max_moon_illumination=50, min_weather_goodness=80)

        obs = Observation(self.place, self.equipment, conditions=conditions)
        obs.start = datetime.datetime(2025, 1, 1, 20, 0, tzinfo=datetime.timezone.utc)
        obs.stop = datetime.datetime(2025, 1, 1, 23, 0, tzinfo=datetime.timezone.utc)
        obs.effective_date = MagicMock()

        # Mock moon altitude to be always negative (e.g., -10 degrees)
        mock_alt = MagicMock()
        mock_alt.degrees = [-10.0] * 10
        self.place.observer.at.return_value.observe.return_value.apparent.return_value.altaz.return_value = (mock_alt, None, None)

        # Mock _compute_weather_goodness to avoid issues when get_weather is called
        obs._compute_weather_goodness = MagicMock(return_value=100.0)

        # is_weather_good should call get_weather
        obs.is_weather_good()

        self.place.get_weather.assert_called_once()

    @patch("apts.weather_providers.get_session")
    @patch("apts.weather_providers._get_aurora_df")
    def test_meteoblue_optimization_skips_basic(self, mock_aurora_df, mock_get_session):
        # Setup Meteoblue provider
        provider = Meteoblue("api_key", 52.0, 21.0, datetime.timezone.utc)
        mock_aurora_df.return_value = pd.DataFrame()

        # Mock response for CLOUDS call: 100% clouds
        mock_resp_clouds = MagicMock()
        mock_resp_clouds.text = '{"data_1h": {"time": ["2025-01-01 20:00"], "totalcloudcover": [100], "visibility": [1000]}}'
        mock_resp_clouds.status_code = 200

        mock_get_session.return_value.get.return_value.__enter__.return_value = mock_resp_clouds

        conditions = Conditions(max_clouds=20, min_weather_goodness=80)
        window = (
            datetime.datetime(2025, 1, 1, 20, 0, tzinfo=datetime.timezone.utc),
            datetime.datetime(2025, 1, 1, 21, 0, tzinfo=datetime.timezone.utc)
        )

        with patch('apts.weather_providers.datetime') as mock_datetime:
             mock_datetime.now.return_value = datetime.datetime(2025, 1, 1, 19, 0, tzinfo=datetime.timezone.utc)
             mock_datetime.combine = datetime.datetime.combine
             mock_datetime.timedelta = datetime.timedelta
             mock_datetime.timezone = datetime.timezone
             provider.download_data(hours=48, conditions=conditions, observation_window=window)

        # Should have called get() only ONCE (for clouds-1h)
        self.assertEqual(mock_get_session.return_value.get.call_count, 1)
        self.assertIn("clouds-1h", mock_get_session.return_value.get.call_args[0][0])

        # Verify that aurora enrichment was also skipped
        mock_aurora_df.assert_not_called()

    @patch("apts.weather_providers.get_session")
    @patch("apts.weather_providers._get_aurora_df")
    def test_meteoblue_optimization_calls_basic_when_good(self, mock_aurora_df, mock_get_session):
        # Setup Meteoblue provider
        provider = Meteoblue("api_key", 52.0, 21.0, datetime.timezone.utc)
        mock_aurora_df.return_value = pd.DataFrame()

        # Mock response for CLOUDS call: clear sky
        mock_resp_clouds = MagicMock()
        mock_resp_clouds.text = '{"data_1h": {"time": ["2025-01-01 20:00"], "totalcloudcover": [0], "visibility": [20000]}}'
        mock_resp_clouds.status_code = 200

        # Mock response for BASIC call
        mock_resp_basic = MagicMock()
        mock_resp_basic.text = '{"data_1h": {"time": ["2025-01-01 20:00"], "precipitation": [0.0], "precipitation_probability": [0], "windspeed": [5], "temperature": [10]}}'
        mock_resp_basic.status_code = 200

        # Set up a side effect for get() itself to return different context managers
        mock_cm_clouds = MagicMock()
        mock_cm_clouds.__enter__.return_value = mock_resp_clouds
        mock_cm_basic = MagicMock()
        mock_cm_basic.__enter__.return_value = mock_resp_basic

        mock_get_session.return_value.get.side_effect = [mock_cm_clouds, mock_cm_basic]

        conditions = Conditions(max_clouds=20, min_weather_goodness=80)
        window = (
            datetime.datetime(2025, 1, 1, 20, 0, tzinfo=datetime.timezone.utc),
            datetime.datetime(2025, 1, 1, 21, 0, tzinfo=datetime.timezone.utc)
        )

        with patch('apts.weather_providers.datetime') as mock_datetime:
             mock_datetime.now.return_value = datetime.datetime(2025, 1, 1, 19, 0, tzinfo=datetime.timezone.utc)
             mock_datetime.combine = datetime.datetime.combine
             mock_datetime.timedelta = datetime.timedelta
             mock_datetime.timezone = datetime.timezone
             provider.download_data(hours=48, conditions=conditions, observation_window=window)

        # Should have called get() TWICE
        self.assertEqual(mock_get_session.return_value.get.call_count, 2)
        self.assertIn("clouds-1h", mock_get_session.return_value.get.call_args_list[0][0][0])
        self.assertIn("basic-1h", mock_get_session.return_value.get.call_args_list[1][0][0])

        # Verify aurora was called
        mock_aurora_df.assert_called_once()

if __name__ == "__main__":
    unittest.main()
