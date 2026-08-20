from datetime import timedelta
from typing import Any, cast

import numpy as np
import pandas as pd
import pytz

from .refraction import calculate_refraction


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
