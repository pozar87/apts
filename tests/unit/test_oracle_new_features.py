import unittest
from datetime import datetime, timezone
from apts.place import Place
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType
from apts.skyfield_searches import find_seasons, find_conjunctions

utc = timezone.utc

class OracleNewFeaturesTest(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=52.2, lon=21.0)  # Warsaw
        self.start_date = datetime(2023, 1, 1, tzinfo=utc)
        self.end_date = datetime(2023, 12, 31, tzinfo=utc)

    def test_seasons(self):
        events = find_seasons(self.start_date, self.end_date)
        self.assertEqual(len(events), 4)

        event_names = [e["event"] for e in events]
        self.assertIn("Vernal Equinox", event_names)
        self.assertIn("Summer Solstice", event_names)
        self.assertIn("Autumnal Equinox", event_names)
        self.assertIn("Winter Solstice", event_names)

        # Verify AstronomicalEvents integration
        ast_events = AstronomicalEvents(self.place, self.start_date, self.end_date,
                                        events_to_calculate=[EventType.SEASONS])
        events_df = ast_events.get_events()
        self.assertEqual(len(events_df), 4)
        self.assertTrue(all(events_df["type"] == "Season"))
        self.assertTrue(all(events_df["rarity"] == 4))

    def test_moon_conjunction_timing_accuracy(self):
        # Known Moon-Jupiter conjunction on 2023-01-26
        start = datetime(2023, 1, 25, 0, 0, tzinfo=utc)
        end = datetime(2023, 1, 27, 0, 0, tzinfo=utc)

        events = find_conjunctions(self.place.observer, "moon", "jupiter", start, end, threshold_degrees=5.0)
        self.assertGreater(len(events), 0)

        # With step_days=0.05, we expect the time to be quite accurate
        # In Warsaw, it's around 03:30 UTC on Jan 26
        event_date = events[0]["date"]
        self.assertEqual(event_date.day, 26)
        self.assertEqual(event_date.hour, 3)

    def test_vectorized_moon_star_messier_conjunctions(self):
        # Test that vectorized conjunctions still find the same events
        start = datetime(2023, 8, 24, tzinfo=utc)
        end = datetime(2023, 8, 26, tzinfo=utc)

        # Star Conjunctions
        ast_events_star = AstronomicalEvents(self.place, start, end,
                                              events_to_calculate=[EventType.MOON_STAR_CONJUNCTIONS])
        events_star_df = ast_events_star.get_events()
        self.assertIn("Antares", events_star_df["object2"].values)

        # Messier Conjunctions
        ast_events_messier = AstronomicalEvents(self.place, start, end,
                                                 events_to_calculate=[EventType.MOON_MESSIER_CONJUNCTIONS])
        events_messier_df = ast_events_messier.get_events()
        # M4 is very close to Antares
        self.assertIn("M4", events_messier_df["object2"].values)

if __name__ == "__main__":
    unittest.main()
