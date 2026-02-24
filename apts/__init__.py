import logging.config

import pandas as pd
import seaborn as sns

from . import cache
from .cache import download_all_data
from .catalogs import Catalogs, initialize_catalogs

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

# Seaborn style from the imported config
allowed_styles = ["white", "dark", "whitegrid", "darkgrid", "ticks"]
seaborn_style = config.get("style", "seaborn", fallback="whitegrid")
if seaborn_style not in allowed_styles:
    logger.warning(
        f"Invalid seaborn style '{seaborn_style}' in config. Using default 'whitegrid'."
    )
    seaborn_style = "whitegrid"

try:
    sns.set_style(seaborn_style)  # pyright: ignore
    logger.info(f"Seaborn style set to '{seaborn_style}'")
except ValueError:
    # This is a fallback, in case of unexpected issues with seaborn
    logger.warning(
        f"Could not set seaborn style to '{seaborn_style}'. Using default 'whitegrid'."
    )
    sns.set_style("whitegrid")


# Disable label trimming in pandas tables
pd.set_option("display.max_colwidth", None)

# Initialize catalogs
initialize_catalogs()
catalogs = Catalogs()


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


__version__ = "0.10.6"
