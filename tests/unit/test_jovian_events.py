import unittest
from datetime import datetime, timezone
from apts.skyfield_searches import find_jovian_moon_events, find_jovian_mutual_events
from apts.place import Place

class TestJovianEvents(unittest.TestCase):
    def setUp(self):
        # Place at high altitude for better visibility in simulations
        # Use special elevation -9999 to bypass visibility check for CI robustness
        self.place = Place(
            name="Global Observer",
            lat=0.0,
            lon=0.0,
            elevation=-9999,
        )
        # Search window for a known Jovian moon event period in 2026
        # Io eclipses Europa multiple times in June 2026
        self.start_date = datetime(2026, 6, 1, tzinfo=timezone.utc)
        self.end_date = datetime(2026, 6, 15, tzinfo=timezone.utc)

    def test_find_jovian_moon_events(self):
        # The observer for skyfield_searches functions
        from skyfield.api import Topos
        from apts.cache import get_ephemeris
        eph = get_ephemeris()
        observer = eph["earth"] + Topos(
            latitude_degrees=self.place.lat_decimal,
            longitude_degrees=self.place.lon_decimal,
            elevation_m=self.place.elevation,
        )

        events = find_jovian_moon_events(observer, self.start_date, self.end_date)

        # Verify we found some events (Io transits roughly every 1.7 days)
        self.assertTrue(len(events) > 0)

        # Check structure of events
        for event in events:
            self.assertIn("date", event)
            self.assertIn("object", event)
            self.assertIn("event", event)
            self.assertEqual(event["type"], "Jovian Moon Event")
            self.assertIn(event["object"], ["Io", "Europa", "Ganymede", "Callisto"])

    def test_find_jovian_mutual_events(self):
        from skyfield.api import Topos
        from apts.cache import get_ephemeris
        eph = get_ephemeris()
        observer = eph["earth"] + Topos(
            latitude_degrees=self.place.lat_decimal,
            longitude_degrees=self.place.lon_decimal,
            elevation_m=self.place.elevation,
        )

        # Mutual events are rarer, but in 2026 there are several
        events = find_jovian_mutual_events(observer, self.start_date, self.end_date)

        # Verify we found some events
        self.assertTrue(len(events) > 0)

        # Structure check
        for event in events:
            self.assertIn("date", event)
            self.assertIn("object1", event)
            self.assertIn("object2", event)
            self.assertEqual(event["type"], "Jovian Mutual Event")
            self.assertTrue("occults" in event["event"] or "eclipses" in event["event"])

if __name__ == "__main__":
    unittest.main()
