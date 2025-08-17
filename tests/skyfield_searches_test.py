import unittest
from datetime import datetime
from skyfield.api import load, Topos, utc
from apts import skyfield_searches
from apts.catalogs import Catalogs
from skyfield.api import Star
import pandas as pd


class SkyfieldSearchesTest(unittest.TestCase):
    def setUp(self):
        self.ts = load.timescale()
        self.eph = load("de421.bsp")
        self.observer = self.eph["earth"] + Topos(
            latitude_degrees=52.2, longitude_degrees=21.0
        )
        self.start_date = datetime(2023, 1, 1, tzinfo=utc)
        self.end_date = datetime(
            2023, 1, 31, tzinfo=utc
        )  # shorter time for faster tests

    def test_find_highest_altitude(self):
        time, alt = skyfield_searches.find_highest_altitude(
            self.observer, self.eph["venus"], self.start_date, self.end_date
        )
        self.assertIsInstance(time, datetime)
        self.assertIsInstance(alt, float)

    def test_find_aphelion_perihelion(self):
        events = skyfield_searches.find_aphelion_perihelion(
            self.eph, "mars", self.start_date, self.end_date
        )
        self.assertIsInstance(events, list)

    def test_find_lunar_occultations(self):
        short_start = datetime(2023, 1, 1, tzinfo=utc)
        short_end = datetime(2023, 1, 2, tzinfo=utc)
        sirius = Catalogs().BRIGHT_STARS[Catalogs().BRIGHT_STARS["Name"] == "Sirius"]
        events = skyfield_searches.find_lunar_occultations(
            self.observer, self.eph, sirius, short_start, short_end
        )
        self.assertIsInstance(events, list)

    def test_find_mercury_inferior_conjunctions(self):
        start_date = datetime(2023, 1, 1, tzinfo=utc)
        end_date = datetime(2023, 12, 31, tzinfo=utc)
        events = skyfield_searches.find_mercury_inferior_conjunctions(
            self.observer, self.eph, start_date, end_date
        )
        self.assertIsInstance(events, list)

    def test_find_moon_apogee_perigee(self):
        events = skyfield_searches.find_moon_apogee_perigee(
            self.eph, self.start_date, self.end_date
        )
        self.assertIsInstance(events, list)

    def test_find_conjunctions(self):
        start_date = datetime(2023, 1, 1, tzinfo=utc)
        end_date = datetime(2023, 3, 31, tzinfo=utc)
        events = skyfield_searches.find_conjunctions(
            self.observer, self.eph, "venus", "jupiter barycenter", start_date, end_date, threshold_degrees=1.0
        )
        self.assertIsInstance(events, list)
        if events:
            self.assertIn('separation_degrees', events[0])
            self.assertLess(events[0]['separation_degrees'], 1.0)

    def test_find_great_conjunction_2020(self):
        start_date = datetime(2020, 12, 20, tzinfo=utc)
        end_date = datetime(2020, 12, 22, tzinfo=utc)
        events = skyfield_searches.find_conjunctions(
            self.observer, self.eph, "jupiter barycenter", "saturn barycenter", start_date, end_date
        )
        self.assertIsInstance(events, list)
        self.assertEqual(len(events), 1)
        event = events[0]
        # Check that the date is December 21, 2020
        self.assertEqual(event['date'].day, 21)
        self.assertAlmostEqual(event['separation_degrees'], 0.1, delta=0.01)

    def test_find_conjunctions_with_threshold(self):
        start_date = datetime(2023, 1, 1, tzinfo=utc)
        end_date = datetime(2023, 12, 31, tzinfo=utc)

        # First, find all conjunctions without a threshold.
        all_events = skyfield_searches.find_conjunctions(
            self.observer, self.eph, "venus", "saturn barycenter", start_date, end_date
        )
        self.assertGreater(len(all_events), 0, "Should find at least one conjunction in 2023")

        # Now, use the separation of the first event to test the thresholding.
        separation = all_events[0]['separation_degrees']

        # Test with a threshold slightly smaller than the actual separation.
        tighter_events = skyfield_searches.find_conjunctions(
            self.observer, self.eph, "venus", "saturn barycenter", start_date, end_date, threshold_degrees=separation - 0.1
        )
        # It's possible other conjunctions are found, so we check that the original event is not present
        found = False
        for event in tighter_events:
            if event['date'] == all_events[0]['date']:
                found = True
                break
        self.assertFalse(found)

        # Test with a threshold slightly larger than the actual separation.
        wider_events = skyfield_searches.find_conjunctions(
            self.observer, self.eph, "venus", "saturn barycenter", start_date, end_date, threshold_degrees=separation + 0.1
        )
        self.assertIn(all_events[0], wider_events)

    def test_find_conjunctions_no_threshold(self):
        start_date = datetime(2023, 1, 1, tzinfo=utc)
        end_date = datetime(2023, 3, 31, tzinfo=utc)
        events = skyfield_searches.find_conjunctions(
            self.observer, self.eph, "venus", "jupiter barycenter", start_date, end_date
        )
        self.assertGreater(len(events), 0)
        self.assertIn('separation_degrees', events[0])

    def test_find_venus_mercury_conjunction_2021(self):
        start_date = datetime(2021, 5, 28, tzinfo=utc)
        end_date = datetime(2021, 5, 30, tzinfo=utc)
        events = skyfield_searches.find_conjunctions(
            self.observer, self.eph, "venus", "mercury", start_date, end_date
        )
        self.assertIsInstance(events, list)
        self.assertEqual(len(events), 1)
        event = events[0]
        # Check that the date is May 29, 2021
        self.assertEqual(event['date'].day, 29)
        self.assertAlmostEqual(event['separation_degrees'], 0.4, delta=0.1)

    def test_find_moon_m45_conjunction_2025(self):
        start_date = datetime(2025, 8, 15, tzinfo=utc)
        end_date = datetime(2025, 8, 17, tzinfo=utc)
        m45_data = Catalogs().MESSIER[Catalogs().MESSIER['Messier'] == 'M45'].iloc[0]
        m45 = Star(ra_hours=m45_data['RA'].to('hour').magnitude,
                   dec_degrees=m45_data['Dec'].to('degree').magnitude)
        events = skyfield_searches.find_conjunctions_with_star(
            self.observer, self.eph, "moon", m45, start_date, end_date
        )
        self.assertIsInstance(events, list)
        self.assertEqual(len(events), 1)
        event = events[0]
        # Check that the date is August 16, 2025
        self.assertEqual(event['date'].day, 16)
        self.assertAlmostEqual(event['separation_degrees'], 0.5, delta=0.2)


if __name__ == "__main__":
    unittest.main()
