import numpy as np

def bortle_to_sqm(bortle_class: float) -> float:
    """
    Converts a Bortle class (1-9) to an approximate Sky Quality Meter (SQM) value
    in mag/arcsec^2. Uses linear interpolation between established midpoints.
    Source: https://en.wikipedia.org/wiki/Bortle_scale
    """
    xp = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    fp = [21.88, 21.67, 21.45, 21.05, 19.77, 18.87, 18.25, 17.5, 16.0]
    return float(np.interp(bortle_class, xp, fp))
