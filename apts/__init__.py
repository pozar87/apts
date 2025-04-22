import configparser
import os
import logging.config

import pandas as pd
import seaborn as sns

from .catalogs import Catalogs
from .equipment import Equipment
from .notify import Notify
from .observations import Observation
from .place import Place
from .utils import Utils
from .weather import Weather

__all__ = ["Catalogs", "Equipment", "Observation", "Place", "Utils"]

logger = logging.getLogger(__name__)

# Init config
config = configparser.ConfigParser()

# Read configurations
example_config = "./examples/apts.ini"
user_config = os.path.expanduser("~") + "/.config/apts/apts.ini"
candidates = [example_config, user_config]
config.read(candidates)

# Set logging level from config
log_level = config.get("logging", "level", fallback="DEBUG")
try:
    logger.setLevel(getattr(logging, log_level.upper()))
except AttributeError:
    logger.setLevel(logging.DEBUG)
    logger.warning(f"Invalid logging level '{log_level}' in config. Using DEBUG level.")

# Load static fields from config
# Weather API Key
setattr(Weather, "API_KEY", config.get("weather", "api_key", fallback=""))

# Note: Notification settings (SMTP host, port, user, pass, recipient, TLS)
# are now read directly from the config when instantiating the Notify class,
# rather than being set as class attributes here.

# Seaborn style
sns.set_style(
    "whitegrid"
    if config.get("style", "seaborn", fallback="whitegrid") == "whitegrid"
    else "white"
)
# Disable label trimming in pandas tables
pd.set_option("display.max_colwidth", None)

__version__ = "0.4.3"
