import configparser
import os

from .catalogs import Catalogs
from .equipment import Equipment
from .notify import Notify
from .observations import Observation
from .place import Place
from .utils import Utils
from .weather import Weather

# Init config
config = configparser.SafeConfigParser()

# Read configurations
example_config = "./examples/apts.ini"
user_config = os.path.expanduser("~") + "/.config/apts/apts.ini"
candidates = [example_config, user_config]
config.read(candidates)

# Load static fields from config
Weather.API_KEY = config['weather']['api_key']
Weather.API_URL = config['weather']['api_url']
Notify.EMAIL_ADDRESS = config['notification']['email_address']
Notify.EMAIL_PASSWORD = config['notification']['email_password']

__version__ = '0.2.17'
