from typing import Union, Optional
import numpy as np


def vectorized_angular_separation(
    ra1: Union[float, np.ndarray],
    dec1: Union[float, np.ndarray],
    ra2: Union[float, np.ndarray],
    dec2: Union[float, np.ndarray],
    sin_dec1: Optional[np.ndarray] = None,
    cd_cr1: Optional[np.ndarray] = None,
    cd_sr1: Optional[np.ndarray] = None,
) -> Union[float, np.ndarray]:
    """
    Calculates angular separation between two sets of coordinates in degrees.
    """
    ra1_rad = np.deg2rad(ra1 * 15.0)
    dec1_rad = np.deg2rad(dec1)
    ra2_rad = np.deg2rad(ra2 * 15.0)
    dec2_rad = np.deg2rad(dec2)

    if sin_dec1 is not None:
        sin_d1 = sin_dec1
        c_d1_c_r1 = cd_cr1
        c_d1_s_r1 = cd_sr1
    else:
        sin_d1 = np.sin(dec1_rad)
        c_d1_c_r1 = np.cos(dec1_rad) * np.cos(ra1_rad)
        c_d1_s_r1 = np.cos(dec1_rad) * np.sin(ra1_rad)

    sin_d2 = np.sin(dec2_rad)
    cos_d2 = np.cos(dec2_rad)
    sin_r2 = np.sin(ra2_rad)
    cos_r2 = np.cos(ra2_rad)

    # cos(sep) = sin(dec1)sin(dec2) + cos(dec1)cos(dec2)cos(ra1-ra2)
    # Expansion: cos(dec1)cos(dec2)cos(ra1-ra2) = cos(dec2)cos(ra2)cos(dec1)cos(ra1) + cos(dec2)sin(ra2)cos(dec1)sin(ra1)
    cos_sep = sin_d1 * sin_d2 + cos_d2 * (cos_r2 * c_d1_c_r1 + sin_r2 * c_d1_s_r1)

    return np.rad2deg(np.arccos(np.clip(cos_sep, -1.0, 1.0)))
