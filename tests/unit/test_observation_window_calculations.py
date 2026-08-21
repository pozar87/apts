import unittest
from datetime import datetime, time, timedelta
from unittest.mock import MagicMock

from apts.constants.twilight import Twilight
from apts.observations.window_calculations import (
    apply_start_time_override,
    calculate_time_limit,
    find_best_observation_window,
    normalize_window,
)


class TestObservationWindowCalculations(unittest.TestCase):
    def test_normalize_window(self):
        start = datetime(2025, 1, 1, 22, 0)
        stop = datetime(2025, 1, 1, 4, 0)
        norm_start, norm_stop = normalize_window(start, stop)
        self.assertEqual(norm_start, start)
        self.assertEqual(norm_stop, datetime(2025, 1, 2, 4, 0))

    def test_apply_start_time_override_string(self):
        start = datetime(2025, 1, 1, 20, 0)
        res = apply_start_time_override(start, "21:30:00")
        self.assertEqual(res, datetime(2025, 1, 1, 21, 30, 0))

    def test_apply_start_time_override_time_object(self):
        start = datetime(2025, 1, 1, 20, 0)
        res = apply_start_time_override(start, time(22, 15, 0))
        self.assertEqual(res, datetime(2025, 1, 1, 22, 15, 0))

    def test_calculate_time_limit(self):
        start = datetime(2025, 1, 1, 20, 0)
        stop = datetime(2025, 1, 2, 5, 0)

        # Case 1: max_return provided
        limit = calculate_time_limit(start, stop, "23:00")
        self.assertEqual(limit, datetime(2025, 1, 1, 23, 0, 0))

        # Case 2: max_return provided overnight
        limit_overnight = calculate_time_limit(start, stop, "02:00")
        self.assertEqual(limit_overnight, datetime(2025, 1, 2, 2, 0, 0))

        # Case 3: max_return None -> defaults to stop
        limit_default = calculate_time_limit(start, stop, None)
        self.assertEqual(limit_default, stop)

        # Case 4: start is None
        self.assertIsNone(calculate_time_limit(None, stop, "23:00"))

    def test_find_best_observation_window(self):
        mock_place = MagicMock()
        mock_place.name = "TestPlace"
        mock_conditions = MagicMock()
        mock_conditions.twilight = Twilight.ASTRONOMICAL

        start_dt = datetime(2025, 1, 1, 21, 0)
        stop_dt = datetime(2025, 1, 2, 5, 0)

        mock_place.sunset_time.return_value = start_dt
        mock_place.sunrise_time.return_value = stop_dt

        start, stop = find_best_observation_window(mock_place, mock_conditions)
        self.assertEqual(start, start_dt)
        self.assertEqual(stop, stop_dt)
