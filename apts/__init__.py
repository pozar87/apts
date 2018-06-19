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

# Init config
config = configparser.ConfigParser()

# Read configurations
example_config = "./examples/apts.ini"
user_config = os.path.expanduser("~") + "/.config/apts/apts.ini"
candidates = [example_config, user_config]
config.read(candidates)

# Load static fields from config
Weather.API_KEY = config.get('weather', 'api_key', fallback="")
Weather.API_URL = config.get('weather', 'api_url', fallback="")
Notify.EMAIL_ADDRESS = config.get('notification', 'email_address', fallback="")
Notify.EMAIL_PASSWORD = config.get('notification', 'email_password', fallback="")

# Seaborn style
sns.set_style(config.get('style', 'seaborn', fallback='whitegrid'))
# Disable label trimming in pandas tables
pd.set_option('display.max_colwidth', config.getint('style', 'max_colwidth', fallback=-1))

# load the logging configuration
logging_config = os.path.expanduser("~") + "/.config/apts/logging.ini"
logging.config.fileConfig(logging_config)

__version__ = '0.2.24'
