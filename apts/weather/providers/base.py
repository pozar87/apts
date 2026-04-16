import json
import logging
from abc import ABC, abstractmethod
from datetime import datetime, timedelta, timezone
from typing import Any, Optional, Tuple, cast

import pandas as pd
import requests_cache

from apts.config import get_cache_settings
from apts.secrets import mask_text

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
                import redis  # type: ignore

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
                error_msg = mask_text(str(e), cache_settings["redis_location"])
                logger.warning(
                    f"Redis connection failed with error: {error_msg}. "
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
        with get_session().get(url, timeout=10) as data:
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
        "seeing",
        "sqm",
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
