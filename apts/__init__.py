import logging.config
from typing import Literal
import pandas as pd
import seaborn as sns

# Import the config object from the new config module
from .config import config

from .catalogs import Catalogs, initialize_catalogs
from .equipment import Equipment
from .notify import Notify
from .observations import Observation
from .place import Place
from .utils import Utils
from .weather import Weather
from .constants.event_types import EventType

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


__version__ = "0.7.5"
