import unittest
from unittest.mock import patch, MagicMock
from apts.place.elevation import get_elevation
from apts.place import Place

class TestElevation(unittest.TestCase):

    @patch("apts.place.elevation.get_session")
    def test_get_elevation_success(self, mock_get_session):
        # Mock the response from the API
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {"elevation": [123.4]}
        mock_get_session.return_value.get.return_value.__enter__.return_value = mock_response

        elevation = get_elevation(50.0, 20.0)
        self.assertEqual(elevation, 123.4)

    @patch("apts.place.elevation.get_session")
    def test_get_elevation_failure(self, mock_get_session):
        # Mock a failed response
        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.status_code = 404
        mock_get_session.return_value.get.return_value.__enter__.return_value = mock_response

        elevation = get_elevation(50.0, 20.0)
        self.assertIsNone(elevation)

    @patch("apts.place.base.get_elevation")
    @patch("apts.place.base.get_place_settings")
    def test_place_init_with_auto_elevation(self, mock_get_settings, mock_get_elevation):
        # Mock settings to enable auto elevation
        mock_get_settings.return_value = {
            "use_online_elevation_api": True,
            "default_elevation": 300
        }
        mock_get_elevation.return_value = 567.8

        place = Place(lat=50.0, lon=20.0)
        self.assertEqual(place.elevation, 567.8)
        mock_get_elevation.assert_called_once_with(50.0, 20.0)

    @patch("apts.place.base.get_elevation")
    @patch("apts.place.base.get_place_settings")
    def test_place_init_with_auto_elevation_failure_fallback(self, mock_get_settings, mock_get_elevation):
        # Mock settings to enable auto elevation but API fails
        mock_get_settings.return_value = {
            "use_online_elevation_api": True,
            "default_elevation": 300
        }
        mock_get_elevation.return_value = None

        place = Place(lat=50.0, lon=20.0)
        self.assertEqual(place.elevation, 300)

    @patch("apts.place.base.get_elevation")
    @patch("apts.place.base.get_place_settings")
    def test_place_init_with_disabled_auto_elevation(self, mock_get_settings, mock_get_elevation):
        # Mock settings to disable auto elevation
        mock_get_settings.return_value = {
            "use_online_elevation_api": False,
            "default_elevation": 400
        }

        place = Place(lat=50.0, lon=20.0)
        self.assertEqual(place.elevation, 400)
        mock_get_elevation.assert_not_called()

    def test_place_init_with_provided_elevation(self):
        # If elevation is provided, it should use it and not call the API
        with patch("apts.place.base.get_elevation") as mock_get_elevation:
            place = Place(lat=50.0, lon=20.0, elevation=800)
            self.assertEqual(place.elevation, 800)
            mock_get_elevation.assert_not_called()
