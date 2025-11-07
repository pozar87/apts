import logging

import pandas as pd
import requests_cache

from typing import Optional

from .utils import Utils
from apts.utils.planetary import get_moon_illumination
from apts.cache import get_timescale
from apts.config import get_dark_mode, get_weather_settings
from apts.constants.graphconstants import get_plot_style
from apts.weather_providers import (
    PirateWeather,
    VisualCrossing,
    OpenWeatherMap,
    Meteoblue,
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
    ):
        self.lat = lat
        self.lon = lon
        self.local_timezone = local_timezone

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
        else:
            logger.error(f"Unknown weather provider specified: {provider_name}")
            raise ValueError(f"Unknown weather provider: {provider_name}")

        logger.info(f"Attempting to download data from {provider_name}.")
        self.data = provider.download_data()
        if self.data is not None and not self.data.empty:
            logger.info(f"Successfully downloaded weather data from {provider_name}.")
            ts = get_timescale()
            self.data["moonIllumination"] = self.data["time"].apply(
                lambda x: get_moon_illumination(ts.from_datetime(x))
            )
        else:
            logger.warning(
                f"Failed to download or received empty data from {provider_name}."
            )

    def _filter_data(self, rows):
        # Always add time column
        columns = list(set(["time"] + rows))
        return self.data[columns]  # pyright: ignore

    def plot_clouds(self, hours=24, dark_mode_override: Optional[bool] = None, **args):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        data = self._filter_data(["cloudCover"])
        if data.empty:
            return None

        ax = args.pop("ax", None)
        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        # Preserve original args for pandas plot
        plot_kwargs = args.copy()
        plot_ax = data.plot(
            x="time", ylim=(0, 105), title="Clouds", ax=ax, **plot_kwargs
        )  # pyright: ignore

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        legend = ax.get_legend()
        if legend:
            legend.get_frame().set_facecolor(style["AXES_FACE_COLOR"])
            legend.get_frame().set_edgecolor(style["AXIS_COLOR"])
            for text_obj in legend.get_texts():  # Changed variable name
                text_obj.set_color(style["TEXT_COLOR"])
            if legend.get_title():
                legend.get_title().set_color(style["TEXT_COLOR"])

        Utils.annotate_plot(ax, "Cloud cover [%]", effective_dark_mode)
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
        if data.empty:
            return None

        ax = args.pop("ax", None)
        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_kwargs = args.copy()
        plot_ax = data.plot(
            x="time",
            title="Precipitation intensity and probability",
            ax=ax,
            **plot_kwargs,
        )  # pyright: ignore

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        legend = ax.get_legend()
        if legend:
            legend.get_frame().set_facecolor(style["AXES_FACE_COLOR"])
            legend.get_frame().set_edgecolor(style["AXIS_COLOR"])
            for text_obj in legend.get_texts():  # Changed variable name
                text_obj.set_color(style["TEXT_COLOR"])
            if legend.get_title():
                legend.get_title().set_color(style["TEXT_COLOR"])

        Utils.annotate_plot(ax, "Probability", effective_dark_mode)
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
        if data.empty:
            return None

        ax = args.pop("ax", None)
        fig = None
        plot_kwargs = args.copy()  # Preserve original args

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        # Pandas pie plot returns an Axes object.
        plot_ax = (
            data.groupby("precipType")  # pyright: ignore
            .size()
            .plot(kind="pie", label="Precipitation type summary", ax=ax, **plot_kwargs)
        )
        # If ax was not passed, it's created by plot command.
        if not ax:
            ax = plot_ax
            fig = ax.figure
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            # For pie charts, explicitly set AXES_FACE_COLOR, as it might not have other elements like grids
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])

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
        if data.empty:
            return None

        ax = args.pop("ax", None)
        fig = None
        plot_kwargs = args.copy()

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_ax = (
            data.groupby("summary")  # pyright: ignore
            .size()
            .plot(kind="pie", label="Cloud summary", ax=ax, **plot_kwargs)
        )
        if not ax:
            ax = plot_ax
            fig = ax.figure
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])

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
        if data.empty:
            return None

        ax = args.pop("ax", None)
        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_kwargs = args.copy()
        plot_ax = data.plot(x="time", title="Temperatures", ax=ax, **plot_kwargs)  # pyright: ignore

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        legend = ax.get_legend()
        if legend:
            legend.get_frame().set_facecolor(style["AXES_FACE_COLOR"])
            legend.get_frame().set_edgecolor(style["AXIS_COLOR"])
            for text_obj in legend.get_texts():  # Changed variable name
                text_obj.set_color(style["TEXT_COLOR"])
            if legend.get_title():
                legend.get_title().set_color(style["TEXT_COLOR"])

        Utils.annotate_plot(ax, "Temperature [°C]", effective_dark_mode)
        return ax

    def plot_wind(self, hours=24, dark_mode_override: Optional[bool] = None, **args):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        max_wind_speed = self.data[["windSpeed"]].max().max()
        data = self._filter_data(["windSpeed"])
        if data.empty:
            return None

        ax = args.pop("ax", None)
        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_kwargs = args.copy()
        plot_ax = data.plot(  # pyright: ignore
            x="time",
            y="windSpeed",
            ylim=(0, max_wind_speed + 1),
            title="Wind speed",
            ax=ax,
            **plot_kwargs,
        )

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        legend = ax.get_legend()
        if legend:
            legend.get_frame().set_facecolor(style["AXES_FACE_COLOR"])
            legend.get_frame().set_edgecolor(style["AXIS_COLOR"])
            for text_obj in legend.get_texts():  # Changed variable name
                text_obj.set_color(style["TEXT_COLOR"])
            if legend.get_title():
                legend.get_title().set_color(style["TEXT_COLOR"])

        Utils.annotate_plot(ax, "Wind speed [km/h]", effective_dark_mode)
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
            if col in self.data.columns
            and self.data[col].astype(str).str.lower().nunique() > 1
            and self.data[col].notna().any()
        ]
        if not available_columns:
            return None  # Nothing to plot

        data = self._filter_data(available_columns)
        if data.empty:
            return None

        ax = args.pop("ax", None)
        fig = None
        plot_kwargs = args.copy()

        if ax:
            fig = ax.figure

        # Determine plot parameters based on available data
        plot_title = "Pressure"
        secondary_y_plot = []
        if "ozone" in available_columns and "pressure" in available_columns:
            plot_title = "Pressure and Ozone"
            secondary_y_plot = ["ozone"]
        elif "ozone" in available_columns:
            plot_title = "Ozone"

        plot_ax = data.plot(  # pyright: ignore
            x="time",
            title=plot_title,
            secondary_y=secondary_y_plot,
            ax=ax,
            **plot_kwargs,
        )

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        # Style primary legend
        legend = ax.get_legend()
        if legend:
            legend.get_frame().set_facecolor(style["AXES_FACE_COLOR"])
            legend.get_frame().set_edgecolor(style["AXIS_COLOR"])
            for text_obj in legend.get_texts():
                text_obj.set_color(style["TEXT_COLOR"])
            if legend.get_title():
                legend.get_title().set_color(style["TEXT_COLOR"])

        # Annotate primary Y axis
        primary_y_label = ""
        if "pressure" in available_columns:
            primary_y_label = "Pressure [hPa]"
        elif "ozone" in available_columns:
            primary_y_label = "Ozone [DU]"  # Assuming Dobson Units for Ozone
        Utils.annotate_plot(ax, primary_y_label, effective_dark_mode)

        # Style secondary Y axis if it exists
        if secondary_y_plot and hasattr(ax, "right_ax"):
            ax_secondary = ax.right_ax
            ax_secondary.set_ylabel(
                "Ozone [DU]",
                color=style["TEXT_COLOR"],  # Assuming Dobson Units
            )
            ax_secondary.tick_params(axis="y", colors=style["TICK_COLOR"])
            ax_secondary.spines["right"].set_color(style["AXIS_COLOR"])

        return ax

    def get_critical_data(self, start, stop):
        if self.data.empty:
            return pd.DataFrame(
                columns=[
                    "time",
                    "cloudCover",
                    "precipProbability",
                    "windSpeed",
                    "temperature",
                    "visibility",
                    "moonIllumination",
                ]
            )
        data = self._filter_data(
            [
                "cloudCover",
                "precipProbability",
                "windSpeed",
                "temperature",
                "visibility",
                "moonIllumination",
            ]
        )
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
        data = data.query("visibility != 'none'")  # pyright: ignore
        if data.empty:
            return None

        ax = args.pop("ax", None)
        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_kwargs = args.copy()
        plot_ax = data.plot(x="time", title="Visibility", ax=ax, **plot_kwargs)  # pyright: ignore

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        legend = ax.get_legend()
        if legend:
            legend.get_frame().set_facecolor(style["AXES_FACE_COLOR"])
            legend.get_frame().set_edgecolor(style["AXIS_COLOR"])
            for text_obj in legend.get_texts():  # Changed variable name
                text_obj.set_color(style["TEXT_COLOR"])
            if legend.get_title():
                legend.get_title().set_color(style["TEXT_COLOR"])

        Utils.annotate_plot(ax, "Visibility [km]", effective_dark_mode)
        return ax

    def plot_moon_illumination(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        data = self._filter_data(["moonIllumination"])
        if data.empty:
            return None

        ax = args.pop("ax", None)
        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_kwargs = args.copy()
        plot_ax = data.plot(
            x="time", ylim=(0, 105), title="Moon Illumination", ax=ax, **plot_kwargs
        )  # pyright: ignore

        if not ax:  # ax was created by data.plot()
            ax = plot_ax
            fig = ax.figure
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
        else:  # ax was passed in, plot_ax is the same as ax. Apply facecolor after plot.
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        ax.set_title(ax.get_title(), color=style["TEXT_COLOR"])

        legend = ax.get_legend()
        if legend:
            legend.get_frame().set_facecolor(style["AXES_FACE_COLOR"])
            legend.get_frame().set_edgecolor(style["AXIS_COLOR"])
            for text_obj in legend.get_texts():  # Changed variable name
                text_obj.set_color(style["TEXT_COLOR"])
            if legend.get_title():
                legend.get_title().set_color(style["TEXT_COLOR"])

        Utils.annotate_plot(ax, "Illumination [%]", effective_dark_mode)
        return ax
