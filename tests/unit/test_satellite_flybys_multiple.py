import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch
import numpy as np
from skyfield.api import load, Topos

from apts.skyfield_searches import _find_satellite_flybys

class TestSatelliteFlybysMultiple(unittest.TestCase):
    def setUp(self):
        self.ts = load.timescale()
        self.topos_observer = Topos(latitude_degrees=52.2, longitude_degrees=21.0)
        self.vector_observer = MagicMock()
        self.start_date = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        self.end_date = self.start_date + timedelta(days=1)

    @patch("apts.skyfield_searches.load.tle_file")
    @patch("apts.skyfield_searches.get_timescale")
    @patch("apts.skyfield_searches.planetary.get_skyfield_obj")
    @patch("apts.skyfield_searches.get_ephemeris")
    @patch("apts.skyfield_searches.calculate_satellite_magnitude")
    def test_multiple_flybys_detection(
        self, mock_mag, mock_eph, mock_get_obj, mock_ts, mock_tle
    ):
        mock_ts.return_value = self.ts
        mock_satellite = MagicMock()
        mock_satellite.name = "ISS (ZARYA)"

        # Pass 1: Full pass in window
        t1_rise = self.ts.utc(self.start_date + timedelta(minutes=10))
        t1_culm = self.ts.utc(self.start_date + timedelta(minutes=15))
        t1_set = self.ts.utc(self.start_date + timedelta(minutes=20))

        # Pass 2: Culmination at start of window (Rise is before window)
        t2_rise = self.ts.utc(self.start_date - timedelta(minutes=3))
        t2_culm = self.ts.utc(self.start_date + timedelta(minutes=2))
        t2_set = self.ts.utc(self.start_date + timedelta(minutes=7))

        # Pass 3: Culmination at end of window (Set is after window)
        t3_rise = self.ts.utc(self.end_date - timedelta(minutes=7))
        t3_culm = self.ts.utc(self.end_date - timedelta(minutes=2))
        t3_set = self.ts.utc(self.end_date + timedelta(minutes=3))

        # Pass 4: Another full pass
        t4_rise = self.ts.utc(self.start_date + timedelta(hours=5))
        t4_culm = self.ts.utc(self.start_date + timedelta(hours=5, minutes=5))
        t4_set = self.ts.utc(self.start_date + timedelta(hours=5, minutes=10))

        # Expected events from find_events in the MAIN window [start_date, end_date]:
        # Pass 2 culmination (1), Pass 2 set (2)
        # Pass 1 rise (0), Pass 1 culmination (1), Pass 1 set (2)
        # Pass 4 rise (0), Pass 4 culmination (1), Pass 4 set (2)
        # Pass 3 rise (0), Pass 3 culmination (1)

        mock_satellite.find_events.side_effect = [
            # Main call
            (
                [t2_culm, t2_set, t1_rise, t1_culm, t1_set, t4_rise, t4_culm, t4_set, t3_rise, t3_culm],
                np.array([1, 2, 0, 1, 2, 0, 1, 2, 0, 1])
            ),
            # Search for Pass 2 rise
            (
                [t2_rise],
                np.array([0])
            ),
            # Search for Pass 3 set
            (
                [t3_set],
                np.array([2])
            )
        ]
        mock_tle.return_value = [mock_satellite]

        # Mock Sun altitude (dark sky)
        mock_sun_alt = MagicMock(degrees=-20)
        self.vector_observer.at.return_value.observe.return_value.apparent.return_value.altaz.return_value = (mock_sun_alt, None, None)

        # Mock satellite position and sunlit status
        mock_sat_at = MagicMock()
        mock_sat_at.is_sunlit.return_value = True
        mock_sat_at.position.km = np.array([7000, 0, 0])

        # Mock topocentric altaz
        mock_topocentric = MagicMock()
        mock_topocentric.altaz.return_value = (MagicMock(degrees=50), MagicMock(degrees=180), MagicMock(km=500))
        mock_sat_at.__sub__.return_value = mock_topocentric
        mock_satellite.at.return_value = mock_sat_at

        # Mock magnitude
        mock_mag.return_value = -2.0

        # Mock topos_observer
        mock_topos = MagicMock()
        mock_topos.at.return_value.position.km = np.array([6400, 0, 0])

        events = _find_satellite_flybys(
            mock_topos,
            self.vector_observer,
            self.start_date,
            self.end_date,
            "ISS (ZARYA)",
            "Test Flyby",
            "ISS Flyby",
            magnitude_threshold=0,
        )

        # Assertions
        print(f"Detected {len(events)} events")
        for i, event in enumerate(events):
            print(f"Event {i}: Culm: {event['culmination_time']}, Rise: {event['rise_time']}, Set: {event['set_time']}")

        self.assertEqual(len(events), 4, f"Should have detected 4 flybys, but got {len(events)}")

        # Verify Pass 2 (rise before window)
        self.assertEqual(events[0]["culmination_time"], t2_culm.utc_datetime())
        self.assertEqual(events[0]["rise_time"], t2_rise.utc_datetime())

        # Verify Pass 3 (set after window)
        self.assertEqual(events[3]["culmination_time"], t3_culm.utc_datetime())
        self.assertEqual(events[3]["set_time"], t3_set.utc_datetime())

if __name__ == "__main__":
    unittest.main()
