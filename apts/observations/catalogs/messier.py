import logging
from typing import TYPE_CHECKING, Optional, Union, cast
from datetime import datetime

import pandas as pd

if TYPE_CHECKING:
    from skyfield.api import Time
    from ...conditions import Conditions
    from ...objects.messier import Messier
    from ...place import Place

from ...i18n import language_context

logger = logging.getLogger(__name__)


class MessierCatalogMixIn:
    if TYPE_CHECKING:
        place: "Place"
        effective_date: Optional[Union["datetime", "Time"]]
        conditions: "Conditions"
        start: Optional["datetime"]
        time_limit: Optional["datetime"]
        limiting_magnitude: Optional[float]
        sun_observation: bool
        _local_messier: Optional["Messier"]

    @property
    def local_messier(self) -> "Messier":
        if self._local_messier is None:
            from apts import catalogs
            from ...objects.messier import Messier

            self._local_messier = Messier(
                self.place, catalogs, calculation_date=self.effective_date
            )
        return self._local_messier

    def get_visible_messier(
        self, language: Optional[str] = None, **args
    ) -> pd.DataFrame:
        if self.sun_observation:
            return pd.DataFrame(columns=self.local_messier.objects.columns)

        with language_context(language):
            from ...i18n import bulk_gettext

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
