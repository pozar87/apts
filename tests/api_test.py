import unittest
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock

from skyfield.api import utc

from apts.api import get_events
from apts.constants.event_types import EventType


class TestApi(unittest.TestCase):
    @patch("apts.api.Observation")
    @patch("apts.api.Place")
    def test_get_events(self, mock_place, mock_observation):
        # Prepare mock objects
        mock_place_instance = MagicMock()
        mock_observation_instance = MagicMock()
        mock_place.return_value = mock_place_instance
        mock_observation.return_value = mock_observation_instance

        # Prepare input data
        lat = 52.2
        lon = 21.0
        start_date = datetime(2023, 1, 1, tzinfo=utc)
        end_date = datetime(2023, 1, 31, tzinfo=utc)
        elevation = 300
        events_to_calculate = [EventType.SOLAR_ECLIPSES]

        # Call the function
        get_events(
            lat=lat,
            lon=lon,
            start_date=start_date,
            end_date=end_date,
            elevation=elevation,
            events_to_calculate=events_to_calculate,
        )

        # Assert that the Place and Observation classes were instantiated correctly
        mock_place.assert_called_once_with(lat=lat, lon=lon, elevation=elevation)
        mock_observation.assert_called_once()

        # Assert that the get_astronomical_events method was called with the correct arguments
        mock_observation_instance.get_astronomical_events.assert_called_once_with(
            start_date=start_date,
            end_date=end_date,
            events_to_calculate=events_to_calculate,
        )


if __name__ == "__main__":
    unittest.main()
