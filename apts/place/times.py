import datetime
from typing import Optional

from apts.constants.twilight import Twilight

from .conditions import PlaceConditionsMixIn
from .utils import (
    get_twilight_time_utc,
    next_rising_time_utc,
    next_setting_time_utc,
    previous_rising_time_utc,
    previous_setting_time_utc,
)


class PlaceTimesMixIn(PlaceConditionsMixIn):
    def _previous_setting_time(self, obj_name, start, horizon_degrees=None):
        res = previous_setting_time_utc(
            self.lat_decimal,
            self.lon_decimal,
            self.elevation,
            obj_name,
            start,
            horizon_degrees=horizon_degrees,
        )
        if res:
            return res.astimezone(self.local_timezone)
        return None

    def _next_setting_time(self, obj_name, start, horizon_degrees=None):
        res = next_setting_time_utc(
            self.lat_decimal,
            self.lon_decimal,
            self.elevation,
            obj_name,
            start,
            horizon_degrees=horizon_degrees,
        )
        if res:
            return res.astimezone(self.local_timezone)
        return None

    def _previous_rising_time(self, obj_name, start, horizon_degrees=None):
        res = previous_rising_time_utc(
            self.lat_decimal,
            self.lon_decimal,
            self.elevation,
            obj_name,
            start,
            horizon_degrees=horizon_degrees,
        )
        if res:
            return res.astimezone(self.local_timezone)
        return None

    def _next_rising_time(self, obj_name, start, horizon_degrees=None):
        res = next_rising_time_utc(
            self.lat_decimal,
            self.lon_decimal,
            self.elevation,
            obj_name,
            start,
            horizon_degrees=horizon_degrees,
        )
        if res:
            return res.astimezone(self.local_timezone)
        return None

    def _get_start_date(self, target_date, start_search_from):
        if start_search_from is not None:
            return start_search_from
        elif target_date:
            if isinstance(target_date, datetime.datetime):
                # Ensure we handle both date and datetime
                target_date = target_date.date()
            local_start_of_day = datetime.datetime.combine(
                target_date, datetime.time.min
            ).replace(tzinfo=self.local_timezone)
            return local_start_of_day.astimezone(datetime.timezone.utc)
        else:
            return self.date.utc_datetime()  # type: ignore

    def _get_twilight_time(self, start_date, twilight: Twilight, event: str):
        res = get_twilight_time_utc(
            self.lat_decimal,
            self.lon_decimal,
            self.elevation,
            start_date,
            twilight,
            event,
        )
        if res:
            return res.astimezone(self.local_timezone)
        return None

    def sunset_time(
        self,
        target_date=None,
        start_search_from: Optional[datetime.datetime] = None,
        twilight: Optional[Twilight] = None,
        horizon_degrees: float = -0.8333,
    ):
        start_date = self._get_start_date(target_date, start_search_from)
        if twilight:
            return self._get_twilight_time(start_date, twilight, "set")
        return self._next_setting_time(
            "sun", start=start_date, horizon_degrees=horizon_degrees
        )

    def sunrise_time(
        self,
        target_date=None,
        start_search_from: Optional[datetime.datetime] = None,
        twilight: Optional[Twilight] = None,
        horizon_degrees: float = -0.8333,
    ):
        start_date = self._get_start_date(target_date, start_search_from)
        if twilight:
            return self._get_twilight_time(start_date, twilight, "rise")
        return self._next_rising_time(
            "sun", start=start_date, horizon_degrees=horizon_degrees
        )

    def moonset_time(
        self,
        target_date=None,
        start_search_from: Optional[datetime.datetime] = None,
        horizon_degrees: float = -0.8333,
    ):
        start_date = self._get_start_date(target_date, start_search_from)
        return self._next_setting_time(
            "moon", start=start_date, horizon_degrees=horizon_degrees
        )

    def moonrise_time(
        self,
        target_date=None,
        start_search_from: Optional[datetime.datetime] = None,
        horizon_degrees: float = -0.8333,
    ):
        start_date = self._get_start_date(target_date, start_search_from)
        return self._next_rising_time(
            "moon", start=start_date, horizon_degrees=horizon_degrees
        )
