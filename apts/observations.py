import logging
from datetime import datetime, timedelta
from importlib import resources
from string import Template
from typing import List, Optional

import numpy
import pandas as pd
from skyfield.api import utc

from apts.constants.plot import CoordinateSystem

from . import plot as apts_plot
from .conditions import Conditions
from .constants.event_types import EventType
from .events import AstronomicalEvents
from .i18n import language_context
from .objects.messier import Messier
from .objects.ngc import NGC
from .objects.solar_objects import SolarObjects
from .objects.stars import Stars
from .utils import Utils

logger = logging.getLogger(__name__)


class Observation:
    NOTIFICATION_TEMPLATE = str(
        resources.files("apts").joinpath("templates/notification.html.template")
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
                    start_time_values = [
                        int(v) for v in self.conditions.start_time.split(":")
                    ]
                    override_start_dt = self.start.replace(
                        hour=start_time_values[0],
                        minute=start_time_values[1],
                        second=start_time_values[2],
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
                h, m, s = (
                    int(value) for value in self.conditions.max_return.split(":")
                )
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

    @property
    def local_messier(self):
        if self._local_messier is None:
            from apts import catalogs

            self._local_messier = Messier(
                self.place, catalogs, calculation_date=self.effective_date
            )
        return self._local_messier

    @property
    def local_planets(self):
        if self._local_planets is None:
            self._local_planets = SolarObjects(
                self.place, calculation_date=self.effective_date
            )
        return self._local_planets

    @property
    def local_ngc(self):
        if self._local_ngc is None:
            from apts import catalogs

            self._local_ngc = NGC(
                self.place, catalogs, calculation_date=self.effective_date
            )
        return self._local_ngc

    @property
    def local_stars(self):
        if self._local_stars is None:
            from apts import catalogs

            self._local_stars = Stars(
                self.place, catalogs, calculation_date=self.effective_date
            )
        return self._local_stars

    def get_visible_messier(self, language: Optional[str] = None, **args):
        with language_context(language):
            from apts.i18n import gettext_

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

    def get_visible_ngc(self, **args):
        return self.local_ngc.get_visible(
            self.conditions,
            self.start,
            self.time_limit,
            limiting_magnitude=self.limiting_magnitude,
            **args,
        )

    def get_visible_planets(self, language: Optional[str] = None, **args):
        with language_context(language):
            return self.local_planets.get_visible(
                self.conditions,
                self.start,
                self.time_limit,
                limiting_magnitude=self.limiting_magnitude,
                **args,
            )

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

    def plot_visible_planets_svg(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return apts_plot.plot_visible_planets_svg(self, dark_mode_override, **args)

    def plot_visible_planets(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return apts_plot.plot_visible_planets(self, dark_mode_override, **args)

    def _normalize_dates(self, start, stop):
        # If the stop time is earlier than the start time, it means the observation
        # spans across midnight, so we add one day to the stop time.
        if stop < start:
            stop += timedelta(days=1)
        return (start, stop)

    def plot_messier(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return apts_plot.plot_messier(self, dark_mode_override, **args)

    def plot_planets(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return apts_plot.plot_planets(self, dark_mode_override, **args)

    def _compute_weather_goodness(self):
        analysis = self.get_weather_analysis()
        if not analysis:
            return 0

        good_hours = sum(1 for hour in analysis if hour["is_good_hour"])
        all_hours = len(analysis)

        logger.debug("Good hours: {} and all hours: {}".format(good_hours, all_hours))
        if all_hours == 0:
            return 0
        return good_hours / all_hours * 100

    def is_weather_good(self):
        if self.place.weather is None:
            logger.info(
                "is_weather_good: self.place.weather is None, calling get_weather."
            )
            self.place.get_weather()
        else:
            logger.info("is_weather_good: self.place.weather already exists.")
        return self._compute_weather_goodness() > self.conditions.min_weather_goodness

    def plot_weather(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return apts_plot.plot_weather(self, dark_mode_override, **args)

    def to_html(
        self,
        custom_template=None,
        css=None,
        language: Optional[str] = None,
    ):
        with language_context(language):
            if custom_template:
                with open(custom_template, "r", encoding="utf-8") as f:
                    template_content = f.read()
            else:
                template_content = self.NOTIFICATION_TEMPLATE.read_text(
                    encoding="utf-8"
                )

            if css:
                style_end_pos = template_content.find("</style>")
                if style_end_pos != -1:
                    template_content = (
                        template_content[:style_end_pos]
                        + css
                        + template_content[style_end_pos:]
                    )
            template = Template(template_content)
            hourly_weather = self.get_hourly_weather_analysis(language=language)
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
                "equipment_table": self.equipment.data().to_html(),
                "place_name": self.place.name,
                "lat": numpy.rad2deg(self.place.lat),
                "lon": numpy.rad2deg(self.place.lon),
                "hourly_weather": hourly_weather,
                "timezone": self.place.local_timezone,
            }
            return str(template.substitute(data))

    def plot_sun_and_moon_path(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return apts_plot.plot_sun_and_moon_path(self, dark_mode_override, **args)

    def plot_skymap(
        self,
        target_name: str,
        dark_mode_override: Optional[bool] = None,
        zoom_deg: Optional[float] = None,
        star_magnitude_limit: Optional[float] = None,
        plot_stars: bool = True,
        plot_messier: bool = False,
        plot_ngc: bool = False,
        plot_planets: bool = False,
        plot_date: Optional[datetime] = None,
        flip_horizontally: Optional[bool] = None,
        flip_vertically: Optional[bool] = None,
        coordinate_system: Optional[CoordinateSystem] = None,
        language: Optional[str] = None,
        **kwargs,
    ):
        """
        Generates and displays a skymap for a specified celestial object.

        This method provides a high-level interface to the plotting capabilities in `apts.plot`.
        It can generate either a full-sky polar plot or a zoomed-in Cartesian plot for a
        given target. The orientation of the view can be flipped to match the output of
        certain telescopes.

        Args:
            target_name (str): The name of the target object to center the skymap on.
            dark_mode_override (Optional[bool]): If set, overrides the system's dark mode setting.
            zoom_deg (Optional[float]): The diameter of the zoomed-in view in degrees. If None, a full skymap is generated.
            star_magnitude_limit (Optional[float]): The faintest magnitude of stars to plot.
            plot_stars (bool): Whether to plot stars on the skymap. Defaults to True.
            plot_messier (bool): Whether to plot Messier objects. Defaults to False.
            plot_ngc (bool): Whether to plot NGC objects. Defaults to False.
            plot_planets (bool): Whether to plot planets. Defaults to False.
            plot_date (Optional[datetime]): The specific date and time for which to generate the skymap.
                                            If None, the middle of the observation window is used.
            flip_horizontally (Optional[bool]): If True, the skymap's horizontal axis is inverted.
            flip_vertically (Optional[bool]): If True, the skymap's vertical axis is inverted.
            coordinate_system (Optional[CoordinateSystem]): The coordinate system to use for the skymap (e.g., 'altaz', 'radec').
            **kwargs: Additional keyword arguments to pass to the plotting function, including `equipment_id`.

        Returns:
            A matplotlib Figure object representing the skymap.
        """
        with language_context(language):
            return apts_plot.plot_skymap(
                self,
                target_name=target_name,
                dark_mode_override=dark_mode_override,
                zoom_deg=zoom_deg,
                star_magnitude_limit=star_magnitude_limit,
                plot_stars=plot_stars,
                plot_messier=plot_messier,
                plot_ngc=plot_ngc,
                plot_planets=plot_planets,
                plot_date=plot_date,
                flip_horizontally=flip_horizontally,
                flip_vertically=flip_vertically,
                coordinate_system=coordinate_system,
                **kwargs,
            )

    def __str__(self) -> str:
        return (
            f"Observation at {self.place.name} from {self.start} to {self.time_limit}"
        )

    def get_weather_analysis(self, language: Optional[str] = None):
        if self._weather_analysis is not None:
            return self._weather_analysis

        if self.place.weather is None:
            self.place.get_weather()
            if self.place.weather is None:
                logger.warning("Weather data unavailable after fetch attempt.")
                return []

        if not all([self.start, self.stop, self.time_limit]):
            logger.warning(
                "Observation window (start, stop, time_limit) is not fully defined."
            )
            return []

        hourly_data = self.place.weather.get_critical_data(self.start, self.stop)
        if "fog" not in hourly_data.columns:
            hourly_data["fog"] = 100
        hourly_data = hourly_data[hourly_data.time <= self.time_limit]

        moon_altitudes = self.place.get_altaz_curve(
            self.place.moon, self.start, self.stop, num_points=len(hourly_data)
        )

        if not moon_altitudes.empty:
            # First, convert Skyfield Time objects to timezone-aware datetimes
            moon_altitudes["Time"] = moon_altitudes["Time"].apply(
                lambda t: t.utc_datetime() if hasattr(t, "utc_datetime") else pd.NaT
            )
            moon_altitudes = moon_altitudes.dropna(subset=["Time"])
            # Then, ensure the dtype (especially precision) matches the other dataframe's key
            moon_altitudes["Time"] = moon_altitudes["Time"].astype(
                hourly_data["time"].dtype
            )
            hourly_data = pd.merge_asof(
                hourly_data.sort_values("time"),
                moon_altitudes.sort_values("Time"),
                left_on="time",
                right_on="Time",
                direction="nearest",
            )
        else:
            hourly_data["Altitude"] = -1

        for col in [
            "cloudCover",
            "precipProbability",
            "windSpeed",
            "temperature",
            "visibility",
            "moonIllumination",
            "fog",
        ]:
            if col in hourly_data.columns:
                hourly_data[col] = pd.to_numeric(hourly_data[col], errors="coerce")

        analysis_results = []
        with language_context(language):
            from apts.i18n import gettext_

            for _, row in hourly_data.iterrows():
                is_good_hour = True
                reasons = []

                if pd.isna(row.cloudCover) or not (
                    row.cloudCover < self.conditions.max_clouds
                ):
                    is_good_hour = False
                    reasons.append(
                        gettext_("Cloud cover %(cloud_cover)s%% exceeds limit")
                        % {"cloud_cover": f"{row.cloudCover:.1f}"}
                    )
                if pd.isna(row.precipProbability) or not (
                    row.precipProbability
                    < self.conditions.max_precipitation_probability
                ):
                    is_good_hour = False
                    reasons.append(
                        gettext_(
                            "Precipitation probability %(precip_prob)s%% exceeds limit"
                        )
                        % {"precip_prob": f"{row.precipProbability:.1f}"}
                    )
                if pd.isna(row.windSpeed) or not (
                    row.windSpeed < self.conditions.max_wind
                ):
                    is_good_hour = False
                    reasons.append(
                        gettext_("Wind speed %(wind_speed)s km/h exceeds limit")
                        % {"wind_speed": f"{row.windSpeed:.1f}"}
                    )
                if pd.isna(row.temperature) or not (
                    self.conditions.min_temperature
                    < row.temperature
                    < self.conditions.max_temperature
                ):
                    is_good_hour = False
                    reasons.append(
                        gettext_("Temperature %(temp)s°C out of range")
                        % {"temp": f"{row.temperature:.1f}"}
                    )
                if pd.isna(row.visibility) or not (
                    row.visibility > self.conditions.min_visibility
                ):
                    is_good_hour = False
                    reasons.append(
                        gettext_("Visibility %(vis)s km below limit")
                        % {"vis": f"{row.visibility:.1f}"}
                    )
                if pd.isna(row.fog) or not (row.fog <= self.conditions.max_fog):
                    is_good_hour = False
                    reasons.append(
                        gettext_("Fog %(fog)s%% exceeds limit of %(max_fog)s%%")
                        % {"fog": f"{row.fog:.1f}", "max_fog": self.conditions.max_fog}
                    )
                if (
                    row["Altitude"] > 0
                    and not row.moonIllumination < self.conditions.max_moon_illumination
                ):
                    is_good_hour = False
                    reasons.append(
                        gettext_(
                            "Moon illumination %(illum)s%% exceeds limit while moon is up"
                        )
                        % {"illum": f"{row.moonIllumination:.1f}"}
                    )

                analysis_results.append(
                    {
                        "time": row.time,
                        "is_good_hour": is_good_hour,
                        "reasons": reasons,
                        "temperature": row.temperature,
                        "clouds": row.cloudCover,
                        "precipitation": row.precipProbability,
                        "wind_speed": row.windSpeed,
                        "visibility": row.visibility,
                        "moon_illumination": row.moonIllumination,
                        "fog": row.fog,
                    }
                )
        self._weather_analysis = analysis_results
        return self._weather_analysis

    def get_hourly_weather_analysis(self, language: Optional[str] = None):
        return self.get_weather_analysis(language=language)
