import os
import shutil
import configparser

from .equipment import Equipment
from .observations import Observation
from .place import Place
from .weather import Weather
from .notify import Notify
from .catalogs import Catalogs
from .utils import Utils

# Default values for configuration values
DEFAULTS = {
    'weather': {
        'api_key': 'unknown',
        'api_url': 'unknown'
    },
    'notification': {
        'email_address': 'unknown',
        'email_password': 'unknown'
    }
}

# Init config with default values
config = configparser.SafeConfigParser(DEFAULTS)

# Read users configuration
user_config = os.path.expanduser("~") + "/.config/apts/apts.ini"
config.read(user_config)

# Load static fields from config
Weather.API_KEY = config['weather']['api_key']
Weather.API_URL = config['weather']['api_url']
Notify.EMAIL_ADDRESS = config['notification']['email_address']
Notify.EMAIL_PASSWORD = config['notification']['email_password']

__version__ = '0.2.9'
