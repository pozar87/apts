import json
import logging
import math
from abc import ABC, abstractmethod
from datetime import datetime, timedelta, timezone
from typing import Any, Optional, Tuple, cast

import pandas as pd
import requests_cache

from apts.config import get_cache_settings
from .secrets import mask_text

logger = logging.getLogger(__name__)

session = None
_last_cache_settings = None


def reset_session():
    """
    Resets the global session, closing it if it exists.
    """
    global session, _last_cache_settings
    if session is not None:
        try:
            session.close()
        except Exception as e:
            logger.debug(f"Error closing session: {e}")
    session = None
    _last_cache_settings = None


def get_session():
    global session, _last_cache_settings
    cache_settings = get_cache_settings()

    # If session exists, check if settings have changed
    if session is not None and cache_settings != _last_cache_settings:
        logger.info("Cache settings changed, resetting session.")
        reset_session()

    if session is None:
        _last_cache_settings = cache_settings
        kwargs = {
            "backend": cache_settings["backend"],
            "expire_after": cache_settings["expire_after"],
        }

        if cache_settings["backend"] == "redis" and cache_settings["redis_location"]:
            try:
                # These imports are here to avoid a hard dependency on redis
                # if the user doesn't use the redis backend.
                import redis

                kwargs["connection"] = redis.from_url(cache_settings["redis_location"])
                # The connection is lazy, so we need to trigger it to test it.
                # A full 'ping' is too slow, so we just initialize the session
                # and let it fail on first use if it's going to. A try/except
                # here on the constructor would be better, but the connection
                # is lazy. Let's try to connect and fall back if it fails.
                temp_session = requests_cache.CachedSession(
                    "weather_cache_test_connection", **kwargs
                )
                temp_session.cache.get_response(
                    "test"
                )  # dummy call to force connection
                session = temp_session

            except (ImportError, Exception) as e:
                logger.warning(
                    f"Redis connection failed with error: {e}. "
                    "Falling back to in-memory cache for this session."
                )
                kwargs.pop("connection", None)
                kwargs["backend"] = "memory"
                session = requests_cache.CachedSession("weather_cache", **kwargs)
        else:
            session = requests_cache.CachedSession("weather_cache", **kwargs)

    return session


def _get_aurora_df(lat, lon, local_timezone) -> pd.DataFrame:
    """
    Fetches aurora forecast data from NOAA and returns it as a pandas DataFrame.
    """
    url = "https://services.swpc.noaa.gov/json/ovation_aurora_latest.json"
    logger.debug("Download aurora data from: {}".format(url))
    try:
        with get_session().get(url) as data:
            data.raise_for_status()
            json_data = json.loads(data.text)
            if "coordinates" not in json_data:
                logger.error(
                    f"KeyError 'coordinates' in aurora data. Full response: {json_data}"
                )
                return pd.DataFrame(columns=pd.Index(["time", "aurora"]))

            df = pd.DataFrame(
                json_data["coordinates"], columns=pd.Index(["lon", "lat", "aurora"])
            )
            df["dist"] = (df["lat"] - lat) ** 2 + (df["lon"] - lon) ** 2
            closest = df.loc[df["dist"].idxmin()]
            aurora_val = closest["aurora"]

            aurora_df = pd.DataFrame(
                [[json_data["Forecast Time"], aurora_val]],
                columns=pd.Index(["time", "aurora"]),
            )
            aurora_df["time"] = pd.to_datetime(aurora_df["time"]).dt.tz_convert(
                local_timezone
            )
            return aurora_df
    except (
        requests_cache.requests.exceptions.RequestException,
        json.JSONDecodeError,
    ) as e:
        logger.error(f"Failed to download or parse aurora data: {e}")
        return pd.DataFrame(columns=pd.Index(["time", "aurora"]))


