from .base import config, logger

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
                try:
                    event_settings[option] = config.getboolean("events", option)
                except Exception as e:
                    logger.error(f"Error reading option {option} in [events]: {e}")

    return event_settings
