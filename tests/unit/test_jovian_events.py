import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime, timezone
import numpy as np
from skyfield.units import Angle, Distance
from apts.skyfield_searches import find_jovian_moon_events, find_jovian_mutual_events
from apts.place import Place

class TestJovianEventsMocked(unittest.TestCase):
    def setUp(self):
        self.place = Place(name="Test", lat=0, lon=0, elevation=-9999)
        self.start_date = datetime(2024, 1, 1, tzinfo=timezone.utc)
        self.end_date = datetime(2024, 1, 2, tzinfo=timezone.utc)

    @patch('apts.cache.get_timescale')
    @patch('apts.cache.get_jovian_ephemeris')
    @patch('apts.skyfield_searches.almanac.find_discrete')
    @patch('apts.skyfield_searches._get_jovian_moon_objects')
    @patch('apts.skyfield_searches.planetary.get_sub_observer_latitude')
    def test_find_jovian_moon_events_integration(self, mock_sub_lat, mock_get_moons, mock_find_discrete, mock_get_eph, mock_get_ts):
        mock_ts = MagicMock()
        mock_get_ts.return_value = mock_ts
        mock_eph = MagicMock()
        mock_get_eph.return_value = mock_eph

        mock_io = MagicMock()
        mock_get_moons.return_value = {"Io": mock_io}

        mock_sun = MagicMock()
        mock_jup = MagicMock()
        mock_eph.__getitem__.side_effect = lambda x: mock_sun if x == "sun" else mock_jup

        te = MagicMock()
        te.utc_datetime.return_value = datetime(2024, 1, 1, 12, 0, tzinfo=timezone.utc)
        mock_find_discrete.return_value = ([te], [1])

        observer = MagicMock()
        observer.vector_functions = [MagicMock(elevation=MagicMock(m=-9999))]

        # Geometry mocks
        j_obs = MagicMock()
        j_obs.altaz.return_value = (Angle(degrees=30), Angle(degrees=0), Distance(km=700000000))
        j_obs.distance.return_value = Distance(km=700000000)
        j_obs.separation_from.return_value = Angle(degrees=1.0)

        m_obs = MagicMock()
        m_obs.distance.return_value = Distance(km=699600000)

        observer.at.return_value.observe.return_value.apparent.return_value = j_obs

        mock_sub_lat.return_value = 0.0

        # Mock Sun observations
        mock_sun_obs_j = MagicMock()
        mock_sun_obs_j.position.au = np.array([5.2, 0, 0])
        mock_sun_obs_j.distance.return_value = Distance(au=5.2)
        mock_sun_obs_j.light_time = 0.04
        mock_sun_obs_j.apparent.return_value = j_obs
        mock_sun.at.return_value.observe.side_effect = [
            mock_sun_obs_j, # j_sun
            mock_sun_obs_j  # m_sun
        ] * 10

        with patch('apts.skyfield_searches.planetary.get_planet_pole_coords', return_value=(0, 90)):
            events = find_jovian_moon_events(observer, self.start_date, self.end_date)
            self.assertTrue(len(events) > 0)
            self.assertEqual(events[0]['object'], "Io")

    @patch('apts.cache.get_timescale')
    @patch('apts.cache.get_jovian_ephemeris')
    @patch('apts.skyfield_searches.almanac.find_discrete')
    @patch('apts.skyfield_searches._get_jovian_moon_objects')
    @patch('apts.skyfield_searches.planetary.get_sub_observer_latitude')
    @patch('apts.skyfield_searches.planetary.get_planet_pole_coords')
    def test_jovian_moon_state_func_logic(self, mock_pole, mock_sub_lat, mock_get_moons, mock_find_discrete, mock_get_eph, mock_get_ts):
        mock_ts = MagicMock()
        mock_get_ts.return_value = mock_ts
        mock_ts.tt_jd.side_effect = lambda x: x

        mock_eph = MagicMock()
        mock_get_eph.return_value = mock_eph
        mock_sun = MagicMock()
        mock_eph.__getitem__.side_effect = lambda x: mock_sun if x == "sun" else MagicMock()

        mock_get_moons.return_value = {"Io": MagicMock()}

        observer = MagicMock()
        observer.vector_functions = [MagicMock(elevation=MagicMock(m=-9999))]

        mock_find_discrete.return_value = ([], [])
        find_jovian_moon_events(observer, self.start_date, self.end_date)
        state_func = mock_find_discrete.call_args[0][2]

        t = MagicMock(shape=(), tt=2460000.0)

        j_obs = MagicMock()
        j_obs.altaz.return_value = (Angle(degrees=30), Angle(degrees=0), Distance(km=700000000))
        j_obs.distance.return_value = Distance(km=700000000)

        m_obs = MagicMock()
        m_obs.distance.return_value = Distance(km=699600000)

        j_obs.separation_from.return_value = Angle(degrees=0.001)

        observer.at.return_value.observe.side_effect = [
            MagicMock(apparent=lambda: j_obs),
            MagicMock(apparent=lambda: m_obs),
            MagicMock(apparent=lambda: j_obs)
        ] * 20

        mock_sub_lat.return_value = 0.0

        mock_j_sun = MagicMock()
        mock_j_sun.separation_from.return_value = Angle(degrees=1.0)
        mock_j_sun.distance.return_value = Distance(km=778000000)
        mock_m_sun = MagicMock()
        mock_m_sun.distance.return_value = Distance(km=778400000)

        mock_sun_at = mock_sun.at.return_value
        mock_sun_obs_j = MagicMock()
        mock_sun_obs_j.apparent.return_value = mock_j_sun
        mock_sun_obs_j.distance.return_value = Distance(au=5.2)
        mock_sun_obs_j.position.au = np.array([5.2, 0, 0])
        mock_sun_obs_j.light_time = 0.04

        mock_sun_obs_m = MagicMock()
        mock_sun_obs_m.apparent.return_value = mock_m_sun
        mock_sun_obs_m.distance.return_value = Distance(km=778400000)

        mock_sun_at.observe.side_effect = [
            mock_sun_obs_j, # j_sun
            mock_sun_obs_m, # m_sun
            mock_sun_obs_j  # pos_sj
        ] * 20

        mock_pole.return_value = (0, 90)

        res = state_func(t)
        self.assertEqual(res[0], 1) # Transit

        m_obs.distance.return_value = Distance(km=700400000)
        observer.at.return_value.observe.side_effect = [
            MagicMock(apparent=lambda: j_obs),
            MagicMock(apparent=lambda: m_obs),
            MagicMock(apparent=lambda: j_obs)
        ] * 20
        mock_sun_at.observe.side_effect = [
            mock_sun_obs_j,
            mock_sun_obs_m,
            mock_sun_obs_j
        ] * 20

        res = state_func(t)
        self.assertEqual(res[0], 2) # Occultation

    @patch('apts.cache.get_timescale')
    @patch('apts.cache.get_jovian_ephemeris')
    @patch('apts.skyfield_searches.almanac.find_discrete')
    @patch('apts.skyfield_searches._get_jovian_moon_objects')
    def test_find_jovian_mutual_events_integration(self, mock_get_moons, mock_find_discrete, mock_get_eph, mock_get_ts):
        mock_ts = MagicMock()
        mock_get_ts.return_value = mock_ts
        mock_eph = MagicMock()
        mock_get_eph.return_value = mock_eph
        mock_eph.__getitem__.return_value = MagicMock()

        mock_io = MagicMock()
        mock_eur = MagicMock()
        mock_get_moons.return_value = {"Io": mock_io, "Europa": mock_eur}

        te = MagicMock()
        te.utc_datetime.return_value = datetime(2024, 1, 1, 12, 0, tzinfo=timezone.utc)

        mock_find_discrete.side_effect = [
            ([te], [1]), # Occultation
            ([], []), # Eclipse 1
            ([], [])  # Eclipse 2
        ]

        observer = MagicMock()
        observer.vector_functions = [MagicMock(elevation=MagicMock(m=-9999))]

        observer.at.return_value.observe.return_value.distance.side_effect = [
            Distance(km=699000000), # Io
            Distance(km=700000000)  # Europa
        ]

        observer.at.return_value.observe.return_value.apparent.return_value = MagicMock(
            separation_from=lambda x: Angle(degrees=0),
            distance=lambda: Distance(km=700000000),
            altaz=lambda **kwargs: (Angle(degrees=30), None, None)
        )

        events = find_jovian_mutual_events(observer, self.start_date, self.end_date)

        self.assertEqual(len(events), 1)
        self.assertIn("Io occults Europa", events[0]['event'])

if __name__ == "__main__":
    unittest.main()
