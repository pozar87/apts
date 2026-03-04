import unittest
from datetime import datetime, timezone
from apts.place import Place
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType

utc = timezone.utc

class LunarPlanetaryOccultationsTest(unittest.TestCase):
    def setUp(self):
        # Greenwich, London
        self.place = Place(lat=51.48, lon=0.0)
        # Mars occultation on 2022-12-08
        self.start_date = datetime(2022, 12, 8, 0, 0, tzinfo=utc)
        self.end_date = datetime(2022, 12, 8, 12, 0, tzinfo=utc)

    def test_mars_occultation_greenwich(self):
        ast_events = AstronomicalEvents(
            self.place,
            self.start_date,
            self.end_date,
            events_to_calculate=[EventType.LUNAR_PLANETARY_OCCULTATIONS]
        )
        events_df = ast_events.get_events()

        self.assertFalse(events_df.empty, "Should find at least one event")

        # Check if Mars was occulted
        mars_occ = events_df[events_df["object2"] == "Mars"]
        self.assertGreater(len(mars_occ), 0, "Should find Mars occultation")

        # Verify the time is around 05:00 UTC
        event_time = mars_occ.iloc[0]["date"]
        self.assertEqual(event_time.year, 2022)
        self.assertEqual(event_time.month, 12)
        self.assertEqual(event_time.day, 8)
        self.assertIn(event_time.hour, [4, 5, 6])

    def test_no_occultation_warsaw_at_same_time(self):
        # Warsaw might see it differently or not at all depending on geometry
        # Actually it was visible from most of Europe.
        # Let's try Tokyo, where it was NOT visible (daytime/wrong geometry)
        tokyo = Place(lat=35.6762, lon=139.6503)
        ast_events = AstronomicalEvents(
            tokyo,
            self.start_date,
            self.end_date,
            events_to_calculate=[EventType.LUNAR_PLANETARY_OCCULTATIONS]
        )
        events_df = ast_events.get_events()

        # It should be empty or at least not have Mars occultation at that time
        if not events_df.empty:
             mars_occ = events_df[events_df["object2"] == "Mars"]
             self.assertEqual(len(mars_occ), 0, "Mars occultation should not be visible from Tokyo")

if __name__ == "__main__":
    unittest.main()
