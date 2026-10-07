from datetime import datetime, timezone
import unittest

from apts.place import Place
from apts import skyfield_searches


class TestSolarEclipseSearchOptimization(unittest.TestCase):
    def test_find_solar_eclipses_dallas_total_eclipse(self):
        """
        Verify that find_solar_eclipses accurately identifies the April 8, 2024 total solar eclipse
        from Dallas, Texas with correct eclipse type, magnitude, and obscuration.
        """
        # Dallas, Texas location
        place = Place(32.7767, -96.7970, 130)
        observer = place.observer

        start_date = datetime(2024, 4, 1, tzinfo=timezone.utc)
        end_date = datetime(2024, 4, 30, tzinfo=timezone.utc)

        events = skyfield_searches.find_solar_eclipses(
            observer, start_date, end_date
        )

        self.assertEqual(len(events), 1)
        event = events[0]

        self.assertEqual(event["type"], "Solar Eclipse")
        self.assertEqual(event["eclipse_type"], "Total")
        self.assertGreater(event["magnitude"], 1.0)
        self.assertAlmostEqual(event["obscuration"], 1.0, places=5)
        self.assertEqual(event["date"].year, 2024)
        self.assertEqual(event["date"].month, 4)
        self.assertEqual(event["date"].day, 8)

    def test_find_solar_eclipses_no_eclipse_period(self):
        """
        Verify that find_solar_eclipses returns an empty list for periods with no visible solar eclipses.
        """
        # Warsaw, Poland - no solar eclipse in June 2024
        place = Place(52.2297, 21.0122, 100)
        observer = place.observer

        start_date = datetime(2024, 6, 1, tzinfo=timezone.utc)
        end_date = datetime(2024, 6, 30, tzinfo=timezone.utc)

        events = skyfield_searches.find_solar_eclipses(
            observer, start_date, end_date
        )

        self.assertEqual(len(events), 0)


if __name__ == "__main__":
    unittest.main()
