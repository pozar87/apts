import logging
from typing import TYPE_CHECKING, Optional, Union
from datetime import datetime

if TYPE_CHECKING:
    from skyfield.api import Time
    from ...objects.stars import Stars
    from ...place import Place

logger = logging.getLogger(__name__)


class StarsCatalogMixIn:
    if TYPE_CHECKING:
        place: "Place"
        effective_date: Optional[Union["datetime", "Time"]]
        _local_stars: Optional["Stars"]

    @property
    def local_stars(self) -> "Stars":
        if self._local_stars is None:
            from apts import catalogs
            from ...objects.stars import Stars

            self._local_stars = Stars(
                self.place, catalogs, calculation_date=self.effective_date
            )
        return self._local_stars
