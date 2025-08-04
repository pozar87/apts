import functools
from skyfield.api import load

@functools.lru_cache(maxsize=None)
def get_timescale():
    """
    Returns a cached timescale object.
    """
    return load.timescale()

@functools.lru_cache(maxsize=None)
def get_ephemeris_path():
    """
    Returns a cached ephemeris file path.
    """
    with load.open('de421.bsp') as f:
        return f.name

def get_ephemeris():
    """
    Returns an ephemeris object.
    """
    return load(get_ephemeris_path())
