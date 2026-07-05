import unittest
from datetime import datetime, timezone
from skyfield.api import Topos
from apts.skyfield_searches import find_iss_flybys
from apts.cache import get_ephemeris

class TestISSFlybysKrakow(unittest.TestCase):
    def test_krakow_flybys_april_2026(self):
        # Krakow (50.095, 19.89)
        lat, lon = 50.095, 19.89
        topos_observer = Topos(latitude_degrees=lat, longitude_degrees=lon)

        eph = get_ephemeris()
        earth = eph["earth"]
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
            magnitude_threshold=5.0,
        )

        # We expect 3 visible flybys (updated based on current TLE for April 2026):
        # 1. 23:20 UTC on 29th (Alt ~33)
        # 2. 00:56 UTC on 30th (Alt ~81)
        # 3. 02:34 UTC on 30th (Alt ~69)

        culmination_hours = [f["culmination_time"].hour for f in flybys]
        culmination_minutes = [f["culmination_time"].minute for f in flybys]

        print(
            f"Found {len(flybys)} flybys at {culmination_hours}:{culmination_minutes}"
        )
        for f in flybys:
            print(
                f"  {f['culmination_time']} Alt: {f['peak_altitude']:.1f} Mag: {f['peak_magnitude']:.1f}"
            )

        self.assertEqual(
            len(flybys), 3, f"Expected 3 visible flybys, found {len(flybys)}: {flybys}"
        )

        # Verify specific flybys with a 5-minute tolerance to account for TLE drift
        def assert_flyby_near(target_time, label):
            found = False
            for f in flybys:
                diff = abs((f["culmination_time"] - target_time).total_seconds())
                if diff <= 300:  # 5 minutes
                    found = True
                    break
            self.assertTrue(
                found,
                f"Could not find {label} flyby near {target_time}. Closest found were: {[f['culmination_time'] for f in flybys]}",
            )

        # Updated times based on current TLE propagation
        assert_flyby_near(datetime(2026, 4, 29, 23, 20, tzinfo=timezone.utc), "23:20")
        assert_flyby_near(datetime(2026, 4, 30, 0, 56, tzinfo=timezone.utc), "00:56")
        assert_flyby_near(datetime(2026, 4, 30, 2, 34, tzinfo=timezone.utc), "02:34")

if __name__ == "__main__":
    unittest.main()
