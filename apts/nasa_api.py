import logging
import requests
from datetime import datetime, timedelta

from .secrets import mask_text

logger = logging.getLogger(__name__)


class NasaAPI:
    def __init__(self, api_key="DEMO_KEY"):
        self.api_key = api_key
        self.base_url = "https://api.nasa.gov/neo/rest/v1/feed"

    def get_comets(self, start_date: datetime, end_date: datetime):
        all_data = {}
        current_start = start_date
        while current_start <= end_date:
            current_end = min(current_start + timedelta(days=6), end_date)
            params = {
                "start_date": current_start.strftime("%Y-%m-%d"),
                "end_date": current_end.strftime("%Y-%m-%d"),
                "api_key": self.api_key,
            }
            try:
                response = requests.get(self.base_url, params=params)
                response.raise_for_status()
                data = response.json()
            except Exception as e:
                error_msg = mask_text(str(e), self.api_key)
                logger.error(f"NASA API request failed: {error_msg}")
                raise

            if not all_data:
                all_data = data
            else:
                # Merge the 'near_earth_objects'
                for date_str, objects in data.get("near_earth_objects", {}).items():
                    if date_str in all_data["near_earth_objects"]:
                        all_data["near_earth_objects"][date_str].extend(objects)
                    else:
                        all_data["near_earth_objects"][date_str] = objects

            current_start += timedelta(days=7)

        # Update element_count
        if "near_earth_objects" in all_data:
            total_elements = sum(
                len(v) for v in all_data["near_earth_objects"].values()
            )
            all_data["element_count"] = total_elements

        return all_data
