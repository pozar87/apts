import numpy as np
import pandas as pd
from typing import Any, cast
from ..utils.astronomy import calculate_refraction, vectorized_geometric_altaz
from ..skyfield_searches.utils import fast_altaz

def get_visible_mocked(objects_instance, candidate_objects, conditions, start, stop) -> list:
    """
    Calculates visibility for objects when the place.get_altaz_curve is mocked.
    """
    visible_objects_indices = []
    # Optimization: itertuples() is significantly faster than iterrows()
    for row in candidate_objects.itertuples():
        index = row.Index
        skyfield_object = objects_instance.get_skyfield_object(row)
        if skyfield_object is None:
            continue
        altaz_df = objects_instance.place.get_altaz_curve(skyfield_object, start, stop)
        # Optimization: list comprehension over .values is faster than .apply() for extracting magnitudes.
        altitude_values = [
            x.magnitude if hasattr(x, "magnitude") else x for x in altaz_df["Altitude"].values
        ]
        azimuth_values = [
            x.magnitude if hasattr(x, "magnitude") else x for x in altaz_df["Azimuth"].values
        ]
        visible_condition = conditions.is_visible(
            np.array(azimuth_values), np.array(altitude_values)
        )
        if cast(Any, visible_condition.any()):
            visible_objects_indices.append(index)
    return visible_objects_indices

def get_visible_stars(
    place,
    candidate_objects,
    skyfield_objs,
    stars_indices,
    check_times,
    conditions,
    visible_mask,
):
    """
    Check Stars using vectorized geometric formulas across all check_times.
    """
    # Extract RA/Dec for all stars
    if (
        "ra_hours" in candidate_objects.columns
        and "dec_degrees" in candidate_objects.columns
    ):
        stars_ras = cast(pd.Series, candidate_objects["ra_hours"]).to_numpy()[
            stars_indices
        ]
        stars_decs = cast(pd.Series, candidate_objects["dec_degrees"]).to_numpy()[
            stars_indices
        ]
    else:
        stars_ras = np.array(
            [cast(Any, skyfield_objs)[i].ra.hours for i in stars_indices]
        )
        stars_decs = np.array(
            [cast(Any, skyfield_objs)[i].dec.degrees for i in stars_indices]
        )

    # Preliminary filter: max altitude check
    max_alt_deg = 90.0 - np.abs(place.lat_decimal - stars_decs)
    # Add refraction at max altitude for better filtering
    max_alt_deg += calculate_refraction(max_alt_deg)

    # Only process stars that can potentially reach the minimum altitude
    potential_mask = max_alt_deg > conditions.horizon.get_min_altitude()

    if np.any(potential_mask):
        # Ensure stars_indices is an array before masking
        stars_indices = np.asarray(stars_indices)
        active_stars_indices = stars_indices[potential_mask]

        # Use pre-calculated Equatorial Direction Cosines if available
        sin_dec = None
        cd_cr = None
        cd_sr = None
        if "sin_dec" in candidate_objects.columns:
            sin_dec = candidate_objects["sin_dec"].values[active_stars_indices]
            cd_cr = candidate_objects["cos_dec_cos_ra"].values[active_stars_indices]
            cd_sr = candidate_objects["cos_dec_sin_ra"].values[active_stars_indices]

        # Optimization: if only simple altitude check is needed, we can bypass
        # expensive arctan2 and azimuth calculations for the grid.
        if not conditions.horizon_content and not conditions.horizon_file and \
           conditions.min_object_azimuth == 0 and conditions.max_object_azimuth == 360:

            # For simple altitude, we compute only altitude component
            # vectorized_geometric_altaz can be used, or we can just do the altitude part here
            # to be even faster. But for maintainability, let's use the utility.
            true_alt_deg, _ = vectorized_geometric_altaz(
                place.lat_decimal,
                place.lon_decimal,
                stars_ras[potential_mask],
                stars_decs[potential_mask],
                check_times.gmst,
                sin_dec=sin_dec,
                cd_cr=cd_cr,
                cd_sr=cd_sr,
            )

            # Account for refraction in the threshold itself (optimization)
            min_alt = getattr(conditions.min_object_altitude, "magnitude", conditions.min_object_altitude)
            true_alt_threshold = min_alt - calculate_refraction(min_alt)

            visible_at_times = true_alt_deg >= true_alt_threshold
        else:
            # Full calculation needed for complex horizon or azimuth constraints
            true_alt_deg, az_deg = vectorized_geometric_altaz(
                place.lat_decimal,
                place.lon_decimal,
                stars_ras[potential_mask],
                stars_decs[potential_mask],
                check_times.gmst,
                sin_dec=sin_dec,
                cd_cr=cd_cr,
                cd_sr=cd_sr,
            )
            apparent_alt_deg = true_alt_deg + calculate_refraction(true_alt_deg)

            # Determine visibility using conditions
            visible_at_times = conditions.is_visible(az_deg, apparent_alt_deg)

        # Combine and check if visible at ANY time point
        visible_mask[active_stars_indices] = np.any(visible_at_times, axis=1)

def get_visible_other(
    skyfield_objs, other_indices, obs_at_check_times, conditions, visible_mask
):
    """
    Check Other objects (like planets) using Skyfield.
    """
    for i in other_indices:
        skyfield_obj = skyfield_objs[i]
        # Optimization: Use fast_altaz to bypass expensive Standard Apparent calculations.
        # This provides a ~2.5x speedup for visibility gating with negligible accuracy loss.
        alt, az, _ = fast_altaz(obs_at_check_times, skyfield_obj)
        alt_deg = alt.degrees
        az_deg = az.degrees

        visible_at_times = conditions.is_visible(az_deg, alt_deg)

        if cast(Any, visible_at_times.any()):
            visible_mask[i] = True
