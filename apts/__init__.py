import os
import shutil
import configparser

from .equipment import Equipment
from .observations import Place, Observation
from .weather import Weather
from .notify import Notify
from .catalog import Catalog
from .utils import Utils

user_config = os.path.expanduser("~") + "/.config/apts/apts.ini"

config = configparser.ConfigParser()
config.read(user_config)

# Load static fields from config
Weather.API_KEY = config['weather']['api_key']
Weather.API_URL = config['weather']['api_url']
Notify.EMAIL_ADDRESS = config['notification']['email_address']
Notify.EMAIL_PASSWORD = config['notification']['email_password']

__version__ = '0.2.1'
