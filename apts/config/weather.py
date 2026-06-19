from typing import Optional
from ..secrets import mask_secret
from .base import config, logger

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
        f"get_weather_settings returning provider: {provider}, api_key: {mask_secret(api_key)}"
    )
    return provider, api_key
