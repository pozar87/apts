import unittest
import numpy as np
import struct
import zlib
import math
import warnings
from unittest.mock import patch, MagicMock, mock_open
from apts.utils.fits_analyzer import FitsAnalyzer

class TestFitsAnalyzer(unittest.TestCase):

    def setUp(self):
        # Create a small simulated image with a star blob
        self.height, self.width = 100, 100
        self.data = np.random.normal(100, 5, (self.height, self.width)).astype(np.float32)
        # Add a Gaussian star blob at (50, 50)
        y, x = np.mgrid[0:self.height, 0:self.width]
        self.star_x, self.star_y = 50.4, 49.6
        sigma = 2.0
        star = 1000 * np.exp(-((x - self.star_x)**2 + (y - self.star_y)**2) / (2 * sigma**2))
        self.data += star.astype(np.float32)

    @patch("apts.utils.fits_analyzer.loader.fits.open")
    def test_load_fits(self, mock_fits_open):
        # Mock FITS structure
        mock_hdu = MagicMock()
        mock_hdu.data = self.data
        mock_hdu.header = {"EXPTIME": 30.0, "NAXIS1": self.width, "NAXIS2": self.height}
        mock_hdul = [mock_hdu]
        mock_fits_open.return_value.__enter__.return_value = mock_hdul

        analyzer = FitsAnalyzer("dummy.fits")
        np.testing.assert_array_equal(analyzer.data, self.data)
        self.assertEqual(analyzer.header["EXPTIME"], 30.0)

    @patch("apts.utils.fits_analyzer.loader.fits.open")
    def test_load_fits_no_data(self, mock_fits_open):
        mock_hdu = MagicMock()
        mock_hdu.data = None
        mock_hdul = [mock_hdu]
        mock_fits_open.return_value.__enter__.return_value = mock_hdul
        with self.assertRaises(ValueError):
            FitsAnalyzer("dummy.fits")

    def test_is_xisf(self):
        m = mock_open(read_data=b"XISF0100someheader")
        with patch("builtins.open", m):
            analyzer = FitsAnalyzer.__new__(FitsAnalyzer)
            self.assertTrue(analyzer._is_xisf("dummy.xisf"))

        m = mock_open(read_data=b"NOTXISF")
        with patch("builtins.open", m):
            self.assertFalse(analyzer._is_xisf("dummy.fits"))

    def test_byte_unshuffle(self):
        analyzer = FitsAnalyzer.__new__(FitsAnalyzer)
        # 4 elements, 2 bytes each. Elements: [0x0102, 0x0304, 0x0506, 0x0708]
        # In memory (LE): 02 01 04 03 06 05 08 07
        # Shuffled (byte 0 of all, then byte 1 of all): 02 04 06 08 01 03 05 07
        shuffled = bytes([0x02, 0x04, 0x06, 0x08, 0x01, 0x03, 0x05, 0x07])
        unshuffled = analyzer._byte_unshuffle(shuffled, 2)
        expected = bytes([0x02, 0x01, 0x04, 0x03, 0x06, 0x05, 0x08, 0x07])
        self.assertEqual(unshuffled, expected)

        # Test edge case: item_size 1
        self.assertEqual(analyzer._byte_unshuffle(b"abc", 1), b"abc")
        # Test edge case: data shorter than item_size
        self.assertEqual(analyzer._byte_unshuffle(b"a", 2), b"a")

    @patch("apts.utils.fits_analyzer.FitsAnalyzer._is_xisf", return_value=True)
    def test_load_xisf_basic(self, mock_is_xisf):
        # Create a minimal valid XISF-like structure
        # Magic (8) + Header length (4) + Reserved (4) + Header + Attachment
        width, height = 10, 10
        data = np.arange(width * height, dtype=np.float32).reshape(height, width)
        data_bytes = data.tobytes()

        xml_header = f"""<?xml version="1.0" encoding="UTF-8"?>
<xisf version="1.0">
   <Image geometry="{width}:{height}:1" sampleFormat="Float32" pixelStorage="planar" location="attachment:16:{len(data_bytes)}"/>
</xisf>""".encode('utf-8')

        header_len = len(xml_header)
        xisf_data = b"XISF0100" + struct.pack("<II", header_len, 0) + xml_header + data_bytes

        m = mock_open(read_data=xisf_data)
        with patch("builtins.open", m):
            analyzer = FitsAnalyzer("dummy.xisf")
            np.testing.assert_array_almost_equal(analyzer.data, data)
            self.assertEqual(analyzer.header["NAXIS1"], width)

    @patch("apts.utils.fits_analyzer.FitsAnalyzer._is_xisf", return_value=True)
    def test_load_xisf_zlib_shuffled(self, mock_is_xisf):
        width, height = 4, 4
        data = np.linspace(0, 1, width * height, dtype=np.float32).reshape(height, width)
        raw_bytes = data.tobytes()

        # Shuffle
        analyzer = FitsAnalyzer.__new__(FitsAnalyzer)
        arr = np.frombuffer(raw_bytes, dtype=np.uint8).reshape(len(raw_bytes)//4, 4).T
        shuffled_bytes = arr.tobytes()

        compressed = zlib.compress(shuffled_bytes)

        xml_header = f"""<?xml version="1.0" encoding="UTF-8"?>
<xisf version="1.0">
   <Image geometry="{width}:{height}:1" sampleFormat="Float32" pixelStorage="planar" location="attachment:16:{len(compressed)}" compression="zlib+sh:4"/>
</xisf>""".encode('utf-8')

        header_len = len(xml_header)
        xisf_data = b"XISF0100" + struct.pack("<II", header_len, 0) + xml_header + compressed

        m = mock_open(read_data=xisf_data)
        with patch("builtins.open", m):
            analyzer = FitsAnalyzer("dummy.xisf")
            np.testing.assert_array_almost_equal(analyzer.data, data)

    def test_detect_stars(self):
        analyzer = FitsAnalyzer.__new__(FitsAnalyzer)
        analyzer.data = self.data
        analyzer.stars = []
        stars = analyzer.detect_stars(fwhm_est=2.0, threshold=5.0)
        self.assertGreaterEqual(len(stars), 1)
        found = False
        for s in stars:
            if abs(s['x'] - self.star_x) < 1.0 and abs(s['y'] - self.star_y) < 1.0:
                found = True
                break
        self.assertTrue(found)

        # Test no sources found
        analyzer.data = np.zeros((50, 50))
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.assertEqual(analyzer.detect_stars(), [])

    def test_analyze_and_classification(self):
        # Create image with stars elongated radially (too short backfocus)
        h, w = 200, 200
        cx, cy = w/2, h/2

        stars_meta = [
            (50, 50), (150, 50), (50, 150), (150, 150), (100, 50), (100, 150)
        ]

        analyzer = FitsAnalyzer.__new__(FitsAnalyzer)
        analyzer.data = np.zeros((h, w), dtype=np.float32)
        analyzer.header = {}
        analyzer.stars = [{"x": sx, "y": sy, "flux": 1000} for sx, sy in stars_meta]

        # Mock progress callback
        progress_mock = MagicMock()

        # Inject radially elongated fitted stars directly
        fitted = []
        for sx, sy in stars_meta:
            dx, dy = sx - cx, sy - cy
            angle = math.atan2(dy, dx)
            fitted.append({
                "x": sx, "y": sy, "fwhm_major": 5.0, "fwhm_minor": 1.0,
                "fwhm_geom": math.sqrt(5.0), "eccentricity": math.sqrt(1 - (1.0/5.0)**2),
                "position_angle": angle
            })

        # Mock _fit_stars to use our manually created 'fitted' stars
        with patch.object(FitsAnalyzer, '_fit_stars', return_value=fitted):
            analyzer.analyze(progress_cb=progress_mock)

        self.assertEqual(analyzer.classification['verdict'], 'short')
        self.assertGreater(analyzer.classification['score'], 0.2)
        progress_mock.assert_not_called() # _fit_stars was mocked

    def test_fit_stars_real(self):
        analyzer = FitsAnalyzer.__new__(FitsAnalyzer)
        analyzer.data = self.data
        stars = [{"x": self.star_x, "y": self.star_y, "flux": 1000}]
        progress_cb = MagicMock()
        fitted = analyzer._fit_stars(self.data, stars, progress_cb=progress_cb)
        self.assertEqual(len(fitted), 1)
        self.assertAlmostEqual(fitted[0]['x'], self.star_x, delta=0.5)
        progress_cb.assert_called_with(0, 1)

        # Test out of bounds star
        stars_out = [{"x": -10, "y": -10, "flux": 1000}]
        fitted_out = analyzer._fit_stars(self.data, stars_out)
        self.assertEqual(len(fitted_out), 0)

    def test_fit_one_star_failures(self):
        analyzer = FitsAnalyzer.__new__(FitsAnalyzer)
        # Mock cutout with no signal
        cutout = np.zeros((25, 25))
        res = analyzer._fit_one_star({"x": 10, "y": 10}, cutout, 0, 0, 25, 12, (None, None))
        self.assertIsNone(res)

    def test_classify_backfocus_long(self):
        analyzer = FitsAnalyzer.__new__(FitsAnalyzer)
        cx, cy = 100, 100
        fitted = []
        fitted.append({
            "x": 50, "y": 100, "eccentricity": 0.5, "position_angle": math.pi / 2,
            "fwhm_major": 5.0, "fwhm_minor": 3.0, "fwhm_geom": 4.0
        })
        fitted.append({
            "x": 150, "y": 100, "eccentricity": 0.5, "position_angle": math.pi / 2,
            "fwhm_major": 5.0, "fwhm_minor": 3.0, "fwhm_geom": 4.0
        })

        res = analyzer._classify_backfocus(fitted, (cx, cy))
        self.assertEqual(res['verdict'], 'long')
        self.assertLess(res['score'], -0.2)

        # Test no scores (low eccentricity stars)
        fitted_low_ecc = [{"x": 100, "y": 100, "eccentricity": 0.05, "position_angle": 0}]
        res_low = analyzer._classify_backfocus(fitted_low_ecc, (cx, cy))
        self.assertEqual(res_low['verdict'], 'correct')
        self.assertEqual(res_low['score'], 0)

    def test_build_surface_and_summary(self):
        analyzer = FitsAnalyzer.__new__(FitsAnalyzer)
        w, h = 200, 200
        fitted = []
        for x in [50, 100, 150]:
            for y in [50, 100, 150]:
                dist = math.sqrt((x-100)**2 + (y-100)**2)
                fwhm = 2.0 + (dist / 100.0)
                fitted.append({
                    "x": x, "y": y, "fwhm_geom": fwhm, "eccentricity": 0.05,
                    "position_angle": 0, "fwhm_major": fwhm, "fwhm_minor": fwhm
                })

        surface = analyzer._build_surface(fitted, (h, w))
        self.assertIsNotNone(surface)
        self.assertGreater(surface['gradient_pct'], 0)

        # Test too few stars for surface
        self.assertIsNone(analyzer._build_surface(fitted[:3], (h, w)))

        analyzer.fitted_stars = fitted
        analyzer.surface = surface
        analyzer.classification = {"verdict": "correct", "score": 0.05}
        analyzer.header = {"EXPTIME": 10.0, "CCD-TEMP": -10.0, "FILTER": "L"}

        summary = analyzer.get_summary()
        self.assertEqual(summary['stars_count'], 9)
        self.assertEqual(summary['backfocus_verdict'], 'correct')

        # Test summary with missing classification/surface
        analyzer.classification = None
        analyzer.surface = None
        summary_empty = analyzer.get_summary()
        self.assertNotIn('backfocus_verdict', summary_empty)
        self.assertNotIn('fwhm_gradient', summary_empty)

if __name__ == "__main__":
    unittest.main()
