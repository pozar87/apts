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

    def test_load_xisf_mock(self):
        import io
        import struct
        import zlib

        # Mock XISF file content
        # 8 bytes magic
        magic = b"XISF0100"
        # XML Header
        xml_header = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<xisf version="1.0">'
            '<Image geometry="4:4:1" sampleFormat="Float32" pixelStorage="planar" location="attachment:100:64" compression="zlib:64" />'
            '</xisf>'
        ).encode("utf-8")

        header_len = len(xml_header)
        reserved = 0
        file_header = magic + struct.pack("<II", header_len, reserved) + xml_header

        # Data: 4x4 Float32 = 16 * 4 = 64 bytes
        data = np.arange(16, dtype=np.float32).tobytes()
        compressed_data = zlib.compress(data)

        # Re-adjust location for the compressed data in the XML
        # We'll just make the file long enough and put it at offset 512
        # Actually, in XISF, 'size' in location is the size of the STORED data (compressed).

        xml_header_v2 = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<xisf version="1.0">'
            f'<Image geometry="4:4:1" sampleFormat="Float32" pixelStorage="planar" location="attachment:512:{len(compressed_data)}" compression="zlib:{len(data)}" />'
            '</xisf>'
        ).encode("utf-8")
        header_len_v2 = len(xml_header_v2)
        file_header_v2 = magic + struct.pack("<II", header_len_v2, reserved) + xml_header_v2

        # Ensure we have enough space before the attachment
        padding_size = 512 - len(file_header_v2)
        if padding_size < 0:
            raise ValueError(f"Header too long: {len(file_header_v2)}")

        full_file = file_header_v2 + b"\0" * padding_size + compressed_data

        with patch("builtins.open", return_value=io.BytesIO(full_file)):
            analyzer = FitsAnalyzer("mock.xisf")
            self.assertEqual(analyzer.data.shape, (4, 4))
            self.assertTrue(np.allclose(analyzer.data.flatten(), np.arange(16)))
            self.assertEqual(analyzer.header["NAXIS1"], 4)

    def test_load_xisf_multi_channel(self):
        import io
        import struct

        magic = b"XISF0100"
        # 3 channels, 2x2, interleaved (packed)
        xml_header = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<xisf version="1.0">'
            '<Image geometry="2:2:3" sampleFormat="UInt8" pixelStorage="packed" location="attachment:512:12" />'
            '</xisf>'
        ).encode("utf-8")

        reserved = 0
        file_header = magic + struct.pack("<II", len(xml_header), reserved) + xml_header

        # Data: 2*2*3 = 12 bytes
        data = np.arange(12, dtype=np.uint8).tobytes()
        full_file = file_header + b"\0" * (512 - len(file_header)) + data

        with patch("builtins.open", return_value=io.BytesIO(full_file)):
            analyzer = FitsAnalyzer("mock.xisf")
            self.assertEqual(analyzer.data.shape, (2, 2))
            # Packed: [R00, G00, B00, R01, G01, B01, ...]
            # Code takes [:, :, 0] which should be R channel: 0, 3, 6, 9
            self.assertTrue(np.array_equal(analyzer.data.flatten(), [0, 3, 6, 9]))

    def test_load_xisf_planar(self):
        import io
        import struct

        magic = b"XISF0100"
        # 2 channels, 2x2, planar
        xml_header = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<xisf version="1.0">'
            '<Image geometry="2:2:2" sampleFormat="UInt8" pixelStorage="planar" location="attachment:512:8" />'
            '</xisf>'
        ).encode("utf-8")

        reserved = 0
        file_header = magic + struct.pack("<II", len(xml_header), reserved) + xml_header

        # Data: 2*2*2 = 8 bytes. Ch1: 0,1,2,3. Ch2: 4,5,6,7
        data = np.arange(8, dtype=np.uint8).tobytes()
        full_file = file_header + b"\0" * (512 - len(file_header)) + data

        with patch("builtins.open", return_value=io.BytesIO(full_file)):
            analyzer = FitsAnalyzer("mock.xisf")
            self.assertEqual(analyzer.data.shape, (2, 2))
            self.assertTrue(np.array_equal(analyzer.data.flatten(), [0, 1, 2, 3]))

    def test_byte_unshuffle(self):
        analyzer = FitsAnalyzer.__new__(FitsAnalyzer)
        # 2 elements of 4 bytes each
        # Element 1: [0x01, 0x02, 0x03, 0x04]
        # Element 2: [0x05, 0x06, 0x07, 0x08]
        # Shuffled (by byte index): 01 05, 02 06, 03 07, 04 08
        shuffled = bytes([0x01, 0x05, 0x02, 0x06, 0x03, 0x07, 0x04, 0x08])
        expected = bytes([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08])

        unshuffled = analyzer._byte_unshuffle(shuffled, 4)
        self.assertEqual(unshuffled, expected)


if __name__ == "__main__":
    unittest.main()
