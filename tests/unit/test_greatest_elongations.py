import unittest
from datetime import datetime, timezone
from unittest.mock import patch
from apts.place import Place
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType

utc = timezone.utc

class GreatestElongationsTest(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=52.2, lon=21.0)  # Warsaw

    @patch("apts.events.get_event_settings")
    def test_venus_greatest_elongation_2025(self, mock_get_event_settings):
        # Venus Greatest Eastern Elongation was on 2025-01-10
        mock_get_event_settings.return_value = {"greatest_elongations": True}
        start = datetime(2025, 1, 1, tzinfo=utc)
        end = datetime(2025, 1, 20, tzinfo=utc)

        ast_events = AstronomicalEvents(self.place, start, end, events_to_calculate=[EventType.GREATEST_ELONGATIONS])
        events_df = ast_events.get_events()

        self.assertFalse(events_df.empty)
        venus_events = events_df[events_df["object"] == "Venus"]
        self.assertGreater(len(venus_events), 0)

        event = venus_events.iloc[0]
        self.assertEqual(event["direction"], "Eastern")
        self.assertEqual(event["date"].year, 2025)
        self.assertEqual(event["date"].month, 1)
        self.assertEqual(event["date"].day, 10)
        # Separation should be around 47 degrees for Venus
        self.assertAlmostEqual(event["separation_degrees"], 47.1, delta=1.0)

    @patch("apts.events.get_event_settings")
    def test_mercury_greatest_elongation_2024(self, mock_get_event_settings):
        # Mercury Greatest Western Elongation was on 2024-01-12
        mock_get_event_settings.return_value = {"greatest_elongations": True}
        start = datetime(2024, 1, 1, tzinfo=utc)
        end = datetime(2024, 1, 20, tzinfo=utc)

        ast_events = AstronomicalEvents(self.place, start, end, events_to_calculate=[EventType.GREATEST_ELONGATIONS])
        events_df = ast_events.get_events()

        self.assertFalse(events_df.empty)
        mercury_events = events_df[events_df["object"] == "Mercury"]
        self.assertGreater(len(mercury_events), 0)

        event = mercury_events.iloc[0]
        self.assertEqual(event["direction"], "Western")
        self.assertEqual(event["date"].year, 2024)
        self.assertEqual(event["date"].month, 1)
        self.assertEqual(event["date"].day, 12)
        # Separation should be around 23 degrees
        self.assertAlmostEqual(event["separation_degrees"], 23.5, delta=1.0)

if __name__ == "__main__":
    unittest.main()
