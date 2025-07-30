import unittest
from datetime import datetime, timezone
from unittest.mock import patch, MagicMock
from apts.events import AstronomicalEvents
from apts.place import Place


class TestAstronomicalEvents(unittest.TestCase):
    def setUp(self):
        self.place = Place(
            name="Test Place", lat=50.0647, lon=19.9450, elevation=220
        )
        self.start_date = datetime(2024, 7, 29, tzinfo=timezone.utc)
        self.end_date = datetime(2024, 8, 29, tzinfo=timezone.utc)
        self.events = AstronomicalEvents(
            self.place, self.start_date, self.end_date
        )

    @patch("apts.events.as_completed")
    @patch("apts.events.ThreadPoolExecutor")
    def test_get_events_parallelization(self, mock_executor, mock_as_completed):
        # Mock the executor instance that the 'with' statement will use
        mock_executor_instance = mock_executor.return_value.__enter__.return_value

        # Create a list of mock futures
        mock_futures = [MagicMock() for _ in range(10)]
        for future in mock_futures:
            future.result.return_value = []

        # Have the submit method return a different mock future each time
        mock_executor_instance.submit.side_effect = mock_futures

        # have as_completed return the list of mock_futures
        mock_as_completed.return_value = mock_futures

        self.events.get_events()

        # Check that submit was called for each calculation method
        self.assertEqual(mock_executor_instance.submit.call_count, 10)
        # Check that as_completed was called with the futures list
        mock_as_completed.assert_called_once()
        self.assertEqual(len(mock_as_completed.call_args[0][0]), 10)


if __name__ == "__main__":
    unittest.main()
