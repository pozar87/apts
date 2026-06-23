import json
import logging
from datetime import datetime, timedelta, timezone
from typing import Any, Optional, Tuple, cast

import pandas as pd

from . import base
from .base import WeatherProvider

logger = logging.getLogger(__name__)


class VisualCrossing(WeatherProvider):
    API_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{lon}/next{hours}hours?unitGroup=metric&key={apikey}&include=hours"

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

    def _convert_units_and_types(self, df: pd.DataFrame) -> pd.DataFrame:
        # Convert units and types
        df["time"] = (
            pd.to_datetime(df["time"], unit="s")
            .dt.tz_localize("UTC")
            .dt.tz_convert(self.local_timezone)
        )

        # Visual Crossing returns humidity as 0-100, we want 0-1
        if "humidity" in df.columns:
            df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce") / 100  # type: ignore[operator]

        # Visual Crossing returns precipprob and cloudcover as 0-100, which is what we want.
        # No need to multiply by 100 as in some other providers.

        if "visibility" in df.columns:
            df["visibility"] = pd.to_numeric(df["visibility"], errors="coerce")
            # Fog in [%] based on visibility (km)
            df["fog"] = (10 - df["visibility"].clip(0, 10)) * 10
        return df

    def _process_precip_type(self, df: pd.DataFrame) -> pd.DataFrame:
        if "precipType" in df.columns:
            # Visual Crossing returns a list of strings for preciptype
            df["precipType"] = [
                ", ".join(pt) if isinstance(pt, list) else pt for pt in df["precipType"]
            ]
        return df

    def _post_process_data(self, df: pd.DataFrame, hours: int) -> pd.DataFrame:
        # Ensure all required columns are present
        for col in self.REQUIRED_COLUMNS:
            if col not in df.columns and col != "aurora":
                df[col] = "none"

        # Filter by hours
        cutoff = datetime.now(timezone.utc) + timedelta(hours=hours)
        df = cast(pd.DataFrame, df[df.time <= cutoff.astimezone(self.local_timezone)])

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
        url = self.API_URL.format(
            apikey=self.api_key, lat=self.lat, lon=self.lon, hours=hours
        )
        self._log_download_url(url)

        json_data = self._parse_json_response(url)
        if not json_data:
            logger.error("No weather data received.")
            return self._empty_df()

        if "days" not in json_data:
            logger.error(f"KeyError 'days' in weather data. Full response: {json_data}")
            return self._empty_df()

        try:
            all_hours_data = []
            for day in json_data["days"]:
                if "hours" in day:
                    all_hours_data.extend(day["hours"])

            if not all_hours_data:
                logger.warning("No hourly data found in Visual Crossing response.")
                return self._empty_df()

            df = pd.DataFrame(all_hours_data)

            # Rename columns to match the standard format
            rename_map = {
                "datetimeEpoch": "time",
                "conditions": "summary",
                "preciptype": "precipType",
                "precipprob": "precipProbability",
                "precip": "precipIntensity",
                "temp": "temperature",
                "feelslike": "apparentTemperature",
                "dew": "dewPoint",
                "humidity": "humidity",
                "windspeed": "windSpeed",
                "cloudcover": "cloudCover",
                "visibility": "visibility",
                "pressure": "pressure",
                "ozone": "ozone",
            }
            # Only rename columns that exist
            existing_rename_map = {
                k: v for k, v in rename_map.items() if k in df.columns
            }
            df.rename(columns=existing_rename_map, inplace=True)

            df = self._process_precip_type(df)
            df = self._convert_units_and_types(df)
            return self._post_process_data(df, hours)
        except Exception as e:
            self._log_download_error(e, "")
            return self._empty_df()
