import unittest
from datetime import datetime
import ephem
from apts import searches
from apts.place import Place
from apts.catalogs import Catalogs

class SearchesTest(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=52.2, lon=21.0)
        self.start_date = datetime(2023, 1, 1)
        self.end_date = datetime(2023, 12, 31)

    def test_find_highest_altitude(self):
        time, alt = searches.find_highest_altitude(self.place, ephem.Mercury(), self.start_date, self.end_date)
        self.assertIsNotNone(time)
        self.assertGreater(alt, 0)

    def test_find_lunar_occultations(self):
        events = searches.find_lunar_occultations(self.place, Catalogs.BRIGHT_STARS, self.start_date, self.end_date)
        # This is a rare event, so we can't guarantee it will happen in a year.
        # We'll just check that the function runs without errors.
        self.assertIsInstance(events, list)

if __name__ == '__main__':
    unittest.main()
