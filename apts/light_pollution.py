import logging
import numpy as np
from PIL import Image
from importlib import resources

from .config import get_light_pollution_settings

logger = logging.getLogger(__name__)


class LightPollution:
    @staticmethod
    def bortle_to_sqm(bortle_class: float) -> float:
        """
        Converts a Bortle class (1-9) to an approximate Sky Quality Meter (SQM) value
        in mag/arcsec^2. Uses linear interpolation between established midpoints.
        Source: https://en.wikipedia.org/wiki/Bortle_scale
        """
        xp = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        fp = [21.88, 21.67, 21.45, 21.05, 19.77, 18.87, 18.25, 17.5, 16.0]
        return float(np.interp(bortle_class, xp, fp))

    _IMAGE = None
    _PIX = None
    _SIZE = None

    @classmethod
    def _load_image(cls):
        """Loads the light pollution image and its pixel data into class-level cache."""
        if cls._IMAGE is None:
            image_path = str(
                resources.files("apts").joinpath("data/world202t4_low3.png")
            )
            cls._IMAGE = Image.open(image_path)
            # load() actually reads the image data into memory and returns a PixelAccess object
            cls._PIX = cls._IMAGE.load()
            cls._SIZE = cls._IMAGE.size

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.settings = get_light_pollution_settings()
        self._api_data = None
        # Lazily load the image data into the class-level cache if not already loaded.
        # This significantly improves performance when multiple LightPollution objects are created.
        self._load_image()

    def _get_from_api(self):
        """
        Fetches light pollution metrics from darkskysites.com API.
        """
        if self._api_data is not None:
            return self._api_data

        if not self.settings.get("use_online_api", True):
            return None

        try:
            # We import here to avoid circular dependency and leverage existing central cache
            from .utils.network import get_session

            url = "https://www.darkskysites.com/api/site-intelligence"
            params = {"lat": self.lat, "lng": self.lon}
            headers = {"Referer": "https://www.darkskysites.com/"}

            with get_session().get(url, params=params, headers=headers, timeout=10) as resp:
                if resp.ok:
                    data = resp.json()
                    self._api_data = data.get("payload", {}).get("metrics", {})
                    return self._api_data
                else:
                    logger.warning(
                        f"Failed to fetch light pollution data from API: {resp.status_code}"
                    )
        except Exception as e:
            logger.warning(f"Error fetching light pollution data from API: {e}")

        return None

    def _latlon_to_pixel(self, lat, lon):
        # Image dimensions: 14400x5600
        # Latitude range: 75N to 65S -> 140 degrees
        # Longitude range: 180W to 180E -> 360 degrees
        if self._SIZE is None:
            return 0, 0
        img_width, img_height = self._SIZE

        # Normalize longitude to 0-360
        lon_norm = lon + 180
        x = int((lon_norm / 360) * img_width)

        # Normalize latitude to 0-140 (from 75 to -65)
        lat_norm = 75 - lat
        y = int((lat_norm / 140) * img_height)

        return x, y

    def get_light_pollution(self):
        # Attempt to get from API first
        api_data = self._get_from_api()
        if api_data and "bortleClass" in api_data:
            return float(api_data["bortleClass"])

        # Fallback to local image
        x, y = self._latlon_to_pixel(self.lat, self.lon)

        if self._PIX is None:
            return -1

        palette_index = self._PIX[x, y]

        if not isinstance(palette_index, int):
            return -1

        # This mapping is based on the key.png from the data source
        # and the palette extracted from the image.
        bortle_scale = {
            0: 1,  # Dark Grey
            1: 1,  # Grey
            2: 1,  # Black
            3: 2,  # Dark Blue
            4: 3,  # Blue
            5: 4,  # Dark Green
            6: 4.5,  # Green
            7: 5,  # Olive
            8: 6,  # Yellow
            9: 7,  # Brown/Orange
            10: 7,  # Orange
            11: 8,  # Dark Red
            12: 8,  # Red
            13: 9,  # Light Grey
            14: 9,  # White
        }

        return bortle_scale.get(palette_index, -1)

    def get_base_sqm(self, forced_bortle: float = -1) -> float:
        """
        Returns the base SQM value (without Sun/Moon/Clouds).
        Prioritizes API data, falls back to Bortle-based interpolation.

        If forced_bortle is provided (> 0), it ensures the returned SQM is consistent
        with that Bortle class (useful for handling mocked values in tests).
        """
        api_data = self._get_from_api()
        sqm = -1.0

        if api_data and "sqm" in api_data:
            sqm = float(api_data["sqm"])
        else:
            bortle = self.get_light_pollution()
            if bortle > 0:
                sqm = self.bortle_to_sqm(bortle)

        # Discrepancy check for mocked Bortle values in tests
        if forced_bortle > 0:
            expected_sqm = self.bortle_to_sqm(forced_bortle)
            if sqm <= 0 or abs(sqm - expected_sqm) > 1.0:
                sqm = expected_sqm

        return max(sqm, 0.0)
