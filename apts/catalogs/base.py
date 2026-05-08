import logging
import pandas as pd

from .messier import get_messier
from .ngc import get_ngc
from .stars import get_bright_stars

logger = logging.getLogger(__name__)

class Catalogs:
    """
    This class provides access to astronomical catalogs.
    To improve application startup time, catalogs are loaded lazily on first access.
    """

    def __init__(self):
        pass

    @property
    def MESSIER(self) -> pd.DataFrame:
        return get_messier()

    @property
    def NGC(self) -> pd.DataFrame:
        return get_ngc()

    @property
    def BRIGHT_STARS(self) -> pd.DataFrame:
        return get_bright_stars()

def initialize_catalogs():
    logger.info("Initializing catalogs...")
    catalogs = Catalogs()
    _ = catalogs.MESSIER
    _ = catalogs.NGC
    _ = catalogs.BRIGHT_STARS
