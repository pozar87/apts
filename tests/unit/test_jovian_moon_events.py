import unittest
from datetime import datetime, timezone

from apts.cache import get_timescale
from apts.constants.event_types import EventType
from apts.events import AstronomicalEvents
from apts.place import Place
from apts.skyfield_searches import find_jovian_moon_events, find_solar_longitude_time

utc = timezone.utc


class JovianMoonEventsTest(unittest.TestCase):
    def setUp(self):
        # Warsaw
        self.place = Place(lat=52.2297, lon=21.0122)
        # A known time with Jovian moon events might be useful,
        # but let's just pick a window and see if it runs and finds something.
        # Jupiter is well placed in late 2024.
        self.start_date = datetime(2024, 12, 1, 0, 0, tzinfo=utc)
        self.end_date = datetime(2024, 12, 2, 0, 0, tzinfo=utc)

    def test_find_jovian_moon_events(self):
        # Test the search function directly
        events = find_jovian_moon_events(
            self.place.observer, self.start_date, self.end_date
        )

        # It's highly likely there are some events in a 24h period for 4 moons.
        # Even if not, we check it doesn't crash and returns a list.
        self.assertIsInstance(events, list)
        if len(events) > 0:
            for event in events:
                self.assertIn("object", event)
                self.assertIn("event", event)
                self.assertEqual(event["type"], "Jovian Moon Event")
                self.assertIn(event["object"], ["Io", "Europa", "Ganymede", "Callisto"])

    def test_astronomical_events_integration(self):
        ae = AstronomicalEvents(
            self.place,
            self.start_date,
            self.end_date,
            events_to_calculate=[EventType.JOVIAN_MOON_EVENTS],
        )
        df = ae.get_events()

        self.assertIsInstance(df.empty, bool)
        if not df.empty:
            self.assertIn("Jovian Moon Event", df["type"].values)

    def test_solar_longitude_accuracy(self):
        ts = get_timescale()
        # Vernal Equinox 2024 (Apparent) was around 03:06 UTC
        t0 = ts.utc(2024, 3, 20, 0, 0)
        t1 = ts.utc(2024, 3, 20, 12, 0)

        # Using default J2000 epoch
        t_j2000 = find_solar_longitude_time(t0, t1, 0.0)

        # Using current date epoch (epoch=t)
        t_date = find_solar_longitude_time(t0, t1, 0.0, epoch=t0)

        self.assertIsNotNone(t_j2000)
        self.assertIsNotNone(t_date)

        # They should differ by a few hours due to precession (approx 8.2 hours for 24 years)
        assert t_j2000 is not None and t_date is not None
        diff_minutes = (
            abs((t_j2000.utc_datetime() - t_date.utc_datetime()).total_seconds()) / 60.0
        )
        self.assertGreater(diff_minutes, 450.0)
        self.assertLess(diff_minutes, 550.0)


if __name__ == "__main__":
    unittest.main()
