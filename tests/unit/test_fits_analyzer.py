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
            "NAXIS1": 100,
            "NAXIS2": 100
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
        with patch("apts.utils.fits_analyzer.DAOStarFinder") as mock_finder:
            mock_finder_inst = mock_finder.return_value
            mock_finder_inst.return_value = [
                {"xcentroid": 10, "ycentroid": 10, "flux": 1000},
                {"xcentroid": 20, "ycentroid": 20, "flux": 2000},
            ]
            stars = analyzer.detect_stars(threshold=5.0)
            self.assertEqual(len(stars), 2)

    def test_classify_backfocus(self):
        analyzer = FitsAnalyzer.__new__(FitsAnalyzer)
        center = (500, 500)

        # Mock stars for 'short' backfocus (radial elongation)
        # Radial angle for star at (600, 500) is 0. Position angle 0 means radial.
        stars_short = [
            {"x": 600, "y": 500, "eccentricity": 0.5, "position_angle": 0},
            {"x": 500, "y": 600, "eccentricity": 0.5, "position_angle": np.pi/2},
            {"x": 400, "y": 500, "eccentricity": 0.5, "position_angle": np.pi},
            {"x": 500, "y": 400, "eccentricity": 0.5, "position_angle": 3*np.pi/2},
        ]
        res = analyzer._classify_backfocus(stars_short, center)
        self.assertEqual(res["verdict"], "short")

        # Mock stars for 'long' backfocus (tangential elongation)
        stars_long = [
            {"x": 600, "y": 500, "eccentricity": 0.5, "position_angle": np.pi/2},
            {"x": 500, "y": 600, "eccentricity": 0.5, "position_angle": np.pi},
            {"x": 400, "y": 500, "eccentricity": 0.5, "position_angle": 3*np.pi/2},
            {"x": 500, "y": 400, "eccentricity": 0.5, "position_angle": 0},
        ]
        res = analyzer._classify_backfocus(stars_long, center)
        self.assertEqual(res["verdict"], "long")

        # Mock stars for 'correct' backfocus (low eccentricity or mixed)
        stars_correct = [
            {"x": 600, "y": 500, "eccentricity": 0.05, "position_angle": 0},
        ]
        res = analyzer._classify_backfocus(stars_correct, center)
        self.assertEqual(res["verdict"], "correct")

    def test_build_surface(self):
        analyzer = FitsAnalyzer.__new__(FitsAnalyzer)
        # Need at least 6 stars
        stars = [
            {"x": 100, "y": 100, "fwhm_geom": 2.0},
            {"x": 900, "y": 100, "fwhm_geom": 3.0},
            {"x": 100, "y": 900, "fwhm_geom": 3.0},
            {"x": 900, "y": 900, "fwhm_geom": 4.0},
            {"x": 500, "y": 500, "fwhm_geom": 1.5},
            {"x": 500, "y": 100, "fwhm_geom": 2.5},
        ]
        res = analyzer._build_surface(stars, (1000, 1000))
        self.assertIsNotNone(res)
        if res is not None:
            self.assertIn("gradient_pct", res)
            self.assertIsInstance(res["gradient_pct"], float)

    @patch("astropy.io.fits.open")
    def test_full_analyze(self, mock_fits_open):
        mock_hdu = MagicMock()
        mock_hdu.header = {"NAXIS1": 1000, "NAXIS2": 1000}
        mock_hdu.data = np.zeros((1000, 1000))
        mock_hdulist = [mock_hdu]
        mock_fits_open.return_value.__enter__.return_value = mock_hdulist

        analyzer = FitsAnalyzer("fake.fits")
        analyzer.stars = [{"x": 100, "y": 100, "flux": 1000}]

        with patch.object(analyzer, "_fit_stars") as mock_fit:
            mock_fit.return_value = [
                {"x": 100, "y": 100, "fwhm_geom": 2.0, "eccentricity": 0.1, "position_angle": 0},
                {"x": 900, "y": 100, "fwhm_geom": 2.1, "eccentricity": 0.1, "position_angle": 0},
                {"x": 100, "y": 900, "fwhm_geom": 2.1, "eccentricity": 0.1, "position_angle": 0},
                {"x": 900, "y": 900, "fwhm_geom": 2.2, "eccentricity": 0.1, "position_angle": 0},
                {"x": 500, "y": 500, "fwhm_geom": 1.9, "eccentricity": 0.1, "position_angle": 0},
                {"x": 500, "y": 100, "fwhm_geom": 2.0, "eccentricity": 0.1, "position_angle": 0},
            ]
            summary = analyzer.analyze()
            self.assertIn("backfocus_verdict", summary)
            self.assertIn("fwhm_gradient", summary)


if __name__ == "__main__":
    unittest.main()
