import logging
import pytz
import pandas

from datetime import timedelta
from ..constants import ObjectTableLabels
from skyfield.api import Star, load
from skyfield import almanac
from skyfield.searchlib import find_discrete

logger = logging.getLogger(__name__)


class Objects:
    def __init__(self, place):
        self.place = place
        self.objects: pandas.DataFrame = pandas.DataFrame()
        self.ts = load.timescale()

    def get_visible(
        self, conditions, start, stop, hours_margin=0, sort_by=ObjectTableLabels.TRANSIT
    ):
        visible = self.objects
        # Add ID collumn
        visible["ID"] = visible.index
        visible = visible[
            # Filter objects by they transit
            (visible.Transit > start - timedelta(hours=hours_margin))
            & (visible.Transit < stop + timedelta(hours=hours_margin))
            &
            # Filter objects by they min altitude at transit
            (visible.Altitude > conditions.min_object_altitude)
            &
            # Filter object by they magnitude
            # Handle pint.Quantity objects for magnitude
            (
                visible.Magnitude.apply(
                    lambda x: x.magnitude if hasattr(x, "magnitude") else x
                )
                < conditions.max_object_magnitude
            )
        ]
        # Sort objects by given order
        visible = visible.sort_values(by=sort_by, ascending=True)
        return visible

    @staticmethod
    def fixed_body(RA, Dec):
        # Create body at given coordinates
        return Star(ra_hours=RA, dec_degrees=Dec)

    def _compute_tranzit(self, body, observer):
        # Return transit time in local time
        t0 = self.ts.utc(observer.date.utc_datetime())
        t1 = self.ts.utc(observer.date.utc_datetime() + timedelta(days=1))
        f = almanac.meridian_transits(self.place.eph, body, self.place.location)
        t, y = almanac.find_discrete(t0, t1, f)
        if len(t) > 0:
            return (
                t[0]
                .utc_datetime()
                .replace(tzinfo=pytz.UTC)
                .astimezone(observer.local_timezone)
            )
        return None

    def _compute_setting(self, body, observer):
        # Return setting time in local time
        t0 = self.ts.utc(observer.date.utc_datetime())
        t1 = self.ts.utc(observer.date.utc_datetime() + timedelta(days=1))
        f = almanac.risings_and_settings(self.place.eph, body, self.place.location)
        t, y = find_discrete(t0, t1, f)
        for ti, yi in zip(t, y):
            if yi == 0:
                return (
                    ti.utc_datetime()
                    .replace(tzinfo=pytz.UTC)
                    .astimezone(observer.local_timezone)
                )
        return None

    def _compute_rising(self, body, observer):
        # Return rising time in local time
        t0 = self.ts.utc(observer.date.utc_datetime())
        t1 = self.ts.utc(observer.date.utc_datetime() + timedelta(days=1))
        f = almanac.risings_and_settings(self.place.eph, body, self.place.location)
        t, y = find_discrete(t0, t1, f)
        for ti, yi in zip(t, y):
            if yi == 1:
                return (
                    ti.utc_datetime()
                    .replace(tzinfo=pytz.UTC)
                    .astimezone(observer.local_timezone)
                )
        return None

    def _altitude_at_transit(self, body, transit, observer):
        # Calculate objects altitude at transit time
        if transit is None:
            return 0
        t = self.ts.utc(transit)
        alt, _, _ = self.place.observer.at(t).observe(body).apparent().altaz()
        return alt.degrees
