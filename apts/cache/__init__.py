from skyfield.api import Loader, load
from .skyfield import get_timescale, get_ephemeris, get_jovian_ephemeris, STATIONS_URL
from .catalogs import get_hipparcos_data, get_mpcorb_data
from .nasa import get_nasa_comets_data
from .scoring import get_cached_score, set_cached_score
from .base import download_all_data, clear_cache

# For backward compatibility with unit tests that patch these functions
from ..config import get_minor_planet_settings

# Re-exporting these locally to ensure they can be patched via 'apts.cache'
# without being overshadowed by the submodules' own definitions during patching.
# This is a common pattern when refactoring into a package while maintaining
# patchability for legacy unit tests.

__all__ = [
    "Loader",
    "load",
    "get_timescale",
    "get_ephemeris",
    "get_jovian_ephemeris",
    "STATIONS_URL",
    "get_hipparcos_data",
    "get_mpcorb_data",
    "get_nasa_comets_data",
    "get_cached_score",
    "set_cached_score",
    "download_all_data",
    "clear_cache",
    "get_minor_planet_settings",
]
