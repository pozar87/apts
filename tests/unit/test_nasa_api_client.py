import unittest
import datetime
import requests_mock
from apts.nasa_api import NasaAPI


class TestNasaAPI(unittest.TestCase):
    def setUp(self):
        self.api = NasaAPI(api_key="TEST_KEY")

    def test_get_comets(self):
        start_date = datetime.datetime(2023, 1, 1)
        end_date = datetime.datetime(2023, 1, 2)

        # Mock data for Jan 1st and Jan 2nd
        mock_response = {
            "near_earth_objects": {
                "2023-01-01": [{"name": "Asteroid 1"}],
                "2023-01-02": [{"name": "Asteroid 2"}],
            },
            "element_count": 2,
        }

        with requests_mock.Mocker() as m:
            m.get("https://api.nasa.gov/neo/rest/v1/feed", json=mock_response)

            data = self.api.get_comets(start_date, end_date)

            self.assertEqual(data["element_count"], 2)
            self.assertIn("2023-01-01", data["near_earth_objects"])
            self.assertIn("2023-01-02", data["near_earth_objects"])
            self.assertEqual(len(data["near_earth_objects"]["2023-01-01"]), 1)
            self.assertEqual(
                data["near_earth_objects"]["2023-01-01"][0]["name"], "Asteroid 1"
            )

    def test_get_comets_multi_page(self):
        # Test multi-page (more than 7 days)
        start_date = datetime.datetime(2023, 1, 1)
        end_date = datetime.datetime(2023, 1, 10)  # 10 days

        # Page 1 (Jan 1 to Jan 7)
        mock_response_1 = {
            "near_earth_objects": {"2023-01-01": [{"name": "Asteroid 1"}]}
        }
        # Page 2 (Jan 8 to Jan 10)
        mock_response_2 = {
            "near_earth_objects": {"2023-01-08": [{"name": "Asteroid 2"}]}
        }

        with requests_mock.Mocker() as m:
            # Match by params start_date
            m.get(
                "https://api.nasa.gov/neo/rest/v1/feed?start_date=2023-01-01&end_date=2023-01-07&api_key=TEST_KEY",
                json=mock_response_1,
            )
            m.get(
                "https://api.nasa.gov/neo/rest/v1/feed?start_date=2023-01-08&end_date=2023-01-10&api_key=TEST_KEY",
                json=mock_response_2,
            )

            data = self.api.get_comets(start_date, end_date)

            self.assertEqual(data["element_count"], 2)
            self.assertIn("2023-01-01", data["near_earth_objects"])
            self.assertIn("2023-01-08", data["near_earth_objects"])
