import os
from .config import get_data_settings

# Use abspath to ensure the path is absolute
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))


def get_ephemeris_path():
    """
    Returns the path to the ephemeris file based on the data mode.
    """
    mode = get_data_settings()
    if mode == "light":
        return "de421.bsp"
    else:
        return "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de440.bsp"


def get_mpcorb_path():
    """
    Returns the path to the MPCORB data file based on the data mode.
    """
    mode = get_data_settings()
    if mode == "light":
        return os.path.join(DATA_DIR, "MPCORB.DAT.small.gz")
    else:
        return "https://www.minorplanetcenter.net/iau/MPCORB/MPCORB.DAT.gz"