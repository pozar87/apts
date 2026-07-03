import functools
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd

from ..config import get_api_key
from ..nasa_api import NasaAPI

@functools.lru_cache(maxsize=None)
def get_nasa_comets_data(start_date, end_date) -> "pd.DataFrame":
    """
    Returns a cached comets catalog as a pandas DataFrame.
    Data is from NASA NeoWs API.
    """
    import pandas as pd
    api_key = get_api_key("nasa")
    nasa_api = NasaAPI(api_key)
    comets = nasa_api.get_comets(start_date, end_date)
    records = []
    for date in comets.get("near_earth_objects", {}):
        for comet in comets["near_earth_objects"][date]:
            if "comet" in comet.get("name", "").lower():
                records.append(comet)
    return pd.DataFrame(records)
