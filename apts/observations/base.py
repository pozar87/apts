import logging
from datetime import datetime
from typing import Optional, Union

from skyfield.api import Time

from ..conditions import Conditions
from .catalogs import CatalogMixIn
from .events import EventsMixIn
from .html import HtmlExportMixIn
from .plotting import PlottingMixIn
from .weather import WeatherAnalysisMixIn
from .window import ObservationWindow

logger = logging.getLogger(__name__)


class Observation(
    WeatherAnalysisMixIn,
    PlottingMixIn,
    CatalogMixIn,
    HtmlExportMixIn,
    EventsMixIn,
):
    effective_date: Optional[Union[datetime, Time]]

    def __init__(
        self,
        place,
        equipment,
        conditions=Conditions(),
        target_date=None,
        sun_observation=False,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        limiting_magnitude: Optional[float] = None,
    ):
        self.place = place
        self.equipment = equipment
        self.conditions = conditions
        self.sun_observation = sun_observation
        self.limiting_magnitude = limiting_magnitude

        # Initialize observation window logic
        window = ObservationWindow(
            place,
            conditions,
            target_date=target_date,
            sun_observation=sun_observation,
            start_time=start_time,
            end_time=end_time,
        )

        self.start = window.start
        self.stop = window.stop
        self.effective_date = window.effective_date
        self.observation_local_time = window.observation_local_time
        self.time_limit = window.time_limit

        # Catalog objects are lazy-loaded to improve performance
        self._local_messier = None
        self._local_planets = None
        self._local_ngc = None
        self._local_stars = None
        self._weather_analysis = None
        self._plot = None

    def __str__(self) -> str:
        return (
            f"Observation at {self.place.name} from {self.start} to {self.time_limit}"
        )
