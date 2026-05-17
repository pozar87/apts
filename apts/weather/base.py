import logging
from datetime import datetime
from typing import Any, Optional, Tuple, cast

import pandas as pd

from apts.cache import get_timescale
from apts.config import get_weather_settings
from apts.utils.planetary import get_moon_illumination_details

from .models import WeatherPlottingMixIn
from .providers import get_provider

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

        provider_name, api_key = self._resolve_provider_and_key(provider_name, api_key)

        logger.info(
            f"Initializing weather provider: {provider_name} for lat={self.lat}, lon={self.lon}"
        )

        try:
            provider = get_provider(
                provider_name, api_key, self.lat, self.lon, self.local_timezone
            )
        except ValueError as e:
            logger.error(str(e))
            raise e

        logger.info(f"Attempting to download data from {provider_name}.")
        self.data = provider.download_data(
            hours=self.hours,
            conditions=conditions,
            observation_window=observation_window,
            force=force,
        )

        if self.data is not None and not cast(pd.DataFrame, self.data).empty:
            logger.info(f"Successfully downloaded weather data from {provider_name}.")
            self._process_downloaded_data(provider)
            self._enrich_moon_data()
        else:
            logger.warning(
                f"Failed to download or received empty data from {provider_name}."
            )
            if self.data is None or cast(pd.DataFrame, self.data).empty:
                self.data = provider._empty_df()

    def _resolve_provider_and_key(
        self, provider_name: Optional[str], api_key: Optional[str]
    ) -> Tuple[str, str]:
        """Resolves provider name and API key from arguments or settings."""
        if provider_name is None:
            resolved_provider, config_api_key = get_weather_settings()
            api_key = config_api_key if config_api_key is not None else api_key
        else:
            resolved_provider = provider_name
            if api_key is None:
                _, config_api_key = get_weather_settings(resolved_provider)
                api_key = config_api_key if config_api_key is not None else api_key

        if api_key is None:
            api_key = "12345"
            logger.warning(
                f"API key for {resolved_provider or 'default provider'} not found in config. Using dummy key '12345'."
            )

        return resolved_provider, api_key

    def _process_downloaded_data(self, provider: Any):
        """Ensures all required columns are present and numeric where appropriate."""
        for col in provider.REQUIRED_COLUMNS:
            if col not in self.data.columns:
                self.data[col] = "none"

            if col not in ["time", "summary", "precipType", "moonWaxing"]:
                self.data[col] = pd.to_numeric(self.data[col], errors="coerce")

    def _enrich_moon_data(self):
        """Enriches data with moon illumination details."""
        ts = get_timescale()
        times = ts.from_datetimes(self.data["time"].tolist())
        illumination, is_waxing = get_moon_illumination_details(times)
        self.data["moonIllumination"] = illumination
        self.data["moonWaxing"] = is_waxing

    def _filter_data(self, rows) -> pd.DataFrame:
        # Always add time column, ensuring it's first and all columns are unique.
        columns = ["time"]
        for col in rows:
            if col not in columns:
                columns.append(col)

        # Ensure all requested columns exist in self.data.
        # This is now handled in _process_downloaded_data, but we keep a simplified
        # version here for safety for custom columns.
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
