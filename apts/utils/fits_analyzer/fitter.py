import math
import numpy as np
from scipy.optimize import curve_fit
from astropy.stats import sigma_clipped_stats
from photutils.detection import DAOStarFinder
from .constants import ANALYSIS_DEFAULTS

def gaussian_2d(xy, amplitude, x0, y0, sigma_x, sigma_y, theta, offset):
    """
    2D Gaussian model for star fitting.
    """
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

def fit_one_star(star, cutout, x0, y0, box_size, half, xy):
    """
    Fits a single star using 2D Gaussian.
    """
    bg = np.median(cutout)
    cutout_sub = cutout - bg
    amp_guess = cutout_sub.max()
    if amp_guess <= 0:
        return None
    p0 = [amp_guess, half, half, 2.0, 2.0, 0.0, 0.0]
    try:
        popt, _ = curve_fit(
            gaussian_2d, xy, cutout_sub.ravel(), p0=p0, maxfev=1000
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

def fit_stars(data, stars, progress_cb=None):
    """
    Fits all detected stars in the image data.
    """
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
        res = fit_one_star(star, cutout, x0, y0, box_size, half, xy)
        if res:
            results.append(res)
        if progress_cb:
            progress_cb(i, len(stars))
    return results

def detect_stars(data, fwhm_est=None, threshold=None):
    """
    Detects stars in image data.
    """
    if fwhm_est is None:
        fwhm_est = ANALYSIS_DEFAULTS["fwhm_est"]
    if threshold is None:
        threshold = ANALYSIS_DEFAULTS["threshold"]

    data_64 = data.astype(np.float64)
    mean, median, std = sigma_clipped_stats(data_64, sigma=3.0)
    finder = DAOStarFinder(fwhm=fwhm_est, threshold=threshold * std)
    sources = finder(data_64 - median)

    if sources is None:
        return []

    stars = []
    # Support both photutils < 3.0.0 (xcentroid) and >= 3.0.0 (x_centroid)
    x_col = "x_centroid" if "x_centroid" in sources.colnames else "xcentroid"
    y_col = "y_centroid" if "y_centroid" in sources.colnames else "ycentroid"
    for row in sources:
        stars.append(
            {
                "x": float(row[x_col]),
                "y": float(row[y_col]),
                "flux": float(row["flux"]),
            }
        )
    return stars
