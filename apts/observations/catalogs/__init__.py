from typing import TYPE_CHECKING, Optional, Union

from .messier import MessierCatalogMixIn
from .ngc import NgcCatalogMixIn
from .planets import PlanetsCatalogMixIn
from .stars import StarsCatalogMixIn

if TYPE_CHECKING:
    from datetime import datetime
    from skyfield.api import Time
    from ...conditions import Conditions
    from ...objects.messier import Messier
    from ...objects.ngc import NGC
    from ...objects import SolarObjects
    from ...objects.stars import Stars
    from ...place import Place


class CatalogMixIn(
    MessierCatalogMixIn,
    NgcCatalogMixIn,
    PlanetsCatalogMixIn,
    StarsCatalogMixIn,
):
    if TYPE_CHECKING:
        place: "Place"
        effective_date: Optional[Union["datetime", "Time"]]
        conditions: "Conditions"
        start: Optional["datetime"]
        time_limit: Optional["datetime"]
        limiting_magnitude: Optional[float]
        sun_observation: bool
        _local_messier: Optional["Messier"]
        _local_planets: Optional["SolarObjects"]
        _local_ngc: Optional["NGC"]
        _local_stars: Optional["Stars"]
