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
        data = None
        try:
            with base.get_session().get(url, timeout=10) as data:
                logger.debug(f"Data {data}")
                data.raise_for_status()
                json_data = json.loads(data.text)

            if "hourly" not in json_data:
                logger.error(
                    f"KeyError 'hourly' in weather data. Full response: {json_data}"
                )
                return self._empty_df()

            df = pd.DataFrame(json_data["hourly"])

            # The 'weather' column contains a list with a dictionary, extract the description
            df["summary"] = df["weather"].apply(
                lambda x: x[0]["description"] if x else "none"
            )
            df["precipType"] = df["weather"].apply(
                lambda x: x[0]["main"] if x else "none"
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
            if "rain" in df.columns and isinstance(df["rain"].iloc[0], dict):
                df["precipIntensity"] = df["rain"].apply(
                    lambda x: x.get("1h", 0) if isinstance(x, dict) else 0
                )
            elif "snow" in df.columns and isinstance(df["snow"].iloc[0], dict):
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
                df["precipProbability"] *= 100

            if "humidity" in df.columns:
                df["humidity"] /= 100

            # Convert wind speed from m/s to km/h
            if "windSpeed" in df.columns:
                df["windSpeed"] *= 3.6

            # Convert visibility from meters to km
            if "visibility" in df.columns:
                df["visibility"] /= 1000
            df["visibility"] = pd.to_numeric(df["visibility"], errors="coerce")
            df["fog"] = (10 - df["visibility"].clip(0, 10)) * 10  # Fog in [%]

            # Ensure all required columns are present
            required_columns = [
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
            for col in required_columns:
                if col not in df.columns:
                    df[col] = "none"

            # Filter by hours
            cutoff = datetime.now(timezone.utc) + timedelta(hours=hours)
            df = cast(
                pd.DataFrame, df[df.time <= cutoff.astimezone(self.local_timezone)]
            )

            df = self._enrich_with_aurora_data(df)
            if "aurora" in df.columns:
                required_columns.append("aurora")
            return cast(pd.DataFrame, df[required_columns])
        except Exception as e:
            self._log_download_error(e, data.text if data is not None else "")
            return self._empty_df()
