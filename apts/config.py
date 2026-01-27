import configparser
import logging
import os
from typing import Optional

logger = logging.getLogger(__name__)

# Init config
config = configparser.ConfigParser()

# Define potential config file locations (can be modified at runtime)
config_paths = [
    "./examples/apts.ini",  # Relative to project root if run from there
    os.path.expanduser("~/.config/apts/apts.ini"),
]


def load_config():
    """
    Load configuration from the defined config paths.
    This function can be called multiple times to reload configuration.
    """
    # Clear existing configuration
    config.clear()

    # Read configurations
    logger.debug(f"Attempting to load configuration from candidates: {config_paths}")
    found_configs = config.read(config_paths)

    if not found_configs:
        logger.warning(f"No configuration file found. Looked in: {config_paths}")
    else:
        logger.info(f"Loaded configuration from: {found_configs}")
        # Also log the content of the weather section if it exists
        if config.has_section("weather"):
            logger.debug(
                f"Content of [weather] section: {dict(config.items('weather'))}"
            )
        else:
            logger.debug("No [weather] section found in loaded configuration.")

    # Ensure [Display] section and dark_mode option exist with a default value
    if not config.has_section("Display"):
        config.add_section("Display")
    if not config.has_option("Display", "dark_mode"):
        config.set("Display", "dark_mode", "false")


def add_config_path(path, priority=False):
    """
    Add a new configuration file path.

    Args:
        path (str): Path to the configuration file
        priority (bool): If True, insert at the beginning (highest priority)
    """
    if priority:
        config_paths.insert(0, path)
    else:
        config_paths.append(path)


def remove_config_path(path):
    """
    Remove a configuration file path.

    Args:
        path (str): Path to remove from the config paths list
    """
    if path in config_paths:
        config_paths.remove(path)


def get_dark_mode() -> bool:
    """
    Reads the dark_mode setting from the [Display] section.

    Returns:
        bool: The value of dark_mode, or False if not found.
    """
    try:
        return config.getboolean("Display", "dark_mode")
    except (configparser.NoSectionError, configparser.NoOptionError):
        logger.warning(
            "No 'dark_mode' option found in section [Display]. Defaulting to False."
        )
        return False


def get_plot_format() -> str:
    """
    Reads the plot_format setting from the [Display] section.

    Returns:
        str: The value of plot_format, or "png" if not found.
    """
    return config.get("Display", "plot_format", fallback="png")


def get_event_settings() -> dict:
    """
    Reads the event settings from the [events] section.

    Returns:
        dict: A dictionary of event types and their enabled/disabled status.
    """
    event_settings = {}
    if config.has_section("events"):
        options = config.options("events")
        if options:
            for option in options:
                event_settings[option] = config.getboolean("events", option)  # pyright: ignore
    return event_settings


def get_weather_settings(provider: Optional[str] = None) -> tuple[str, str]:
    """
    Reads the weather settings from the [weather] section.

    Returns:
        tuple: A tuple containing the provider name and the API key.
    """
    logger.debug(f"Inside get_weather_settings. Provider: {provider}")
    api_key = ""  # Initialize api_key to an empty string

    if config.has_section("weather"):
        if provider is None:
            # Try to get default provider from config
            configured_provider = config.get(
                "weather", "provider", fallback="pirateweather"
            )
            # Then try to get API key for that configured provider
            api_key = config.get(
                "weather", f"{configured_provider}_api_key", fallback=""
            )
            provider = configured_provider  # Update provider to the configured one
        else:
            # Get API key for specific provider passed as argument
            api_key = config.get("weather", f"{provider}_api_key", fallback="")
    else:
        # No weather section, return defaults
        if provider is None:
            provider = "pirateweather"  # Default provider if no config section

    logger.debug(
        f"get_weather_settings returning provider: {provider}, api_key: {api_key}"
    )
    return provider, api_key


def get_minor_planet_settings() -> list[str]:
    """
    Reads the minor planet settings from the [minor_planets] section.
    The setting should be a comma-separated list of packed designations.

    Returns:
        list: A list of minor planet packed designations to load.
    """
    if config.has_option("minor_planets", "load_only"):
        planets_str = config.get("minor_planets", "load_only")
        if planets_str:
            return [p.strip() for p in planets_str.split(",")]
    return []


def get_cache_settings() -> dict:
    """
    Reads the cache settings from the [cache] section.

    Returns:
        dict: A dictionary of cache-related settings.
    """
    cache_settings = {
        "backend": "memory",
        "expire_after": 300,
        "redis_location": None,
    }

    if config.has_section("cache"):
        if config.has_option("cache", "backend"):
            cache_settings["backend"] = config.get("cache", "backend")
        if config.has_option("cache", "expire_after"):
            cache_settings["expire_after"] = config.getint("cache", "expire_after")
        if config.has_option("cache", "redis_location"):
            cache_settings["redis_location"] = config.get("cache", "redis_location")

    return cache_settings


def set_redis_location(redis_location: str):
    """
    Overrides the redis location for the cache.
    """

    if not config.has_section("cache"):
        config.add_section("cache")
    config.set("cache", "redis_location", redis_location)
    config.set("cache", "backend", "redis")


def get_data_settings() -> str:
    """
    Reads the data settings from the [data] section.

    Returns:
        str: The data mode ('light' or 'full').
    """
    return config.get("data", "mode", fallback="light")


def get_performance_settings() -> dict:
    """
    Reads performance settings from the [performance] section.

    Returns:
        dict: A dictionary of performance-related settings.
    """
    performance_settings = {
        "auto_preload_data": False,  # Default to no auto-preloading for faster imports
        "preload_essential_only": False,
        "lazy_loading": True,
        "cache_size": 128,
    }

    if config.has_section("performance"):
        if config.has_option("performance", "auto_preload_data"):
            performance_settings["auto_preload_data"] = config.getboolean(
                "performance", "auto_preload_data"
            )
        if config.has_option("performance", "preload_essential_only"):
            performance_settings["preload_essential_only"] = config.getboolean(
                "performance", "preload_essential_only"
            )
        if config.has_option("performance", "lazy_loading"):
            performance_settings["lazy_loading"] = config.getboolean(
                "performance", "lazy_loading"
            )
        if config.has_option("performance", "cache_size"):
            performance_settings["cache_size"] = config.getint(
                "performance", "cache_size"
            )

    return performance_settings


def should_auto_preload_data() -> bool:
    """
    Check if data should be automatically preloaded at import time.

    Returns:
        bool: True if data should be preloaded automatically, False otherwise.
    """
    settings = get_performance_settings()
    return settings.get("auto_preload_data", False)


def should_preload_essential_only() -> bool:
    """
    Check if only essential data should be preloaded.

    Returns:
        bool: True if only essential data should be preloaded, False for full preloading.
    """
    settings = get_performance_settings()
    return settings.get("preload_essential_only", False)


# Load initial configuration
load_config()


def get_api_key(service: str) -> str:
    """
    Reads the API key for a given service from the [api_keys] section.

    Args:
        service (str): The name of the service (e.g., 'nasa').

    Returns:
        str: The API key, or an empty string if not found.
    """
    return config.get("api_keys", f"{service}_api_key", fallback="")
