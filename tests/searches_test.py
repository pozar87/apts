import unittest
from datetime import datetime
from skyfield.api import load, Topos, utc
from apts import searches
from apts.catalogs import Catalogs


class SearchesTest(unittest.TestCase):
    def setUp(self):
        self.ts = load.timescale()
        self.eph = load("de421.bsp")
        self.observer = self.eph["earth"] + Topos(
            latitude_degrees=52.2, longitude_degrees=21.0
        )
        self.start_date = datetime(2023, 1, 1, tzinfo=utc)
        self.end_date = datetime(
            2023, 12, 31, tzinfo=utc
        )  # shorter time for faster tests

    def test_find_highest_altitude(self):
        time, alt = searches.find_highest_altitude(
            self.observer, self.eph["venus"], self.start_date, self.end_date
        )
        self.assertIsNotNone(time)
        self.assertGreater(alt, 0)

    def test_find_aphelion_perihelion(self):
        events = searches.find_aphelion_perihelion(
            self.eph, "mars", self.start_date, self.end_date
        )
        # May not occur in a short time frame, just check if it runs
        self.assertIsInstance(events, list)

    def test_find_lunar_occultations(self):
        # This test is slow and complex, so we'll just check if it runs without error
        # on a very short time scale and a single bright star.
        short_start = datetime(2023, 1, 1, tzinfo=utc)
        short_end = datetime(2023, 1, 2, tzinfo=utc)
        sirius = Catalogs.BRIGHT_STARS[Catalogs.BRIGHT_STARS["Name"] == "Sirius"]
        events = searches.find_lunar_occultations(
            self.observer, self.eph, sirius, short_start, short_end
        )
        self.assertIsInstance(events, list)

    def test_find_mercury_inferior_conjunctions(self):
        start_date = datetime(2023, 1, 1, tzinfo=utc)
        end_date = datetime(2023, 12, 31, tzinfo=utc)
        events = searches.find_mercury_inferior_conjunctions(
            self.eph, start_date, end_date
        )
        self.assertGreater(len(events), 0)

    def test_find_moon_apogee_perigee(self):
        events = searches.find_moon_apogee_perigee(
            self.eph, self.start_date, self.end_date
        )
        self.assertGreater(len(events), 2)  # Should have at least one of each

    def test_find_conjunctions(self):
        start_date = datetime(2023, 1, 1, tzinfo=utc)
        end_date = datetime(2023, 3, 31, tzinfo=utc)
        events = searches.find_conjunctions(
            self.eph, "venus", "jupiter barycenter", start_date, end_date
        )
        self.assertGreater(len(events), 0)


if __name__ == "__main__":
    unittest.main()
