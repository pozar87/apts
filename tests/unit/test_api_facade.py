import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from skyfield.api import utc
from apts.api import get_events

class TestApi(unittest.TestCase):
    @patch("apts.api.Place")
    @patch("apts.api.Equipment")
    @patch("apts.api.Observation")
    def test_get_events(self, mock_observation_class, mock_equipment_class, mock_place_class):
        # Setup mocks
        mock_place = mock_place_class.return_value
        mock_equipment = mock_equipment_class.return_value
        mock_observation = mock_observation_class.return_value

        mock_events = MagicMock()
        mock_observation.get_astronomical_events.return_value = mock_events

        start_date = datetime(2023, 1, 1, tzinfo=utc)
        end_date = datetime(2023, 1, 2, tzinfo=utc)

        events = get_events(lat=52.2, lon=21.0, start_date=start_date, end_date=end_date)

        # Verify calls
        mock_place_class.assert_called_once_with(lat=52.2, lon=21.0, elevation=300)
        mock_equipment_class.assert_called_once()
        mock_observation_class.assert_called_once_with(mock_place, mock_equipment)

        mock_observation.get_astronomical_events.assert_called_once_with(
            start_date=start_date,
            end_date=end_date,
            events_to_calculate=None
        )

        self.assertEqual(events, mock_events)

if __name__ == "__main__":
    unittest.main()
