import logging
from datetime import datetime, timedelta
from typing import TYPE_CHECKING, List, Optional

from skyfield.api import utc

if TYPE_CHECKING:
    from ..place import Place
    from ..constants.event_types import EventType

from ..events import AstronomicalEvents

logger = logging.getLogger(__name__)


class EventsMixIn:
    if TYPE_CHECKING:
        start: Optional[datetime]
        stop: Optional[datetime]
        place: "Place"

    def get_astronomical_events(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        events_to_calculate: Optional[List["EventType"]] = None,
    ):
        if start_date is None:
            start_date = self.start
        if end_date is None:
            end_date = self.stop

        if start_date is None:
            start_date = datetime.now(utc)
        if end_date is None:
            end_date = start_date + timedelta(days=365)

        events = AstronomicalEvents(
            self.place, start_date, end_date, events_to_calculate=events_to_calculate
        )
        return events.get_events()
