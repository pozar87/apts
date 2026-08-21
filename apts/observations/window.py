import logging
from datetime import datetime, timedelta, timezone
from typing import Optional, Union

from skyfield.api import Time

from ..conditions import Conditions
from ..constants.twilight import Twilight
from .window_calculations import (
    apply_start_time_override,
    calculate_time_limit,
    find_best_observation_window,
    normalize_window,
)

logger = logging.getLogger(__name__)


class ObservationWindow:
    """
    Handles the calculation and normalization of an observation window.
    """

    def __init__(
        self,
        place,
        conditions: Conditions,
        target_date: Optional[Union[datetime, Time]] = None,
        sun_observation: bool = False,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
    ):
        self.place = place
        self.conditions = conditions
        self.sun_observation = sun_observation

        self.start: Optional[datetime] = None
        self.stop: Optional[datetime] = None
        self.effective_date: Optional[Time] = None
        self.observation_local_time: Optional[datetime] = None
        self.time_limit: Optional[datetime] = None

        if sun_observation and start_time and end_time:
            self._init_window_from_times(start_time, end_time)
        elif target_date:
            self._init_window_from_target_date(target_date)
        else:
            self._init_window_legacy()

        # Fallback for effective_date if it couldn't be determined (e.g. polar day/night)
        if self.effective_date is None:
            if target_date:
                if isinstance(target_date, datetime):
                    self.effective_date = self.place.ts.utc(target_date)
                else:
                    # target_date could be a Skyfield Time (has utc_datetime) or a date/other type
                    if hasattr(target_date, "utc_datetime"):
                        target_dt = target_date.utc_datetime().date()  # type: ignore[union-attr]
                    else:
                        target_dt = target_date
                    self.effective_date = self.place.ts.utc(
                        datetime.combine(target_dt, datetime.min.time()).replace(  # type: ignore[arg-type]
                            tzinfo=self.place.local_timezone
                        )
                    )
            else:
                self.effective_date = self.place.date

        if self.observation_local_time is None and self.effective_date is not None:
            # effective_date could be a Skyfield Time or other date-like object
            if hasattr(self.effective_date, "utc_datetime"):
                effective_dt = self.effective_date.utc_datetime().replace(  # type: ignore[union-attr]
                    tzinfo=timezone.utc
                )
            else:
                effective_dt = self.effective_date
            self.observation_local_time = effective_dt.astimezone(  # type: ignore[union-attr]
                self.place.local_timezone
            )

        # Normalize start and stop dates for the observation window
        if self.start is not None and self.stop is not None:
            self.start, self.stop = self._normalize_window(
                self.start,
                self.stop,
            )

        self._init_time_limit()

    def _init_window_from_times(self, start_time: datetime, end_time: datetime):
        self.start = start_time
        self.stop = end_time
        self.effective_date = self.place.ts.utc(
            start_time
        )  # Convert to Skyfield Time for moon/weather calculations
        self.observation_local_time = (
            start_time  # Use start_time as local observation time
        )

    def _find_best_observation_window(self, target_date=None):
        return find_best_observation_window(self.place, self.conditions, target_date=target_date)

    def _init_window_from_target_date(self, target_date):
        if self.sun_observation:
            self.start = self.place.sunrise_time(target_date=target_date)
            self.stop = self.place.sunset_time(target_date=target_date)
        else:
            self.start, self.stop = self._find_best_observation_window(
                target_date=target_date
            )

        if self.start is None or self.stop is None:
            logger.warning(
                f"Could not determine observation window for {self.place.name} "
                f"on {target_date} with twilight '{self.conditions.twilight.value}' "
                "or any less strict twilights. Sun may be always up or down."
            )
        else:
            if self.conditions.start_time:
                self._apply_start_time_override()
            self.effective_date = self.place.ts.utc(self.start)
            self.observation_local_time = self.start

    def _apply_start_time_override(self):
        assert self.start is not None
        assert self.conditions.start_time is not None
        self.start = apply_start_time_override(self.start, self.conditions.start_time)

    def _init_window_legacy(self):
        # Legacy behavior: use place.date
        if self.sun_observation:
            self.start = self.place.sunrise_time()
            self.stop = self.place.sunset_time()
        else:
            self.start, self.stop = self._find_best_observation_window()

        if self.start:
            self.effective_date = self.place.ts.utc(self.start)
            self.observation_local_time = self.start
        else:
            self.effective_date = self.place.date
            if hasattr(self.effective_date, "utc_datetime"):
                effective_dt = self.effective_date.utc_datetime().replace(  # type: ignore[union-attr, reportOptionalMemberAccess]
                    tzinfo=timezone.utc
                )
            else:
                effective_dt = self.effective_date
            self.observation_local_time = effective_dt.astimezone(  # type: ignore[union-attr]
                self.place.local_timezone
            )

    def _normalize_window(self, start, stop):
        return normalize_window(start, stop)

    def _init_time_limit(self):
        self.time_limit = calculate_time_limit(
            self.start, self.stop, self.conditions.max_return
        )
