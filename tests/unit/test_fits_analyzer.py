import unittest
from unittest.mock import MagicMock, patch
from apts.utils.fits_analyzer import FitsAnalyzer
import numpy as np


class TestFitsAnalyzer(unittest.TestCase):
    @patch("astropy.io.fits.open")
    def test_basic_analysis(self, mock_fits_open):
        # Create a mock FITS HDUList
        mock_hdu = MagicMock()
        mock_hdu.header = {
            "EXPTIME": 30.0,
            "CCD-TEMP": -10.0,
            "FILTER": "H-alpha",
            "INSTRUME": "ASI2600MM",
            "TELESCOP": "SharpStar 61EDPH",
        }
        # Mock data (100x100 array)
        mock_hdu.data = np.random.randint(0, 65535, (100, 100), dtype=np.uint16)

        mock_hdulist = [mock_hdu]
        mock_fits_open.return_value.__enter__.return_value = mock_hdulist

        analyzer = FitsAnalyzer("fake.fits")
        summary = analyzer.get_summary()

        self.assertEqual(summary["exposure"], 30.0)
        self.assertEqual(summary["temperature"], -10.0)
        self.assertEqual(summary["filter"], "H-alpha")

        # Test star detection (should run without error)
        # We need to mock photutils as well if we want to be sure it works
        stars = analyzer.detect_stars(threshold=5.0)
        self.assertIsInstance(stars, list)


if __name__ == "__main__":
    unittest.main()
