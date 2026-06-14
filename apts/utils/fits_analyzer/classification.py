import math
import numpy as np

def build_surface(fitted, shape):
    """
    Builds an FWHM surface map from fitted stars.
    """
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

def classify_backfocus(fitted, center):
    """
    Classifies backfocus error direction.
    """
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
