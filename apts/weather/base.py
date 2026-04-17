import logging
from datetime import datetime
from typing import Any, Optional, cast

import pandas as pd

from apts.cache import get_timescale
from apts.config import get_weather_settings
from apts.utils.planetary import get_moon_illumination_details

from .models import WeatherPlottingMixIn
from .providers import (
    Meteoblue,
    OpenWeatherMap,
    PirateWeather,
    StormGlass,
    VisualCrossing,
)

logger = logging.getLogger(__name__)


class Weather(WeatherPlottingMixIn):
    data: pd.DataFrame

    def __init__(
        self,
        lat,
        lon,
        local_timezone,
        provider_name: Optional[str] = None,
        api_key: Optional[str] = None,
        hours: int = 48,
        conditions: Optional[Any] = None,
        observation_window: Optional[Any] = None,
        force: bool = False,
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
        self.data = provider.download_data(
            hours=self.hours,
            conditions=conditions,
            observation_window=observation_window,
            force=force,
        )
        if self.data is not None and not cast(pd.DataFrame, self.data).empty:
            logger.info(f"Successfully downloaded weather data from {provider_name}.")

            # Ensure all required columns are present and numeric where appropriate
            for col in provider.REQUIRED_COLUMNS:
                if col not in self.data.columns:
                    self.data[col] = "none"

                if col not in ["time", "summary", "precipType", "moonWaxing"]:
                    self.data[col] = pd.to_numeric(self.data[col], errors="coerce")

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

        # Ensure all requested columns exist in self.data.
        # This is now also handled in __init__, but we keep it here for safety
        # and to handle cases where 'rows' contains columns not in REQUIRED_COLUMNS.
        for col in columns:
            if col not in self.data.columns:
                self.data[col] = "none"

        # Ensure numeric columns are numeric
        result = self.data[columns].copy()  # type: ignore
        for col in columns:
            if col != "time" and col not in ["summary", "precipType", "moonWaxing"]:
                result[col] = pd.to_numeric(result[col], errors="coerce")

        return cast(pd.DataFrame, result)

    def get_critical_data(self, start: datetime, stop: datetime) -> pd.DataFrame:
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
                        "moon_altitude",
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
            "seeing",
            "sqm",
            "moon_altitude",
        ]
        data = self._filter_data(critical_data_columns)
        return data[(data.time >= start) & (data.time <= stop)]  # pyright: ignore
