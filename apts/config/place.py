from .base import config

def get_light_pollution_settings() -> dict:
    """
    Reads the light pollution settings from the [light_pollution] section.

    Returns:
        dict: A dictionary of light pollution settings.
    """
    settings = {
        "use_online_api": True,
    }

    if config.has_section("light_pollution"):
        if config.has_option("light_pollution", "use_online_api"):
            settings["use_online_api"] = config.getboolean(
                "light_pollution", "use_online_api"
            )

    return settings


def get_place_settings() -> dict:
    """
    Reads the place settings from the [place] section.

    Returns:
        dict: A dictionary of place settings.
    """
    settings = {
        "use_online_elevation_api": True,
        "default_elevation": 300,
    }

    if config.has_section("place"):
        if config.has_option("place", "use_online_elevation_api"):
            settings["use_online_elevation_api"] = config.getboolean(
                "place", "use_online_elevation_api"
            )
        if config.has_option("place", "default_elevation"):
            settings["default_elevation"] = config.getint("place", "default_elevation")

    return settings
