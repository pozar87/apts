import logging.config
import pandas as pd
import seaborn as sns

# Import the config object from the new config module
from .config import config

from .catalogs import Catalogs
from .equipment import Equipment
from .notify import Notify
from .observations import Observation
from .place import Place
from .utils import Utils
from .weather import Weather

__all__ = ["Catalogs", "Equipment", "Observation", "Place", "Utils"]

logger = logging.getLogger(__name__)

# Set logging level from the imported config
log_level_str = config.get("logging", "level", fallback="INFO")  # Default to INFO
try:
    log_level = getattr(logging, log_level_str.upper())
    # Basic logging configuration for the library
    logging.basicConfig(
        level=log_level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    logger.info(f"Logging level set to {log_level_str}")
except AttributeError:
    logging.basicConfig(level=logging.INFO)  # Fallback level
    logger.warning(
        f"Invalid logging level '{log_level_str}' in config. Using INFO level."
    )

# Load static fields from the imported config
# Weather API Key
weather_api_key = config.get("weather", "api_key", fallback="")
if weather_api_key:
    setattr(Weather, "API_KEY", weather_api_key)
else:
    logger.warning(
        "Weather API key not found in configuration. Weather features may fail."
    )

# Note: Notification settings are handled within the Notify class using the imported config.

# Seaborn style from the imported config
seaborn_style = config.get("style", "seaborn", fallback="whitegrid")
try:
    sns.set_style(seaborn_style)
    logger.info(f"Seaborn style set to '{seaborn_style}'")
except ValueError:
    logger.warning(
        f"Invalid seaborn style '{seaborn_style}' in config. Using default 'whitegrid'."
    )
    sns.set_style("whitegrid")


# Disable label trimming in pandas tables
pd.set_option("display.max_colwidth", None)

__version__ = "0.5.6"
