from .base import config

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
