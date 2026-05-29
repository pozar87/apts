import logging
from datetime import datetime, timedelta
from typing import Optional, Union

from skyfield.api import Time

from ..conditions import Conditions
from .catalogs import CatalogMixIn
from .events import EventsMixIn
from .html import HtmlExportMixIn
from .plotting import PlottingMixIn
from .weather import WeatherAnalysisMixIn

logger = logging.getLogger(__name__)


class Observation(
    WeatherAnalysisMixIn,
    PlottingMixIn,
    CatalogMixIn,
    HtmlExportMixIn,
    EventsMixIn,
):
    effective_date: Optional[Union[datetime, Time]]

    def __init__(
        self,
        place,
        equipment,
        conditions=Conditions(),
        target_date=None,
        sun_observation=False,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        limiting_magnitude: Optional[float] = None,
    ):
        self.place = place
        self.equipment = equipment
        self.conditions = conditions
        self.sun_observation = sun_observation
        self.limiting_magnitude = limiting_magnitude

        # Initialize core attributes that depend on date calculations
        self.effective_date = None
        self.observation_local_time = None
        self.start = None
        self.stop = None
        self.time_limit = None

        if sun_observation and start_time and end_time:
            self._init_window_from_times(start_time, end_time)
        elif target_date:
            self._init_window_from_target_date(target_date)
        else:
            self._init_window_legacy()

        # Normalize start and stop dates for the observation window
        if self.start is not None and self.stop is not None:
            self.start, self.stop = self._normalize_window(
                self.start,
                self.stop,
            )

        # Catalog objects are lazy-loaded to improve performance
        self._local_messier = None
        self._local_planets = None
        self._local_ngc = None
        self._local_stars = None
        self._weather_analysis = None
        self._plot = None

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

    def _init_window_from_target_date(self, target_date):
        if self.sun_observation:
            self.start = self.place.sunrise_time(target_date=target_date)
            self.stop = self.place.sunset_time(target_date=target_date)
        else:
            self.start = self.place.sunset_time(
                target_date=target_date, twilight=self.conditions.twilight
            )
            if self.start:
                self.stop = self.place.sunrise_time(
                    start_search_from=self.start, twilight=self.conditions.twilight
                )
            else:
                self.stop = None

        if self.start is None or self.stop is None:
            logger.warning(
                f"Could not determine observation window for {self.place.name} "
                f"on {target_date} with twilight '{self.conditions.twilight.value}'. "
                "Sun may be always up or down."
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
        self.effective_date = self.place.date
        if self.sun_observation:
            self.start = self.place.sunrise_time()
            self.stop = self.place.sunset_time()
        else:
            self.start = self.place.sunset_time(twilight=self.conditions.twilight)
            if self.start:
                self.stop = self.place.sunrise_time(
                    start_search_from=self.start, twilight=self.conditions.twilight
                )
            else:
                self.stop = None
        self.observation_local_time = self.start

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

    def __str__(self) -> str:
        return (
            f"Observation at {self.place.name} from {self.start} to {self.time_limit}"
        )
