#!/usr/bin/env python3
"""
FITS / XISF Backfocus Analyzer – single-image diagnostics.

Detects stars, fits elliptical Gaussians, builds FWHM surface map,
and classifies backfocus error direction (too short / too long) via
radial vs tangential elongation pattern analysis.

Supported formats: FITS (.fits .fit .fts), compressed FITS (.fits.fz .fit.fz),
                   XISF (.xisf) — all case-insensitive.

Requires: numpy, scipy, astropy, photutils, matplotlib
"""

import math
import os
import struct
import xml.etree.ElementTree as ET
import zlib
import re

import numpy as np
from scipy.optimize import curve_fit
from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from photutils.detection import DAOStarFinder

# ═══════════════════════════════════════════════════════════════════
#  DEFAULTS
# ═══════════════════════════════════════════════════════════════════
ANALYSIS_DEFAULTS = {
    "fwhm_est": 5.0,
    "threshold": 8.0,
    "star_limit": 500,
    "edge_margin": 50,
    "box_size": 25,
    "min_stars": 10,
    "retry_threshold": 4.0,
    "max_eccentricity": 0.95,
    "max_chi2": 5.0,
    "progress_interval": 20,
    "ecc_threshold": 0.15,
    "radial_positive_threshold": 0.3,
    "radial_negative_threshold": -0.3,
    "annular_zones": 4,
    "annular_weights": [0.1, 0.2, 0.3, 0.4],
    "grid_size": 50,
    "poly_degree": 2,
    "sigma_clip_iters": 3,
    "sigma_clip_sigma": 2.5,
    "autobin_threshold": 4096,
    "mosaic_tile_fraction": 0.20,
}


