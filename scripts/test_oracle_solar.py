
import unittest
from datetime import datetime, timezone
from skyfield import eclipselib
from apts.place import Place
from apts.events import AstronomicalEvents
from apts.skyfield_searches.solar import find_solar_eclipses, find_lunar_eclipses
from skyfield.api import Topos
import time

class TestOracleSolar(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=40.7128, lon=-74.0060) # New York
        self.observer = Topos(latitude_degrees=40.7128, longitude_degrees=-74.0060)

    def test_solar_eclipse_2024(self):
        # Total Solar Eclipse April 8, 2024
        start_date = datetime(2024, 4, 8, 0, 0, tzinfo=timezone.utc)
        end_date = datetime(2024, 4, 9, 0, 0, tzinfo=timezone.utc)

        start_time = time.time()
        events = find_solar_eclipses(self.place.observer, start_date, end_date)
        end_time = time.time()

        print(f"Solar search took {end_time - start_time:.4f} seconds")
        for e in events:
            print(e)

        self.assertGreater(len(events), 0)
        self.assertEqual(events[0]['eclipse_type'], 'Partial') # NYC was partial

    def test_lunar_eclipse_kinds(self):
        # Partial Lunar Eclipse Sept 18, 2024
        start_date = datetime(2024, 9, 17, 0, 0, tzinfo=timezone.utc)
        end_date = datetime(2024, 9, 19, 0, 0, tzinfo=timezone.utc)

        try:
            events = find_lunar_eclipses(start_date, end_date, observer=self.place.observer)
            for e in events:
                print(e)
        except Exception as e:
            print(f"Caught expected/potential bug: {e}")

if __name__ == "__main__":
    # Check eclipselib constants
    print(f"LUNAR_ECLIPSES: {eclipselib.LUNAR_ECLIPSES}")
    unittest.main()
