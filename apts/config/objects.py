from .base import config

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
