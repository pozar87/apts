import logging
from typing import TYPE_CHECKING, Optional, Union, cast
from datetime import datetime

import pandas as pd

if TYPE_CHECKING:
    from skyfield.api import Time
    from ...conditions import Conditions
    from ...objects.ngc import NGC
    from ...place import Place

from ...i18n import language_context

logger = logging.getLogger(__name__)


class NgcCatalogMixIn:
    if TYPE_CHECKING:
        place: "Place"
        effective_date: Optional[Union["datetime", "Time"]]
        conditions: "Conditions"
        start: Optional["datetime"]
        time_limit: Optional["datetime"]
        limiting_magnitude: Optional[float]
        sun_observation: bool
        _local_ngc: Optional["NGC"]

    @property
    def local_ngc(self) -> "NGC":
        if self._local_ngc is None:
            from apts import catalogs
            from ...objects.ngc import NGC

            self._local_ngc = NGC(
                self.place, catalogs, calculation_date=self.effective_date
            )
        return self._local_ngc

    def get_visible_ngc(
        self, language: Optional[str] = None, **args
    ) -> pd.DataFrame:
        if self.sun_observation:
            return pd.DataFrame(columns=self.local_ngc.objects.columns)

        with language_context(language):
            from ...i18n import bulk_gettext

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
