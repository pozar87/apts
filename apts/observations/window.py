import logging
from datetime import datetime, timedelta
from typing import Optional, Union

from skyfield.api import Time

from ..conditions import Conditions
from ..constants.twilight import Twilight

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
                    self.effective_date = self.place.ts.utc(
                        datetime.combine(target_date, datetime.min.time()).replace(
                            tzinfo=self.place.local_timezone
                        )
                    )
            else:
                self.effective_date = self.place.date

        if self.observation_local_time is None:
            self.observation_local_time = self.effective_date.astimezone(
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
        """
        Attempts to find sunset and sunrise times using the requested twilight.
        If the requested twilight is not reached (common at high latitudes),
        it falls back to less strict twilights.
        """
        requested_twilight = self.conditions.twilight

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
            start = self.place.sunset_time(target_date=target_date, twilight=twilight)
            if start:
                stop = self.place.sunrise_time(
                    start_search_from=start, twilight=twilight
                )
                if stop:
                    if twilight != requested_twilight:
                        logger.warning(
                            f"Could not determine observation window for {self.place.name} "
                            f"with requested twilight '{requested_twilight.value}'. "
                            f"Falling back to '{twilight.value if twilight else 'sunset/sunrise'}'. "
                        )
                    return start, stop
        return None, None

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
        if isinstance(self.conditions.start_time, str):
            parts = [int(v) for v in self.conditions.start_time.split(":")]
            h = parts[0]
            m = parts[1] if len(parts) > 1 else 0
            s = parts[2] if len(parts) > 2 else 0
            override_start_dt = self.start.replace(
                hour=h,
                minute=m,
                second=s,
            )
        else:
            # Assume it's a datetime/time object and take its time components
            override_start_dt = self.start.replace(
                hour=self.conditions.start_time.hour,
                minute=self.conditions.start_time.minute,
                second=self.conditions.start_time.second,
            )
        self.start = override_start_dt

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
            self.observation_local_time = self.effective_date.astimezone(
                self.place.local_timezone
            )

    def _normalize_window(self, start, stop):
        # If the stop time is earlier than the start time, it means the observation
        # spans across midnight, so we add one day to the stop time.
        if stop < start:
            stop += timedelta(days=1)
        return (start, stop)

    def _init_time_limit(self):
        # Compute time limit for observation
        if self.start is not None:
            if self.conditions.max_return:
                parts = [int(v) for v in self.conditions.max_return.split(":")]
                h = parts[0]
                m = parts[1] if len(parts) > 1 else 0
                s = parts[2] if len(parts) > 2 else 0
                self.time_limit = self.start.replace(
                    hour=h, minute=m, second=s, microsecond=0
                )
                # Adjust for overnight observations if necessary.
                if self.time_limit < self.start:
                    self.time_limit += timedelta(days=1)
            else:
                # If max_return is None, default time_limit to dawn (self.stop)
                self.time_limit = self.stop
