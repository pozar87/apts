import logging
from typing import List, Optional, Dict

from ...config import get_event_settings
from ...constants.event_types import EventType

logger = logging.getLogger(__name__)

class EventSettingsManager:
    """
    Manages the configuration of which astronomical events should be calculated.
    Handles defaults, config file overrides, and runtime explicit requests.
    """

    EXPENSIVE_EVENTS = [
        "golden_hour",
        "blue_hour",
        "culminations",
        "jovian_moon_events",
    ]

    def __init__(self, events_to_calculate: Optional[List[EventType]] = None):
        self.settings: Dict[str, bool] = self._initialize_settings(events_to_calculate)

    def _initialize_settings(self, events_to_calculate: Optional[List[EventType]] = None) -> Dict[str, bool]:
        # Load global settings from config
        config_settings = get_event_settings()

        # Start with all events enabled by default
        settings = {event.value: True for event in EventType}

        # Disable expensive events by default
        for event_key in self.EXPENSIVE_EVENTS:
            if event_key in settings:
                settings[event_key] = False

        # Override with config settings if present
        for key, value in config_settings.items():
            if key in settings:
                settings[key] = value

        logger.debug(
            f"EventSettingsManager initialized. Config-based settings: {settings}"
        )

        if events_to_calculate is not None:
            # If a list of events is provided, it should explicitly enable those
            # but ONLY if they are not explicitly disabled in config.
            events_to_calculate_str = [str(e) for e in events_to_calculate]
            logger.debug(f"Limiting to events_to_calculate: {events_to_calculate_str}")

            new_settings = {event.value: False for event in EventType}
            for e_str in events_to_calculate_str:
                # Use config if present, otherwise default to True for the requested event
                new_settings[e_str] = config_settings.get(e_str, True)

            settings = new_settings
            logger.debug(f"Final event_settings after explicit override: {settings}")

        return settings

    def is_enabled(self, event_key: str) -> bool:
        return self.settings.get(event_key, False)

    def get_all(self) -> Dict[str, bool]:
        return self.settings.copy()
