import logging.config
from typing import Any

from . import cache
from .cache import download_all_data
from .catalogs import Catalogs

# Import the config object from the new config module
from .config import config, should_auto_preload_data, should_preload_essential_only
from .constants.event_types import EventType

logger = logging.getLogger(__name__)

# Global objects that are lazy-loaded
_pd = None
_sns = None
_Observation = None
_Place = None
_Equipment = None
_Weather = None
_Utils = None
_Notify = None
_set_language = None


def __getattr__(name: str) -> Any:
    global _pd, _sns, _Observation, _Place, _Equipment, _Weather, _Utils, _Notify, _set_language
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
    if name == "Observation":
        if _Observation is None:
            from .observations import Observation

            _Observation = Observation
        return _Observation
    if name == "Place":
        if _Place is None:
            from .place import Place

            _Place = Place
        return _Place
    if name == "Equipment":
        if _Equipment is None:
            from .equipment import Equipment

            _Equipment = Equipment
        return _Equipment
    if name == "Weather":
        if _Weather is None:
            from .weather import Weather

            _Weather = Weather
        return _Weather
    if name == "Utils":
        if _Utils is None:
            from .utils import Utils

            _Utils = Utils
        return _Utils
    if name == "Notify":
        if _Notify is None:
            from .notify import Notify

            _Notify = Notify
        return _Notify
    if name == "set_language":
        if _set_language is None:
            from .i18n import set_language

            _set_language = set_language
        return _set_language

    raise AttributeError(f"module {__name__} has no attribute {name}")


# Initialize catalogs eagerly as an instance of Catalogs
# This maintains the original public API where 'apts.catalogs' is the Catalogs instance.
catalogs = Catalogs()

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
