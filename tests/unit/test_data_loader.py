import unittest
from unittest.mock import patch
from apts.data_loader import get_ephemeris_path, get_mpcorb_path

class TestDataLoader(unittest.TestCase):
    @patch("apts.data_loader.get_data_settings")
    def test_get_ephemeris_path(self, mock_get_data_settings):
        mock_get_data_settings.return_value = "light"
        self.assertEqual(get_ephemeris_path(), "de421.bsp")

        mock_get_data_settings.return_value = "full"
        self.assertEqual(get_ephemeris_path(), "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de440.bsp")

    @patch("apts.data_loader.get_data_settings")
    @patch("apts.data_loader.DATA_DIR", "/fake/data")
    def test_get_mpcorb_path(self, mock_get_data_settings):
        mock_get_data_settings.return_value = "light"
        path = get_mpcorb_path()
        self.assertTrue(path.endswith("MPCORB.DAT.small.gz"))

        mock_get_data_settings.return_value = "full"
        self.assertEqual(get_mpcorb_path(), "https://www.minorplanetcenter.net/iau/MPCORB/MPCORB.DAT.gz")

if __name__ == "__main__":
    unittest.main()
