from typing import TYPE_CHECKING, Any, Callable, Optional

if TYPE_CHECKING:
    from skyfield.api import Time, Timescale
    from apts.light_pollution import LightPollution
    from ...weather import Weather

from .light_pollution import LightPollutionMixIn
from .sqm import SqmMixIn
from .seeing import SeeingMixIn
from .weather import WeatherMixIn


class PlaceConditionsMixIn(
    LightPollutionMixIn,
    SqmMixIn,
    SeeingMixIn,
    WeatherMixIn,
):
    if TYPE_CHECKING:
        light_pollution: Optional[LightPollution]

        @property
        def lat_decimal(self) -> float: ...
        @property
        def lon_decimal(self) -> float: ...

        date: Time
        observer: Any
        sun: Any
        moon: Any
        local_timezone: Any
        weather: Optional[Weather]
        ts: Timescale
        eph: Any
        elevation: float
        sunset_time: Callable[..., Any]
        sunrise_time: Callable[..., Any]
        get_altaz_curve: Callable[..., Any]
