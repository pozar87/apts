import logging
from datetime import datetime
from typing import TYPE_CHECKING, Callable, Optional, Union, cast

import pandas as pd

if TYPE_CHECKING:
    from skyfield.api import Time

    from ...conditions import Conditions
    from ...place import Place

from ...utils.planetary import get_moon_illumination
from .constants import DEFAULT_WEATHER_VALUES
from .engine import get_good_hour_mask

logger = logging.getLogger(__name__)


def calculate_moon_altitudes(place: "Place", times_list: list[datetime]) -> pd.Series:
    """Calculates moon altitudes for a list of datetimes using place observer."""
    ts = place.ts
    times = ts.from_datetimes(times_list)
    alt, _, _ = place.observer.at(times).observe(place.moon).apparent().altaz()
    return pd.Series(alt.degrees)


def check_moon_condition(
    start: Optional[datetime],
    stop: Optional[datetime],
    place: "Place",
    conditions: "Conditions",
    effective_date: Optional[Union[datetime, "Time"]] = None,
    get_moon_illumination_fn: Optional[Callable] = None,
) -> bool:
    """
    Evaluates whether the moon condition is met for the observation window.
    Returns True if conditions are met or if start/stop window is undefined.
    """
    if not start or not stop:
        return True

    if get_moon_illumination_fn is None:
        get_moon_illumination_fn = get_moon_illumination

    # Use effective_date for moon illumination if available, otherwise fallback to place.date.
    # We avoid using 'or' here because Skyfield Time objects can raise TypeError when evaluated in boolean context.
    date_for_illumination = (
        effective_date if effective_date is not None else place.date
    )
    moon_illumination = get_moon_illumination_fn(date_for_illumination)
    if moon_illumination <= conditions.max_moon_illumination:
        return True

    # Illumination is too high, check if moon is up during observation window
    ts = place.ts
    t0 = ts.from_datetime(start)
    t1 = ts.from_datetime(stop)
    # Check at 10 points during the observation
    times = ts.linspace(t0, t1, 10)
    alt, _, _ = place.observer.at(times).observe(place.moon).apparent().altaz()

    # Calculate how much of the time the moon is up
    moon_up_ratio = sum(1 for a in alt.degrees if a > 0) / 10.0
    # If moon is up for more than (100 - min_weather_goodness)% of the time, it's bad
    allowed_bad_ratio = (100 - conditions.min_weather_goodness) / 100.0

    if moon_up_ratio > allowed_bad_ratio:
        logger.info(
            f"Moon condition not met: illumination {moon_illumination:.1f}% "
            f"exceeds {conditions.max_moon_illumination}% and moon is up for "
            f"{moon_up_ratio * 100:.1f}% of the observation window."
        )
        return False

    return True


def prepare_weather_dataframe(
    place: "Place",
    start: Optional[datetime],
    stop: Optional[datetime],
    time_limit: Optional[datetime] = None,
) -> pd.DataFrame:
    """Retrieves and prepares the weather DataFrame for analysis."""
    if place.weather is None or start is None or stop is None:
        return pd.DataFrame()

    hourly_data = cast(
        pd.DataFrame, place.weather.get_critical_data(start, stop)
    )
    if hourly_data.empty:
        return hourly_data

    # Filter by time limit if defined
    if time_limit is not None:
        t_limit = pd.Timestamp(time_limit)
        if t_limit.tzinfo is None:
            t_limit = t_limit.tz_localize(place.local_timezone)
        hourly_data = cast(
            pd.DataFrame, hourly_data[hourly_data.time <= t_limit].copy()
        )
    else:
        hourly_data = cast(pd.DataFrame, hourly_data.copy())

    # Populate missing columns with default values
    for col, default_val in DEFAULT_WEATHER_VALUES.items():
        if col not in hourly_data.columns:
            hourly_data[col] = default_val

    # Calculate moon altitudes if not already present or if all NaN
    if (
        "moon_altitude" in hourly_data.columns
        and not cast(pd.Series, hourly_data["moon_altitude"]).isna().all()
    ):
        hourly_data["Altitude"] = cast(pd.Series, hourly_data["moon_altitude"])
    else:
        alts = calculate_moon_altitudes(place, hourly_data["time"].tolist())
        alts.index = hourly_data.index
        hourly_data["Altitude"] = alts

    # Coerce to numeric
    for col in DEFAULT_WEATHER_VALUES.keys():
        hourly_data[col] = pd.to_numeric(hourly_data[col], errors="coerce")

    return hourly_data


def compute_weather_goodness_ratio(
    hourly_data: pd.DataFrame,
    conditions: "Conditions",
    cached_analysis: Optional[list[dict]] = None,
) -> float:
    """
    Calculates the percentage of good observation hours within the window.
    Uses cached analysis if provided, otherwise calculates from hourly_data.
    """
    if cached_analysis is not None:
        if not cached_analysis:
            return 0.0
        good_hours = sum(1 for hour in cached_analysis if hour["is_good_hour"])
        all_hours = len(cached_analysis)
        return (good_hours / all_hours * 100) if all_hours > 0 else 0.0

    if hourly_data.empty:
        return 0.0

    is_good_mask = get_good_hour_mask(hourly_data, conditions)
    good_hours = is_good_mask.sum()
    all_hours = len(is_good_mask)

    logger.debug(f"Good hours: {good_hours} and all hours: {all_hours}")

    return (good_hours / all_hours * 100) if all_hours > 0 else 0.0
