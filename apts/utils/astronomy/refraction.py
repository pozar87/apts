from typing import Union
import numpy as np


def calculate_refraction(alt_deg: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """
    Calculates atmospheric refraction in degrees using Bennett's formula.
    Accurate to ~0.02' for altitudes > 0.
    """
    alt_deg_arr = np.atleast_1d(alt_deg)
    refraction_deg = np.zeros_like(alt_deg_arr, dtype=float)
    # Apply only for objects above -1 degree to avoid tan(0) or instability
    mask = alt_deg_arr > -1.0
    if np.any(mask):
        # R in arcminutes = 1 / tan(h + 7.31 / (h + 4.4))
        r_arcmin = 1.0 / np.tan(
            np.deg2rad(alt_deg_arr[mask] + 7.31 / (alt_deg_arr[mask] + 4.4))
        )
        refraction_deg[mask] = r_arcmin / 60.0

    return (
        refraction_deg[0]
        if np.isscalar(alt_deg) or (isinstance(alt_deg, np.ndarray) and alt_deg.ndim == 0)
        else refraction_deg
    )
