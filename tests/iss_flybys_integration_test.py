import unittest
from datetime import datetime
from skyfield.api import load, Topos, utc
from unittest.mock import patch, MagicMock
from apts import skyfield_searches


class ISSFlybysIntegrationTest(unittest.TestCase):
    """Integration tests for ISS flyby detection functionality"""

    def setUp(self):
        self.ts = load.timescale()
        self.eph = load("de421.bsp")
        self.topos_observer = Topos(latitude_degrees=52.2, longitude_degrees=21.0)
        self.vector_observer = self.eph["earth"] + self.topos_observer
        self.start_date = datetime(2023, 6, 1, tzinfo=utc)
        self.end_date = datetime(2023, 6, 2, tzinfo=utc)

    def test_tle_load_network_error(self):
        """Test graceful handling of network errors when loading TLE"""
        with patch("skyfield.api.load.tle_file") as mock_tle:
            mock_tle.side_effect = Exception("Network connection failed")

            events = skyfield_searches.find_iss_flybys(
                self.topos_observer,
                self.vector_observer,
                self.start_date,
                self.end_date,
            )

            self.assertEqual(events, [])

    def test_no_iss_in_tle_file(self):
        """Test graceful handling when ISS is not found in TLE file"""
        with patch("skyfield.api.load.tle_file") as mock_tle:
            # Mock TLE file with other satellites but no ISS
            mock_other_sat = MagicMock()
            mock_other_sat.name = "HUBBLE SPACE TELESCOPE"
            mock_tle.return_value = [mock_other_sat]

            # This should raise StopIteration when looking for ISS
            events = skyfield_searches.find_iss_flybys(
                self.topos_observer,
                self.vector_observer,
                self.start_date,
                self.end_date,
            )

            self.assertEqual(len(events), 0)

    def test_empty_events_from_find_events(self):
        """Test handling when find_events returns no events"""
        with patch("skyfield.api.load.tle_file") as mock_tle:
            mock_satellite = MagicMock()
            mock_satellite.name = "ISS (ZARYA)"
            mock_satellite.find_events.return_value = ([], [])  # No events
            mock_tle.return_value = [mock_satellite]

            events = skyfield_searches.find_iss_flybys(
                self.topos_observer,
                self.vector_observer,
                self.start_date,
                self.end_date,
            )

            self.assertEqual(len(events), 0)

    def test_function_parameters_and_defaults(self):
        """Test that the function accepts all expected parameters"""
        with patch("skyfield.api.load.tle_file") as mock_tle:
            mock_satellite = MagicMock()
            mock_satellite.name = "ISS (ZARYA)"
            mock_satellite.find_events.return_value = ([], [])
            mock_tle.return_value = [mock_satellite]

            # Test with custom parameters
            events = skyfield_searches.find_iss_flybys(
                self.topos_observer,
                self.vector_observer,
                self.start_date,
                self.end_date,
                magnitude_threshold=-2.0,
                peak_altitude_threshold=30,
                rise_altitude_threshold=5,
            )

            self.assertIsInstance(events, list)
            self.assertEqual(len(events), 0)

    def test_basic_function_signature(self):
        """Test that the function has the correct signature and returns a list"""
        with patch("skyfield.api.load.tle_file") as mock_tle:
            mock_satellite = MagicMock()
            mock_satellite.name = "ISS (ZARYA)"
            mock_satellite.find_events.return_value = ([], [])
            mock_tle.return_value = [mock_satellite]

            # Test basic call
            events = skyfield_searches.find_iss_flybys(
                self.topos_observer,
                self.vector_observer,
                self.start_date,
                self.end_date,
            )

            self.assertIsInstance(events, list)

    def test_tle_url_is_correct(self):
        """Test that the correct TLE URL is used"""
        with patch("skyfield.api.load.tle_file") as mock_tle:
            mock_satellite = MagicMock()
            mock_satellite.name = "ISS (ZARYA)"
            mock_satellite.find_events.return_value = ([], [])
            mock_tle.return_value = [mock_satellite]

            skyfield_searches.find_iss_flybys(
                self.topos_observer,
                self.vector_observer,
                self.start_date,
                self.end_date,
            )

            # Verify the correct URL was called
            mock_tle.assert_called_once_with(
                "https://celestrak.org/NORAD/elements/stations.txt", reload=True
            )

    def test_iss_name_search(self):
        """Test that the function looks for ISS with correct name"""
        with patch("skyfield.api.load.tle_file") as mock_tle:
            # Create multiple satellites with different names
            mock_sat1 = MagicMock()
            mock_sat1.name = "HUBBLE SPACE TELESCOPE"
            mock_sat2 = MagicMock()
            mock_sat2.name = "ISS (ZARYA)"
            mock_sat2.find_events.return_value = ([], [])
            mock_sat3 = MagicMock()
            mock_sat3.name = "TIANGONG"

            mock_tle.return_value = [mock_sat1, mock_sat2, mock_sat3]

            events = skyfield_searches.find_iss_flybys(
                self.topos_observer,
                self.vector_observer,
                self.start_date,
                self.end_date,
            )

            # Should find ISS and call find_events on it
            mock_sat2.find_events.assert_called_once()
            self.assertIsInstance(events, list)

    def test_return_structure_when_no_events(self):
        """Test that function returns proper structure even with no events"""
        with patch("skyfield.api.load.tle_file") as mock_tle:
            mock_satellite = MagicMock()
            mock_satellite.name = "ISS (ZARYA)"
            mock_satellite.find_events.return_value = ([], [])
            mock_tle.return_value = [mock_satellite]

            events = skyfield_searches.find_iss_flybys(
                self.topos_observer,
                self.vector_observer,
                self.start_date,
                self.end_date,
            )

            self.assertIsInstance(events, list)
            self.assertEqual(len(events), 0)

    def test_time_conversion_handling(self):
        """Test that the function properly handles time conversions"""
        from skyfield.api import Time

        with patch("skyfield.api.load.tle_file") as mock_tle:
            mock_satellite = MagicMock()
            mock_satellite.name = "ISS (ZARYA)"
            mock_satellite.find_events.return_value = ([], [])
            mock_tle.return_value = [mock_satellite]

            # Test with different date formats
            events = skyfield_searches.find_iss_flybys(
                self.topos_observer,
                self.vector_observer,
                datetime(2023, 1, 1, tzinfo=utc),
                datetime(2023, 1, 2, tzinfo=utc),
            )

            # Should not raise any time conversion errors
            self.assertIsInstance(events, list)

    def test_exception_handling_during_processing(self):
        """Test exception handling during ISS search and processing"""
        with patch("skyfield.api.load.tle_file") as mock_tle:
            # Simulate an error during satellite search
            def bad_generator():
                raise StopIteration("ISS not found")

            mock_tle.side_effect = lambda *args, **kwargs: bad_generator()

            events = skyfield_searches.find_iss_flybys(
                self.topos_observer,
                self.vector_observer,
                self.start_date,
                self.end_date,
            )

            # Should handle the exception gracefully
            self.assertEqual(events, [])


if __name__ == "__main__":
    unittest.main()
