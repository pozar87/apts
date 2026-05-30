import unittest
from datetime import datetime, timezone
from unittest.mock import MagicMock, patch
from apts.place import Place
from apts.skyfield_searches.jovian import find_jovian_mutual_events

class TestJovianMutualEvents(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=52.2297, lon=21.0122)
        self.start_date = datetime(2021, 1, 1, tzinfo=timezone.utc)
        self.end_date = datetime(2021, 1, 2, tzinfo=timezone.utc)

    @patch("apts.skyfield_searches.jovian.mutual.get_timescale")
    @patch("skyfield.almanac.find_discrete")
    @patch("apts.cache.get_jovian_ephemeris")
    def test_find_jovian_mutual_events_basic(self, mock_get_jovian_ephemeris, mock_find_discrete, mock_get_timescale):
        """Test that find_jovian_mutual_events returns correctly structured data when events are found."""
        # Mock timescale
        mock_ts = MagicMock()
        mock_get_timescale.return_value = mock_ts

        # Mock ts.utc(date) returns a Time object
        mock_t0 = MagicMock()
        mock_t0.shape = () # Scalar
        mock_ts.utc.return_value = mock_t0

        # Mock ephemeris
        mock_eph = MagicMock()
        mock_get_jovian_ephemeris.return_value = mock_eph

        # Mock moons and Jupiter/Sun
        mock_moon = MagicMock()

        # Mock find_discrete to return one event transition (0 -> 1)
        mock_t_event = MagicMock()
        mock_t_event.utc_datetime.return_value = datetime(2021, 1, 1, 12, 0, tzinfo=timezone.utc)
        mock_find_discrete.return_value = ([mock_t_event], [1]) # Transition to state 1 (Occultation)

        mock_observer = MagicMock()
        # Mock observer.at(t).observe(obj)
        mock_obs_pos = MagicMock()
        mock_observer.at.return_value.observe.return_value = mock_obs_pos

        # Mock separation and distance
        mock_obs_pos.separation_from.return_value.degrees = 0.001
        mock_obs_pos.distance.return_value.km = 600000000.0

        # Mock altaz for visibility (via Apparent)
        with patch("apts.skyfield_searches.jovian.utils.Apparent") as mock_app_class:
            mock_app = MagicMock()
            mock_app_class.return_value = mock_app
            mock_app.altaz.return_value = (MagicMock(degrees=45), None, None)
            mock_app.separation_from.return_value.degrees = 45 # for elongation

            # Mock j_obs.light_time
            mock_obs_pos.light_time = 0.03 # days

            # Mock observer elevation
            mock_vf = MagicMock()
            mock_vf.elevation.m = -9999
            mock_observer.vector_functions = [mock_vf]

            # Mock Sun perspective positions
            mock_sun = MagicMock()

            mock_m1_s = MagicMock()
            mock_m1_s.distance.return_value.km = 600001000.0
            mock_m1_s.separation_from.return_value.degrees = 0.002

            mock_m2_s = MagicMock()
            mock_m2_s.distance.return_value.km = 600002000.0

            # Chain for sun.at(t_emitted).observe(m1_obj)
            mock_sun.at.return_value.observe.side_effect = [mock_m1_s, mock_m2_s] * 100

            def eph_getitem(key):
                if key == "sun":
                    return mock_sun
                return mock_moon

            mock_eph.__getitem__.side_effect = eph_getitem

            events = find_jovian_mutual_events(mock_observer, self.start_date, self.end_date)

            self.assertIsInstance(events, list)
            self.assertGreater(len(events), 0)
            self.assertEqual(events[0]["type"], "Jovian Mutual Occultation")
            self.assertIn("Mutual Occultation", events[0]["event"])

    @patch("apts.cache.get_jovian_ephemeris")
    def test_find_jovian_mutual_events_empty(self, mock_get_jovian_ephemeris):
        """Test that find_jovian_mutual_events returns an empty list when no ephemeris is found."""
        mock_get_jovian_ephemeris.return_value = {} # Empty dict will cause KeyError in find_jovian_mutual_events

        # Use a dummy observer to avoid more mocking
        events = find_jovian_mutual_events(MagicMock(), self.start_date, self.end_date)
        self.assertEqual(events, [])

if __name__ == "__main__":
    unittest.main()
