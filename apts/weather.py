import json
import logging
from datetime import datetime, timedelta

import pandas as pd
import requests
import requests_cache

from typing import Optional  # Added Optional

from .utils import Utils
from apts.config import get_dark_mode
from apts.constants.graphconstants import get_plot_style
# pyplot may be needed if we need to create figures explicitly, but pandas plot often handles it.
# from matplotlib import pyplot

logger = logging.getLogger(__name__)

requests_cache.install_cache("apts_cache", backend="memory", expire_after=300)


class Weather:
    API_KEY = ""
    API_URL = "https://api.pirateweather.net/forecast/{apikey}/{lat},{lon}?units=si"

    def __init__(self, lat, lon, local_timezone):
        self.lat = lat
        self.lon = lon
        self.local_timezone = local_timezone
        self.data = self.download_data()

    def _filter_data(self, rows):
        # Always add time column
        columns = list(set(["time"] + rows))
        return self.data[columns]

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
            data.groupby("precipType")
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
            data.groupby("summary")
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
        data = self._filter_data(
            ["temperature", "apparentTemperature", "dewPoint"]
        )
        if data.empty:
            return None

        ax = args.pop("ax", None)
        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_kwargs = args.copy()
        plot_ax = data.plot(x="time", title="Temperatures", ax=ax, **plot_kwargs)

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
        plot_ax = data.plot(
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
        data = self._filter_data(["pressure", "ozone"])
        if data.empty:
            return None

        ax = args.pop("ax", None)
        fig = None
        plot_kwargs = args.copy()

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call
            # For secondary_y plots, ensure the primary axis spines are also styled early if needed,
            # though annotate_plot should handle this for the primary axis.
            # ax.spines['left'].set_color(style['AXIS_COLOR']) # Example

        plot_ax = data.plot(
            x="time",
            title="Pressure and Ozone",
            secondary_y=["ozone"],
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

        # Style primary legend
        legend = ax.get_legend()
        if legend:
            legend.get_frame().set_facecolor(style["AXES_FACE_COLOR"])
            legend.get_frame().set_edgecolor(style["AXIS_COLOR"])
            for text_obj in legend.get_texts():
                text_obj.set_color(style["TEXT_COLOR"])
            if legend.get_title():
                legend.get_title().set_color(style["TEXT_COLOR"])

        # Utils.annotate_plot handles primary X and Y axes (labels, ticks, spines)
        Utils.annotate_plot(ax, "Pressure [hPa]", effective_dark_mode)

        # Style secondary Y axis (right axis for 'ozone')
        if hasattr(ax, "right_ax"):
            ax_secondary = ax.right_ax
            ax_secondary.set_ylabel(
                ax_secondary.get_ylabel(), color=style["TEXT_COLOR"]
            )
            ax_secondary.tick_params(axis="y", colors=style["TICK_COLOR"])
            # Ensure the spine for the secondary y-axis is styled.
            # Other spines (top, bottom) are shared and should be styled by annotate_plot on primary ax.
            # The 'left' spine is for the primary y-axis.
            ax_secondary.spines["right"].set_color(style["AXIS_COLOR"])
            # If primary y-axis spine ('left') was not handled by annotate_plot for some reason:
            # ax.spines['left'].set_color(style['AXIS_COLOR'])

        return ax

    def get_critical_data(self, start, stop):
        data = self._filter_data(["cloudCover", "precipProbability", "windSpeed", "temperature"])
        return data[(data.time >= start) & (data.time < stop)]

    def plot_visibility(
        self, hours=24, dark_mode_override: Optional[bool] = None, **args
    ):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        data = self._filter_data(["visibility"], hours)
        data = data.query("visibility != 'none'")
        if data.empty:
            return None

        ax = args.pop("ax", None)
        fig = None

        if ax:
            fig = ax.figure
            # ax.set_facecolor(style['AXES_FACE_COLOR']) # Moved after pandas plot call

        plot_kwargs = args.copy()
        plot_ax = data.plot(x="time", title="Visibility", ax=ax, **plot_kwargs)

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

    def download_data(self):
        url = Weather.API_URL.format(apikey=Weather.API_KEY, lat=self.lat, lon=self.lon)
        logger.debug("Download weather from: {}".format(url))
        with requests.get(url) as data:
            logger.debug(f"Data {data}")
            columns = [
                "time",
                "summary",
                "precipType",
                "precipProbability",
                "precipIntensity",
                "temperature",
                "apparentTemperature",
                "dewPoint",
                "humidity",
                "windSpeed",
                "cloudCover",
                "visibility",
                "pressure",
                "ozone",
            ]
            json_data = json.loads(data.text)
            try:
                raw_data = [
                    [
                        (item[column] if column in item.keys() else "none")
                        for column in columns
                    ]
                    for item in json_data["hourly"]["data"]
                ]
            except KeyError as e:
                logger.error(f"KeyError in weather data: {e}. Full response: {json_data}")
                return pd.DataFrame(columns=columns) # Return empty DataFrame with expected columns
            result = pd.DataFrame(raw_data, columns=columns)
            # Convert units
            result["precipProbability"] *= 100
            result["cloudCover"] *= 100
            result.time = (
                result.time.astype("datetime64[s]")
                .dt.tz_localize("UTC")
                .dt.tz_convert(self.local_timezone)
            )
            return result
