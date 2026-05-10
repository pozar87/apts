import logging
import pandas as pd
from ...constants import ObjectTableLabels

logger = logging.getLogger(__name__)


def suggest_polar_alignment_stars(
    observation, magnitude_limit=4.0, min_alt=20, max_alt=70
):
    """
    Suggests bright stars for polar alignment based on current visibility and horizon.
    Optimal stars are between 20 and 70 degrees in altitude.
    """
    if observation.effective_date is None:
        logger.warning("Observation effective_date is None, cannot suggest stars.")
        return pd.DataFrame()

    # We want stars visible AT THE MOMENT of alignment
    start_time = observation.observation_local_time
    if start_time is None:
        # Fallback to place date
        if hasattr(observation.place.date, "utc_datetime"):
            start_time = observation.place.date.utc_datetime()
        else:
            start_time = observation.place.date

    # Use a very short window for 'now'
    if isinstance(start_time, pd.Timestamp):
        stop_time = start_time + pd.Timedelta(seconds=1)
    elif isinstance(start_time, (int, float)):
        # Probably shouldn't happen but let's be safe
        stop_time = start_time + 1 / 86400.0
    else:
        from datetime import timedelta

        try:
            stop_time = start_time + timedelta(seconds=1)
        except Exception:
            # Last resort
            stop_time = start_time

    visible_stars = observation.local_stars.get_visible(
        observation.conditions,
        start_time,
        stop_time,
        star_magnitude_limit=magnitude_limit,
    )

    if visible_stars.empty:
        return visible_stars

    # Filter by altitude range
    # Note: get_visible ensures ALTITUDE is computed for visible objects
    mask = (visible_stars[ObjectTableLabels.ALTITUDE] >= min_alt) & (
        visible_stars[ObjectTableLabels.ALTITUDE] <= max_alt
    )

    candidates = visible_stars[mask].copy()

    # Sort by brightness
    if "Magnitude_float" in candidates.columns:
        candidates = candidates.sort_values(by="Magnitude_float")

    return candidates
