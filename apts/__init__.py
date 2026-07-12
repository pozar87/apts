import logging.config
from typing import TYPE_CHECKING, Any, Callable, Dict

from . import cache
from .cache import download_all_data
from .catalogs import Catalogs

# Import the config object from the new config module
from .config import config, should_auto_preload_data, should_preload_essential_only
from .constants.event_types import EventType

if TYPE_CHECKING:
    from .equipment import Equipment
    from .i18n import set_language
    from .notify import Notify
    from .observations import Observation
    from .place import Place
    from .utils import Utils
    from .weather import Weather

logger = logging.getLogger(__name__)


def _load_pd():
    import pandas as pd

    # Disable label trimming in pandas tables
    pd.set_option("display.max_colwidth", None)
    return pd


def _load_sns():
    import seaborn as sns

    return sns


def _load_observation():
    from .observations import Observation

    return Observation


def _load_place():
    from .place import Place

    return Place


def _load_equipment():
    from .equipment import Equipment

    return Equipment


def _load_weather():
    from .weather import Weather

    return Weather


def _load_utils():
    from .utils import Utils

    return Utils


def _load_notify():
    from .notify import Notify

    return Notify


def _load_set_language():
    from .i18n import set_language

    return set_language


# Registry of loader functions for lazy-loaded attributes
_LOADERS: Dict[str, Callable[[], Any]] = {
    "pd": _load_pd,
    "sns": _load_sns,
    "Observation": _load_observation,
    "Place": _load_place,
    "Equipment": _load_equipment,
    "Weather": _load_weather,
    "Utils": _load_utils,
    "Notify": _load_notify,
    "set_language": _load_set_language,
}

# Cache for lazy-loaded attributes
_CACHE: Dict[str, Any] = {}


def __getattr__(name: str) -> Any:
    """
    Lazy-load modules and classes when they are first accessed.
    This improves initial import time for the library.
    """
    if name in _LOADERS:
        if name not in _CACHE:
            _CACHE[name] = _LOADERS[name]()
        return _CACHE[name]

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
    "config",
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


__version__ = "0.15.6"
