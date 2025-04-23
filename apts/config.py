import configparser
import os
import logging

logger = logging.getLogger(__name__)

# Init config
config = configparser.ConfigParser()

# Define potential config file locations
example_config = "./examples/apts.ini"  # Relative to project root if run from there
user_config = os.path.expanduser("~/.config/apts/apts.ini")
candidates = [example_config, user_config]

# Read configurations
found_configs = config.read(candidates)

if not found_configs:
    logger.warning(f"No configuration file found. Looked in: {candidates}")
else:
    logger.info(f"Loaded configuration from: {found_configs}")

# Optional: Helper function for safer config access (can be added if needed)
# def get_config_value(section, option, fallback=None, value_type=str): ...
