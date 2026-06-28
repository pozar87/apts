import logging
from typing import TYPE_CHECKING, Optional, Union, cast

import numpy as np
import pandas as pd

if TYPE_CHECKING:
    from datetime import datetime

    from skyfield.api import Time

    from ..conditions import Conditions
    from ..objects.messier import Messier
    from ..objects.ngc import NGC
    from ..objects import SolarObjects
    from ..objects.stars import Stars
    from ..place import Place

from ..i18n import language_context

logger = logging.getLogger(__name__)


class CatalogMixIn:
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

    @property
    def local_messier(self) -> "Messier":
        if self._local_messier is None:
            from apts import catalogs

            from ..objects.messier import Messier

            self._local_messier = Messier(
                self.place, catalogs, calculation_date=self.effective_date
            )
        return self._local_messier

    @property
    def local_planets(self) -> "SolarObjects":
        if self._local_planets is None:
            from ..objects import SolarObjects

            self._local_planets = SolarObjects(
                self.place, calculation_date=self.effective_date, lazy=True
            )
        return self._local_planets

    @property
    def local_ngc(self) -> "NGC":
        if self._local_ngc is None:
            from apts import catalogs

            from ..objects.ngc import NGC

            self._local_ngc = NGC(
                self.place, catalogs, calculation_date=self.effective_date
            )
        return self._local_ngc

    @property
    def local_stars(self) -> "Stars":
        if self._local_stars is None:
            from apts import catalogs

            from ..objects.stars import Stars

            self._local_stars = Stars(
                self.place, catalogs, calculation_date=self.effective_date
            )
        return self._local_stars

    def get_visible_messier(
        self, language: Optional[str] = None, **args
    ) -> pd.DataFrame:
        if self.sun_observation:
            return pd.DataFrame(columns=self.local_messier.objects.columns)

        with language_context(language):
            from ..i18n import bulk_gettext

            visible = self.local_messier.get_visible(
                self.conditions,
                self.start,
                self.time_limit,
                limiting_magnitude=self.limiting_magnitude,
                **args,
            )
            # Optimization: use bulk_gettext (unique value mapping) instead of .apply(gettext_)
            if "Type" in visible.columns:
                visible["Type"] = cast(pd.Series, bulk_gettext(visible["Type"])).astype(
                    "string"
                )
            if "Constellation" in visible.columns:
                visible["Constellation"] = cast(
                    pd.Series, bulk_gettext(visible["Constellation"])
                ).astype("string")
            return visible

    def get_visible_ngc(
        self, language: Optional[str] = None, **args
    ) -> pd.DataFrame:
        if self.sun_observation:
            return pd.DataFrame(columns=self.local_ngc.objects.columns)

        with language_context(language):
            from ..i18n import bulk_gettext

            visible = self.local_ngc.get_visible(
                self.conditions,
                self.start,
                self.time_limit,
                limiting_magnitude=self.limiting_magnitude,
                **args,
            )
            # Optimization: use bulk_gettext (unique value mapping) instead of .apply(gettext_)
            if "Type" in visible.columns:
                visible["Type"] = cast(pd.Series, bulk_gettext(visible["Type"])).astype(
                    "string"
                )
            if "Constellation" in visible.columns:
                visible["Constellation"] = cast(
                    pd.Series, bulk_gettext(visible["Constellation"])
                ).astype("string")
            return visible

    def get_visible_planets(
        self, language: Optional[str] = None, **args
    ) -> pd.DataFrame:
        with language_context(language):
            from ..i18n import bulk_gettext

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
                from ..constants import ObjectTableLabels

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
