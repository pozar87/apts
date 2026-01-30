import unittest
from datetime import datetime
from skyfield.api import Topos, utc
from apts import skyfield_searches
from apts.cache import get_ephemeris, get_timescale
from apts.utils import planetary
from apts.events import AstronomicalEvents
from apts.place import Place

class MercuryTransitTest(unittest.TestCase):
    def setUp(self):
        self.eph = get_ephemeris()
        self.ts = get_timescale()
        self.observer = self.eph["earth"] + Topos(latitude_degrees=0.0, longitude_degrees=0.0)

    def test_mercury_transit_2019(self):
        # 2019-11-11 was an inferior transit
        start_date = datetime(2019, 11, 10, tzinfo=utc)
        end_date = datetime(2019, 11, 12, tzinfo=utc)

        events = skyfield_searches.find_mercury_inferior_conjunctions(self.observer, start_date, end_date)

        self.assertEqual(len(events), 1, "Should find exactly one inferior conjunction in Nov 2019")
        event = events[0]

        # Check if it's on the "right side" (closer to us than the sun)
        t = self.ts.from_datetime(event["date"])
        mercury = planetary.get_skyfield_obj("mercury")
        sun = planetary.get_skyfield_obj("sun")

        m_dist = self.observer.at(t).observe(mercury).distance().au
        s_dist = self.observer.at(t).observe(sun).distance().au

        self.assertLess(m_dist, s_dist, "Mercury should be closer to Earth than the Sun during inferior conjunction")
        self.assertTrue(event.get("is_transit"), "2019-11-11 should be a transit")

    def test_mercury_superior_conjunction_2019_not_found(self):
        # 2019-09-04 was a superior conjunction
        start_date = datetime(2019, 9, 3, tzinfo=utc)
        end_date = datetime(2019, 9, 6, tzinfo=utc)

        events = skyfield_searches.find_mercury_inferior_conjunctions(
            self.observer, start_date, end_date, threshold_degrees=5.0
        )

        self.assertEqual(
            len(events),
            0,
            "Superior conjunction should NOT be returned by find_mercury_inferior_conjunctions",
        )

    def test_mercury_inferior_conjunction_non_transit_2023(self):
        # 2023-05-02 was an inferior conjunction but not a transit (separation ~0.7 deg)
        start_date = datetime(2023, 4, 30, tzinfo=utc)
        end_date = datetime(2023, 5, 4, tzinfo=utc)

        events = skyfield_searches.find_mercury_inferior_conjunctions(self.observer, start_date, end_date, threshold_degrees=5.0)

        self.assertEqual(len(events), 1)
        event = events[0]

        t = self.ts.from_datetime(event["date"])
        mercury = planetary.get_skyfield_obj("mercury")
        sun = planetary.get_skyfield_obj("sun")

        m_dist = self.observer.at(t).observe(mercury).distance().au
        s_dist = self.observer.at(t).observe(sun).distance().au

        self.assertLess(m_dist, s_dist)
        self.assertGreater(event["separation_degrees"], 0.3, "This should not be a transit")
        self.assertFalse(event.get("is_transit"), "2023-05-02 should NOT be a transit")

    def test_astronomical_events_mercury_transit(self):
        # Test that AstronomicalEvents correctly labels the transit
        place = Place(lat=0.0, lon=0.0, elevation=0.0, name="Equator")
        # 2019-11-11 transit
        start_date = datetime(2019, 11, 11, 0, 0, 0, tzinfo=utc)
        end_date = datetime(2019, 11, 11, 23, 59, 59, tzinfo=utc)

        ae = AstronomicalEvents(place, start_date, end_date)
        events_df = ae.calculate_mercury_inferior_conjunctions()

        self.assertEqual(len(events_df), 1)
        event = events_df[0]
        self.assertEqual(event["event"], "Mercury Transit")
        self.assertTrue(event["is_transit"])

if __name__ == "__main__":
    unittest.main()
