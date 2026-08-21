import logging
from datetime import datetime, timedelta, timezone
from typing import Optional, Any
from ..constants.twilight import Twilight

logger = logging.getLogger(__name__)


def find_best_observation_window(place: Any, conditions: Any, target_date: Optional[Any] = None) -> tuple[Optional[datetime], Optional[datetime]]:
    """
    Attempts to find sunset and sunrise times using the requested twilight.
    If the requested twilight is not reached (common at high latitudes),
    it falls back to less strict twilights.
    """
    requested_twilight = conditions.twilight

    # Define the priority of twilights (strictest to least strict)
    twilight_priority = [
        Twilight.ASTRONOMICAL,
        Twilight.NAUTICAL,
        Twilight.CIVIL,
        None,  # Actual sunset/sunrise
    ]

    # Find where to start based on requested twilight
    try:
        start_idx = twilight_priority.index(requested_twilight)
    except ValueError:
        # Fallback if somehow an unknown twilight is passed
        start_idx = 0

    for i in range(start_idx, len(twilight_priority)):
        twilight = twilight_priority[i]
        start = place.sunset_time(target_date=target_date, twilight=twilight)
        if start:
            stop = place.sunrise_time(
                start_search_from=start, twilight=twilight
            )
            if stop:
                if twilight != requested_twilight:
                    logger.warning(
                        f"Could not determine observation window for {place.name} "
                        f"with requested twilight '{requested_twilight.value}'. "
                        f"Falling back to '{twilight.value if twilight else 'sunset/sunrise'}'. "
                    )
                return start, stop
    return None, None


def apply_start_time_override(start: datetime, start_time_setting: Any) -> datetime:
    """
    Applies start_time override from conditions to start datetime.
    """
    if isinstance(start_time_setting, str):
        parts = [int(v) for v in start_time_setting.split(":")]
        h = parts[0]
        m = parts[1] if len(parts) > 1 else 0
        s = parts[2] if len(parts) > 2 else 0
        return start.replace(
            hour=h,
            minute=m,
            second=s,
        )
    else:
        # Assume it's a datetime/time object and take its time components
        return start.replace(
            hour=start_time_setting.hour,
            minute=start_time_setting.minute,
            second=start_time_setting.second,
        )


def normalize_window(start: datetime, stop: datetime) -> tuple[datetime, datetime]:
    """
    If the stop time is earlier than the start time, it means the observation
    spans across midnight, so we add one day to the stop time.
    """
    if stop < start:
        stop += timedelta(days=1)
    return (start, stop)


def calculate_time_limit(start: Optional[datetime], stop: Optional[datetime], max_return: Optional[str]) -> Optional[datetime]:
    """
    Computes time limit for observation based on max_return condition or stop time.
    """
    if start is None:
        return None

    if max_return:
        parts = [int(v) for v in max_return.split(":")]
        h = parts[0]
        m = parts[1] if len(parts) > 1 else 0
        s = parts[2] if len(parts) > 2 else 0
        time_limit = start.replace(
            hour=h, minute=m, second=s, microsecond=0
        )
        # Adjust for overnight observations if necessary.
        if time_limit < start:
            time_limit += timedelta(days=1)
        return time_limit

    # If max_return is None, default time_limit to dawn (stop)
    return stop
