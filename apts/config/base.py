import configparser
import logging
import os

from ..secrets import mask_secret

# Initialize logger with the same name as before to maintain compatibility with tests
logger = logging.getLogger("apts.config")

# Init config
config = configparser.ConfigParser()

# Define potential config file locations (can be modified at runtime)
config_paths = [
    "./apts.ini",
    "./examples/apts.ini",  # Relative to project root if run from there
    os.path.expanduser("~/.config/apts/apts.ini"),
]


def read(filenames):
    """
    Reads and parses a list of filenames.
    """
    return config.read(filenames)


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
        # Log all sections with masked secrets
        for section in config.sections():
            masked_section = {
                k: mask_secret(v)
                if any(
                    s in k.lower()
                    for s in [
                        "api_key",
                        "password",
                        "redis_location",
                        "token",
                        "secret",
                        "auth",
                        "credential",
                    ]
                )
                else v
                for k, v in config.items(section)
            }
            logger.debug(f"Content of [{section}] section: {masked_section}")

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


# Load initial configuration
load_config()
