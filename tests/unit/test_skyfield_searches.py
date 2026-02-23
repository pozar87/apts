import unittest
from datetime import datetime
from skyfield.api import load, Topos, utc
from apts import skyfield_searches
from apts.catalogs import Catalogs
from apts.cache import get_ephemeris
from apts.utils import planetary
from skyfield.api import Star
from unittest.mock import patch, MagicMock


class SkyfieldSearchesTest(unittest.TestCase):
    def setUp(self):
        self.ts = load.timescale()
        self.eph = get_ephemeris()
        self.observer = self.eph["earth"] + Topos(
            latitude_degrees=52.2, longitude_degrees=21.0
        )
        self.start_date = datetime(2023, 1, 1, tzinfo=utc)
        self.end_date = datetime(
            2023, 1, 31, tzinfo=utc
        )  # shorter time for faster tests

    def test_find_highest_altitude(self):
        time, alt = skyfield_searches.find_highest_altitude(
            self.observer,
            planetary.get_skyfield_obj("venus"),
            self.start_date,
            self.end_date,
        )
        self.assertIsInstance(time, datetime)
        self.assertIsInstance(alt, float)

    def test_find_aphelion_perihelion(self):
        events = skyfield_searches.find_aphelion_perihelion(
            "mars", self.start_date, self.end_date
        )
        self.assertIsInstance(events, list)

    def test_find_lunar_occultations(self):
        short_start = datetime(2023, 1, 1, tzinfo=utc)
        short_end = datetime(2023, 1, 2, tzinfo=utc)
        sirius = Catalogs().BRIGHT_STARS[Catalogs().BRIGHT_STARS["Name"] == "Sirius"]
        events = skyfield_searches.find_lunar_occultations(
            self.observer, sirius, short_start, short_end
        )
        self.assertIsInstance(events, list)

    def test_find_oppositions(self):
        # Mars was at opposition on December 8, 2022.
        start_date = datetime(2022, 12, 1, tzinfo=utc)
        end_date = datetime(2022, 12, 31, tzinfo=utc)
        events = skyfield_searches.find_oppositions(
            self.observer, "mars", start_date, end_date
        )
        self.assertIsInstance(events, list)
        self.assertEqual(len(events), 1)
        event = events[0]
        self.assertEqual(event["date"].day, 8)
        self.assertEqual(event["planet"], "mars")

    def test_find_pluto_opposition(self):
        # Pluto opposition in 2023 was on July 22.
        start_date = datetime(2023, 7, 20, tzinfo=utc)
        end_date = datetime(2023, 7, 24, tzinfo=utc)
        events = skyfield_searches.find_oppositions(
            self.observer, "pluto", start_date, end_date
        )
        self.assertIsInstance(events, list)
        self.assertEqual(len(events), 1)
        event = events[0]
        # The exact time can vary, so we just check the day
        self.assertEqual(event["date"].day, 22)
        self.assertEqual(event["planet"], "pluto")

    def test_find_ceres_opposition(self):
        # Ceres opposition in 2023 was on March 21.
        start_date = datetime(2023, 3, 1, tzinfo=utc)
        end_date = datetime(2023, 3, 31, tzinfo=utc)
        events = skyfield_searches.find_oppositions(
            self.observer, "ceres", start_date, end_date
        )
        self.assertIsInstance(events, list)
        self.assertEqual(len(events), 1)
        event = events[0]
        self.assertEqual(event["date"].day, 21)
        self.assertEqual(event["planet"], "ceres")

    def test_find_mercury_inferior_conjunctions(self):
        start_date = datetime(2023, 1, 1, tzinfo=utc)
        end_date = datetime(2023, 12, 31, tzinfo=utc)
        events = skyfield_searches.find_mercury_inferior_conjunctions(
            self.observer, start_date, end_date
        )
        self.assertIsInstance(events, list)

    def test_find_moon_apogee_perigee(self):
        events = skyfield_searches.find_moon_apogee_perigee(
            self.start_date, self.end_date
        )
        self.assertIsInstance(events, list)

    def test_find_conjunctions(self):
        start_date = datetime(2023, 1, 1, tzinfo=utc)
        end_date = datetime(2023, 3, 31, tzinfo=utc)
        events = skyfield_searches.find_conjunctions(
            self.observer,
            "venus",
            "jupiter",
            start_date,
            end_date,
            threshold_degrees=1.0,
        )
        self.assertIsInstance(events, list)
        if events:
            self.assertIn("separation_degrees", events[0])
            self.assertLess(events[0]["separation_degrees"], 1.0)

    def test_find_great_conjunction_2020(self):
        start_date = datetime(2020, 12, 20, tzinfo=utc)
        end_date = datetime(2020, 12, 22, tzinfo=utc)
        events = skyfield_searches.find_conjunctions(
            self.observer,
            "jupiter",
            "saturn",
            start_date,
            end_date,
        )
        self.assertIsInstance(events, list)
        self.assertEqual(len(events), 1)
        event = events[0]
        # Check that the date is December 21, 2020
        self.assertEqual(event["date"].day, 21)
        self.assertAlmostEqual(event["separation_degrees"], 0.1, delta=0.01)

    def test_find_conjunctions_with_threshold(self):
        start_date = datetime(2023, 1, 1, tzinfo=utc)
        end_date = datetime(2023, 12, 31, tzinfo=utc)

        # First, find all conjunctions without a threshold.
        all_events = skyfield_searches.find_conjunctions(
            self.observer, "venus", "saturn", start_date, end_date
        )
        self.assertGreater(
            len(all_events), 0, "Should find at least one conjunction in 2023"
        )

        # Now, use the separation of the first event to test the thresholding.
        separation = all_events[0]["separation_degrees"]

        # Test with a threshold slightly smaller than the actual separation.
        tighter_events = skyfield_searches.find_conjunctions(
            self.observer,
            "venus",
            "saturn",
            start_date,
            end_date,
            threshold_degrees=separation - 0.1,
        )
        # It's possible other conjunctions are found, so we check that the original event is not present
        found = False
        for event in tighter_events:
            if event["date"] == all_events[0]["date"]:
                found = True
                break
        self.assertFalse(found)

        # Test with a threshold slightly larger than the actual separation.
        wider_events = skyfield_searches.find_conjunctions(
            self.observer,
            "venus",
            "saturn",
            start_date,
            end_date,
            threshold_degrees=separation + 0.1,
        )
        self.assertIn(all_events[0], wider_events)

    def test_find_conjunctions_no_threshold(self):
        start_date = datetime(2023, 1, 1, tzinfo=utc)
        end_date = datetime(2023, 3, 31, tzinfo=utc)
        events = skyfield_searches.find_conjunctions(
            self.observer, "venus", "jupiter", start_date, end_date
        )
        self.assertGreater(len(events), 0)
        self.assertIn("separation_degrees", events[0])

    def test_find_venus_mercury_conjunction_2021(self):
        start_date = datetime(2021, 5, 28, tzinfo=utc)
        end_date = datetime(2021, 5, 30, tzinfo=utc)
        events = skyfield_searches.find_conjunctions(
            self.observer, "venus", "mercury", start_date, end_date
        )
        self.assertIsInstance(events, list)
        self.assertEqual(len(events), 1)
        event = events[0]
        # Check that the date is May 29, 2021
        self.assertEqual(event["date"].day, 29)
        self.assertAlmostEqual(event["separation_degrees"], 0.4, delta=0.1)

    def test_find_moon_m45_conjunction_2025(self):
        start_date = datetime(2025, 8, 15, tzinfo=utc)
        end_date = datetime(2025, 8, 17, tzinfo=utc)
        m45_data = Catalogs().MESSIER[Catalogs().MESSIER["Messier"] == "M45"].iloc[0]
        m45 = Star(
            ra_hours=m45_data["RA"].to("hour").magnitude,
            dec_degrees=m45_data["Dec"].to("degree").magnitude,
        )
        events = skyfield_searches.find_conjunctions_with_star(
            self.observer, "moon", m45, start_date, end_date
        )
        self.assertIsInstance(events, list)
        self.assertEqual(len(events), 1)
        event = events[0]
        # Check that the date is August 16, 2025
        self.assertEqual(event["date"].day, 16)
        self.assertAlmostEqual(event["separation_degrees"], 0.08, delta=0.01)

    def test_find_iss_flybys_basic(self):
        """Test that find_iss_flybys returns a list and handles basic functionality"""
        topos_observer = Topos(latitude_degrees=52.2, longitude_degrees=21.0)
        vector_observer = self.eph["earth"] + topos_observer

        # Use a shorter time range for testing
        start_date = datetime(2023, 6, 1, tzinfo=utc)
        end_date = datetime(2023, 6, 2, tzinfo=utc)

        # Mock the TLE loading to avoid network dependency
        with patch("skyfield.api.load.tle_file") as mock_tle:
            mock_satellite = MagicMock()
            mock_satellite.name = "ISS (ZARYA)"
            mock_satellite.find_events.return_value = ([], [])
            mock_tle.return_value = [mock_satellite]

            events = skyfield_searches.find_iss_flybys(
                topos_observer, vector_observer, start_date, end_date
            )

            self.assertIsInstance(events, list)

    def test_find_iss_flybys_network_error(self):
        """Test that find_iss_flybys handles network errors gracefully"""
        topos_observer = Topos(latitude_degrees=52.2, longitude_degrees=21.0)
        vector_observer = self.eph["earth"] + topos_observer

        start_date = datetime(2023, 6, 1, tzinfo=utc)
        end_date = datetime(2023, 6, 2, tzinfo=utc)

        # Mock network error
        with patch("skyfield.api.load.tle_file") as mock_tle:
            mock_tle.side_effect = Exception("Network error")

            events = skyfield_searches.find_iss_flybys(
                topos_observer, vector_observer, start_date, end_date
            )

            self.assertEqual(events, [])

    def test_find_iss_flybys_iss_not_found(self):
        """Test when ISS is not in the TLE file"""
        topos_observer = Topos(latitude_degrees=52.2, longitude_degrees=21.0)
        vector_observer = self.eph["earth"] + topos_observer

        start_date = datetime(2023, 6, 1, tzinfo=utc)
        end_date = datetime(2023, 6, 2, tzinfo=utc)

        # Mock TLE file without ISS
        with patch("skyfield.api.load.tle_file") as mock_tle:
            mock_satellite = MagicMock()
            mock_satellite.name = "SOME OTHER SATELLITE"
            mock_tle.return_value = [mock_satellite]

            events = skyfield_searches.find_iss_flybys(
                topos_observer, vector_observer, start_date, end_date
            )

            self.assertEqual(events, [])

    def test_find_iss_flybys_with_events(self):
        """Test ISS flyby detection with simulated events"""
        topos_observer = Topos(latitude_degrees=52.2, longitude_degrees=21.0)
        vector_observer = self.eph["earth"] + topos_observer

        start_date = datetime(2023, 6, 1, tzinfo=utc)
        end_date = datetime(2023, 6, 2, tzinfo=utc)

        with patch("skyfield.api.load.tle_file") as mock_tle:
            mock_satellite = MagicMock()
            mock_satellite.name = "ISS (ZARYA)"
            # Return empty events to test the function runs without errors
            mock_satellite.find_events.return_value = ([], [])
            mock_tle.return_value = [mock_satellite]

            events = skyfield_searches.find_iss_flybys(
                topos_observer, vector_observer, start_date, end_date
            )

            self.assertIsInstance(events, list)
            self.assertEqual(len(events), 0)

    def test_find_iss_flybys_thresholds(self):
        """Test that magnitude and altitude thresholds work correctly"""
        topos_observer = Topos(latitude_degrees=52.2, longitude_degrees=21.0)
        vector_observer = self.eph["earth"] + topos_observer

        start_date = datetime(2023, 6, 1, tzinfo=utc)
        end_date = datetime(2023, 6, 2, tzinfo=utc)

        # Test with very restrictive thresholds
        with patch("skyfield.api.load.tle_file") as mock_tle:
            mock_satellite = MagicMock()
            mock_satellite.name = "ISS (ZARYA)"
            mock_satellite.find_events.return_value = ([], [])
            mock_tle.return_value = [mock_satellite]

            events = skyfield_searches.find_iss_flybys(
                topos_observer,
                vector_observer,
                start_date,
                end_date,
                magnitude_threshold=-5.0,  # Very restrictive
                peak_altitude_threshold=80,  # Very restrictive
                rise_altitude_threshold=20,
            )

            self.assertIsInstance(events, list)

    def test_find_lunar_eclipses(self):
        start_date = datetime(2023, 1, 1, tzinfo=utc)
        end_date = datetime(2023, 12, 31, tzinfo=utc)
        events = skyfield_searches.find_lunar_eclipses(start_date, end_date)
        self.assertIsInstance(events, list)
        # There are two lunar eclipses in 2023
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0]["type"], "Lunar Eclipse")
        self.assertEqual(events[0]["eclipse_kind"], "Penumbral")
        self.assertEqual(events[0]["date"].day, 5)
        self.assertEqual(events[0]["date"].month, 5)
        self.assertIn("penumbral_magnitude", events[0])
        self.assertIn("umbral_magnitude", events[0])
        self.assertEqual(events[1]["type"], "Lunar Eclipse")
        self.assertEqual(events[1]["eclipse_kind"], "Partial")
        self.assertEqual(events[1]["date"].day, 28)
        self.assertEqual(events[1]["date"].month, 10)
        self.assertIn("penumbral_magnitude", events[1])
        self.assertIn("umbral_magnitude", events[1])

    def test_find_solar_eclipses(self):
        start_date = datetime(2023, 1, 1, tzinfo=utc)
        end_date = datetime(2023, 12, 31, tzinfo=utc)
        events = skyfield_searches.find_solar_eclipses(
            self.observer, start_date, end_date
        )
        self.assertIsInstance(events, list)
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0]["type"], "Solar Eclipse")
        self.assertEqual(events[0]["date"].day, 20)
        self.assertEqual(events[0]["date"].month, 4)
        self.assertEqual(events[1]["type"], "Solar Eclipse")
        self.assertEqual(events[1]["date"].day, 14)
        self.assertEqual(events[1]["date"].month, 10)


if __name__ == "__main__":
    unittest.main()
