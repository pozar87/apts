import logging
from typing import Any, Optional, cast

import pandas as pd

from apts.cache import get_timescale
from apts.config import get_dark_mode, get_weather_settings
from apts.constants.graphconstants import get_plot_style
from apts.i18n import gettext_
from apts.utils.planetary import get_moon_illumination_details
from apts.utils.plot import Utils as PlotUtils
from apts.weather_providers import (
    Meteoblue,
    OpenWeatherMap,
    PirateWeather,
    StormGlass,
    VisualCrossing,
)

logger = logging.getLogger(__name__)


class Weather:
    def __init__(
        self,
        lat,
        lon,
        local_timezone,
        provider_name: Optional[str] = None,
        api_key: Optional[str] = None,
        hours: int = 48,
    ):
        self.lat = lat
        self.lon = lon
        self.local_timezone = local_timezone
        self.hours = hours

        # If provider_name is not explicitly given, get it from settings
        if provider_name is None:
            provider_name, config_api_key = get_weather_settings()
            # Use config_api_key if it's not None, otherwise use the passed api_key (which might be None)
            api_key = config_api_key if config_api_key is not None else api_key
        # If provider_name is given but api_key is not, try to get api_key from settings for that provider
        elif api_key is None:
            _, config_api_key = get_weather_settings(provider_name)
            api_key = config_api_key if config_api_key is not None else api_key

        # Fallback to default dummy key if API key is still None
        if api_key is None:
            api_key = "12345"
            logger.warning(
                f"API key for {provider_name or 'default provider'} not found in config. Using dummy key '12345'."
            )

        logger.info(
            f"Initializing weather provider: {provider_name} for lat={self.lat}, lon={self.lon}"
        )

        if provider_name == "pirateweather":
            provider = PirateWeather(api_key, lat, lon, local_timezone)
        elif provider_name == "visualcrossing":
            provider = VisualCrossing(api_key, lat, lon, local_timezone)
        elif provider_name == "openweathermap":
            provider = OpenWeatherMap(api_key, lat, lon, local_timezone)
        elif provider_name == "meteoblue":
            provider = Meteoblue(api_key, lat, lon, local_timezone)
        elif provider_name == "stormglass":
            provider = StormGlass(api_key, lat, lon, local_timezone)
        else:
            logger.error(f"Unknown weather provider specified: {provider_name}")
            raise ValueError(f"Unknown weather provider: {provider_name}")

        logger.info(f"Attempting to download data from {provider_name}.")
        self.data = provider.download_data(hours=self.hours)
        if self.data is not None and not cast(pd.DataFrame, self.data).empty:
            logger.info(f"Successfully downloaded weather data from {provider_name}.")
            ts = get_timescale()
            times = ts.from_datetimes(self.data["time"].tolist())
            illumination, is_waxing = get_moon_illumination_details(times)
            self.data["moonIllumination"] = illumination
            self.data["moonWaxing"] = is_waxing
        else:
            logger.warning(
                f"Failed to download or received empty data from {provider_name}."
            )
            if self.data is None or cast(pd.DataFrame, self.data).empty:
                self.data = provider._empty_df()

    def _filter_data(self, rows) -> pd.DataFrame:
        # Always add time column, ensuring it's first and all columns are unique.
        columns = ["time"]
        for col in rows:
            if col not in columns:
                columns.append(col)

        # Ensure all requested columns exist in self.data
        for col in columns:
            if col not in self.data.columns:
                self.data[col] = "none"

        # Ensure numeric columns are numeric
        result = self.data[columns].copy()  # type: ignore
        for col in columns:
            if col != "time" and col not in ["summary", "precipType", "moonWaxing"]:
                result[col] = pd.to_numeric(result[col], errors="coerce")

        return cast(pd.DataFrame, result)

    def plot_clouds(self, hours=24, dark_mode_override: Optional[bool] = None, **args):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        data = self._filter_data(["cloudCover"])
        ax = args.pop("ax", None)
        if data.empty:
            return PlotUtils.plot_no_data(ax, gettext_("Clouds"), effective_dark_mode)

        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        # Preserve original args for pandas plot
        plot_kwargs = args.copy()
        plot_ax = data.plot(
            x="time",
            xlim=(data.time.min(), data.time.max()),
            ylim=(0, 105),
            title=gettext_("Clouds"),
            ax=ax,
            x_compat=True,
            **plot_kwargs,
        )  # pyright: ignore

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        PlotUtils.style_legend(ax, style)

        PlotUtils.annotate_plot(
            ax, gettext_("Cloud cover [%]"), effective_dark_mode, self.local_timezone
        )
        return ax

    def plot_precipitation(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        data = self._filter_data(["precipIntensity", "precipProbability"])
        ax = args.pop("ax", None)
        if data.empty:
            return PlotUtils.plot_no_data(
                ax,
                gettext_("Precipitation intensity and probability"),
                effective_dark_mode,
            )

        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_kwargs = args.copy()
        plot_ax = data.plot(
            x="time",
            xlim=(data.time.min(), data.time.max()),
            title=gettext_("Precipitation intensity and probability"),
            ax=ax,
            x_compat=True,
            **plot_kwargs,
        )  # pyright: ignore

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        PlotUtils.style_legend(ax, style)

        PlotUtils.annotate_plot(
            ax, gettext_("Probability"), effective_dark_mode, self.local_timezone
        )
        return ax

    def plot_precipitation_type_summary(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)  # Use effective_dark_mode
        data = self._filter_data(["precipType"])
        ax = args.pop("ax", None)
        if data.empty:
            return PlotUtils.plot_no_data(
                ax, gettext_("Precipitation type summary"), effective_dark_mode
            )

        fig = None
        plot_kwargs = args.copy()  # Preserve original args

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        # Pandas pie plot returns an Axes object.
        plot_ax = (
            data.groupby("precipType")  # pyright: ignore
            .size()
            .plot(
                kind="pie",
                label=gettext_("Precipitation type summary"),
                ax=ax,
                **plot_kwargs,
            )
        )
        # If ax was not passed, it's created by plot command.
        if not ax:
            ax = plot_ax
            fig = ax.figure
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            # For pie charts, explicitly set AXES_FACE_COLOR, as it might not have other elements like grids
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        # Style title and ylabel (pie charts often use ylabel for the 'label' arg)
        title_text = ax.get_title()
        if (
            not title_text and "label" in plot_kwargs
        ):  # Pandas might use 'label' for title in pie
            title_text = plot_kwargs["label"]
        if not title_text and hasattr(ax, "get_label"):  # Fallback if available
            title_text = ax.get_label()

        ax.set_title(title_text, color=style["TEXT_COLOR"])
        ax.set_ylabel(
            ax.get_ylabel(), color=style["TEXT_COLOR"]
        )  # Y-label (usually the category name)

        # Style texts within the pie chart (percentages, labels)
        for text_obj in ax.texts:
            text_obj.set_color(style["TEXT_COLOR"])

        # Pie charts don't typically have legends in the same way line plots do.
        # Wedge colors can be passed via `colors` kwarg in plot_kwargs if needed.
        return ax

    def plot_clouds_summary(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)  # Use effective_dark_mode
        data = self._filter_data(["summary"])
        ax = args.pop("ax", None)
        if data.empty:
            return PlotUtils.plot_no_data(
                ax, gettext_("Cloud summary"), effective_dark_mode
            )

        fig = None
        plot_kwargs = args.copy()

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_ax = (
            data.groupby("summary")  # pyright: ignore
            .size()
            .plot(kind="pie", label=gettext_("Cloud summary"), ax=ax, **plot_kwargs)
        )
        if not ax:
            ax = plot_ax
            fig = ax.figure
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        title_text = ax.get_title()
        if not title_text and "label" in plot_kwargs:
            title_text = plot_kwargs["label"]
        if not title_text and hasattr(ax, "get_label"):
            title_text = ax.get_label()

        ax.set_title(title_text, color=style["TEXT_COLOR"])
        ax.set_ylabel(ax.get_ylabel(), color=style["TEXT_COLOR"])

        for text_obj in ax.texts:
            text_obj.set_color(style["TEXT_COLOR"])

        return ax

    def plot_temperature(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        data = self._filter_data(["temperature", "apparentTemperature", "dewPoint"])
        ax = args.pop("ax", None)
        if data.empty:
            return PlotUtils.plot_no_data(
                ax, gettext_("Temperatures"), effective_dark_mode
            )

        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_kwargs = args.copy()
        plot_ax = data.plot(
            x="time",
            xlim=(data.time.min(), data.time.max()),
            title=gettext_("Temperatures"),
            ax=ax,
            x_compat=True,
            **plot_kwargs,
        )  # pyright: ignore

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        PlotUtils.style_legend(ax, style)

        PlotUtils.annotate_plot(
            ax, gettext_("Temperature [°C]"), effective_dark_mode, self.local_timezone
        )
        return ax

    def plot_wind(self, hours=24, dark_mode_override: Optional[bool] = None, **args):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        data = self._filter_data(["windSpeed"])
        ax = args.pop("ax", None)
        if data.empty:
            return PlotUtils.plot_no_data(
                ax, gettext_("Wind speed"), effective_dark_mode
            )

        # Ensure windSpeed is numeric for max calculation
        data["windSpeed"] = pd.to_numeric(data["windSpeed"], errors="coerce")
        max_wind_speed = data[["windSpeed"]].max().max()

        if pd.isna(max_wind_speed):
            return PlotUtils.plot_no_data(
                ax, gettext_("Wind speed"), effective_dark_mode
            )

        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_kwargs = args.copy()
        plot_ax = data.plot(  # pyright: ignore
            x="time",
            y="windSpeed",
            xlim=(data.time.min(), data.time.max()),
            ylim=(0, max_wind_speed + 1),
            title=gettext_("Wind speed"),
            ax=ax,
            x_compat=True,
            **plot_kwargs,
        )

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        PlotUtils.style_legend(ax, style)

        PlotUtils.annotate_plot(
            ax, gettext_("Wind speed [km/h]"), effective_dark_mode, self.local_timezone
        )
        return ax

    def plot_pressure_and_ozone(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)

        # Check for available columns
        available_columns = [
            col
            for col in ["pressure", "ozone"]
            if col in cast(pd.DataFrame, self.data).columns
            and bool(
                cast(pd.DataFrame, self.data)[col].astype(str).str.lower().nunique() > 1
            )
            and bool(cast(pd.DataFrame, self.data)[col].notna().any())
        ]
        ax = args.pop("ax", None)
        if not available_columns:
            return PlotUtils.plot_no_data(
                ax, gettext_("Pressure and Ozone"), effective_dark_mode
            )

        data = self._filter_data(available_columns)
        if data.empty:
            return PlotUtils.plot_no_data(
                ax, gettext_("Pressure and Ozone"), effective_dark_mode
            )

        fig = None
        plot_kwargs = args.copy()

        if ax:
            fig = ax.figure

        # Determine plot parameters based on available data
        plot_title = gettext_("Pressure")
        secondary_y_plot = []
        if "ozone" in available_columns and "pressure" in available_columns:
            plot_title = gettext_("Pressure and Ozone")
            secondary_y_plot = ["ozone"]
        elif "ozone" in available_columns:
            plot_title = gettext_("Ozone")

        plot_ax = data.plot(  # pyright: ignore
            x="time",
            xlim=(data.time.min(), data.time.max()),
            title=plot_title,
            secondary_y=secondary_y_plot,
            ax=ax,
            x_compat=True,
            **plot_kwargs,
        )

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        # Style primary legend
        PlotUtils.style_legend(ax, style)

        # Annotate primary Y axis
        primary_y_label = ""
        if "pressure" in available_columns:
            primary_y_label = gettext_("Pressure [hPa]")
        elif "ozone" in available_columns:
            primary_y_label = gettext_("Ozone [DU]")  # Assuming Dobson Units for Ozone
        PlotUtils.annotate_plot(
            ax, primary_y_label, effective_dark_mode, self.local_timezone
        )

        # Style secondary Y axis if it exists
        if secondary_y_plot and hasattr(ax, "right_ax"):
            ax_secondary = ax.right_ax
            ax_secondary.set_ylabel(
                gettext_("Ozone [DU]"),
                color=style["TEXT_COLOR"],  # Assuming Dobson Units
            )
            ax_secondary.tick_params(axis="y", colors=style["TICK_COLOR"])
            ax_secondary.spines["right"].set_color(style["AXIS_COLOR"])

        return ax

    def get_critical_data(self, start, stop):
        if cast(pd.DataFrame, self.data).empty:
            return pd.DataFrame(
                columns=pd.Index(
                    [
                        "time",
                        "cloudCover",
                        "precipProbability",
                        "windSpeed",
                        "temperature",
                        "visibility",
                        "moonIllumination",
                        "fog",
                        "aurora",
                    ]
                )
            )

        critical_data_columns = [
            "cloudCover",
            "precipProbability",
            "precipIntensity",
            "windSpeed",
            "temperature",
            "visibility",
            "moonIllumination",
            "fog",
            "aurora",
        ]
        data = self._filter_data(critical_data_columns)
        return data[(data.time >= start) & (data.time <= stop)]  # pyright: ignore

    def plot_visibility(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        data = self._filter_data(["visibility"])
        data = data[data["visibility"].notna()]
        ax = args.pop("ax", None)
        if data.empty:
            return PlotUtils.plot_no_data(
                ax, gettext_("Visibility"), effective_dark_mode
            )

        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_kwargs = args.copy()
        plot_ax = data.plot(
            x="time",
            xlim=(data.time.min(), data.time.max()),
            title=gettext_("Visibility"),
            ax=ax,
            x_compat=True,
            **plot_kwargs,
        )  # pyright: ignore

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        PlotUtils.style_legend(ax, style)

        PlotUtils.annotate_plot(
            ax, gettext_("Visibility [km]"), effective_dark_mode, self.local_timezone
        )
        return ax

    def plot_fog(self, hours=24, dark_mode_override: Optional[bool] = None, **args):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        data = self._filter_data(["fog"])
        ax = args.pop("ax", None)
        if data.empty:
            return PlotUtils.plot_no_data(ax, gettext_("Fog"), effective_dark_mode)

        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_kwargs = args.copy()
        plot_ax = data.plot(
            x="time",
            xlim=(data.time.min(), data.time.max()),
            ylim=(0, 105),
            title=gettext_("Fog"),
            ax=ax,
            x_compat=True,
            **plot_kwargs,
        )  # pyright: ignore

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        PlotUtils.style_legend(ax, style)

        PlotUtils.annotate_plot(
            ax, gettext_("Fog [%]"), effective_dark_mode, self.local_timezone
        )
        return ax

    def plot_moon_illumination(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        data = self._filter_data(["moonIllumination", "moonWaxing"])
        ax = args.pop("ax", None)
        if data.empty:
            return PlotUtils.plot_no_data(
                ax, gettext_("Moon Illumination"), effective_dark_mode
            )

        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        # Determine the title based on waxing/waning
        # Taking the status from the first data point for simplicity
        is_waxing = data["moonWaxing"].iloc[0]
        title = (
            f"{gettext_('Moon Illumination')} "
            f"({gettext_('Waxing') if is_waxing else gettext_('Waning')})"
        )

        plot_kwargs = args.copy()
        plot_ax = data.plot(
            x="time",
            y="moonIllumination",
            xlim=(data.time.min(), data.time.max()),
            ylim=(0, 105),
            title=title,
            ax=ax,
            x_compat=True,
            **plot_kwargs,
        )  # pyright: ignore

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        PlotUtils.style_legend(ax, style)

        PlotUtils.annotate_plot(
            ax, gettext_("Illumination [%]"), effective_dark_mode, self.local_timezone
        )
        return ax

    def plot_aurora(self, hours=24, dark_mode_override: Optional[bool] = None, **args):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        ax = args.pop("ax", None)
        if "aurora" not in self.data.columns:
            return PlotUtils.plot_no_data(ax, gettext_("Aurora"), effective_dark_mode)

        style = get_plot_style(effective_dark_mode)
        data = self._filter_data(["aurora"])
        if data.empty:
            return PlotUtils.plot_no_data(ax, gettext_("Aurora"), effective_dark_mode)

        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_kwargs = args.copy()
        plot_ax = data.plot(
            x="time",
            y="aurora",
            xlim=(data.time.min(), data.time.max()),
            ylim=(0, 105),
            title=gettext_("Aurora"),
            ax=ax,
            x_compat=True,
            **plot_kwargs,
        )  # pyright: ignore

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            cast(Any, fig).patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        PlotUtils.style_legend(ax, style)

        PlotUtils.annotate_plot(
            ax, gettext_("Aurora"), effective_dark_mode, self.local_timezone
        )
        return ax
