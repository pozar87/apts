import pandas as pd

from ..constants import ObjectTableLabels
from .rules import ALTITUDE_RULE, WINDOW_RULE, FOV_RULE, BRIGHTNESS_RULE, MOON_RULE


def calculate_altitude_score(altitude: float) -> int:
    """S_alt: Altitude score (Max 30 pts)"""
    return ALTITUDE_RULE.score(altitude)


def calculate_window_score(window_minutes: float) -> int:
    """S_win: Imaging Window score (Max 20 pts)"""
    return WINDOW_RULE.score(window_minutes / 60.0)


def calculate_fov_score(fov_ratio: float) -> int:
    """S_fov: FOV Fit score (Max 30 pts)"""
    return FOV_RULE.score(fov_ratio)


def calculate_moon_penalty_score(
    moon_separation: float, is_narrowband: bool = False
) -> float:
    """S_moon: Moon Penalty score (Max 20 pts)"""
    return MOON_RULE.score(moon_separation, is_narrowband)


def calculate_brightness_score(magnitude: float) -> int:
    """S_bright: Brightness score (Max 10 pts)"""
    return BRIGHTNESS_RULE.score(magnitude)


def calculate_scores_bulk(
    df: pd.DataFrame, is_narrowband: bool = False
) -> pd.DataFrame:
    """
    Vectorized calculation of scores for a DataFrame of targets.
    """
    alt = df[ObjectTableLabels.ALTITUDE].to_numpy()
    s_alt = ALTITUDE_RULE.score_bulk(alt)

    hours = df["window_minutes"].to_numpy() / 60.0
    s_win = WINDOW_RULE.score_bulk(hours)

    fov = df["fov_ratio"].to_numpy()
    s_fov = FOV_RULE.score_bulk(fov)

    moon_sep = df["moon_separation"].to_numpy()
    s_moon = MOON_RULE.score_bulk(moon_sep, is_narrowband)

    mag = df["Magnitude_float"].to_numpy()
    s_bright = BRIGHTNESS_RULE.score_bulk(mag)

    total_score = s_alt + s_win + s_fov + s_moon + s_bright

    return pd.DataFrame(
        {
            "total_score": total_score,
            "s_alt": s_alt,
            "s_win": s_win,
            "s_fov": s_fov,
            "s_moon": s_moon,
            "s_bright": s_bright,
            "altitude": alt,
            "window_minutes": df["window_minutes"].to_numpy(),
            "moon_separation": moon_sep,
        },
        index=df.index,
    )
