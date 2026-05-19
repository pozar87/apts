from typing import Optional, cast

import numpy as np
import pandas as pd

from ...conditions import Conditions
from ...i18n import language_context


def compute_condition_masks(
    hourly_data: pd.DataFrame, conditions: Conditions
) -> dict[str, pd.Series]:
    """Performs vectorized condition checks and returns masks for bad weather."""
    return {
        "is_bad_clouds": hourly_data.cloudCover.isna()
        | (hourly_data.cloudCover > conditions.max_clouds),
        "is_bad_precip_prob": hourly_data.precipProbability.isna()
        | (
            hourly_data.precipProbability
            > conditions.max_precipitation_probability
        ),
        "is_bad_precip_intens": hourly_data.precipIntensity.isna()
        | (hourly_data.precipIntensity > conditions.max_precipitation_intensity),
        "is_bad_wind": hourly_data.windSpeed.isna()
        | (hourly_data.windSpeed > conditions.max_wind),
        "is_bad_temp": hourly_data.temperature.isna()
        | (
            (conditions.min_temperature > hourly_data.temperature)
            | (hourly_data.temperature > conditions.max_temperature)
        ),
        "is_bad_vis": hourly_data.visibility.isna()
        | (hourly_data.visibility < conditions.min_visibility),
        "is_bad_fog": hourly_data.fog.isna()
        | (hourly_data.fog > conditions.max_fog),
        "is_bad_moon": (hourly_data["Altitude"] > 0)
        & (hourly_data.moonIllumination > conditions.max_moon_illumination),
        "is_bad_aurora": hourly_data.aurora.isna()
        | (hourly_data.aurora < conditions.min_aurora),
        "is_bad_seeing": hourly_data.seeing.isna()
        | (hourly_data.seeing > conditions.max_seeing),
        "is_bad_sqm": hourly_data.sqm.isna() | (hourly_data.sqm < conditions.min_sqm),
    }


def get_good_hour_mask(
    hourly_data: pd.DataFrame,
    conditions: Conditions,
    masks: Optional[dict[str, pd.Series]] = None,
) -> pd.Series:
    """
    Returns a boolean mask indicating which hours meet all weather conditions.
    This is much faster than generate_analysis_records as it skips localized
    string generation and dictionary conversion.
    """
    if masks is None:
        masks = compute_condition_masks(hourly_data, conditions)

    if not masks:
        return pd.Series(True, index=hourly_data.index)

    return ~pd.concat(masks.values(), axis=1).any(axis=1)