class WeatherProvider(ABC):
    REQUIRED_COLUMNS = [
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
        "moonIllumination",
        "moonWaxing",
        "aurora",
    ]

    def __init__(self, api_key, lat, lon, local_timezone):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.local_timezone = local_timezone

    def _log_download_url(self, url):
        logger.debug("Download weather from: {}".format(mask_text(url, self.api_key)))

    def _log_download_error(self, e, data_text):
        error_msg = mask_text(e, self.api_key)
        masked_response = mask_text(data_text, self.api_key)
        logger.error(
            f"Error downloading or parsing weather data: {error_msg}. Full response: {masked_response}"
        )

    @abstractmethod
    def download_data(
        self,
        hours: int = 48,
        conditions: Optional[Any] = None,
        observation_window: Optional[Tuple[datetime, datetime]] = None,
        force: bool = False,
    ) -> pd.DataFrame:
        pass

    def _empty_df(self) -> pd.DataFrame:
        """
        Returns an empty DataFrame with the required columns.
        """
        return pd.DataFrame(columns=pd.Index(self.REQUIRED_COLUMNS))

    def _enrich_with_aurora_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Enriches the weather data with aurora forecast data.
        """
        aurora_df = _get_aurora_df(self.lat, self.lon, self.local_timezone)
        if not aurora_df.empty:
            aurora_df["time"] = aurora_df["time"].astype(df["time"].dtype)
            df = pd.merge_asof(
                df.sort_values("time"),
                aurora_df.sort_values("time"),
                on="time",
                direction="nearest",
            )
            df["aurora"] = df["aurora"].ffill().bfill()
        return df


class PirateWeather(WeatherProvider):
    API_URL = "https://api.pirateweather.net/forecast/{apikey}/{lat},{lon}?units=si"

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
            with get_session().get(url) as data:
                logger.debug(f"Data {data}")
                data.raise_for_status()
                json_data = json.loads(data.text)

            columns = [
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
            if "hourly" in json_data and "data" in json_data["hourly"]:
                raw_data = [
                    [
                        (item[column] if column in item.keys() else "none")
                        for column in columns
                    ]
                    for item in json_data["hourly"]["data"]
                ]
            else:
                logger.error(
                    f"Missing 'hourly.data' in weather data. Full response: {json_data}"
                )
                return self._empty_df()
            result = pd.DataFrame(raw_data, columns=pd.Index(columns))
            # Convert units
            result["precipProbability"] *= 100
            result["cloudCover"] *= 100
            result["visibility"] = pd.to_numeric(result["visibility"], errors="coerce")
            result["fog"] = (10 - result["visibility"].clip(0, 10)) * 10  # Fog in [%]
            result.time = (
                result.time.astype("datetime64[s]")
                .dt.tz_localize("UTC")
                .dt.tz_convert(self.local_timezone)
            )
            # Filter by hours
            cutoff = datetime.now(timezone.utc) + timedelta(hours=hours)
            result = cast(
                pd.DataFrame,
                result[result.time <= cutoff.astimezone(self.local_timezone)],
            )
            return self._enrich_with_aurora_data(result)
        except Exception as e:
            self._log_download_error(e, data.text if data is not None else "")
            return self._empty_df()


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
            with get_session().get(url) as data:
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
            with get_session().get(url, headers=headers) as data:
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

        good_hours = 0
        for _, row in df_window.iterrows():
            is_good = True
            # Check clouds
            if (
                is_good
                and "cloudCover" in row
                and pd.notna(row.cloudCover)
                and row.cloudCover != "none"
            ):
                if float(row.cloudCover) >= conditions.max_clouds:
                    is_good = False
            # Check visibility
            if (
                is_good
                and "visibility" in row
                and pd.notna(row.visibility)
                and row.visibility != "none"
            ):
                if float(row.visibility) <= conditions.min_visibility:
                    is_good = False
            # Check fog
            if (
                is_good
                and "fog" in row
                and pd.notna(row.fog)
                and row.fog != "none"
            ):
                if float(row.fog) >= conditions.max_fog:
                    is_good = False
            # Check precipitation
            if (
                is_good
                and "precipProbability" in row
                and pd.notna(row.precipProbability)
                and row.precipProbability != "none"
            ):
                if (
                    float(row.precipProbability)
                    >= conditions.max_precipitation_probability
                ):
                    is_good = False
            if (
                is_good
                and "precipIntensity" in row
                and pd.notna(row.precipIntensity)
                and row.precipIntensity != "none"
            ):
                if float(row.precipIntensity) >= conditions.max_precipitation_intensity:
                    is_good = False
            # Check wind
            if (
                is_good
                and "windSpeed" in row
                and pd.notna(row.windSpeed)
                and row.windSpeed != "none"
            ):
                if float(row.windSpeed) >= conditions.max_wind:
                    is_good = False
            # Check temperature
            if (
                is_good
                and "temperature" in row
                and pd.notna(row.temperature)
                and row.temperature != "none"
            ):
                temp = float(row.temperature)
                if (
                    temp <= conditions.min_temperature
                    or temp >= conditions.max_temperature
                ):
                    is_good = False

            if is_good:
                good_hours += 1

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
            with get_session().get(url_clouds) as resp_clouds:
                resp_clouds.raise_for_status()
                df = self._parse_meteoblue_response(resp_clouds.text)
        except Exception as e:
            self._log_download_error(
                e, resp_basic.text if resp_basic is not None else ""
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
            with get_session().get(url_basic) as resp_basic:
                resp_basic.raise_for_status()
                df_basic = self._parse_meteoblue_response(resp_basic.text)
                if not df_basic.empty:
                    # Merge with cloud data
                    df = pd.merge(df, df_basic, on="time", suffixes=("", "_basic"))
        except Exception as e:
            self._log_download_error(
                e, resp_clouds.text if resp_clouds is not None else ""
            )
            # Continue with basic data only if clouds fetch fails

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
            with get_session().get(url) as data:
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
