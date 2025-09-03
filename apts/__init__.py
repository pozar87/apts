import logging.config
from typing import Literal
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
from .constants.event_types import EventType

__all__ = ["Catalogs", "Equipment", "Observation", "Place", "Utils", "EventType", "Notify", "Weather"]

logger = logging.getLogger(__name__)

# The logging level is already set to DEBUG above.
# This block can be removed or commented out if it's causing issues,
# but for now, we'll keep it as is, as the basicConfig call above takes precedence.
# log_level_str = config.get("logging", "level", fallback="INFO")  # Default to INFO
# try:
#     log_level = getattr(logging, log_level_str.upper())
#     # Basic logging configuration for the library
#     logging.basicConfig(
#         level=log_level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#     )
#     logger.info(f"Logging level set to {log_level_str}")
# except AttributeError:
#     logging.basicConfig(level=logging.INFO)  # Fallback level
#     logger.warning(
#         f"Invalid logging level '{log_level_str}' in config. Using INFO level."
#     )

# Load static fields from the imported config
# Weather API Key (handled directly by Weather class and config.get_weather_settings)

# Note: Notification settings are handled within the Notify class using the imported config.

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

__version__ = "0.7.3"
