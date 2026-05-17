from .base import WeatherProvider, get_session, reset_session, _get_aurora_df
from .meteoblue import Meteoblue
from .open_weather_map import OpenWeatherMap
from .pirate_weather import PirateWeather
from .storm_glass import StormGlass
from .visual_crossing import VisualCrossing

def get_provider(provider_name, api_key, lat, lon, local_timezone) -> WeatherProvider:
    """
    Returns an instance of the specified weather provider.
    """
    if provider_name == "pirateweather":
        return PirateWeather(api_key, lat, lon, local_timezone)
    elif provider_name == "visualcrossing":
        return VisualCrossing(api_key, lat, lon, local_timezone)
    elif provider_name == "openweathermap":
        return OpenWeatherMap(api_key, lat, lon, local_timezone)
    elif provider_name == "meteoblue":
        return Meteoblue(api_key, lat, lon, local_timezone)
    elif provider_name == "stormglass":
        return StormGlass(api_key, lat, lon, local_timezone)
    else:
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
