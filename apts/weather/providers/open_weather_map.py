import json
import logging
from datetime import datetime, timedelta, timezone
from typing import Any, Optional, Tuple, cast

import numpy as np
import pandas as pd

from . import base
from .base import WeatherProvider

logger = logging.getLogger(__name__)


class OpenWeatherMap(WeatherProvider):
    API_URL = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={apikey}&units=metric&exclude=minutely,daily,alerts"

    def _parse_json_response(self, url: str) -> Optional[dict]:
        data = None
        try:
            with base.get_session().get(url, timeout=10) as data:
                logger.debug(f"Data {data}")
                data.raise_for_status()
                return json.loads(data.text)
        except Exception as e:
            self._log_download_error(e, data.text if data is not None else "")
            return None

    def _extract_weather_info(self, df: pd.DataFrame) -> pd.DataFrame:
        if "weather" in df.columns:
            # Optimization: Using list comprehension instead of .apply() for better performance
            weather_col = df["weather"].values
            df["summary"] = [
                w[0]["description"] if isinstance(w, list) and len(w) > 0 else "none"
                for w in weather_col
            ]
            df["precipType"] = [
                w[0]["main"] if isinstance(w, list) and len(w) > 0 else "none"
                for w in weather_col
            ]
        return df

    def _extract_precipitation_intensity(self, df: pd.DataFrame) -> pd.DataFrame:
        # Optimization: Extract precipIntensity using list comprehensions.
        # This also fixes a bug where rain/snow was missed if the first row was None.
        precip_intensity = np.zeros(len(df))
        if "rain" in df.columns:
            rain_vals = df["rain"].values
            precip_intensity += [
                x.get("1h", 0.0) if isinstance(x, dict) else 0.0 for x in rain_vals
            ]
        if "snow" in df.columns:
            snow_vals = df["snow"].values
            precip_intensity += [
                x.get("1h", 0.0) if isinstance(x, dict) else 0.0 for x in snow_vals
            ]
        df["precipIntensity"] = precip_intensity
        return df

    def _convert_units_and_types(self, df: pd.DataFrame) -> pd.DataFrame:
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
        return df

    def _post_process_data(self, df: pd.DataFrame, hours: int) -> pd.DataFrame:
        # Ensure all required columns are present from the base class
        # (excluding aurora which is added by _enrich_with_aurora_data)
        for col in self.REQUIRED_COLUMNS:
            if col not in df.columns and col != "aurora":
                df[col] = "none"

        # Filter by hours
        cutoff = datetime.now(timezone.utc) + timedelta(hours=hours)
        df = cast(
            pd.DataFrame, df[df.time <= cutoff.astimezone(self.local_timezone)]
        )

        df = self._enrich_with_aurora_data(df)

        # Final check for required columns
        for col in self.REQUIRED_COLUMNS:
            if col not in df.columns:
                df[col] = "none"

        return cast(pd.DataFrame, df[self.REQUIRED_COLUMNS])

    def download_data(
        self,
        hours: int = 48,
        conditions: Optional[Any] = None,
        observation_window: Optional[Tuple[datetime, datetime]] = None,
        force: bool = False,
    ) -> pd.DataFrame:  # pyright: ignore
        url = self.API_URL.format(apikey=self.api_key, lat=self.lat, lon=self.lon)
        self._log_download_url(url)

        json_data = self._parse_json_response(url)
        if not json_data:
            logger.error("No weather data received.")
            return self._empty_df()
        if "hourly" not in json_data:
            logger.error(
                f"KeyError 'hourly' in weather data. Full response: {json_data}"
            )
            return self._empty_df()

        try:
            df = pd.DataFrame(json_data["hourly"])
            df = self._extract_weather_info(df)
            df.rename(
                columns={
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
                },
                inplace=True,
            )

            df = self._extract_precipitation_intensity(df)
            df = self._convert_units_and_types(df)
            return self._post_process_data(df, hours)
        except Exception as e:
            self._log_download_error(e, "")
            return self._empty_df()
