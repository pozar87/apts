import logging.config
from typing import Any

from . import cache
from .cache import download_all_data

# Import the config object from the new config module
from .config import config, should_auto_preload_data, should_preload_essential_only
from .constants.event_types import EventType
from .equipment import Equipment
from .i18n import set_language
from .notify import Notify
from .observations import Observation
from .place import Place
from .utils import Utils
from .weather import Weather

__all__ = [
    "Catalogs",
    "Equipment",
    "Observation",
    "Place",
    "Utils",
    "EventType",
    "Notify",
    "Weather",
    "catalogs",
    "preload_data",
    "preload_essential_data",
    "set_language",
    "download_all_data",
]

logger = logging.getLogger(__name__)

# Global objects that are lazy-loaded
_pd = None
_sns = None
_catalogs = None


def __getattr__(name: str) -> Any:
    global _pd, _sns, _catalogs
    if name == "pd":
        if _pd is None:
            import pandas as pd

            # Disable label trimming in pandas tables
            pd.set_option("display.max_colwidth", None)
            _pd = pd
        return _pd
    if name == "sns":
        if _sns is None:
            import seaborn as sns

            _sns = sns
        return _sns
    if name == "catalogs":
        if _catalogs is None:
            from .catalogs import Catalogs
            _catalogs = Catalogs()
        return _catalogs
    raise AttributeError(f"module {__name__} has no attribute {name}")


def preload_data():
    """
    Optionally preload expensive astronomical data for faster subsequent operations.

    This function loads:
    - Timescale data
    - Ephemeris data (planetary positions)
    - Minor Planet Center orbit data

    Call this function once at application startup if you want to frontload
    the initialization cost. Otherwise, data will be loaded lazily as needed.
    """
    logger.info("Preloading ephemeris and other data...")
    cache.get_timescale()
    cache.get_ephemeris()
    cache.get_mpcorb_data()
    logger.info("Data preloading complete.")


def preload_essential_data():
    """
    Preload only the most essential data for basic operations.
    This is faster than preload_data() but still provides some performance benefit.
    """
    logger.info("Preloading essential astronomical data...")
    cache.get_timescale()
    logger.info("Essential data preloading complete.")


# Conditional preloading based on configuration
if should_auto_preload_data():
    if should_preload_essential_only():
        preload_essential_data()
    else:
        preload_data()


__version__ = "0.14.5"
