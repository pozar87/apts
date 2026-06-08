import numpy as np
import pandas as pd
from typing import Any, cast
from .utils import calculate_refraction
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
        altitude_values = altaz_df["Altitude"].apply(
            lambda x: x.magnitude if hasattr(x, "magnitude") else x
        )
        azimuth_values = altaz_df["Azimuth"].apply(
            lambda x: x.magnitude if hasattr(x, "magnitude") else x
        )
        visible_condition = conditions.is_visible(azimuth_values, altitude_values)
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
        active_ras_hours = stars_ras[potential_mask]
        active_decs_deg = stars_decs[potential_mask]

        # Get LST for all check times (in hours)
        lst_hours = check_times.gmst + place.lon_decimal / 15.0

        # Pre-calculate trigonometric values for O(N+M) optimization
        lat_rad = np.deg2rad(place.lat_decimal)
        sin_lat = np.sin(lat_rad)
        cos_lat = np.cos(lat_rad)

        # For active stars (N_active)
        ra_rad = np.deg2rad(active_ras_hours * 15.0)
        dec_rad = np.deg2rad(active_decs_deg)
        sin_ra = np.sin(ra_rad)[:, np.newaxis]
        cos_ra = np.cos(ra_rad)[:, np.newaxis]
        sin_dec = np.sin(dec_rad)[:, np.newaxis]
        cos_dec = np.cos(dec_rad)[:, np.newaxis]
        tan_dec = np.tan(dec_rad)[:, np.newaxis]

        # For check times (M_times)
        lst_rad = np.deg2rad(lst_hours * 15.0)
        sin_lst = np.sin(lst_rad)[np.newaxis, :]
        cos_lst = np.cos(lst_rad)[np.newaxis, :]

        # Use identity: cos(H) = cos(LST-RA) = cos(LST)cos(RA) + sin(LST)sin(RA)
        cos_h = cos_lst * cos_ra + sin_lst * sin_ra
        # Use identity: sin(H) = sin(LST-RA) = sin(LST)cos(RA) - cos(LST)sin(RA)
        sin_h = sin_lst * cos_ra - cos_lst * sin_ra

        # Geometric altitude and azimuth calculation
        sin_alt = sin_lat * sin_dec + cos_lat * cos_dec * cos_h

        # Convert to degrees and add atmospheric refraction
        true_alt_deg = np.rad2deg(np.arcsin(np.clip(sin_alt, -1.0, 1.0)))
        apparent_alt_deg = true_alt_deg + calculate_refraction(true_alt_deg)

        # Determine azimuth
        x = cos_h * sin_lat - tan_dec * cos_lat
        y = sin_h
        az_deg = (np.rad2deg(np.arctan2(y, x)) + 180.0) % 360.0

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
