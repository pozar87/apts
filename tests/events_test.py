import unittest
from datetime import datetime, timezone
from apts.events import AstronomicalEvents

utc = timezone.utc
from apts.place import Place


class EventsTest(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=52.2, lon=21.0)  # Warsaw
        self.start_date = datetime(2023, 1, 5, tzinfo=utc)
        self.end_date = datetime(2023, 1, 22, tzinfo=utc)
        self.events = AstronomicalEvents(self.place, self.start_date, self.end_date)

    def test_moon_phases(self):
        events_df = self.events.get_events()

        # New Moons within January 5, 2023, to January 22, 2023:
        #  - January 21, 2023
        self.assertEqual(sum(events_df["event"] == "New Moon"), 1)

        # Full Moons within January 5, 2023, to January 22, 2023:
        #  - January 6, 2023
        self.assertEqual(sum(events_df["event"] == "Full Moon"), 1)

    def test_eclipses(self):
        events_df = self.events.get_events()
        self.assertIn("event", events_df.columns)


if __name__ == "__main__":
    unittest.main()
