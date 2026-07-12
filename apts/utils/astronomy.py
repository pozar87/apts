from datetime import timedelta
from typing import Any, cast, Tuple, Union, Optional

import numpy as np
import pandas as pd
import pytz


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


def vectorized_geometric_altaz(
    lat_deg: float,
    lon_decimal: float,
    ras: np.ndarray,
    decs: np.ndarray,
    check_times_gmst: Union[float, np.ndarray],
    sin_dec: Optional[np.ndarray] = None,
    cd_cr: Optional[np.ndarray] = None,
    cd_sr: Optional[np.ndarray] = None,
) -> Tuple[np.ndarray, np.ndarray]:
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

    # sin(alt) = sin(lat)sin(dec) + cos(lat)cos(dec)cos(LST-RA)
    # Expansion: cos(dec)cos(LST-RA) = cos(LST)cos(dec)cos(RA) + sin(LST)cos(dec)sin(RA)
    sin_alt = sin_lat * sin_dec + cos_lat * (cos_lst * cd_cr + sin_lst * cd_sr)
    true_alt_deg = np.rad2deg(np.arcsin(np.clip(sin_alt, -1.0, 1.0)))

    # Azimuth calculation using direction cosines
    # x_cd = cos(H)sin(lat) - tan(dec)cos(lat) * cos(dec) = cos(H)sin(lat)cos(dec) - sin(dec)cos(lat)
    x_cd = (cos_lst * cd_cr + sin_lst * cd_sr) * sin_lat - sin_dec * cos_lat
    y_cd = sin_lst * cd_cr - cos_lst * cd_sr
    az_deg = (np.rad2deg(np.arctan2(y_cd, x_cd)) + 180.0) % 360.0

    return true_alt_deg, az_deg


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


def vectorized_geometric_compute(
    ts,
    lat_deg,
    lon_decimal,
    local_timezone,
    observer_date,
    ras,
    decs,
    valid_mask,
    df_len,
    sin_dec=None,
    cd_cr=None,
    cd_sr=None,
):
    """
    Generic vectorized transit, altitude, rising, and setting calculation.
    Uses vectorized numpy operations and geometric approximations for speed.
    """
    current_dt = observer_date.utc_datetime()
    t0_dt = current_dt.replace(
        hour=0, minute=0, second=0, microsecond=0, tzinfo=pytz.UTC
    )
    t0 = ts.utc(t0_dt)
    lon_hours = lon_decimal / 15.0
    current_gmst = t0.gmst
    sidereal_to_solar = 0.99726957

    # Vectorized Transit calculation
    target_gmst = (ras - lon_hours) % 24
    dt_solar = ((target_gmst - current_gmst) % 24) * sidereal_to_solar

    # Use pandas for datetime vectorization
    t0_ts = pd.Timestamp(t0_dt)
    transit_times = (t0_ts + pd.to_timedelta(dt_solar * 3600, unit="s")).floor("s")

    # Adjust for 12-hour window relative to current time
    cutoff = current_dt - timedelta(hours=12)
    shift = timedelta(hours=24 * sidereal_to_solar)

    transit_times = pd.Series(transit_times)
    cutoff_ts = pd.Timestamp(cutoff)
    if transit_times.dt.tz is None and cutoff_ts.tz is not None:
        cutoff_ts = cutoff_ts.replace(tzinfo=None)
    elif transit_times.dt.tz is not None and cutoff_ts.tz is None:
        cutoff_ts = cutoff_ts.replace(tzinfo=pytz.UTC)

    needs_shift = transit_times < cutoff_ts
    transit_times.loc[needs_shift] += shift

    # Localize transits
    transit_times_local = transit_times.dt.tz_convert(local_timezone)
    transits = (
        transit_times_local.astype(object)
        .where(valid_mask & transit_times_local.notnull(), None)
        .to_list()
    )

    # Vectorized Altitude calculation
    altitudes = 90.0 - np.abs(lat_deg - decs)
    altitudes += calculate_refraction(altitudes)
    alts = np.where(valid_mask, altitudes, 0).tolist()

    # Vectorized Rise/Set (Geometric) calculation
    lat_rad = np.deg2rad(lat_deg)
    h0_rad = np.deg2rad(-34.0 / 60.0)

    if sin_dec is not None:
        cos_dec = np.cos(np.deg2rad(decs))
        cos_H = (np.sin(h0_rad) - np.sin(lat_rad) * sin_dec) / (
            np.cos(lat_rad) * cos_dec
        )
    else:
        decs_rad = np.deg2rad(decs)
        cos_H = (np.sin(h0_rad) - np.sin(lat_rad) * np.sin(decs_rad)) / (
            np.cos(lat_rad) * np.cos(decs_rad)
        )

    H_hours = np.full(df_len, np.nan)
    h_mask = valid_mask & (cos_H >= -1) & (cos_H <= 1)
    H_hours[h_mask] = (
        np.arccos(np.clip(cos_H[h_mask], -1.0, 1.0))
        * (12.0 / np.pi)
        * sidereal_to_solar
    )

    H_delta = cast(Any, pd.to_timedelta(H_hours * 3600, unit="s")).round("s")
    rising_times = (transit_times - H_delta).dt.floor("s")
    setting_times = (transit_times + H_delta).dt.floor("s")

    rising_times_local = rising_times.dt.tz_convert(local_timezone)
    setting_times_local = setting_times.dt.tz_convert(local_timezone)

    rises = (
        rising_times_local.astype(object)
        .where(rising_times_local.notnull(), None)
        .to_list()
    )
    sets = (
        setting_times_local.astype(object)
        .where(setting_times_local.notnull(), None)
        .to_list()
    )

    return transits, alts, rises, sets


