import logging
from ..utils.network import get_session

logger = logging.getLogger(__name__)


def get_elevation(lat: float, lon: float) -> float | None:
    """
    Fetches elevation for a given latitude and longitude using the Open-Meteo Elevation API.
    Returns elevation in meters or None if fetching fails.
    """
    url = "https://api.open-meteo.com/v1/elevation"
    params = {"latitude": lat, "longitude": lon}
    try:
        with get_session().get(url, params=params, timeout=10) as resp:
            if resp.ok:
                data = resp.json()
                elevation_list = data.get("elevation", [])
                if elevation_list:
                    elevation = float(elevation_list[0])
                    logger.debug(f"Fetched elevation {elevation} for {lat}, {lon}")
                    return elevation
            else:
                logger.warning(
                    f"Failed to fetch elevation from API: {resp.status_code}"
                )
    except Exception as e:
        logger.warning(f"Error fetching elevation from API: {e}")

    return None
