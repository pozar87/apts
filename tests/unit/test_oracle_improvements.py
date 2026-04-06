
import unittest
from datetime import datetime, timezone
import numpy as np
from apts.place import Place
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType
import time

utc = timezone.utc

class TestOracleImprovements(unittest.TestCase):
    def setUp(self):
        # Warsaw
        self.place = Place(lat=52.2, lon=21.0)

    def test_optimized_solar_eclipse_2024(self):
        # Total Solar Eclipse April 8, 2024 (Visible as Partial from Warsaw?)
        # Wait, April 8 2024 was not visible from Warsaw. Let's check visibility from Mazatlan, Mexico
        mazatlan = Place(lat=23.2, lon=-106.4)
        start_date = datetime(2024, 4, 8, 0, 0, tzinfo=utc)
        end_date = datetime(2024, 4, 9, 0, 0, tzinfo=utc)

        events_calc = AstronomicalEvents(
            mazatlan,
            start_date,
            end_date,
            events_to_calculate=[EventType.SOLAR_ECLIPSES]
        )

        start_time = time.time()
        df = events_calc.get_events()
        duration = time.time() - start_time

        print(f"Solar eclipse search took {duration:.4f}s")

        self.assertGreater(len(df), 0)
        eclipse = df.iloc[0]
        self.assertEqual(eclipse['type'], 'Solar Eclipse')
        self.assertEqual(eclipse['eclipse_type'], 'Total')
        self.assertGreater(eclipse['magnitude'], 1.0)

        # Verify it is fast (should be sub-second with optimization)
        self.assertLess(duration, 2.0)

    def test_enriched_opposition_data(self):
        # Jupiter opposition Nov 3, 2023
        start_date = datetime(2023, 11, 1, tzinfo=utc)
        end_date = datetime(2023, 11, 5, tzinfo=utc)

        events_calc = AstronomicalEvents(
            self.place,
            start_date,
            end_date,
            events_to_calculate=[EventType.OPPOSITIONS]
        )

        df = events_calc.get_events()

        self.assertGreater(len(df), 0)
        opposition = df[df['object'] == 'Jupiter'].iloc[0]

        self.assertIn('magnitude', opposition)
        self.assertIn('distance_au', opposition)
        self.assertIn('angular_diameter_arcsec', opposition)

        # Jupiter at opposition is bright (~ -2.9)
        self.assertLess(opposition['magnitude'], -2.0)
        # Distance should be around 4 AU
        self.assertGreater(opposition['distance_au'], 3.9)
        self.assertLess(opposition['distance_au'], 4.1)
        # Angular diameter should be around 49 arcsec
        self.assertGreater(opposition['angular_diameter_arcsec'], 45)
        self.assertLess(opposition['angular_diameter_arcsec'], 55)

    def test_lunar_eclipse_visibility_2024(self):
        # Partial Lunar Eclipse Sept 18, 2024 (Visible from Warsaw)
        start_date = datetime(2024, 9, 18, 0, 0, tzinfo=utc)
        end_date = datetime(2024, 9, 19, 0, 0, tzinfo=utc)

        events_calc = AstronomicalEvents(
            self.place,
            start_date,
            end_date,
            events_to_calculate=[EventType.LUNAR_ECLIPSES]
        )

        df = events_calc.get_events()
        self.assertGreater(len(df), 0)
        eclipse = df.iloc[0]
        # Should be visible from Warsaw
        self.assertTrue(eclipse['is_visible'])

if __name__ == "__main__":
    unittest.main()
