import numpy as np
import pandas as pd
from typing import List, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ...conditions import Conditions


def analyze_weather_data(
    hourly_data: pd.DataFrame, effective_conditions: "Conditions", gettext_
) -> List[Dict[str, Any]]:
    """
    Performs vectorized weather analysis and generates reason strings for bad hours.
    """
    # Vectorized condition checks
    is_bad_clouds = hourly_data.cloudCover.isna() | (
        hourly_data.cloudCover > effective_conditions.max_clouds
    )
    is_bad_precip_prob = hourly_data.precipProbability.isna() | (
        hourly_data.precipProbability
        > effective_conditions.max_precipitation_probability
    )
    is_bad_precip_intens = hourly_data.precipIntensity.isna() | (
        hourly_data.precipIntensity > effective_conditions.max_precipitation_intensity
    )
    is_bad_wind = hourly_data.windSpeed.isna() | (
        hourly_data.windSpeed > effective_conditions.max_wind
    )
    is_bad_temp = hourly_data.temperature.isna() | (
        (effective_conditions.min_temperature > hourly_data.temperature)
        | (hourly_data.temperature > effective_conditions.max_temperature)
    )
    is_bad_vis = hourly_data.visibility.isna() | (
        hourly_data.visibility < effective_conditions.min_visibility
    )
    is_bad_fog = hourly_data.fog.isna() | (
        hourly_data.fog > effective_conditions.max_fog
    )
    is_bad_moon = (hourly_data["Altitude"] > 0) & (
        hourly_data.moonIllumination > effective_conditions.max_moon_illumination
    )
    is_bad_aurora = hourly_data.aurora.isna() | (
        hourly_data.aurora < effective_conditions.min_aurora
    )
    is_bad_seeing = hourly_data.seeing.isna() | (
        hourly_data.seeing > effective_conditions.max_seeing
    )
    is_bad_sqm = hourly_data.sqm.isna() | (
        hourly_data.sqm < effective_conditions.min_sqm
    )

    # Determine good hours
    is_good_hour_mask = ~(
        is_bad_clouds
        | is_bad_precip_prob
        | is_bad_precip_intens
        | is_bad_wind
        | is_bad_temp
        | is_bad_vis
        | is_bad_fog
        | is_bad_moon
        | is_bad_aurora
        | is_bad_seeing
        | is_bad_sqm
    )

    # Pre-populate analysis_results with vectorized data
    hourly_data = hourly_data.copy()
    hourly_data["is_good_hour"] = is_good_hour_mask
    # Initialize reasons with empty lists
    reasons_col = [[] for _ in range(len(hourly_data))]
    reason_keys_col = [[] for _ in range(len(hourly_data))]

    # Only iterate over "bad" hours to generate reason strings (optimization)
    bad_indices = np.where(~is_good_hour_mask)[0]
    if len(bad_indices) > 0:
        # Convert only bad rows to dict for much faster access than iloc in loop
        bad_rows = hourly_data.iloc[bad_indices].to_dict("records")
        for i, row in enumerate(bad_rows):
            idx = bad_indices[i]
            reasons = []
            reason_keys = []
            if is_bad_clouds.iloc[idx]:
                reason_keys.append("BAD_CLOUDS")
                reasons.append(
                    gettext_(
                        "Cloud cover %(cloud_cover)s%% exceeds limit of %(max_clouds)s%%"
                    )
                    % {
                        "cloud_cover": f"{row['cloudCover']:.1f}",
                        "max_clouds": effective_conditions.max_clouds,
                    }
                )
            if is_bad_precip_prob.iloc[idx]:
                reason_keys.append("BAD_PRECIP")
                reasons.append(
                    gettext_(
                        "Precipitation probability %(precip_prob)s%% exceeds limit of %(max_precip_prob)s%%"
                    )
                    % {
                        "precip_prob": f"{row['precipProbability']:.1f}",
                        "max_precip_prob": effective_conditions.max_precipitation_probability,
                    }
                )
            if is_bad_precip_intens.iloc[idx]:
                reason_keys.append("BAD_PRECIP")
                reasons.append(
                    gettext_(
                        "Precipitation intensity %(precip_intens)s mm exceeds limit of %(max_precip_intens)s mm"
                    )
                    % {
                        "precip_intens": f"{row['precipIntensity']:.1f}",
                        "max_precip_intens": effective_conditions.max_precipitation_intensity,
                    }
                )
            if is_bad_wind.iloc[idx]:
                reason_keys.append("BAD_WIND")
                reasons.append(
                    gettext_(
                        "Wind speed %(wind_speed)s km/h exceeds limit of %(max_wind)s km/h"
                    )
                    % {
                        "wind_speed": f"{row['windSpeed']:.1f}",
                        "max_wind": effective_conditions.max_wind,
                    }
                )
            if is_bad_temp.iloc[idx]:
                reason_keys.append("BAD_TEMP")
                reasons.append(
                    gettext_(
                        "Temperature %(temp)s°C out of range (%(min_temp)s - %(max_temp)s°C)"
                    )
                    % {
                        "temp": f"{row['temperature']:.1f}",
                        "min_temp": effective_conditions.min_temperature,
                        "max_temp": effective_conditions.max_temperature,
                    }
                )
            if is_bad_vis.iloc[idx]:
                reason_keys.append("BAD_VIS")
                reasons.append(
                    gettext_("Visibility %(vis)s km below limit of %(min_vis)s km")
                    % {
                        "vis": f"{row['visibility']:.1f}",
                        "min_vis": effective_conditions.min_visibility,
                    }
                )
            if is_bad_fog.iloc[idx]:
                reason_keys.append("BAD_FOG")
                reasons.append(
                    gettext_("Fog %(fog)s%% exceeds limit of %(max_fog)s%%")
                    % {
                        "fog": f"{row['fog']:.1f}",
                        "max_fog": effective_conditions.max_fog,
                    }
                )
            if is_bad_moon.iloc[idx]:
                reason_keys.append("BAD_MOON")
                reasons.append(
                    gettext_(
                        "Moon illumination %(illum)s%% exceeds limit of %(max_illum)s%% while moon is up"
                    )
                    % {
                        "illum": f"{row['moonIllumination']:.1f}",
                        "max_illum": effective_conditions.max_moon_illumination,
                    }
                )
            if is_bad_aurora.iloc[idx]:
                reason_keys.append("BAD_AURORA")
                reasons.append(
                    gettext_("Aurora %(aurora)s%% below limit of %(min_aurora)s%%")
                    % {
                        "aurora": f"{row['aurora']:.1f}",
                        "min_aurora": effective_conditions.min_aurora,
                    }
                )
            if is_bad_seeing.iloc[idx]:
                reason_keys.append("BAD_SEEING")
                reasons.append(
                    gettext_(
                        "Seeing %(seeing)s arcsec exceeds limit of %(max_seeing)s arcsec"
                    )
                    % {
                        "seeing": f"{row['seeing']:.1f}",
                        "max_seeing": effective_conditions.max_seeing,
                    }
                )
            if is_bad_sqm.iloc[idx]:
                reason_keys.append("BAD_SQM")
                reasons.append(
                    gettext_(
                        "Sky brightness %(sqm)s mag/arcsec² below limit of %(min_sqm)s mag/arcsec²"
                    )
                    % {
                        "sqm": f"{row['sqm']:.1f}",
                        "min_sqm": effective_conditions.min_sqm,
                    }
                )
            reasons_col[idx] = reasons
            reason_keys_col[idx] = reason_keys

    hourly_data["reasons"] = reasons_col
    hourly_data["reason_keys"] = reason_keys_col

    from .constants import RENAME_MAP, FINAL_COLS

    result_df = pd.DataFrame(hourly_data[FINAL_COLS]).rename(columns=RENAME_MAP)
    return result_df.to_dict("records")
