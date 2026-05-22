import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd

logger = logging.getLogger(__name__)


class Catalogs:
    """
    This class provides access to astronomical catalogs.
    To improve application startup time, catalogs are loaded lazily on first access.
    """

    def __init__(self):
        pass

    @property
    def MESSIER(self) -> "pd.DataFrame":
        from .messier import get_messier

        return get_messier()

    @property
    def NGC(self) -> "pd.DataFrame":
        from .ngc import get_ngc

        return get_ngc()

    @property
    def BRIGHT_STARS(self) -> "pd.DataFrame":
        from .stars import get_bright_stars

        return get_bright_stars()

def initialize_catalogs():
    logger.info("Initializing catalogs...")
    catalogs = Catalogs()
    _ = catalogs.MESSIER
    _ = catalogs.NGC
    _ = catalogs.BRIGHT_STARS
