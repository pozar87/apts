import functools
from skyfield.api import load
from skyfield.data import hipparcos
import pandas as pd

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

@functools.lru_cache(maxsize=None)
def get_hipparcos_data() -> pd.DataFrame:
    """
    Returns a cached Hipparcos catalog as a pandas DataFrame.
    """
    with load.open(hipparcos.URL) as f:
        return hipparcos.load_dataframe(f)