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
        data = None
        try:
            with base.get_session().get(url, timeout=10) as data:
                logger.debug(f"Data {data}")
                data.raise_for_status()
                json_data = json.loads(data.text)

            if "days" not in json_data:
                logger.error(
                    f"KeyError 'days' in weather data. Full response: {json_data}"
                )
                return self._empty_df()

            all_hours_data = []
            for day in json_data["days"]:
                all_hours_data.extend(day["hours"])

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
            df.rename(columns=rename_map, inplace=True)

            # Convert units and types
            df["time"] = (
                pd.to_datetime(df["time"], unit="s")
                .dt.tz_localize("UTC")
                .dt.tz_convert(self.local_timezone)
            )
            if "precipProbability" in df.columns:
                df["precipProbability"] *= 100
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
