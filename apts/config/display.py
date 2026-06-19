import configparser
from .base import config, logger

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