def generate_analysis_records(
    hourly_data: pd.DataFrame,
    masks: dict[str, pd.Series],
    conditions: Conditions,
    language: Optional[str] = None,
) -> list[dict]:
    """Generates localized analysis records for each hour."""
    # Determine good hours
    is_good_hour_mask = get_good_hour_mask(hourly_data, conditions, masks=masks)
    hourly_data["is_good_hour"] = is_good_hour_mask

    reasons_col = [[] for _ in range(len(hourly_data))]
    reason_keys_col = [[] for _ in range(len(hourly_data))]

    with language_context(language):
        from ...i18n import gettext_

        bad_indices = np.where(~is_good_hour_mask)[0]
        if len(bad_indices) > 0:
            # Optimization: Extract data only for bad hours as Python primitives
            # and iterate over them. Iterating over a list of dicts is faster
            # than row access in a large DataFrame.
            bad_data_subset = hourly_data.iloc[bad_indices]
            bad_rows = bad_data_subset.to_dict("records")
            for i, row in enumerate(bad_rows):
                idx = bad_indices[i]
                reasons = []
                reason_keys = []

                if masks["is_bad_clouds"].iloc[idx]:
                    reason_keys.append("BAD_CLOUDS")
                    reasons.append(
                        gettext_(
                            "Cloud cover %(cloud_cover)s%% exceeds limit of %(max_clouds)s%%"
                        )
                        % {
                            "cloud_cover": f"{row['cloudCover']:.1f}",
                            "max_clouds": conditions.max_clouds,
                        }
                    )
                if masks["is_bad_precip_prob"].iloc[idx]:
                    reason_keys.append("BAD_PRECIP")
                    reasons.append(
                        gettext_(
                            "Precipitation probability %(precip_prob)s%% exceeds limit of %(max_precip_prob)s%%"
                        )
                        % {
                            "precip_prob": f"{row['precipProbability']:.1f}",
                            "max_precip_prob": conditions.max_precipitation_probability,
                        }
                    )
                if masks["is_bad_precip_intens"].iloc[idx]:
                    reason_keys.append("BAD_PRECIP")
                    reasons.append(
                        gettext_(
                            "Precipitation intensity %(precip_intens)s mm exceeds limit of %(max_precip_intens)s mm"
                        )
                        % {
                            "precip_intens": f"{row['precipIntensity']:.1f}",
                            "max_precip_intens": conditions.max_precipitation_intensity,
                        }
                    )
                if masks["is_bad_wind"].iloc[idx]:
                    reason_keys.append("BAD_WIND")
                    reasons.append(
                        gettext_(
                            "Wind speed %(wind_speed)s km/h exceeds limit of %(max_wind)s km/h"
                        )
                        % {
                            "wind_speed": f"{row['windSpeed']:.1f}",
                            "max_wind": conditions.max_wind,
                        }
                    )
                if masks["is_bad_temp"].iloc[idx]:
                    reason_keys.append("BAD_TEMP")
                    reasons.append(
                        gettext_(
                            "Temperature %(temp)s°C out of range (%(min_temp)s - %(max_temp)s°C)"
                        )
                        % {
                            "temp": f"{row['temperature']:.1f}",
                            "min_temp": conditions.min_temperature,
                            "max_temp": conditions.max_temperature,
                        }
                    )
                if masks["is_bad_vis"].iloc[idx]:
                    reason_keys.append("BAD_VIS")
                    reasons.append(
                        gettext_(
                            "Visibility %(vis)s km below limit of %(min_vis)s km"
                        )
                        % {
                            "vis": f"{row['visibility']:.1f}",
                            "min_vis": conditions.min_visibility,
                        }
                    )
                if masks["is_bad_fog"].iloc[idx]:
                    reason_keys.append("BAD_FOG")
                    reasons.append(
                        gettext_("Fog %(fog)s%% exceeds limit of %(max_fog)s%%")
                        % {
                            "fog": f"{row['fog']:.1f}",
                            "max_fog": conditions.max_fog,
                        }
                    )
                if masks["is_bad_moon"].iloc[idx]:
                    reason_keys.append("BAD_MOON")
                    reasons.append(
                        gettext_(
                            "Moon illumination %(illum)s%% exceeds limit of %(max_illum)s%% while moon is up"
                        )
                        % {
                            "illum": f"{row['moonIllumination']:.1f}",
                            "max_illum": conditions.max_moon_illumination,
                        }
                    )
                if masks["is_bad_aurora"].iloc[idx]:
                    reason_keys.append("BAD_AURORA")
                    reasons.append(
                        gettext_(
                            "Aurora %(aurora)s%% below limit of %(min_aurora)s%%"
                        )
                        % {
                            "aurora": f"{row['aurora']:.1f}",
                            "min_aurora": conditions.min_aurora,
                        }
                    )
                if masks["is_bad_seeing"].iloc[idx]:
                    reason_keys.append("BAD_SEEING")
                    reasons.append(
                        gettext_(
                            "Seeing %(seeing)s arcsec exceeds limit of %(max_seeing)s arcsec"
                        )
                        % {
                            "seeing": f"{row['seeing']:.1f}",
                            "max_seeing": conditions.max_seeing,
                        }
                    )
                if masks["is_bad_sqm"].iloc[idx]:
                    reason_keys.append("BAD_SQM")
                    reasons.append(
                        gettext_(
                            "Sky brightness %(sqm)s mag/arcsec² below limit of %(min_sqm)s mag/arcsec²"
                        )
                        % {
                            "sqm": f"{row['sqm']:.1f}",
                            "min_sqm": conditions.min_sqm,
                        }
                    )
                reasons_col[idx] = reasons
                reason_keys_col[idx] = reason_keys

    hourly_data["reasons"] = reasons_col
    hourly_data["reason_keys"] = reason_keys_col

    rename_map = {
        "cloudCover": "clouds",
        "precipProbability": "precipitation",
        "precipIntensity": "precipitation_intensity",
        "windSpeed": "wind_speed",
        "moonIllumination": "moon_illumination",
    }
    final_cols = [
        "time",
        "is_good_hour",
        "reasons",
        "reason_keys",
        "temperature",
        "cloudCover",
        "precipProbability",
        "precipIntensity",
        "windSpeed",
        "visibility",
        "moonIllumination",
        "fog",
        "aurora",
        "seeing",
        "sqm",
    ]
    return (
        cast(pd.DataFrame, hourly_data[final_cols])
        .rename(columns=rename_map)
        .to_dict("records")
    )
