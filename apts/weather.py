import json
import logging
from datetime import datetime, timedelta

import pandas as pd
import requests
import requests_cache

from .utils import Utils

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

    def _filter_data(self, rows, hours):
        # Always add time column
        columns = ["time"] + rows
        # Calculate time horizon base on number of hours (max is 48h as longer predictions are inacurate)
        time_horizon = datetime.utcnow().replace(
            tzinfo=self.local_timezone
        ) + timedelta(hours=min(hours, 48))
        return self.data[columns][self.data.time < time_horizon]

    def plot_clouds(self, hours=24, **args):
        data = self._filter_data(["cloudCover"], hours)
        # Check if there is something to plot
        if data.empty:
            return None
            plot = data.plot(x="time", ylim=(0, 105), title="Clouds", **args)
            Utils.annotate_plot(plot, "Cloud cover [%]")
            return plot

    def plot_precipitation(self, hours=24, **args):
        data = self._filter_data(["precipIntensity", "precipProbability"], hours)
        # Check if there is something to plot
        if data.empty:
            return None
            plot = data.plot(
                x="time", title="Precipitation intensity and probability", **args
            )
            Utils.annotate_plot(plot, "Probability")
            return plot

    def plot_precipitation_type_summary(self, hours=24, **args):
        data = self._filter_data(["precipType"], hours)
        # Check if there is something to plot
        if data.empty:
            return None
            plot = (
                data.groupby("precipType")
                .size()
                .plot(kind="pie", label="Precipitation type summary", **args)
            )
            return plot

    def plot_clouds_summary(self, hours=24, **args):
        data = self._filter_data(["summary"], hours)
        # Check if there is something to plot
        if data.empty:
            return None
            plot = (
                data.groupby("summary")
                .size()
                .plot(kind="pie", label="Cloud summary", **args)
            )
            return plot

    def plot_temperature(self, hours=24, **args):
        data = self._filter_data(
            ["temperature", "apparentTemperature", "dewPoint"], hours
        )
        # Check if there is something to plot
        if data.empty:
            return None
            plot = data.plot(x="time", title="Temperatures", **args)
            Utils.annotate_plot(plot, "Temperature [°C]")
            return plot

    def plot_wind(self, hours=24, **args):
        max_wind_speed = self.data[["windSpeed"]].max().max()
        data = self._filter_data(["windSpeed"], hours)
        # Check if there is something to plot
        if data.empty:
            return None
            plot = data.plot(
                x="time",
                y="windSpeed",
                ylim=(0, max_wind_speed + 1),
                title="Wind speed",
                **args,
            )
            Utils.annotate_plot(plot, "Wind speed [km/h]")
            return plot

    def plot_pressure_and_ozone(self, hours=24, **args):
        data = self._filter_data(["pressure", "ozone"], hours)
        # Check if there is something to plot
        if data.empty:
            return None
            plot = data.plot(
                x="time", title="Pressure and Ozone", secondary_y=["ozone"], **args
            )
            Utils.annotate_plot(plot, "Pressure [hPa]")
            return plot

    def get_critical_data(self, start, stop):
        data = self._filter_data(
            ["cloudCover", "precipProbability", "windSpeed", "temperature"],
            hours=24,
        )
        return data[(data.time > start) & (data.time < stop)]

    def plot_visibility(self, hours=24, **args):
        data = self._filter_data(["visibility"], hours)
        data = data.query("visibility != 'none'")
        # Check if there is something to plot
        if data.empty:
            return None
            plot = data.plot(x="time", title="Visibility", **args)
            Utils.annotate_plot(plot, "Visibility [km]")
            return plot

    def download_data(self):
        url = Weather.API_URL.format(apikey=Weather.API_KEY, lat=self.lat, lon=self.lon)
        logger.debug("Download weather from: {}".format(url))
        try:
            with requests.get(url) as response:
                response.raise_for_status()
                data = response.json()
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
                raw_data = [
                    [
                        (item[column] if column in item.keys() else "none")
                        for column in columns
                    ]
                    for item in data["hourly"]["data"]
                ]
                result = pd.DataFrame(raw_data, columns=columns)
                # Convert units
                if not result.empty:
                    result["precipProbability"] *= 100
                    result["cloudCover"] *= 100
                    result.time = (
                        result.time.astype("datetime64[s]")
                        .dt.tz_localize("UTC")
                        .dt.tz_convert(self.local_timezone)
                    )
                    return result
        except requests.RequestException as e:
            logger.error(f"Failed to download weather data: {e}")
            return None
