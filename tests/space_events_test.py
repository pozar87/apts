import unittest
from datetime import datetime, timezone
from unittest.mock import MagicMock, patch

from apts.constants.event_types import EventType
from apts.events import AstronomicalEvents
from apts.place import Place

utc = timezone.utc


class SpaceEventsTest(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=52.2, lon=21.0)  # Warsaw
        self.start_date = datetime(2023, 1, 1, tzinfo=utc)
        self.end_date = datetime(2023, 1, 31, tzinfo=utc)
        self.events = AstronomicalEvents(
            self.place,
            self.start_date,
            self.end_date,
            events_to_calculate=[EventType.SPACE_LAUNCHES, EventType.SPACE_EVENTS],
        )

    @patch("apts.events.requests.get")
    def test_calculate_space_launches(self, mock_get):
        mock_launch_response = MagicMock()
        mock_launch_response.json.return_value = {
            "results": [
                {
                    "name": "Falcon 9 Block 5 | Starlink Group 5-2",
                    "window_start": "2023-01-26T14:22:00Z",
                }
            ]
        }

        mock_event_response = MagicMock()
        mock_event_response.json.return_value = {"results": []}

        def side_effect(url):
            if "launch" in url:
                return mock_launch_response
            return mock_event_response

        mock_get.side_effect = side_effect

        events_df = self.events.get_events()
        self.assertEqual(len(events_df), 1)
        self.assertEqual(
            events_df.iloc[0]["event"], "Falcon 9 Block 5 | Starlink Group 5-2"
        )
        self.assertEqual(events_df.iloc[0]["type"], "Start rakiety")
        self.assertEqual(
            events_df.iloc[0]["date"], datetime(2023, 1, 26, 14, 22, tzinfo=utc)
        )

    @patch("apts.events.requests.get")
    def test_calculate_space_events(self, mock_get):
        mock_launch_response = MagicMock()
        mock_launch_response.json.return_value = {"results": []}

        mock_event_response = MagicMock()
        mock_event_response.json.return_value = {
            "results": [
                {
                    "name": "ISS Resupply Mission (CRS-27)",
                    "date": "2023-01-15T10:00:00Z",
                }
            ]
        }

        def side_effect(url):
            if "launch" in url:
                return mock_launch_response
            return mock_event_response

        mock_get.side_effect = side_effect

        events_df = self.events.get_events()
        self.assertEqual(len(events_df), 1)
        self.assertEqual(events_df.iloc[0]["event"], "ISS Resupply Mission (CRS-27)")
        self.assertEqual(events_df.iloc[0]["type"], "Wydarzenie kosmiczne")
        self.assertEqual(
            events_df.iloc[0]["date"], datetime(2023, 1, 15, 10, 0, tzinfo=utc)
        )


if __name__ == "__main__":
    unittest.main()