class FitsAnalyzer:
    """
    Backfocus analyzer for a single FITS/XISF image.
    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.data, self.header = self._load_data(filepath)
        self.stars = []
        self.fitted_stars = []
        self.surface = None
        self.classification = None

    def _load_data(self, filepath):
        name_lower = os.path.basename(filepath).lower()
        if name_lower.endswith(".xisf") or self._is_xisf(filepath):
            return self._load_xisf(filepath)
        else:
            with fits.open(filepath) as hdul:
                data = None
                header = None
                for hdu in hdul:
                    hdu_data = getattr(hdu, "data", None)
                    if hdu_data is not None and hdu_data.ndim >= 2:
                        data = hdu_data
                        header = getattr(hdu, "header", None)
                        break
                if data is None:
                    raise ValueError("No image data found in FITS file")
                return data, header

    def _is_xisf(self, filepath):
        try:
            with open(filepath, "rb") as f:
                return f.read(8) == b"XISF0100"
        except OSError:
            return False

    def _byte_unshuffle(self, data_bytes, item_size):
        n_bytes = len(data_bytes)
        if item_size <= 1 or n_bytes < item_size:
            return data_bytes
        n_elements = n_bytes // item_size
        usable = n_elements * item_size
        arr = np.frombuffer(data_bytes[:usable], dtype=np.uint8)
        unshuffled = arr.reshape(item_size, n_elements).T.tobytes()
        if usable < n_bytes:
            unshuffled += data_bytes[usable:]
        return unshuffled

    def _load_xisf(self, filepath):
        with open(filepath, "rb") as f:
            magic = f.read(8)
            if magic != b"XISF0100":
                raise ValueError("Not a valid XISF file (bad magic)")
            header_len, _reserved = struct.unpack("<II", f.read(8))
            xml_bytes = f.read(header_len)
            xml_str = xml_bytes.decode("utf-8", errors="replace")
            xml_str = re.sub(r'\s+xmlns\s*=\s*["\'][^"\']*["\']', "", xml_str)
            root = ET.fromstring(xml_str)
            img_el = root.find(".//Image")
            if img_el is None:
                raise ValueError("No Image element found in XISF header")
            geom = img_el.get("geometry", "")
            parts = geom.split(":")
            width = int(parts[0])
            height = int(parts[1])
            channels = int(parts[2]) if len(parts) > 2 else 1
            sample_fmt = img_el.get("sampleFormat", "Float32")
            dtype_map = {
                "UInt8": np.uint8,
                "UInt16": np.uint16,
                "UInt32": np.uint32,
                "UInt64": np.uint64,
                "Int8": np.int8,
                "Int16": np.int16,
                "Int32": np.int32,
                "Int64": np.int64,
                "Float32": np.float32,
                "Float64": np.float64,
            }
            dtype = dtype_map.get(sample_fmt)
            pixel_storage = img_el.get("pixelStorage", "planar")
            location = img_el.get("location", "")
            compression = img_el.get("compression", "")
            if location.startswith("attachment:"):
                loc_parts = location.split(":")
                offset = int(loc_parts[1])
                size = int(loc_parts[2])
                f.seek(offset)
                raw = f.read(size)
            else:
                raise ValueError(f"Unsupported XISF location: {location}")

            if compression:
                comp_parts = compression.split(":")
                codec = comp_parts[0].lower()
                shuffle_item_size = (
                    int(comp_parts[2])
                    if len(comp_parts) > 2
                    else np.dtype(dtype).itemsize
                )
                byte_shuffle = "+sh" in codec
                base_codec = codec.replace("+sh", "")
                if base_codec == "zlib":
                    raw = zlib.decompress(raw)
                else:
                    raise ValueError(f"Unsupported XISF compression: {codec}")
                if byte_shuffle:
                    raw = self._byte_unshuffle(raw, shuffle_item_size)

            data = np.frombuffer(raw, dtype=dtype)
            if channels > 1:
                if pixel_storage == "planar":
                    data = data.reshape(channels, height, width)[0]
                else:
                    data = data.reshape(height, width, channels)[:, :, 0]
            else:
                data = data.reshape(height, width)

        header = {"XISF": True, "NAXIS1": width, "NAXIS2": height}
        return data, header

    def detect_stars(self, fwhm_est=None, threshold=None):
        if fwhm_est is None:
            fwhm_est = ANALYSIS_DEFAULTS["fwhm_est"]
        if threshold is None:
            threshold = ANALYSIS_DEFAULTS["threshold"]

        data = self.data.astype(np.float64)
        mean, median, std = sigma_clipped_stats(data, sigma=3.0)
        finder = DAOStarFinder(fwhm=fwhm_est, threshold=threshold * std)
        sources = finder(data - median)

        if sources is None:
            return []

        self.stars = []
        for row in sources:
            self.stars.append(
                {
                    "x": float(row["xcentroid"]),
                    "y": float(row["ycentroid"]),
                    "flux": float(row["flux"]),
                }
            )
        return self.stars

    def analyze(self, progress_cb=None):
        if not self.stars:
            self.detect_stars()

        self.fitted_stars = self._fit_stars(
            self.data, self.stars, progress_cb=progress_cb
        )
        h, w = self.data.shape
        self.surface = self._build_surface(self.fitted_stars, (h, w))
        self.classification = self._classify_backfocus(
            self.fitted_stars, (w / 2, h / 2)
        )
        return self.get_summary()

    def get_summary(self):
        summary = {
            "exposure": self.header.get("EXPTIME") if self.header else None,
            "temperature": self.header.get("CCD-TEMP") if self.header else None,
            "filter": self.header.get("FILTER") if self.header else None,
            "stars_count": len(self.fitted_stars),
        }
        if self.classification:
            summary["backfocus_verdict"] = self.classification["verdict"]
            summary["radial_score"] = self.classification["score"]
        if self.surface:
            summary["fwhm_gradient"] = self.surface["gradient_pct"]
        return summary

    def _fit_stars(self, data, stars, progress_cb=None):
        box_size = ANALYSIS_DEFAULTS["box_size"]
        half = box_size // 2
        h, w = data.shape
        results = []

        y_grid, x_grid = np.mgrid[0:box_size, 0:box_size]
        xy = (x_grid.ravel(), y_grid.ravel())

        for i, star in enumerate(stars):
            sx, sy = int(round(star["x"])), int(round(star["y"]))
            x0, y0 = sx - half, sy - half
            if x0 < 0 or y0 < 0 or x0 + box_size > w or y0 + box_size > h:
                continue
            cutout = data[y0 : y0 + box_size, x0 : x0 + box_size]
            res = self._fit_one_star(star, cutout, x0, y0, box_size, half, xy)
            if res:
                results.append(res)
            if progress_cb:
                progress_cb(i, len(stars))
        return results

    def _fit_one_star(self, star, cutout, x0, y0, box_size, half, xy):
        bg = np.median(cutout)
        cutout_sub = cutout - bg
        amp_guess = cutout_sub.max()
        if amp_guess <= 0:
            return None
        p0 = [amp_guess, half, half, 2.0, 2.0, 0.0, 0.0]
        try:
            popt, _ = curve_fit(
                self._gaussian_2d, xy, cutout_sub.ravel(), p0=p0, maxfev=1000
            )
            amp, fit_cx, fit_cy, sigma_x, sigma_y, theta, offset = popt
            fwhm_x, fwhm_y = abs(sigma_x) * 2.355, abs(sigma_y) * 2.355
            f_major, f_minor = max(fwhm_x, fwhm_y), min(fwhm_x, fwhm_y)
            ecc = math.sqrt(1 - (f_minor / f_major) ** 2) if f_major > 0 else 0
            pa = theta if fwhm_x >= fwhm_y else theta + math.pi / 2
            return {
                "x": star["x"],
                "y": star["y"],
                "fwhm_major": f_major,
                "fwhm_minor": f_minor,
                "fwhm_geom": math.sqrt(f_major * f_minor),
                "eccentricity": ecc,
                "position_angle": pa,
            }
        except Exception:
            return None

    @staticmethod
    def _gaussian_2d(xy, amplitude, x0, y0, sigma_x, sigma_y, theta, offset):
        x, y = xy
        cos_t, sin_t = math.cos(theta), math.sin(theta)
        a = cos_t**2 / (2 * sigma_x**2) + sin_t**2 / (2 * sigma_y**2)
        b = -math.sin(2 * theta) / (4 * sigma_x**2) + math.sin(2 * theta) / (
            4 * sigma_y**2
        )
        c = sin_t**2 / (2 * sigma_x**2) + cos_t**2 / (2 * sigma_y**2)
        return (
            amplitude
            * np.exp(
                -(a * (x - x0) ** 2 + 2 * b * (x - x0) * (y - y0) + c * (y - y0) ** 2)
            )
            + offset
        ).ravel()

    def _build_surface(self, fitted, shape):
        if len(fitted) < 6:
            return None
        h, w = shape
        xs = np.array([s["x"] for s in fitted])
        ys = np.array([s["y"] for s in fitted])
        fwhms = np.array([s["fwhm_geom"] for s in fitted])
        xn, yn = (xs - w / 2) / (w / 2), (ys - h / 2) / (h / 2)
        A = np.column_stack([np.ones_like(xn), xn, yn, xn**2, xn * yn, yn**2])
        try:
            coeffs, _, _, _ = np.linalg.lstsq(A, fwhms, rcond=None)
            center_fwhm = max(coeffs[0], 0.1)
            edge_fwhm = np.mean([coeffs[0] + coeffs[3], coeffs[0] + coeffs[5]])
            return {"gradient_pct": (edge_fwhm - center_fwhm) / center_fwhm * 100}
        except Exception:
            return None

    def _classify_backfocus(self, fitted, center):
        cx, cy = center
        scores = []
        for s in fitted:
            if s["eccentricity"] < 0.15:
                continue
            dx, dy = s["x"] - cx, s["y"] - cy
            rad_angle = math.atan2(dy, dx)
            delta = abs(s["position_angle"] - rad_angle) % math.pi
            if delta > math.pi / 2:
                delta = math.pi - delta
            scores.append(math.cos(2 * delta) * s["eccentricity"])
        if not scores:
            return {"score": 0, "verdict": "correct"}
        avg_score = np.mean(scores)
        verdict = (
            "short" if avg_score > 0.2 else ("long" if avg_score < -0.2 else "correct")
        )
        return {"score": avg_score, "verdict": verdict}
