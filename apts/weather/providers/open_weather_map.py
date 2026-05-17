import json
import logging
from datetime import datetime, timedelta, timezone
from typing import Any, Optional, Tuple, cast

import pandas as pd

from . import base
from .base import WeatherProvider

logger = logging.getLogger(__name__)


class OpenWeatherMap(WeatherProvider):
    API_URL = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={apikey}&units=metric&exclude=minutely,daily,alerts"

    def download_data(
        self,
        hours: int = 48,
        conditions: Optional[Any] = None,
        observation_window: Optional[Tuple[datetime, datetime]] = None,
        force: bool = False,
    ) -> pd.DataFrame:  # pyright: ignore
        url = self.API_URL.format(apikey=self.api_key, lat=self.lat, lon=self.lon)
        self._log_download_url(url)
        try:
            json_data, data_text = self._fetch_raw_data(url)

            if "hourly" not in json_data:
                logger.error(
                    f"KeyError 'hourly' in weather data. Full response: {json_data}"
                )
                return self._empty_df()

            df = pd.DataFrame(json_data["hourly"])
            df = self._standardize_dataframe(df, hours)

            df = self._enrich_with_aurora_data(df)
            required_columns = self.REQUIRED_COLUMNS.copy()
            final_columns = [col for col in required_columns if col in df.columns]
            return cast(pd.DataFrame, df[final_columns])
        except Exception as e:
            self._log_download_error(e, "")
            return self._empty_df()

    def _fetch_raw_data(self, url: str) -> Tuple[dict, str]:
        """Fetches raw JSON data from OpenWeatherMap API."""
        with base.get_session().get(url, timeout=10) as response:
            logger.debug(f"Data {response}")
            response.raise_for_status()
            data_text = response.text
            try:
                json_data = response.json()
                # Handle MagicMocks in tests that return another mock for .json()
                if not isinstance(json_data, (dict, list)):
                    json_data = json.loads(data_text)
            except (AttributeError, ValueError, TypeError, json.JSONDecodeError):
                json_data = json.loads(data_text)
            return json_data, data_text

    def _standardize_dataframe(self, df: pd.DataFrame, hours: int) -> pd.DataFrame:
        """Applies renames, unit conversions, and derived fields to the dataframe."""
        # The 'weather' column contains a list with a dictionary, extract the description
        df["summary"] = df["weather"].apply(
            lambda x: x[0]["description"] if x and len(x) > 0 else "none"
        )
        df["precipType"] = df["weather"].apply(
            lambda x: x[0]["main"] if x and len(x) > 0 else "none"
        )

        # Rename columns to match the standard format
        rename_map = {
            "dt": "time",
            "pop": "precipProbability",
            "temp": "temperature",
            "feels_like": "apparentTemperature",
            "dew_point": "dewPoint",
            "humidity": "humidity",
            "wind_speed": "windSpeed",
            "clouds": "cloudCover",
            "visibility": "visibility",
            "pressure": "pressure",
        }
        df.rename(columns=rename_map, inplace=True)

        # precipIntensity
        if "rain" in df.columns and len(df) > 0 and isinstance(df["rain"].iloc[0], dict):
            df["precipIntensity"] = df["rain"].apply(
                lambda x: x.get("1h", 0) if isinstance(x, dict) else 0
            )
        elif "snow" in df.columns and len(df) > 0 and isinstance(df["snow"].iloc[0], dict):
            df["precipIntensity"] = df["snow"].apply(
                lambda x: x.get("1h", 0) if isinstance(x, dict) else 0
            )
        else:
            df["precipIntensity"] = 0

        # Convert units and types
        df["time"] = (
            pd.to_datetime(df["time"], unit="s")
            .dt.tz_localize("UTC")
            .dt.tz_convert(self.local_timezone)
        )
        if "precipProbability" in df.columns:
            df["precipProbability"] = pd.to_numeric(df["precipProbability"], errors="coerce") * 100

        if "humidity" in df.columns:
            df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce") / 100

        # Convert wind speed from m/s to km/h
        if "windSpeed" in df.columns:
            df["windSpeed"] = pd.to_numeric(df["windSpeed"], errors="coerce") * 3.6

        # Convert visibility from meters to km
        if "visibility" in df.columns:
            df["visibility"] = pd.to_numeric(df["visibility"], errors="coerce") / 1000

        df["visibility"] = pd.to_numeric(df["visibility"], errors="coerce")
        df["fog"] = (10 - df["visibility"].clip(0, 10)) * 10  # Fog in [%]

        # Ensure all required columns are present
        for col in self.REQUIRED_COLUMNS:
            if col not in df.columns:
                df[col] = "none"

        # Filter by hours
        cutoff = datetime.now(timezone.utc) + timedelta(hours=hours)
        df = df[df.time <= cutoff.astimezone(self.local_timezone)]

        return df
