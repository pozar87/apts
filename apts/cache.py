import functools
from skyfield.api import load
from skyfield.data import hipparcos, mpc
import pandas as pd
import zlib
import io

@functools.lru_cache(maxsize=None)
def get_timescale():
    """
    Returns a cached timescale object.
    """
    return load.timescale()

@functools.lru_cache(maxsize=None)
def get_ephemeris():
    """
    Returns an ephemeris object, loading from a URL.
    This ensures that the file is downloaded if not present.
    """
    # de440 is a comprehensive ephemeris that includes dwarf planets.
    url = "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de440.bsp"
    return load(url)

@functools.lru_cache(maxsize=None)
def get_hipparcos_data() -> pd.DataFrame:
    """
    Returns a cached Hipparcos catalog as a pandas DataFrame.
    """
    with load.open(hipparcos.URL) as f:
        return hipparcos.load_dataframe(f)

@functools.lru_cache(maxsize=None)
def get_mpcorb_data() -> pd.DataFrame:
    """
    Returns a cached Minor Planet Center orbit catalog as a pandas DataFrame.
    """
    with load.open(mpc.MPCORB_URL, reload=False) as f:
        data = zlib.decompress(f.read(), wbits=zlib.MAX_WBITS | 16)
        return mpc.load_mpcorb_dataframe(io.BytesIO(data))