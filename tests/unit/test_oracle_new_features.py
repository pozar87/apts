import unittest
from datetime import datetime, timezone
from unittest.mock import patch
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

    @patch("apts.events.get_event_settings")
    def test_seasons(self, mock_get_event_settings):
        mock_get_event_settings.return_value = {"seasons": True}
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
        self.assertTrue(all(events_df["rarity"] == 2))

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

class TestOracleLundarMars(unittest.TestCase):
    def test_lunar_eclipse_visibility_filtering(self):
        # Total Lunar Eclipse: March 14, 2025.
        # Greatest eclipse around 06:58 UTC.
        # For Tokyo (35.7, 139.7), the Moon is below the horizon at this time.

        start_date = datetime(2025, 3, 14, 0, 0, tzinfo=utc)
        end_date = datetime(2025, 3, 15, 0, 0, tzinfo=utc)

        place_tokyo = Place(lat=35.6895, lon=139.6917, name="Tokyo")
        from apts.skyfield_searches import find_lunar_eclipses
        eclipses_tokyo = find_lunar_eclipses(start_date, end_date, observer=place_tokyo.observer)

        self.assertGreater(len(eclipses_tokyo), 0)
        eclipse = eclipses_tokyo[0]
        self.assertFalse(eclipse["is_visible"])
        self.assertLess(eclipse["altitude"], 0)

        # For New York (40.7, -74.0), it should be visible.
        # 06:58 UTC is 02:58 EDT.
        place_ny = Place(lat=40.7128, lon=-74.0060, name="New York")
        eclipses_ny = find_lunar_eclipses(start_date, end_date, observer=place_ny.observer)
        self.assertGreater(len(eclipses_ny), 0)
        self.assertTrue(eclipses_ny[0]["is_visible"])
        self.assertGreater(eclipses_ny[0]["altitude"], 0)

    def test_mars_closest_approach_2025(self):
        # Mars closest approach in 2025 is Jan 12.
        # Opposition is Jan 16.
        start_date = datetime(2025, 1, 1, tzinfo=utc)
        end_date = datetime(2025, 1, 31, tzinfo=utc)

        from apts.skyfield_searches import find_mars_closest_approach
        events = find_mars_closest_approach(start_date, end_date)
        self.assertGreater(len(events), 0)
        self.assertEqual(events[0]["date"].day, 12)
        self.assertEqual(events[0]["date"].month, 1)
        self.assertIn("distance_au", events[0])

    def test_astronomical_events_integration(self):
        start_date = datetime(2025, 1, 1, tzinfo=utc)
        end_date = datetime(2025, 1, 31, tzinfo=utc)
        place = Place(lat=52.2, lon=21.0) # Warsaw

        ae = AstronomicalEvents(place, start_date, end_date, events_to_calculate=[EventType.MARS_CLOSEST_APPROACH])
        df = ae.get_events()

        self.assertFalse(df.empty)
        self.assertEqual(df.iloc[0]["event"], "Mars Closest Approach")
        self.assertEqual(df.iloc[0]["rarity"], 4)


if __name__ == "__main__":
    unittest.main()
