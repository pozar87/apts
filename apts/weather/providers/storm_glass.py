import json
import logging
from datetime import datetime, timedelta, timezone
from typing import Any, Optional, Tuple, cast

import numpy as np
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
        data = None
        try:
            json_data, data = self._fetch_raw_data(hours, params)
            if json_data is None:
                return self._empty_df()

            df = self._parse_stormglass_hours(json_data, params)
            df = self._convert_units(df)
            df = self._standardize_dataframe(df, hours)

            df = self._enrich_with_aurora_data(df)
            required_columns = self.REQUIRED_COLUMNS[:]
            if "aurora" not in df.columns:
                required_columns.remove("aurora")

            # moon columns are added by Weather class
            for col in ["moonIllumination", "moonWaxing", "seeing", "sqm"]:
                if col in required_columns:
                    required_columns.remove(col)

            return cast(pd.DataFrame, df[required_columns])
        except Exception as e:
            self._log_download_error(e, data.text if data is not None else "")
            return self._empty_df()

    def _fetch_raw_data(
        self, hours: int, params: list[str]
    ) -> tuple[Optional[dict], Any]:
        """Fetches raw JSON data from StormGlass API."""
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
        with base.get_session().get(url, headers=headers, timeout=10) as response:
            logger.debug(f"Data {response}")
            response.raise_for_status()
            json_data = json.loads(response.text)

        if "hours" not in json_data:
            logger.error(
                f"KeyError 'hours' in weather data. Full response: {json_data}"
            )
            return None, response

        return json_data, response

    def _parse_stormglass_hours(
        self, json_data: dict, params: list[str]
    ) -> pd.DataFrame:
        """Parses the 'hours' list from StormGlass JSON response into a DataFrame."""
        rows = []
        for item in json_data["hours"]:
            row = {"time": item["time"]}
            for p in params:
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
        return pd.DataFrame(rows)

    def _convert_units(self, df: pd.DataFrame) -> pd.DataFrame:
        """Renames columns and converts units for StormGlass data."""
        rename_map = {
            "airTemperature": "temperature",
            "dewPointTemperature": "dewPoint",
            "precipitation": "precipIntensity",
        }
        df.rename(columns=rename_map, inplace=True)
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

        if "windSpeed" in df.columns:
            df["windSpeed"] *= 3.6

        if "visibility" in df.columns:
            df["fog"] = (10 - df["visibility"].clip(0, 10)) * 10
        else:
            df["fog"] = "none"

        # Optimization: Vectorized precipitation type calculation to avoid slow apply(axis=1).
        precip = pd.to_numeric(df["precipIntensity"], errors="coerce").fillna(0)
        rain = pd.to_numeric(df.get("rain"), errors="coerce")
        snow = pd.to_numeric(df.get("snow"), errors="coerce")

        # Default is rain
        precip_type = np.full(len(df), "rain", dtype=object)

        # Condition for none: intensity <= 0
        precip_type[precip <= 0] = "none"

        # Condition for snow: intensity > 0 AND snow > rain
        if snow is not None and rain is not None:
            snow_mask = (precip > 0) & snow.notna() & rain.notna() & (snow > rain)
            precip_type[snow_mask] = "snow"

        df["precipType"] = precip_type
        return df

    def _get_precip_type(self, row: pd.Series) -> str:
        """
        Determines precipitation type (none, rain, snow) for a single row.
        Deprecated: Use vectorized logic in _convert_units instead.
        """
        precip_intensity = row.get("precipIntensity", 0)
        if (
            precip_intensity is None
            or bool(pd.isna(precip_intensity))
            or (isinstance(precip_intensity, (int, float)) and precip_intensity <= 0)
            or precip_intensity == "none"
        ):
            return "none"
        rain = row.get("rain", 0)
        snow = row.get("snow", 0)
        if (
            snow is not None
            and rain is not None
            and bool(pd.notna(snow))
            and bool(pd.notna(rain))
            and snow != "none"
            and rain != "none"
            and bool(float(snow) > float(rain))
        ):
            return "snow"
        return "rain"

    def _standardize_dataframe(self, df: pd.DataFrame, hours: int) -> pd.DataFrame:
        """Ensures all standard columns exist and filters by requested hours."""
        df["summary"] = "none"
        if (
            "precipProbability" not in df.columns
            or bool(df["precipProbability"].isna().all())
            or bool((df["precipProbability"] == "none").all())
        ):
            # Optimization: Vectorized precipitation probability calculation to avoid slow apply().
            precip_nums = pd.to_numeric(df["precipIntensity"], errors="coerce").fillna(0)
            df["precipProbability"] = (precip_nums > 0).astype(int) * 100

        if (
            "apparentTemperature" not in df.columns
            or bool(df["apparentTemperature"].isna().all())
            or bool((df["apparentTemperature"] == "none").all())
        ):
            df["apparentTemperature"] = df["temperature"]

        df["ozone"] = "none"

        required = [
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
        for col in required:
            if col not in df.columns:
                df[col] = "none"

        cutoff = datetime.now(timezone.utc) + timedelta(hours=hours)
        return cast(pd.DataFrame, df[df.time <= cutoff.astimezone(self.local_timezone)])
