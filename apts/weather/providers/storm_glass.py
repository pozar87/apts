import json
import logging
from datetime import datetime, timedelta, timezone
from typing import Any, Optional, Tuple, cast

import pandas as pd

from . import base
from .base import WeatherProvider

logger = logging.getLogger(__name__)


class StormGlass(WeatherProvider):
    API_URL = "https://api.stormglass.io/v2/weather/point?key={apikey}&lat={lat}&lng={lon}&params={params}&start={start}&end={end}"

    def download_data(
        self,
        hours: int = 48,
        conditions: Optional[Any] = None,
        observation_window: Optional[Tuple[datetime, datetime]] = None,
        force: bool = False,
    ) -> pd.DataFrame:
        params = [
            "airTemperature",
            "pressure",
            "cloudCover",
            "dewPointTemperature",
            "humidity",
            "precipitation",
            "visibility",
            "windSpeed",
            "gust",
            "rain",
            "snow",
        ]
        start = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
        end = start + timedelta(hours=hours)
        url = self.API_URL.format(
            lat=self.lat,
            lon=self.lon,
            apikey=self.api_key,
            params=",".join(params),
            start=start.strftime("%Y-%m-%dT%H:%M:%SZ"),
            end=end.strftime("%Y-%m-%dT%H:%M:%SZ"),
        )
        self._log_download_url(url)
        headers = {"Authorization": self.api_key}
        data = None
        try:
            with base.get_session().get(url, headers=headers, timeout=10) as data:
                logger.debug(f"Data {data}")
                data.raise_for_status()
                json_data = json.loads(data.text)

            if "hours" not in json_data:
                logger.error(
                    f"KeyError 'hours' in weather data. Full response: {json_data}"
                )
                return self._empty_df()

            rows = []
            for item in json_data["hours"]:
                row = {"time": item["time"]}
                for p in params:
                    # Pick 'sg' source if available, otherwise first available
                    if p in item:
                        if "sg" in item[p]:
                            row[p] = item[p]["sg"]
                        elif item[p]:
                            row[p] = next(iter(item[p].values()))
                        else:
                            row[p] = "none"
                    else:
                        row[p] = "none"
                rows.append(row)

            df = pd.DataFrame(rows)

            # Rename columns to match the standard format
            rename_map = {
                "airTemperature": "temperature",
                "dewPointTemperature": "dewPoint",
                "precipitation": "precipIntensity",
            }
            df.rename(columns=rename_map, inplace=True)

            # Convert units and types
            df["time"] = pd.to_datetime(df["time"]).dt.tz_convert(self.local_timezone)

            for col in [
                "temperature",
                "dewPoint",
                "precipIntensity",
                "humidity",
                "windSpeed",
                "cloudCover",
                "visibility",
                "pressure",
                "rain",
                "snow",
                "apparentTemperature",
            ]:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors="coerce")

            # windSpeed is in m/s, convert to km/h
            if "windSpeed" in df.columns:
                df["windSpeed"] *= 3.6

            if "visibility" in df.columns:
                df["fog"] = (10 - df["visibility"].clip(0, 10)) * 10  # Fog in [%]
            else:
                df["fog"] = "none"

            # Derive precipType
            def get_precip_type(row):
                if (
                    pd.isna(row.get("precipIntensity"))
                    or row.get("precipIntensity", 0) <= 0
                ):
                    return "none"
                rain = row.get("rain", 0)
                snow = row.get("snow", 0)
                if not pd.isna(snow) and not pd.isna(rain) and snow > rain:
                    return "snow"
                return "rain"

            df["precipType"] = df.apply(get_precip_type, axis=1)

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
                "fog",
            ]

            # Add missing standard columns
            df["summary"] = "none"
            df = cast(pd.DataFrame, df)
            # Derive a dummy precipProbability based on precipIntensity if not available
            if (
                "precipProbability" not in df.columns
                or bool(df["precipProbability"].isna().all())
                or bool((df["precipProbability"] == "none").all())
            ):
                df["precipProbability"] = df["precipIntensity"].apply(
                    lambda x: 100 if pd.notna(x) and x != "none" and x > 0 else 0
                )
            if (
                "apparentTemperature" not in df.columns
                or bool(df["apparentTemperature"].isna().all())
                or bool((df["apparentTemperature"] == "none").all())
            ):
                df["apparentTemperature"] = df["temperature"]
            df["ozone"] = "none"

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
