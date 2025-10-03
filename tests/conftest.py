import pytest
from apts.cache import get_mpcorb_data, get_timescale, get_ephemeris, get_hipparcos_data

@pytest.fixture(autouse=True)
def clear_lru_caches():
    """Clear all lru_cache instances before each test."""
    get_mpcorb_data.cache_clear()
    get_timescale.cache_clear()
    get_ephemeris.cache_clear()
    get_hipparcos_data.cache_clear()