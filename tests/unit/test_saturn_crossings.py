import unittest
from datetime import datetime, timezone
from apts.events import AstronomicalEvents
from apts.place import Place
from apts.constants.event_types import EventType

utc = timezone.utc

class SaturnCrossingsTest(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=0, lon=0)
        # Next Saturn ring plane crossing is in March 2025
        self.start_date = datetime(2025, 1, 1, tzinfo=utc)
        self.end_date = datetime(2026, 1, 1, tzinfo=utc)

    def test_saturn_ring_crossing_2025(self):
        events_calculator = AstronomicalEvents(
            self.place,
            self.start_date,
            self.end_date,
            events_to_calculate=[EventType.SATURN_RING_CROSSINGS],
        )
        events_df = events_calculator.get_events()

        # Earth crosses the ring plane in March 2025
        # Sun crosses the ring plane in May 2025 (Saturn equinox)

        earth_crossings = events_df[events_df["event"] == "Saturn Ring Plane Crossing (Earth)"]
        sun_crossings = events_df[events_df["event"] == "Saturn Ring Plane Crossing (Sun)"]

        self.assertGreaterEqual(len(earth_crossings), 1)
        self.assertGreaterEqual(len(sun_crossings), 1)

        # Verify approximate dates
        # Earth crossing is approx March 23, 2025
        event_date = earth_crossings.iloc[0]["date"]
        self.assertEqual(event_date.year, 2025)
        self.assertEqual(event_date.month, 3)
        self.assertTrue(20 <= event_date.day <= 25)

        # Sun crossing is approx May 6, 2025
        event_date_sun = sun_crossings.iloc[0]["date"]
        self.assertEqual(event_date_sun.year, 2025)
        self.assertEqual(event_date_sun.month, 5)
        self.assertTrue(1 <= event_date_sun.day <= 10)

if __name__ == "__main__":
    unittest.main()
