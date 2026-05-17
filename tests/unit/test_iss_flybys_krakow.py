import unittest
from datetime import datetime, timezone
from skyfield.api import Topos
from apts.skyfield_searches.satellites import find_iss_flybys
from apts.cache import get_ephemeris

class TestISSFlybysKrakow(unittest.TestCase):
    def test_krakow_flybys_april_2026(self):
        # Krakow (50.095, 19.89)
        lat, lon = 50.095, 19.89
        topos_observer = Topos(latitude_degrees=lat, longitude_degrees=lon)

        eph = get_ephemeris()
        earth = eph['earth']
        vector_observer = earth + topos_observer

        # User provided date: 30 April 2026.
        # We search from the evening of the 29th to the morning of the 30th UTC.
        start_date = datetime(2026, 4, 29, 20, 0, 0, tzinfo=timezone.utc)
        end_date = datetime(2026, 4, 30, 10, 0, 0, tzinfo=timezone.utc)

        # We use default parameters which should now include the first two flybys
        # (even though they are partly in shadow or lower than 40 degrees)
        # Note: We set magnitude_threshold higher to ensure we catch all of them.
        flybys = find_iss_flybys(
            topos_observer,
            vector_observer,
            start_date,
            end_date,
            magnitude_threshold=5.0
        )

        # We expect 3 visible flybys:
        # 1. 22:52 UTC (Alt ~21, partly in shadow)
        # 2. 00:28 UTC (Alt ~79, partly in shadow)
        # 3. 02:05 UTC (Alt ~65, sunlit)

        # The later ones (03:42 and 05:18 UTC) are in daylight (Sun Alt > -6)

        culmination_hours = [f['culmination_time'].hour for f in flybys]
        culmination_minutes = [f['culmination_time'].minute for f in flybys]

        print(f"Found {len(flybys)} flybys at {culmination_hours}:{culmination_minutes}")
        for f in flybys:
             print(f"  {f['culmination_time']} Alt: {f['peak_altitude']:.1f} Mag: {f['peak_magnitude']:.1f}")

        self.assertEqual(len(flybys), 3, f"Expected 3 visible flybys, found {len(flybys)}: {flybys}")

        # Verify specific flybys
        # Flyby 1 (~22:52 UTC)
        self.assertTrue(any(f['culmination_time'].hour == 22 and f['culmination_time'].minute == 52 for f in flybys))
        # Flyby 2 (~00:28 UTC)
        self.assertTrue(any(f['culmination_time'].hour == 0 and f['culmination_time'].minute == 28 for f in flybys))
        # Flyby 3 (~02:05 UTC)
        self.assertTrue(any(f['culmination_time'].hour == 2 and f['culmination_time'].minute == 5 for f in flybys))

if __name__ == "__main__":
    unittest.main()
