import requests
from datetime import datetime


class NasaAPI:
    def __init__(self, api_key="DEMO_KEY"):
        self.api_key = api_key
        self.base_url = "https://api.nasa.gov/neo/rest/v1/feed"

    def get_comets(self, start_date: datetime, end_date: datetime):
        params = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "api_key": self.api_key,
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()
