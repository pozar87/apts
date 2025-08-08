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

def get_event_settings() -> dict:
    """
    Reads the event settings from the [events] section.

    Returns:
        dict: A dictionary of event types and their enabled/disabled status.
    """
    event_settings = {}
    if config.has_section('events'):
        for option in config.options('events'):
            event_settings[option] = config.getboolean('events', option)
    return event_settings


def get_weather_settings() -> tuple[str, str]:
    """
    Reads the weather settings from the [weather] section.

    Returns:
        tuple: A tuple containing the provider name and the API key.
    """
    provider = 'pirateweather'
    api_key = '12345'  # Default dummy key

    if config.has_section('weather'):
        if config.has_option('weather', 'provider'):
            provider = config.get('weather', 'provider')
        if config.has_option('weather', 'api_key'):
            api_key = config.get('weather', 'api_key')

    return provider, api_key
