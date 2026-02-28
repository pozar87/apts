import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

import numpy as np
from skyfield.api import Topos

from apts.skyfield_searches import (
    _find_satellite_flybys,
    find_iss_flybys,
    find_tiangong_flybys,
)


class TestSatelliteFlybys(unittest.TestCase):
    def setUp(self):
        self.topos_observer = Topos(latitude_degrees=52.2297, longitude_degrees=21.0122)
        # Mocking a vector observer (earth + topos)
        self.vector_observer = MagicMock()
        self.start_date = datetime(2024, 1, 1, tzinfo=timezone.utc)
        self.end_date = self.start_date + timedelta(days=1)

    @patch("apts.skyfield_searches.load.tle_file")
    @patch("apts.skyfield_searches.get_timescale")
    @patch("apts.skyfield_searches.planetary.get_skyfield_obj")
    @patch("apts.skyfield_searches.get_ephemeris")
    def test_find_satellite_flybys_logic(
        self, mock_eph, mock_get_obj, mock_ts, mock_tle
    ):
        # Setup mocks
        from skyfield.api import load

        ts = load.timescale()
        mock_ts.return_value = ts

        mock_satellite = MagicMock()
        mock_satellite.name = "ISS (ZARYA)"

        # Simulate one culmination event
        t_rise = ts.utc(self.start_date)
        t_culm = ts.utc(self.start_date + timedelta(hours=1))
        t_set = ts.utc(self.start_date + timedelta(hours=2))

        # mock_satellite.find_events returns (times, event_codes)
        # codes: 0=rise, 1=culmination, 2=set
        mock_satellite.find_events.return_value = (
            [t_rise, t_culm, t_set],
            [0, 1, 2],
        )
        mock_tle.return_value = [mock_satellite]

        # Mock Sun position
        mock_sun = MagicMock()
        mock_get_obj.return_value = mock_sun

        # Mock Sun altitude (must be < -18 for dark sky)
        mock_sun_pos = MagicMock()
        mock_sun_pos.apparent.return_value.altaz.return_value = (
            MagicMock(degrees=-20),
            None,
            None,
        )

        # Mock Satellite position and altitude
        mock_sat_at_t = MagicMock()
        mock_satellite.at.return_value = mock_sat_at_t

        # Sunlit check (must be True)
        mock_sat_at_t.is_sunlit.return_value = True

        # Position for magnitude calculation
        mock_sat_at_t.position.km = np.array([7000.0, 0.0, 0.0])

        # Mock Observer and Sun for magnitude
        mock_obs_at_t = MagicMock()
        mock_obs_at_t.position.km = np.array([6371.0, 0.0, 0.0])

        # Mock vector_observer.at(t) to return a mock that can observe things
        self.vector_observer.at.return_value = mock_obs_at_t

        # Mock observing the sun
        def mock_observe(obj):
            if obj == mock_sun:
                return mock_sun_pos
            return MagicMock()

        mock_obs_at_t.observe.side_effect = mock_observe

        # Mock Sun position for magnitude calculation (Sun behind observer for low phase angle)
        mock_sun.at.return_value.position.km = np.array([-150000000.0, 0.0, 0.0])

        # Mock topocentric altaz
        mock_topocentric = MagicMock()
        mock_sat_at_t.__sub__.return_value = mock_topocentric
        # alt, az, distance
        mock_topocentric.altaz.return_value = (
            MagicMock(degrees=45),
            MagicMock(degrees=180),
            MagicMock(km=500),
        )

        # Mock topos_observer to return mock_obs_at_t when at() is called
        mock_topos = MagicMock()
        mock_topos.at.return_value = mock_obs_at_t

        # Execute
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
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["event"], "Test Flyby")
        self.assertIn("peak_magnitude", events[0])
        self.assertLess(events[0]["peak_magnitude"], 0)
        self.assertEqual(events[0]["peak_altitude"], 45)

    @patch("apts.skyfield_searches._find_satellite_flybys")
    def test_find_iss_flybys_wrapper(self, mock_find):
        find_iss_flybys(
            self.topos_observer, self.vector_observer, self.start_date, self.end_date
        )
        mock_find.assert_called_once()
        args = mock_find.call_args[0]
        self.assertEqual(args[4], "ISS (ZARYA)")

    @patch("apts.skyfield_searches._find_satellite_flybys")
    def test_find_tiangong_flybys_wrapper(self, mock_find):
        find_tiangong_flybys(
            self.topos_observer, self.vector_observer, self.start_date, self.end_date
        )
        mock_find.assert_called_once()
        args = mock_find.call_args[0]
        self.assertEqual(args[4], "CSS (TIANHE)")


if __name__ == "__main__":
    unittest.main()
