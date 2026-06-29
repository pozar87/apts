import logging
from typing import TYPE_CHECKING, Optional, Union, cast
from datetime import datetime

import numpy as np
import pandas as pd

if TYPE_CHECKING:
    from skyfield.api import Time
    from ...conditions import Conditions
    from ...objects import SolarObjects
    from ...place import Place

from ...i18n import language_context

logger = logging.getLogger(__name__)


class PlanetsCatalogMixIn:
    if TYPE_CHECKING:
        place: "Place"
        effective_date: Optional[Union["datetime", "Time"]]
        conditions: "Conditions"
        start: Optional["datetime"]
        time_limit: Optional["datetime"]
        limiting_magnitude: Optional[float]
        sun_observation: bool
        _local_planets: Optional["SolarObjects"]

    @property
    def local_planets(self) -> "SolarObjects":
        if self._local_planets is None:
            from ...objects import SolarObjects

            self._local_planets = SolarObjects(
                self.place, calculation_date=self.effective_date, lazy=True
            )
        return self._local_planets

    def get_visible_planets(
        self, language: Optional[str] = None, **args
    ) -> pd.DataFrame:
        with language_context(language):
            from ...i18n import bulk_gettext

            visible = self.local_planets.get_visible(
                self.conditions,
                self.start,
                self.time_limit,
                limiting_magnitude=self.limiting_magnitude,
                **args,
            )

            if self.sun_observation and not visible.empty:
                # In sun observation mode, only very bright objects are visible.
                # Usually Sun, Moon, and potentially Venus/Jupiter if they are bright enough.
                # We use a threshold of 0 magnitude for daytime planet visibility.
                from ...constants import ObjectTableLabels

                def _get_mag(x):
                    return getattr(x, "magnitude", x)

                mags = np.array([_get_mag(val) for val in visible[ObjectTableLabels.MAGNITUDE].values])
                tech_names = visible["TechnicalName"].values
                # Keep Sun, Moon, or anything with magnitude < 0
                mask = (tech_names == "sun") | (tech_names == "moon") | (mags < 0)
                visible = visible[mask].copy()

            # Optimization: use bulk_gettext (unique value mapping) instead of .apply(gettext_)
            if "Name" in visible.columns:
                visible["Name"] = cast(pd.Series, bulk_gettext(visible["Name"])).astype(
                    "string"
                )
            return visible
