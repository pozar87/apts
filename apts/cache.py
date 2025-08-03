import functools
from skyfield.api import load

@functools.lru_cache(maxsize=None)
def get_timescale():
    """
    Returns a cached timescale object.
    """
    return load.timescale()

@functools.lru_cache(maxsize=None)
def get_ephemeris():
    """
    Returns a cached ephemeris object.
    """
    return load('de421.bsp')