def vectorized_geometric_imaging_duration(
    lat_deg,
    ras,
    decs,
    valid_mask,
    transits,
    dark_start,
    dark_end,
    min_altitude=30.0,
    sin_dec=None,
):
    """
    Fast calculation of imaging window duration (minutes above threshold during darkness)
    for a set of Stars using vectorized geometric formulas.
    """
    sidereal_to_solar = 0.99726957
    lat_rad = np.deg2rad(lat_deg)
    h0_rad = np.deg2rad(min_altitude)

    if sin_dec is not None:
        cos_dec = np.cos(np.deg2rad(decs))
        cos_H = (np.sin(h0_rad) - np.sin(lat_rad) * sin_dec) / (
            np.cos(lat_rad) * cos_dec
        )
    else:
        decs_rad = np.deg2rad(decs)
        cos_H = (np.sin(h0_rad) - np.sin(lat_rad) * np.sin(decs_rad)) / (
            np.cos(lat_rad) * np.cos(decs_rad)
        )

    H_hours = np.full(len(ras), np.nan)
    h_mask = valid_mask & (cos_H >= -1) & (cos_H <= 1)
    H_hours[h_mask] = (
        np.arccos(np.clip(cos_H[h_mask], -1.0, 1.0))
        * (12.0 / np.pi)
        * sidereal_to_solar
    )

    H_delta = pd.to_timedelta(H_hours * 3600, unit="s").round("s")  # type: ignore[arg-type]
    rising_times = (transits - H_delta).dt.floor("s")
    setting_times = (transits + H_delta).dt.floor("s")

    def to_utc_naive(dt):
        if hasattr(dt, "utc_datetime"):
            dt = dt.utc_datetime()
        ts = pd.Timestamp(dt)
        if ts.tz is not None:
            return ts.tz_convert(None)
        return ts

    dark_start_ts = to_utc_naive(dark_start)
    dark_end_ts = to_utc_naive(dark_end)

    rises_utc = rising_times.dt.tz_localize(None)
    sets_utc = setting_times.dt.tz_localize(None)

    win_starts = pd.Series(
        np.maximum(rises_utc.values, dark_start_ts.to_datetime64()),
        index=transits.index,
    )
    win_ends = pd.Series(
        np.minimum(sets_utc.values, dark_end_ts.to_datetime64()), index=transits.index
    )

    durations = (win_ends - win_starts).dt.total_seconds() / 60.0
    durations = np.where((durations > 0) & h_mask, durations, 0.0)

    return durations.tolist()
