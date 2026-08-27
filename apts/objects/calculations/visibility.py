import numpy as np
import pandas as pd
from typing import Any, Optional, cast, Union


def filter_objects_by_magnitude(
    objects_df: pd.DataFrame,
    conditions: Any,
    star_magnitude_limit: Optional[Any] = None,
    limiting_magnitude: Optional[Any] = None,
) -> pd.DataFrame:
    """
    Filters objects based on magnitude limits.
    """
    max_magnitude_q = (
        limiting_magnitude
        if limiting_magnitude is not None
        else (
            star_magnitude_limit
            if star_magnitude_limit is not None
            else conditions.max_object_magnitude
        )
    )

    # Ensure max_magnitude is a float for comparison with magnitude_values
    max_mag_float = (
        max_magnitude_q.magnitude
        if hasattr(max_magnitude_q, "magnitude")
        else max_magnitude_q
    )

    # Optimization: use pre-calculated float magnitudes if available
    if "Magnitude_float" in objects_df.columns:
        magnitude_values = objects_df["Magnitude_float"]
    else:
        # Optimization: list comprehension over .values is faster than .apply() for extracting magnitudes.
        magnitude_values = np.array(
            [
                x.magnitude if hasattr(x, "magnitude") else x
                for x in objects_df["Magnitude"].values
            ]
        )
    return cast(pd.DataFrame, objects_df[magnitude_values < max_mag_float].copy())


def calculate_visible_stars_mask(
    lat_decimal: float,
    lon_decimal: float,
    stars_ras: np.ndarray,
    stars_decs: np.ndarray,
    check_times_gmst: Union[float, np.ndarray],
    conditions: Any,
    sin_dec: Optional[np.ndarray] = None,
    cos_dec_cos_ra: Optional[np.ndarray] = None,
    cos_dec_sin_ra: Optional[np.ndarray] = None,
) -> np.ndarray:
    """
    Check Stars using vectorized geometric formulas across all check_times.
    Returns a boolean mask of which stars are visible at ANY time point.
    """
    from ...utils.astronomy.refraction import calculate_refraction
    from ...utils.astronomy.altaz import vectorized_geometric_altaz

    # Preliminary filter: max altitude check
    max_alt_deg = 90.0 - np.abs(lat_decimal - stars_decs)
    min_alt = conditions.horizon.get_min_altitude()

    # Optimization: Refraction is monotonically decreasing with altitude for alt > -1.0.
    # Evaluating calculate_refraction on the full N-element max_alt_deg array (e.g., 14,000 objects)
    # before pruning is expensive. Pre-computing a conservative scalar upper-bound refraction offset
    # at min_alt - 1.0 deg provides an exact lower bound for max altitude checks with zero false negatives
    # and avoids array-wide refraction calculations.
    ref_bound = float(calculate_refraction(max(-0.99, min_alt - 1.0)))

    # Only process stars that can potentially reach the minimum altitude
    potential_mask = max_alt_deg > (min_alt - ref_bound)

    visible_stars_mask = np.zeros(len(stars_ras), dtype=bool)

    if np.any(potential_mask):
        # Filter arrays for active stars
        active_ras = stars_ras[potential_mask]
        active_decs = stars_decs[potential_mask]

        active_sin_dec = sin_dec[potential_mask] if sin_dec is not None else None
        active_cd_cr = cos_dec_cos_ra[potential_mask] if cos_dec_cos_ra is not None else None
        active_cd_sr = cos_dec_sin_ra[potential_mask] if cos_dec_sin_ra is not None else None

        # Optimization: if only simple altitude check is needed, we can bypass
        # expensive arctan2 and azimuth calculations for the grid.
        if not conditions.horizon_content and not conditions.horizon_file and \
           conditions.min_object_azimuth == 0 and conditions.max_object_azimuth == 360:

            # Optimization: By comparing sin(alt) directly with sin(threshold), we can
            # bypass expensive arcsin calls on the N x M grid.
            # This provides a ~2x speedup compared to calculating altitude degrees alone.
            sin_alt, _ = vectorized_geometric_altaz(
                lat_decimal,
                lon_decimal,
                active_ras,
                active_decs,
                check_times_gmst,
                sin_dec=active_sin_dec,
                cd_cr=active_cd_cr,
                cd_sr=active_cd_sr,
                return_azimuth=False,
                return_alt_degrees=False,
            )

            # Account for refraction in the threshold itself (optimization)
            min_alt = getattr(conditions.min_object_altitude, "magnitude", conditions.min_object_altitude)
            true_alt_threshold = min_alt - calculate_refraction(min_alt)
            sin_threshold = np.sin(np.deg2rad(true_alt_threshold))

            visible_at_times = sin_alt >= sin_threshold
        else:
            # Full calculation needed for complex horizon or azimuth constraints
            true_alt_deg, az_deg = vectorized_geometric_altaz(
                lat_decimal,
                lon_decimal,
                active_ras,
                active_decs,
                check_times_gmst,
                sin_dec=active_sin_dec,
                cd_cr=active_cd_cr,
                cd_sr=active_cd_sr,
            )
            apparent_alt_deg = true_alt_deg + calculate_refraction(true_alt_deg)

            # Determine visibility using conditions
            visible_at_times = conditions.is_visible(az_deg, apparent_alt_deg)

        # Combine and check if visible at ANY time point
        visible_stars_mask[potential_mask] = np.any(visible_at_times, axis=1)

    return visible_stars_mask
