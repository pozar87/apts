from typing import TYPE_CHECKING, Optional, cast

if TYPE_CHECKING:
    from apts.light_pollution import LightPollution

from apts.light_pollution import LightPollution


class LightPollutionMixIn:
    if TYPE_CHECKING:
        light_pollution: Optional[LightPollution]

        @property
        def lat_decimal(self) -> float: ...
        @property
        def lon_decimal(self) -> float: ...

    def _ensure_light_pollution(self):
        if self.light_pollution is None:
            self.light_pollution = LightPollution(
                self.lat_decimal,
                self.lon_decimal,
            )

    def get_light_pollution(self):
        self._ensure_light_pollution()
        return cast(LightPollution, self.light_pollution).get_light_pollution()
