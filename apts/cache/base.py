import logging
from skyfield.api import load
from .skyfield import get_timescale, get_ephemeris, get_jovian_ephemeris, STATIONS_URL
from .catalogs import get_hipparcos_data, get_mpcorb_data
from .nasa import get_nasa_comets_data
from .scoring import clear_scoring_cache

logger = logging.getLogger(__name__)

def download_all_data():
    """
    Downloads all the necessary data files.
    """
    get_ephemeris()
    get_hipparcos_data()
    get_mpcorb_data()
    get_jovian_ephemeris()
    get_timescale()
    load.tle_file(STATIONS_URL)


def clear_cache():
    """
    Clears all the caches.
    """
    get_timescale.cache_clear()
    get_ephemeris.cache_clear()
    get_hipparcos_data.cache_clear()
    get_mpcorb_data.cache_clear()
    get_jovian_ephemeris.cache_clear()
    get_nasa_comets_data.cache_clear()
    clear_scoring_cache()
