from typing import Tuple, Union, Optional
import numpy as np


def vectorized_geometric_altaz(
    lat_deg: float,
    lon_decimal: float,
    ras: np.ndarray,
    decs: np.ndarray,
    check_times_gmst: Union[float, np.ndarray],
    sin_dec: Optional[np.ndarray] = None,
    cd_cr: Optional[np.ndarray] = None,
    cd_sr: Optional[np.ndarray] = None,
    return_azimuth: bool = True,
    return_alt_degrees: bool = True,
) -> Tuple[np.ndarray, Optional[np.ndarray]]:
    """
    Lightning fast geometric altitude and azimuth calculation using vectorized NumPy operations.
    Supports broadcasting for both single-time and multi-time calculations.

    ras: RA in decimal hours
    decs: Dec in decimal degrees
    check_times_gmst: GMST in decimal hours (scalar or 1D array)
    """
    # LST calculation
    lst_hours = check_times_gmst + lon_decimal / 15.0
    lat_rad = np.deg2rad(lat_deg)
    lst_rad = np.deg2rad(lst_hours * 15.0)

    sin_lat = np.sin(lat_rad)
    cos_lat = np.cos(lat_rad)

    # Handling broadcasting for multi-time (check_times_gmst is 1D array)
    # and multi-object (ras/decs are 1D arrays).
    if isinstance(lst_rad, np.ndarray) and lst_rad.ndim == 1:
        # Shapes: Objects (N, 1), Times (1, M)
        sin_lst = np.sin(lst_rad)[np.newaxis, :]
        cos_lst = np.cos(lst_rad)[np.newaxis, :]
        if sin_dec is not None:
            sin_dec = sin_dec[:, np.newaxis]
            cd_cr = cd_cr[:, np.newaxis]
            cd_sr = cd_sr[:, np.newaxis]
        else:
            ra_rad = np.deg2rad(ras * 15.0)[:, np.newaxis]
            dec_rad = np.deg2rad(decs)[:, np.newaxis]
            sin_dec = np.sin(dec_rad)
            cd_cr = np.cos(dec_rad) * np.cos(ra_rad)
            cd_sr = np.cos(dec_rad) * np.sin(ra_rad)
    else:
        # Scalar time case
        sin_lst = np.sin(lst_rad)
        cos_lst = np.cos(lst_rad)
        if sin_dec is None:
            ra_rad = np.deg2rad(ras * 15.0)
            dec_rad = np.deg2rad(decs)
            sin_dec = np.sin(dec_rad)
            cd_cr = np.cos(dec_rad) * np.cos(ra_rad)
            cd_sr = np.cos(dec_rad) * np.sin(ra_rad)

    # Optimization: cache the intermediate products used by both altitude and azimuth
    # cd_ch = cos(dec) * cos(hour_angle) = cos(dec) * cos(LST - RA)
    # Expansion: cos(dec)cos(LST-RA) = cos(LST)cos(dec)cos(RA) + sin(LST)cos(dec)sin(RA)
    cd_ch = cos_lst * cd_cr + sin_lst * cd_sr

    # sin(alt) = sin(lat)sin(dec) + cos(lat)cos(dec)cos(LST-RA)
    sin_alt = sin_lat * sin_dec + cos_lat * cd_ch

    if return_alt_degrees:
        res_alt = np.rad2deg(np.arcsin(np.clip(sin_alt, -1.0, 1.0)))
    else:
        # Return raw sin(alt) if degrees are not requested
        res_alt = sin_alt

    az_deg = None
    if return_azimuth:
        # Azimuth calculation using direction cosines
        # x_cd = cos(H)sin(lat)cos(dec) - sin(dec)cos(lat)
        x_cd = cd_ch * sin_lat - sin_dec * cos_lat
        y_cd = sin_lst * cd_cr - cos_lst * cd_sr
        az_deg = (np.rad2deg(np.arctan2(y_cd, x_cd)) + 180.0) % 360.0

    return res_alt, az_deg
