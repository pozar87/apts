import unittest
from datetime import datetime, timezone
from unittest.mock import MagicMock

import pandas as pd

from apts.conditions import Conditions
from apts.observations.weather.calculations import (
    calculate_moon_altitudes,
    check_moon_condition,
    compute_weather_goodness_ratio,
    prepare_weather_dataframe,
)


class WeatherObservationsCalculationsTestCase(unittest.TestCase):

    def setUp(self):
        self.conditions = Conditions()

    def test_calculate_moon_altitudes(self):
        mock_place = MagicMock()
        mock_ts = MagicMock()
        mock_place.ts = mock_ts

        mock_alt = MagicMock()
        mock_alt.degrees = [15.0, 25.0]
        mock_place.observer.at.return_value.observe.return_value.apparent.return_value.altaz.return_value = (
            mock_alt,
            None,
            None,
        )

        times = [
            datetime(2025, 1, 1, 20, 0, tzinfo=timezone.utc),
            datetime(2025, 1, 1, 21, 0, tzinfo=timezone.utc),
        ]
        result = calculate_moon_altitudes(mock_place, times)

        self.assertIsInstance(result, pd.Series)
        self.assertEqual(list(result), [15.0, 25.0])

    def test_check_moon_condition_no_window(self):
        mock_place = MagicMock()
        res = check_moon_condition(None, None, mock_place, self.conditions)
        self.assertTrue(res)

    def test_compute_weather_goodness_ratio_cached(self):
        cached = [
            {"is_good_hour": True},
            {"is_good_hour": False},
            {"is_good_hour": True},
            {"is_good_hour": True},
        ]
        ratio = compute_weather_goodness_ratio(
            pd.DataFrame(), self.conditions, cached_analysis=cached
        )
        self.assertEqual(ratio, 75.0)

    def test_compute_weather_goodness_ratio_empty_df(self):
        ratio = compute_weather_goodness_ratio(pd.DataFrame(), self.conditions)
        self.assertEqual(ratio, 0.0)

    def test_prepare_weather_dataframe_empty(self):
        mock_place = MagicMock()
        mock_place.weather = None
        df = prepare_weather_dataframe(
            mock_place,
            datetime(2025, 1, 1, 20, 0),
            datetime(2025, 1, 1, 22, 0),
        )
        self.assertTrue(df.empty)


if __name__ == "__main__":
    unittest.main()
