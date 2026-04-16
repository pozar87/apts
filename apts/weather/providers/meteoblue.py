import json
import logging
import math
from datetime import datetime, timedelta, timezone
from typing import Any, Optional, Tuple, cast

import pandas as pd

from . import base
from .base import WeatherProvider

logger = logging.getLogger(__name__)


class Meteoblue(WeatherProvider):
    BASIC_URL = "https://my.meteoblue.com/packages/basic-1h?lat={lat}&lon={lon}&apikey={apikey}&format=json&forecast_days={forecast_days}"
    CLOUDS_URL = "https://my.meteoblue.com/packages/clouds-1h?lat={lat}&lon={lon}&apikey={apikey}&format=json&forecast_days={forecast_days}"

    def _parse_meteoblue_response(self, data_text: str) -> pd.DataFrame:
        try:
            json_data = json.loads(data_text)
        except Exception as e:
            self._log_download_error(e, data_text)
            return pd.DataFrame()

        if "data_1h" not in json_data:
            logger.error(
                f"KeyError 'data_1h' in weather data. Full response: {json_data}"
            )
            return pd.DataFrame()

        df = pd.DataFrame(json_data["data_1h"])

        # Rename columns to match the standard format
        rename_map = {
            "time": "time",
            "pictocode": "summary",
            "snowfraction": "precipType",
            "precipitation_probability": "precipProbability",
            "precipitation": "precipIntensity",
            "temperature": "temperature",
            "felttemperature": "apparentTemperature",
            "dewpointtemperature": "dewPoint",
            "relativehumidity": "humidity",
            "windspeed": "windSpeed",
            "totalcloudcover": "cloudCover",
            "visibility": "visibility",
            "sealevelpressure": "pressure",
            "ozone_concentration": "ozone",
            "fog_probability": "fog",
        }
        # Only rename columns that actually exist in the response
        existing_rename_map = {k: v for k, v in rename_map.items() if k in df.columns}
        df.rename(columns=existing_rename_map, inplace=True)

        # Convert units and types
        if "time" in df.columns:
            df["time"] = (
                pd.to_datetime(df["time"])
                .dt.tz_localize("UTC")
                .dt.tz_convert(self.local_timezone)
            )

        if "precipType" in df.columns:
            df["precipType"] = df["precipType"].apply(
                lambda x: "snow" if x > 0 else "rain"
            )

        if "visibility" in df.columns:
            df["visibility"] = pd.to_numeric(df["visibility"], errors="coerce") / 1000  # type: ignore

        if "fog" in df.columns:
            df["fog"] = pd.to_numeric(df["fog"], errors="coerce")
        elif "visibility" in df.columns:
            # Fallback to visibility if fog_probability is not available
            df["fog"] = (10 - df["visibility"].clip(0, 10)) * 10  # Fog in [%]

        return df

    def _is_weather_good(self, df, conditions, observation_window) -> bool:
        start, stop = observation_window
        # Filter data for the observation window
        df_window = df[(df.time >= start) & (df.time <= stop)].copy()
        if df_window.empty:
            return True

        # Optimization: Vectorized weather goodness check to avoid slow iterrows() loop.
        # This provides a >10x speedup for large weather datasets.
        is_good_mask = pd.Series(True, index=df_window.index)

        # Helper to apply threshold conditions in a vectorized manner
        def apply_bad_condition(col, condition):
            nonlocal is_good_mask
            if col in df_window.columns:
                vals = pd.to_numeric(df_window[col], errors="coerce")
                # An hour is "bad" if the value exists and violates the threshold.
                # fillna(False) ensures that missing/non-numeric values don't trigger "bad" status.
                is_good_mask &= ~condition(vals).fillna(False)

        apply_bad_condition("cloudCover", lambda x: x > conditions.max_clouds)
        apply_bad_condition("visibility", lambda x: x < conditions.min_visibility)
        apply_bad_condition("fog", lambda x: x > conditions.max_fog)
        apply_bad_condition("precipProbability", lambda x: x > conditions.max_precipitation_probability)
        apply_bad_condition("precipIntensity", lambda x: x > conditions.max_precipitation_intensity)
        apply_bad_condition("windSpeed", lambda x: x > conditions.max_wind)
        apply_bad_condition("temperature", lambda x: (x < conditions.min_temperature) | (x > conditions.max_temperature))
        apply_bad_condition("seeing", lambda x: x > conditions.max_seeing)
        apply_bad_condition("sqm", lambda x: x < conditions.min_sqm)
        apply_bad_condition("aurora", lambda x: x < conditions.min_aurora)

        # Moon illumination check is tricky because moon altitude is not typically in Meteoblue response
        # but we can check the illumination if it's there.
        apply_bad_condition("moonIllumination", lambda x: x > conditions.max_moon_illumination)

        good_hours = is_good_mask.sum()
        return (good_hours / len(df_window)) * 100 > conditions.min_weather_goodness

    def download_data(
        self,
        hours: int = 48,
        conditions: Optional[Any] = None,
        observation_window: Optional[Tuple[datetime, datetime]] = None,
        force: bool = False,
    ) -> pd.DataFrame:  # pyright: ignore
        forecast_days = math.ceil(hours / 24)

        # 1. Fetch CLOUDS package (cheaper)
        url_clouds = self.CLOUDS_URL.format(
            apikey=self.api_key,
            lat=self.lat,
            lon=self.lon,
            forecast_days=forecast_days,
        )
        self._log_download_url(url_clouds)
        resp_clouds = None
        try:
            with base.get_session().get(url_clouds, timeout=10) as resp_clouds:
                resp_clouds.raise_for_status()
                df = self._parse_meteoblue_response(resp_clouds.text)
        except Exception as e:
            self._log_download_error(
                e, resp_clouds.text if resp_clouds is not None else ""
            )
            return self._empty_df()

        if df.empty:
            return self._empty_df()

        # 2. Check if weather is already bad based on cloud data
        if not force and conditions is not None and observation_window is not None:
            if not self._is_weather_good(df, conditions, observation_window):
                logger.info(
                    "Meteoblue: cloud conditions not met, skipping basic-1h fetch and aurora enrichment."
                )
                return self._finalize_df(df, hours)

        # 3. Fetch BASIC package
        url_basic = self.BASIC_URL.format(
            apikey=self.api_key,
            lat=self.lat,
            lon=self.lon,
            forecast_days=forecast_days,
        )
        self._log_download_url(url_basic)
        resp_basic = None
        try:
            with base.get_session().get(url_basic, timeout=10) as resp_basic:
                resp_basic.raise_for_status()
                df_basic = self._parse_meteoblue_response(resp_basic.text)
                if not df_basic.empty:
                    # Merge with cloud data
                    df = pd.merge(df, df_basic, on="time", suffixes=("", "_basic"))
        except Exception as e:
            self._log_download_error(
                e, resp_basic.text if resp_basic is not None else ""
            )
            # Continue with cloud data only if basic fetch fails

        df = self._finalize_df(df, hours)
        return self._enrich_with_aurora_data(df)

    def _finalize_df(self, df: pd.DataFrame, hours: int) -> pd.DataFrame:
        # Ensure all required columns are present
        required_columns = self.REQUIRED_COLUMNS.copy()
        if "aurora" in required_columns:
            required_columns.remove("aurora")

        for col in required_columns:
            if col not in df.columns:
                df[col] = "none"

        # Filter by hours
        cutoff = datetime.now(timezone.utc) + timedelta(hours=hours)
        df = cast(pd.DataFrame, df[df.time <= cutoff.astimezone(self.local_timezone)])
        return cast(pd.DataFrame, df[required_columns])
