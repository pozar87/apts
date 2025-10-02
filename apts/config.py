import configparser
import logging
import os

logger = logging.getLogger(__name__)

# Init config
config = configparser.ConfigParser()

# Define potential config file locations
example_config = "./examples/apts.ini"  # Relative to project root if run from there
user_config = os.path.expanduser("~/.config/apts/apts.ini")
candidates = [example_config, user_config]

# Read configurations
logger.debug(f"Attempting to load configuration from candidates: {candidates}")
found_configs = config.read(candidates)

if not found_configs:
    logger.warning(f"No configuration file found. Looked in: {candidates}")
else:
    logger.info(f"Loaded configuration from: {found_configs}")
    # Also log the content of the weather section if it exists
    if config.has_section('weather'):
        logger.debug(f"Content of [weather] section: {dict(config.items('weather'))}")
    else:
        logger.debug("No [weather] section found in loaded configuration.")

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
        options = config.options('events')
        if options:
            for option in options:
                event_settings[option] = config.getboolean('events', option)  # pyright: ignore
    return event_settings


def get_weather_settings(provider: str = None) -> tuple[str, str]:
    """
    Reads the weather settings from the [weather] section.

    Returns:
        tuple: A tuple containing the provider name and the API key.
    """
    logger.debug(f"Inside get_weather_settings. Provider: {provider}")
    api_key = ""  # Initialize api_key to an empty string

    if config.has_section('weather'):
        if provider is None:
            # Try to get default provider from config
            configured_provider = config.get('weather', 'provider', fallback='pirateweather')
            # Then try to get API key for that configured provider
            api_key = config.get('weather', f'{configured_provider}_api_key', fallback="")
            provider = configured_provider  # Update provider to the configured one
        else:
            # Get API key for specific provider passed as argument
            api_key = config.get('weather', f'{provider}_api_key', fallback="")
    else:
        # No weather section, return defaults
        if provider is None:
            provider = 'pirateweather'  # Default provider if no config section

    logger.debug(f"get_weather_settings returning provider: {provider}, api_key: {api_key}")
    return provider, api_key


def get_minor_planet_settings() -> list[str]:
    """
    Reads the minor planet settings from the [minor_planets] section.
    The setting should be a comma-separated list of packed designations.

    Returns:
        list: A list of minor planet packed designations to load.
    """
    if config.has_option('minor_planets', 'load_only'):
        planets_str = config.get('minor_planets', 'load_only')
        if planets_str:
            return [p.strip() for p in planets_str.split(',')]
    return []
