import json
import logging
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Optional, Tuple

import numpy as np
import pandas as pd
import requests

from apts.secrets import mask_text
from apts.utils.network import get_session

logger = logging.getLogger(__name__)


def _get_aurora_df(lat, lon, local_timezone) -> pd.DataFrame:
    """
    Fetches aurora forecast data from NOAA and returns it as a pandas DataFrame.
    """
    url = "https://services.swpc.noaa.gov/json/ovation_aurora_latest.json"
    logger.debug("Download aurora data from: {}".format(url))
    try:
        with get_session().get(url, timeout=10) as data:
            data.raise_for_status()
            # Optimization: use .json() which might be cached/optimized in some session handlers
            json_data = data.json()
            if "coordinates" not in json_data:
                logger.error(
                    f"KeyError 'coordinates' in aurora data. Full response: {json_data}"
                )
                return pd.DataFrame(columns=pd.Index(["time", "aurora"]))

            # Optimization: Use NumPy for the 64,800-point coordinate search.
            # Creating a full DataFrame for this temporary calculation is expensive.
            coords = np.array(json_data["coordinates"])
            # coords is [lon, lat, aurora]
            lons = coords[:, 0]
            lats = coords[:, 1]
            vals = coords[:, 2]

            # Simple Euclidean distance squared (same as previous logic)
            dists_sq = (lats - lat) ** 2 + (lons - lon) ** 2
            closest_idx = np.argmin(dists_sq)
            aurora_val = vals[closest_idx]

            aurora_df = pd.DataFrame(
                [[json_data["Forecast Time"], aurora_val]],
                columns=pd.Index(["time", "aurora"]),
            )
            aurora_df["time"] = pd.to_datetime(aurora_df["time"]).dt.tz_convert(
                local_timezone
            )
            return aurora_df
    except (
        requests.exceptions.RequestException,
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
            # Optimization: Since aurora_df currently only contains a single global
            # forecast point, we can avoid the expensive merge_asof and sorting.
            # This provides a significant speedup for large weather DataFrames.
            df["aurora"] = aurora_df["aurora"].iloc[0]
        return df
