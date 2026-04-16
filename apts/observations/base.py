import html
import logging
import re
from datetime import datetime, timedelta
from importlib import resources
from string import Template
from typing import List, Optional

import numpy as np
import pandas as pd
from skyfield.api import utc

from .. import plot as apts_plot
from ..conditions import Conditions
from ..constants.event_types import EventType
from ..events import AstronomicalEvents
from ..i18n import language_context
from ..objects.messier import Messier
from ..objects.ngc import NGC
from ..objects.solar_objects import SolarObjects
from ..objects.stars import Stars
from ..utils import Utils
from .plotting import PlottingMixIn
from .weather import WeatherAnalysisMixIn

logger = logging.getLogger(__name__)


class Observation(WeatherAnalysisMixIn, PlottingMixIn):
    NOTIFICATION_TEMPLATE = resources.files("apts").joinpath(
        "templates/notification.html.template"
    )

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
            self.start = start_time
            self.stop = end_time
            self.effective_date = (
                start_time  # Use start_time as effective date for calculations
            )
            self.observation_local_time = (
                start_time  # Use start_time as local observation time
            )
        elif target_date:
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

                self.effective_date = self.place.ts.utc(self.start)
                self.observation_local_time = self.start

        else:
            # Legacy behavior: use place.date
            self.effective_date = self.place.date
            if sun_observation:
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

        # Normalize start and stop dates for the observation window
        if self.start is not None and self.stop is not None:
            self.start, self.stop = self._normalize_dates(
                self.start,
                self.stop,
            )
        # If not, self.start and self.stop remain None

        # Catalog objects are lazy-loaded to improve performance
        self._local_messier = None
        self._local_planets = None
        self._local_ngc = None
        self._local_stars = None
        self._weather_analysis = None

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
        # If self.start is None, self.time_limit remains None.

        self._plot = None

    @property
    def plot(self):
        if self._plot is None:
            try:
                self._plot = apts_plot.Plotter(self)
            except ImportError:
                # Fallback if dependencies are missing or plotting is disabled
                self._plot = apts_plot.NullPlotter()
            except Exception as e:
                # Fallback for any other initialization error
                logger.warning(f"Failed to initialize plotter: {e}")
                self._plot = apts_plot.NullPlotter()
        return self._plot

    @plot.setter
    def plot(self, value):
        self._plot = value

    @property
    def local_messier(self) -> Messier:
        if self._local_messier is None:
            from apts import catalogs

            self._local_messier = Messier(
                self.place, catalogs, calculation_date=self.effective_date
            )
        return self._local_messier

    @property
    def local_planets(self) -> SolarObjects:
        if self._local_planets is None:
            self._local_planets = SolarObjects(
                self.place, calculation_date=self.effective_date, lazy=True
            )
        return self._local_planets

    @property
    def local_ngc(self) -> NGC:
        if self._local_ngc is None:
            from apts import catalogs

            self._local_ngc = NGC(
                self.place, catalogs, calculation_date=self.effective_date
            )
        return self._local_ngc

    @property
    def local_stars(self) -> Stars:
        if self._local_stars is None:
            from apts import catalogs

            self._local_stars = Stars(
                self.place, catalogs, calculation_date=self.effective_date
            )
        return self._local_stars

    def get_visible_messier(
        self, language: Optional[str] = None, **args
    ) -> pd.DataFrame:
        with language_context(language):
            from ..i18n import gettext_

            visible = self.local_messier.get_visible(
                self.conditions,
                self.start,
                self.time_limit,
                limiting_magnitude=self.limiting_magnitude,
                **args,
            )
            if "Type" in visible.columns:
                visible["Type"] = visible["Type"].apply(gettext_).astype("string")
            if "Constellation" in visible.columns:
                visible["Constellation"] = (
                    visible["Constellation"].apply(gettext_).astype("string")
                )
            return visible

    def get_visible_ngc(self, **args) -> pd.DataFrame:
        return self.local_ngc.get_visible(
            self.conditions,
            self.start,
            self.time_limit,
            limiting_magnitude=self.limiting_magnitude,
            **args,
        )

    def get_visible_planets(
        self, language: Optional[str] = None, **args
    ) -> pd.DataFrame:
        with language_context(language):
            from ..i18n import gettext_

            visible = self.local_planets.get_visible(
                self.conditions,
                self.start,
                self.time_limit,
                limiting_magnitude=self.limiting_magnitude,
                **args,
            )
            if "Name" in visible.columns:
                visible["Name"] = visible["Name"].apply(gettext_).astype("string")
            return visible

    def get_astronomical_events(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        events_to_calculate: Optional[List[EventType]] = None,
    ):
        if start_date is None:
            start_date = self.start
        if end_date is None:
            end_date = self.stop

        if start_date is None:
            start_date = datetime.now(utc)
        if end_date is None:
            end_date = start_date + timedelta(days=365)

        events = AstronomicalEvents(
            self.place, start_date, end_date, events_to_calculate=events_to_calculate
        )
        return events.get_events()

    def _normalize_dates(self, start, stop):
        # If the stop time is earlier than the start time, it means the observation
        # spans across midnight, so we add one day to the stop time.
        if stop < start:
            stop += timedelta(days=1)
        return (start, stop)

    def to_html(
        self,
        custom_template=None,
        css=None,
        language: Optional[str] = None,
    ):
        with language_context(language):
            if custom_template:
                # Security: restrict to allowed template extensions and prevent path traversal.
                # We allow absolute paths to support templates located outside the package (and for tests),
                # but we explicitly block directory traversal via '..'.
                str_template = str(custom_template)
                if ".." in str_template:
                    raise ValueError("Path traversal detected in custom template path.")

                if not str_template.lower().endswith((".template", ".html", ".htm")):
                    raise ValueError(
                        "Only .template, .html, or .htm files are allowed as custom templates."
                    )
                with open(custom_template, "r", encoding="utf-8") as f:
                    template_content = f.read()
            else:
                template_content = self.NOTIFICATION_TEMPLATE.read_text(
                    encoding="utf-8"
                )

            if css:
                # Sanitize CSS to prevent breaking out of <style> block.
                # Regex handles variations like </style >, </style/>, etc.
                sanitized_css = re.sub(
                    r"</style\s*/?>", "", str(css), flags=re.IGNORECASE
                )
                # Escape '$' to '$$' to prevent string.Template from interpreting it as a variable.
                sanitized_css = sanitized_css.replace("$", "$$")
                style_end_pos = template_content.find("</style>")
                if style_end_pos != -1:
                    template_content = (
                        template_content[:style_end_pos]
                        + sanitized_css
                        + template_content[style_end_pos:]
                    )
            template = Template(template_content)
            hourly_weather = self.get_hourly_weather_analysis(language=language)
            # Sanitize hourly_weather contents
            sanitized_hourly_weather = []
            for hour in hourly_weather:
                sanitized_hour = {}
                for k, v in hour.items():
                    if isinstance(v, str):
                        sanitized_hour[k] = html.escape(v)
                    elif isinstance(v, list):
                        sanitized_hour[k] = [
                            html.escape(item) if isinstance(item, str) else item
                            for item in v
                        ]
                    else:
                        sanitized_hour[k] = v
                sanitized_hourly_weather.append(sanitized_hour)

            visible_planets_df = self.get_visible_planets(language=language)
            messier_df = self.get_visible_messier(language=language)

            data = {
                "title": "APTS",
                "start": Utils.format_date(self.start),
                "stop": Utils.format_date(self.stop),
                "planets_count": len(visible_planets_df),
                "messier_count": len(messier_df),
                "planets_table": visible_planets_df.drop(
                    columns=["TechnicalName"]
                ).to_html()
                if "TechnicalName" in visible_planets_df.columns
                else visible_planets_df.to_html(),
                "messier_table": messier_df.to_html(),
                "equipment_table": (
                    self.equipment.data()
                    if hasattr(self.equipment, "data")
                    else self.equipment
                ).to_html(),
                "place_name": html.escape(self.place.name),
                "lat": np.rad2deg(self.place.lat),
                "lon": np.rad2deg(self.place.lon),
                "hourly_weather": sanitized_hourly_weather,
                "timezone": html.escape(str(self.place.local_timezone)),
            }
            return str(template.substitute(data))

    def __str__(self) -> str:
        return (
            f"Observation at {self.place.name} from {self.start} to {self.time_limit}"
        )
