from .loader import load_data, is_xisf, byte_unshuffle, load_xisf
from .fitter import detect_stars, fit_stars, fit_one_star, gaussian_2d
from .classification import build_surface, classify_backfocus


class FitsAnalyzer:
    """
    Backfocus analyzer for a single FITS/XISF image.
    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.data, self.header = load_data(filepath)
        self.stars = []
        self.fitted_stars = []
        self.surface = None
        self.classification = None

    def _is_xisf(self, filepath):
        return is_xisf(filepath)

    def _byte_unshuffle(self, data_bytes, item_size):
        return byte_unshuffle(data_bytes, item_size)

    def _load_xisf(self, filepath):
        return load_xisf(filepath)

    def detect_stars(self, fwhm_est=None, threshold=None):
        self.stars = detect_stars(self.data, fwhm_est, threshold)
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
        return fit_stars(data, stars, progress_cb)

    def _fit_one_star(self, star, cutout, x0, y0, box_size, half, xy):
        return fit_one_star(star, cutout, x0, y0, box_size, half, xy)

    @staticmethod
    def _gaussian_2d(xy, amplitude, x0, y0, sigma_x, sigma_y, theta, offset):
        return gaussian_2d(xy, amplitude, x0, y0, sigma_x, sigma_y, theta, offset)

    def _build_surface(self, fitted, shape):
        return build_surface(fitted, shape)

    def _classify_backfocus(self, fitted, center):
        return classify_backfocus(fitted, center)
