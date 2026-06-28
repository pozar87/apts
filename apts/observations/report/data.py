import html
import logging
from typing import TYPE_CHECKING, List, Optional

import numpy as np
import pandas as pd

if TYPE_CHECKING:
    from datetime import datetime
    from ...place import Place
    from ...equipment.base import Equipment

from ...utils import Utils

logger = logging.getLogger(__name__)

class ReportDataMixIn:
    if TYPE_CHECKING:
        start: Optional["datetime"]
        stop: Optional["datetime"]
        place: "Place"
        equipment: "Equipment"

        def get_hourly_weather_analysis(self, language: Optional[str] = None) -> List[dict]: ...
        def get_visible_planets(self, language: Optional[str] = None) -> pd.DataFrame: ...
        def get_visible_messier(self, language: Optional[str] = None) -> pd.DataFrame: ...
        def get_visible_ngc(self, language: Optional[str] = None) -> pd.DataFrame: ...

    def _prepare_html_data(self, language: Optional[str] = None) -> dict:
        hourly_weather = self.get_hourly_weather_analysis(language=language)
        # Sanitize hourly_weather contents
        sanitized_hourly_weather = []
        for hour in hourly_weather:
            sanitized_hour = {}
            for k, v in hour.items():
                if isinstance(v, str):
                    sanitized_hour[k] = html.escape(v)
                elif isinstance(v, list):
                    sanitized_hour[k] = [
                        html.escape(item) if isinstance(item, str) else item
                        for item in v
                    ]
                else:
                    sanitized_hour[k] = v
            sanitized_hourly_weather.append(sanitized_hour)

        visible_planets_df = self.get_visible_planets(language=language)
        messier_df = self.get_visible_messier(language=language)
        ngc_df = self.get_visible_ngc(language=language)

        return {
            "title": "APTS",
            "start": Utils.format_date(self.start),
            "stop": Utils.format_date(self.stop),
            "planets_count": len(visible_planets_df),
            "messier_count": len(messier_df),
            "ngc_count": len(ngc_df),
            "planets_table": visible_planets_df.drop(columns=["TechnicalName"]).to_html()
            if "TechnicalName" in visible_planets_df.columns
            else visible_planets_df.to_html(),
            "messier_table": messier_df.to_html(),
            "ngc_table": ngc_df.drop(
                columns=[
                    "ra_hours",
                    "dec_degrees",
                    "skyfield_object",
                    "NGC_norm",
                    "IC_norm",
                    "Name_norm",
                    "Magnitude_float",
                ],
                errors="ignore",
            ).to_html(),
            "equipment_table": self.equipment.data().to_html(),
            "place_name": html.escape(self.place.name),
            "lat": np.rad2deg(self.place.lat),
            "lon": np.rad2deg(self.place.lon),
            "hourly_weather": sanitized_hourly_weather,
            "timezone": html.escape(str(self.place.local_timezone)),
        }
