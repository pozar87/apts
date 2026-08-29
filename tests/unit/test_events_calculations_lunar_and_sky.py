import unittest
from datetime import datetime, timezone
from unittest.mock import MagicMock, patch

import pandas as pd

from apts.events.calculations import (
    calculate_culminations,
    calculate_golden_blue_hours,
    calculate_lunar_eclipses,
    calculate_lunar_features,
    calculate_lunar_occultations,
    calculate_lunar_planetary_occultations,
    calculate_messier_culminations,
    calculate_meteor_showers,
    calculate_moon_apogee_perigee,
    calculate_moon_libration_maxima,
    calculate_moon_messier_conjunctions,
    calculate_moon_phases,
    calculate_moon_star_conjunctions,
    calculate_nasa_comets,
    calculate_seasons,
    calculate_solar_eclipses,
    calculate_supermoons,
)


class TestEventsCalculationsLunarAndSky(unittest.TestCase):
    def setUp(self):
        self.start_date = datetime(2025, 1, 1, tzinfo=timezone.utc)
        self.end_date = datetime(2025, 1, 2, tzinfo=timezone.utc)
        self.mock_observer = MagicMock()

    @patch("apts.events.calculations.lunar.almanac")
    def test_calculate_moon_phases(self, mock_almanac):
        mock_ts = MagicMock()
        mock_ti = MagicMock()
        mock_ti.utc_datetime.return_value = datetime(2025, 1, 1, 12, 0, tzinfo=timezone.utc)
        mock_almanac.moon_phases.return_value = MagicMock()
        mock_almanac.find_discrete.return_value = ([mock_ti], [0])
        mock_almanac.MOON_PHASES = ["New Moon"]

        res = calculate_moon_phases(mock_ts, self.start_date, self.end_date, MagicMock())
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["event"], "New Moon")
        self.assertEqual(res[0]["type"], "Moon Phase")

    @patch("apts.events.calculations.lunar.skyfield_searches.find_lunar_occultations")
    def test_calculate_lunar_occultations(self, mock_search):
        mock_search.return_value = [{"date": self.start_date, "star": "Spica"}]
        res = calculate_lunar_occultations(self.mock_observer, self.start_date, self.end_date, MagicMock())
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["type"], "Lunar Occultation")

    @patch("apts.events.calculations.lunar.skyfield_searches.find_lunar_planetary_occultations")
    def test_calculate_lunar_planetary_occultations(self, mock_search):
        mock_search.return_value = [{"date": self.start_date, "planet": "Mars"}]
        res = calculate_lunar_planetary_occultations(self.mock_observer, self.start_date, self.end_date)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["type"], "Lunar Planetary Occultation")

    @patch("apts.events.calculations.lunar.skyfield_searches.find_moon_apogee_perigee")
    def test_calculate_moon_apogee_perigee(self, mock_search):
        mock_search.return_value = [{"date": self.start_date, "event": "Perigee"}]
        res = calculate_moon_apogee_perigee(self.start_date, self.end_date)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["type"], "Moon Apogee/Perigee")

    @patch("apts.events.calculations.lunar.skyfield_searches.find_conjunctions_with_stars")
    @patch("apts.events.calculations.lunar.Star")
    def test_calculate_moon_messier_conjunctions(self, mock_star, mock_find_conj):
        mock_find_conj.return_value = [
            {"date": self.start_date, "object2": "M31", "separation_degrees": 2.0}
        ]
        mock_obs = MagicMock()
        spos = MagicMock()
        lats = MagicMock()
        lats.degrees = [0.0]  # within threshold
        spos.ecliptic_latlon.return_value = (lats, None, None)
        mock_obs.at.return_value.observe.return_value = spos

        messier_df = pd.DataFrame({
            "Messier": ["M1"],
            "ra_hours": [5.5],
            "dec_degrees": [22.0],
        })

        res = calculate_moon_messier_conjunctions(mock_obs, self.start_date, self.end_date, messier_df)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["type"], "Moon-Messier Conjunction")

    @patch("apts.events.calculations.lunar.skyfield_searches.find_conjunctions_with_stars")
    @patch("apts.events.calculations.lunar.Star")
    def test_calculate_moon_star_conjunctions(self, mock_star, mock_find_conj):
        mock_find_conj.return_value = [
            {"date": self.start_date, "object2": "Aldebaran", "separation_degrees": 1.5}
        ]
        mock_ts = MagicMock()
        mock_obs = MagicMock()
        spos = MagicMock()
        lats = MagicMock()
        lats.degrees = [0.0]
        spos.ecliptic_latlon.return_value = (lats, None, None)
        mock_obs.at.return_value.observe.return_value = spos

        bright_stars_df = pd.DataFrame({
            "Name": ["Aldebaran"],
            "ra_hours": [4.5],
            "dec_degrees": [16.5],
        })

        res = calculate_moon_star_conjunctions(mock_ts, mock_obs, self.start_date, self.end_date, bright_stars_df)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["type"], "Moon-Star Conjunction")

    @patch("apts.events.calculations.lunar.skyfield_searches.find_lunar_features")
    def test_calculate_lunar_features(self, mock_search):
        mock_search.return_value = [{"date": self.start_date, "event": "Lunar X", "type": "Lunar Feature"}]
        res = calculate_lunar_features(self.mock_observer, self.start_date, self.end_date)
        self.assertEqual(len(res), 1)

    @patch("apts.events.calculations.lunar.skyfield_searches.find_supermoons")
    def test_calculate_supermoons(self, mock_search):
        mock_search.return_value = [{"date": self.start_date, "event": "Supermoon", "type": "Supermoon"}]
        res = calculate_supermoons(self.start_date, self.end_date)
        self.assertEqual(len(res), 1)

    @patch("apts.events.calculations.lunar.skyfield_searches.find_lunar_eclipses")
    def test_calculate_lunar_eclipses(self, mock_search):
        mock_search.return_value = [{"date": self.start_date}]
        res = calculate_lunar_eclipses(self.mock_observer, self.start_date, self.end_date)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["type"], "Lunar Eclipse")

    @patch("apts.events.calculations.lunar.skyfield_searches.find_moon_libration_maxima")
    def test_calculate_moon_libration_maxima(self, mock_search):
        mock_search.return_value = [{"date": self.start_date, "event": "Libration Max", "type": "Moon Libration Maximum"}]
        res = calculate_moon_libration_maxima(self.mock_observer, self.start_date, self.end_date)
        self.assertEqual(len(res), 1)

    @patch("apts.events.calculations.sky.skyfield_searches.find_meteor_showers")
    def test_calculate_meteor_showers(self, mock_search):
        mock_search.return_value = [{"date": self.start_date, "event": "Perseids", "type": "Meteor Shower"}]
        res = calculate_meteor_showers(self.mock_observer, self.start_date, self.end_date)
        self.assertEqual(len(res), 1)

    @patch("apts.events.calculations.sky.skyfield_searches.find_solar_eclipses")
    def test_calculate_solar_eclipses(self, mock_search):
        mock_search.return_value = [{"date": self.start_date, "eclipse_type": "Total"}]
        res = calculate_solar_eclipses(self.mock_observer, self.start_date, self.end_date)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["type"], "Solar Eclipse")
        self.assertEqual(res[0]["event"], "Total Solar Eclipse")

    @patch("apts.events.calculations.sky.skyfield_searches.find_golden_blue_hours")
    def test_calculate_golden_blue_hours(self, mock_search):
        # Test disabled short-circuit
        res_empty = calculate_golden_blue_hours(
            self.mock_observer, self.start_date, self.end_date, {"golden_hour": False, "blue_hour": False}
        )
        self.assertEqual(res_empty, [])
        mock_search.assert_not_called()

        # Test enabled filter
        mock_search.return_value = [
            {"date": self.start_date, "type": "Golden Hour"},
            {"date": self.start_date, "type": "Blue Hour"},
        ]
        res = calculate_golden_blue_hours(
            self.mock_observer, self.start_date, self.end_date, {"golden_hour": True, "blue_hour": False}
        )
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["type"], "Golden Hour")

    @patch("apts.events.calculations.sky.skyfield_searches.find_culminations")
    def test_calculate_culminations(self, mock_search):
        mock_search.return_value = [{"date": self.start_date, "event": "Culmination"}]
        res = calculate_culminations(self.mock_observer, self.start_date, self.end_date)
        self.assertEqual(len(res), 1)

    @patch("apts.events.calculations.sky.skyfield_searches.find_object_culminations")
    def test_calculate_messier_culminations(self, mock_search):
        mock_search.return_value = [{"date": self.start_date, "event": "M31 Culmination"}]
        df = pd.DataFrame({"Messier": ["M31"], "skyfield_object": [MagicMock()]})
        res = calculate_messier_culminations(self.mock_observer, self.start_date, self.end_date, df)
        self.assertEqual(len(res), 1)

    @patch("apts.events.calculations.sky.skyfield_searches.find_seasons")
    def test_calculate_seasons(self, mock_search):
        mock_search.return_value = [{"date": self.start_date, "event": "Equinox"}]
        res = calculate_seasons(self.start_date, self.end_date)
        self.assertEqual(len(res), 1)

    @patch("apts.events.calculations.sky.cache.get_nasa_comets_data")
    def test_calculate_nasa_comets(self, mock_cache):
        # Empty
        mock_cache.return_value = pd.DataFrame()
        self.assertEqual(calculate_nasa_comets(self.start_date, self.end_date), [])

        # Non-empty
        mock_cache.return_value = pd.DataFrame([
            {
                "name": "Halley",
                "close_approach_data": [{"close_approach_date_full": "2025-Jan-01 12:00"}],
            }
        ])
        res = calculate_nasa_comets(self.start_date, self.end_date)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["event"], "Halley")
        self.assertEqual(res[0]["type"], "Comet")


if __name__ == "__main__":
    unittest.main()
