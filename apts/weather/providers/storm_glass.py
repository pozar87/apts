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

        try:
            json_data, data_text = self._fetch_raw_data(url)
            if "hours" not in json_data:
                logger.error(
                    f"KeyError 'hours' in weather data. Full response: {json_data}"
                )
                return self._empty_df()

            rows = self._parse_stormglass_hours(json_data, params)
            df = pd.DataFrame(rows)
            df = self._standardize_dataframe(df, hours)

            df = self._enrich_with_aurora_data(df)
            required_columns = self.REQUIRED_COLUMNS.copy()
            # Filter columns that actually exist in the dataframe
            final_columns = [col for col in required_columns if col in df.columns]
            return cast(pd.DataFrame, df[final_columns])
        except Exception as e:
            # We don't have access to 'data_text' here if _fetch_raw_data fails before returning it,
            # but _fetch_raw_data already handles its own errors or we catch them here.
            self._log_download_error(e, "")
            return self._empty_df()

    def _fetch_raw_data(self, url: str) -> Tuple[dict, str]:
        """Fetches raw JSON data from StormGlass API."""
        headers = {"Authorization": self.api_key}
        with base.get_session().get(url, headers=headers, timeout=10) as response:
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

    def _parse_stormglass_hours(self, json_data: dict, params: list) -> list:
        """Parses the 'hours' section of the StormGlass JSON response."""
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
        return rows

    def _standardize_dataframe(self, df: pd.DataFrame, hours: int) -> pd.DataFrame:
        """Applies renames, unit conversions, and derived fields to the dataframe."""
        # Rename columns to match the standard format
        rename_map = {
            "airTemperature": "temperature",
            "dewPointTemperature": "dewPoint",
            "precipitation": "precipIntensity",
        }
        df.rename(columns=rename_map, inplace=True)

        # Convert units and types
        df["time"] = pd.to_datetime(df["time"]).dt.tz_convert(self.local_timezone)

        numeric_cols = [
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
        ]
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        # windSpeed is in m/s, convert to km/h
        if "windSpeed" in df.columns:
            df["windSpeed"] *= 3.6

        if "visibility" in df.columns:
            df["fog"] = (10 - df["visibility"].clip(0, 10)) * 10  # Fog in [%]
        else:
            df["fog"] = "none"

        df["precipType"] = df.apply(self._get_precip_type, axis=1)

        # Add missing standard columns
        df["summary"] = "none"

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
            df["apparentTemperature"] = (
                df["temperature"] if "temperature" in df.columns else "none"
            )

        df["ozone"] = "none"

        # Ensure all required columns are present
        for col in self.REQUIRED_COLUMNS:
            if col not in df.columns:
                df[col] = "none"

        # Filter by hours
        cutoff = datetime.now(timezone.utc) + timedelta(hours=hours)
        df = df[df.time <= cutoff.astimezone(self.local_timezone)]

        return df

    def _get_precip_type(self, row):
        """Derives precipitation type from intensity and rain/snow flags."""
        intensity = row.get("precipIntensity")
        if pd.isna(intensity) or (isinstance(intensity, (int, float)) and intensity <= 0):
            return "none"
        rain = row.get("rain", 0)
        snow = row.get("snow", 0)
        if not pd.isna(snow) and not pd.isna(rain) and snow > rain:
            return "snow"
        return "rain"
