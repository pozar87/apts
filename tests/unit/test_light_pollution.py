import unittest
from unittest.mock import patch, MagicMock
from apts.light_pollution import LightPollution


class TestLightPollution(unittest.TestCase):
    def setUp(self):
        # We patch Image.open in the setUp to avoid loading the actual image in every test
        self.patcher = patch("apts.light_pollution.Image.open")
        self.mock_image_open = self.patcher.start()
        self.mock_image = MagicMock()
        self.mock_image.size = (14400, 5600)  # Set expected dimensions
        self.mock_pix = MagicMock()
        self.mock_image.load.return_value = self.mock_pix
        self.mock_image_open.return_value = self.mock_image

        self.lp = LightPollution(lat=0, lon=0)

    def tearDown(self):
        self.patcher.stop()

    def test_latlon_to_pixel(self):
        # Test corners and center
        self.assertEqual(self.lp._latlon_to_pixel(75, -180), (0, 0))
        self.assertEqual(self.lp._latlon_to_pixel(-65, 179.99), (14399, 5600))
        self.assertEqual(self.lp._latlon_to_pixel(0, 0), (7200, 3000))
        # Warsaw
        self.assertEqual(self.lp._latlon_to_pixel(52.2297, 21.0122), (8040, 910))

    def test_get_light_pollution(self):
        # Test the mapping from palette index to Bortle scale
        bortle_scale = {
            0: 1,
            1: 1,
            2: 1,
            3: 2,
            4: 3,
            5: 4,
            6: 4.5,
            7: 5,
            8: 6,
            9: 7,
            10: 7,
            11: 8,
            12: 8,
            13: 9,
            14: 9,
        }

        for palette_index, expected_bortle in bortle_scale.items():
            with self.subTest(palette_index=palette_index):
                # Configure the mock pixel data to return the current palette index
                self.mock_pix.__getitem__.return_value = palette_index
                # We can use any lat/lon since the pixel data is mocked
                result = self.lp.get_light_pollution()
                self.assertEqual(result, expected_bortle)

    def test_get_light_pollution_unknown_index(self):
        # Test the case where the palette index is not in the map
        self.mock_pix.__getitem__.return_value = 99  # An unknown index
        result = self.lp.get_light_pollution()
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
