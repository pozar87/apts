from typing import Optional, Any
from .base import WeatherProvider, _get_aurora_df
from ...utils.network import get_session, reset_session
from .meteoblue import Meteoblue
from .open_weather_map import OpenWeatherMap
from .pirate_weather import PirateWeather
from .storm_glass import StormGlass
from .visual_crossing import VisualCrossing

def get_provider(
    provider_name: str, api_key: str, lat: float, lon: float, local_timezone: Any
) -> WeatherProvider:
    """
    Factory function to create a weather provider instance.
    """
    providers = {
        "pirateweather": PirateWeather,
        "visualcrossing": VisualCrossing,
        "openweathermap": OpenWeatherMap,
        "meteoblue": Meteoblue,
        "stormglass": StormGlass,
    }

    provider_class = providers.get(provider_name.lower())
    if provider_class:
        return provider_class(api_key, lat, lon, local_timezone)

    raise ValueError(f"Unknown weather provider: {provider_name}")

__all__ = [
    "WeatherProvider",
    "get_session",
    "reset_session",
    "_get_aurora_df",
    "Meteoblue",
    "OpenWeatherMap",
    "PirateWeather",
    "StormGlass",
    "VisualCrossing",
    "get_provider",
]
