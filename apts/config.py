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

# Ensure [Display] section and dark_mode option exist with a default value
if not config.has_section('Display'):
    config.add_section('Display')
if not config.has_option('Display', 'dark_mode'):
    config.set('Display', 'dark_mode', 'false')


# Optional: Helper function for safer config access (can be added if needed)
# def get_config_value(section, option, fallback=None, value_type=str): ...

def get_dark_mode() -> bool:
    """
    Reads the dark_mode setting from the [Display] section.

    Returns:
        bool: The value of dark_mode, or False if not found.
    """
    try:
        return config.getboolean('Display', 'dark_mode')
    except (configparser.NoSectionError, configparser.NoOptionError):
        logger.warning(
            "No 'dark_mode' option found in section [Display]. "
            "Defaulting to False."
        )
        return False
