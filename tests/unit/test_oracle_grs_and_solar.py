import unittest
from datetime import datetime, timezone
import numpy as np
from apts.events import AstronomicalEvents
from apts.place import Place
from apts.constants.event_types import EventType
from apts.utils import planetary
from apts.cache import get_timescale

class TestOracleImprovements(unittest.TestCase):
    def setUp(self):
        self.place = Place(
            name="Greenwich",
            lat=51.4779,
            lon=0.0015,
            elevation=46,
            date=datetime(2024, 1, 1, tzinfo=timezone.utc),
        )

    def test_grs_light_time_correction(self):
        ts = get_timescale()
        t = ts.utc(2024, 1, 1, 12, 0, 0)

        # This will now include light-time correction
        lon_with_lt = planetary.get_jupiter_system_ii_longitude(t)

        # Manually calculate WITHOUT light-time correction for comparison
        import ephem
        j = ephem.Jupiter()
        j.compute(t.utc_datetime())
        lon_without_lt = float(np.degrees(float(j.cmlII)))

        # Difference should be approx 37 minutes of Jupiter rotation
        # Jupiter rotation is ~9.92 hours per 360 degrees, so ~0.6 degrees/minute
        # 37 mins * 0.6 deg/min approx 22 degrees
        diff = (lon_without_lt - lon_with_lt + 180) % 360 - 180
        print(f"GRS Longitude Diff (deg): {diff}")
        self.assertGreater(abs(diff), 15)
        self.assertLess(abs(diff), 30)

    def test_planet_solar_conjunctions(self):
        # Search for Venus superior conjunction around June 4, 2024
        start = datetime(2024, 6, 1, tzinfo=timezone.utc)
        end = datetime(2024, 6, 10, tzinfo=timezone.utc)

        events = AstronomicalEvents(self.place, start, end, events_to_calculate=[EventType.PLANET_SOLAR_CONJUNCTIONS])
        df = events.get_events()

        # Filter for Venus
        venus_events = df[df['object1'] == 'Venus']
        self.assertFalse(venus_events.empty)

        event = venus_events.iloc[0]
        self.assertEqual(event['conjunction_kind'], 'Superior Conjunction')
        self.assertIn('Venus Solar Superior Conjunction', event['event'])

    def test_grs_dynamic_longitude(self):
        # Reference: 79.6 on 2026-03-18
        t1 = get_timescale().utc(2026, 3, 18)
        lon1 = planetary.get_jupiter_grs_longitude(t1)
        self.assertAlmostEqual(lon1, 79.6, places=1)

        # One month earlier should be approx 0.8 degrees less
        t2 = get_timescale().utc(2026, 2, 18)
        lon2 = planetary.get_jupiter_grs_longitude(t2)
        self.assertLess(lon2, lon1)
        self.assertGreater(lon2, lon1 - 1.0)

if __name__ == "__main__":
    unittest.main()
