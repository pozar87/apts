import unittest
from unittest.mock import patch
from apts.nasa_api import NasaAPI
from datetime import datetime


class TestNasaAPI(unittest.TestCase):
    @patch("requests.get")
    def test_get_comets(self, mock_get):
        # Arrange
        mock_get.return_value.json.return_value = {
            "near_earth_objects": {
                "2024-01-01": [
                    {
                        "name": "1P/Halley",
                        "close_approach_data": [
                            {
                                "close_approach_date_full": "2024-01-01 12:00",
                            }
                        ],
                    }
                ]
            }
        }
        api = NasaAPI()

        # Act
        comets = api.get_comets(datetime(2024, 1, 1), datetime(2024, 1, 1))

        # Assert
        self.assertIsNotNone(comets)
        self.assertEqual(len(comets["near_earth_objects"]["2024-01-01"]), 1)
        self.assertEqual(
            comets["near_earth_objects"]["2024-01-01"][0]["name"], "1P/Halley"
        )


if __name__ == "__main__":
    unittest.main()
