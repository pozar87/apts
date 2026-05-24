import datetime
from functools import lru_cache
from typing import Any

import numpy as np

from ..skyfield_searches.visibility import (
    get_twilight_time_utc,
    next_rising_time_utc,
    next_setting_time_utc,
    previous_rising_time_utc,
    previous_setting_time_utc,
)

get_twilight_time_utc = lru_cache(maxsize=1024)(get_twilight_time_utc)
previous_setting_time_utc = lru_cache(maxsize=1024)(previous_setting_time_utc)
next_rising_time_utc = lru_cache(maxsize=1024)(next_rising_time_utc)
next_setting_time_utc = lru_cache(maxsize=1024)(next_setting_time_utc)
previous_rising_time_utc = lru_cache(maxsize=1024)(previous_rising_time_utc)


class TFProxy:
    def __init__(self):
        self._instance = None

    def __getattr__(self, name):
        if self._instance is None:
            from timezonefinder import TimezoneFinder
            self._instance = TimezoneFinder()
        return getattr(self._instance, name)


def get_scalar_datetime(target_time: Any) -> datetime.datetime:
    """
    Helper to convert a Skyfield Time object (scalar or vector) to a scalar
    timezone-aware UTC datetime.
    """
    dt_raw = target_time.utc_datetime()
    if isinstance(dt_raw, (list, np.ndarray)):
        dt = dt_raw[0]
    else:
        dt = dt_raw

    if dt.tzinfo is None:
        return dt.replace(tzinfo=datetime.timezone.utc)
    return dt
