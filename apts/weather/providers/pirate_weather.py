import json
import logging
from datetime import datetime, timedelta, timezone
from typing import Any, Optional, Tuple, cast

import pandas as pd

from . import base
from .base import WeatherProvider

logger = logging.getLogger(__name__)


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
            with base.get_session().get(url, timeout=10) as data:
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
