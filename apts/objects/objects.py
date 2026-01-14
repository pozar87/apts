import logging
from abc import ABC, abstractmethod
from datetime import timedelta
from typing import cast

import pandas
import pytz
from skyfield import almanac
from skyfield.api import Star, load
from skyfield.searchlib import find_discrete

from ..constants import ObjectTableLabels

logger = logging.getLogger(__name__)


class Objects(ABC):
    @abstractmethod
    def get_skyfield_object(self, obj) -> object:
        pass

    @abstractmethod
    def compute(
        self, calculation_date=None, df_to_compute=None
    ) -> pandas.DataFrame | None:
        pass

    def __init__(self, place, calculation_date=None):
        self.place = place
        self.objects: pandas.DataFrame = pandas.DataFrame()
        self.ts = load.timescale()
        self.calculation_date = calculation_date  # Store it here

    def get_visible(
        self,
        conditions,
        start,
        stop,
        hours_margin=0,
        sort_by=ObjectTableLabels.TRANSIT,
        star_magnitude_limit=None,
        limiting_magnitude=None,
    ) -> pandas.DataFrame:
        if not start or not stop:
            return pandas.DataFrame(columns=self.objects.columns)

        max_magnitude = (
            limiting_magnitude
            if limiting_magnitude is not None
            else (
                star_magnitude_limit
                if star_magnitude_limit is not None
                else conditions.max_object_magnitude
            )
        )
        magnitude_values = self.objects["Magnitude"].apply(
            lambda x: x.magnitude if hasattr(x, "magnitude") else x
        )
        candidate_objects = self.objects[magnitude_values < max_magnitude].copy()

        # Compute transit/rise/set if they haven't been already for sorting purposes
        if (
            sort_by
            in [
                ObjectTableLabels.TRANSIT,
                ObjectTableLabels.RISING,
                ObjectTableLabels.SETTING,
            ]
            and (
                sort_by not in candidate_objects.columns
                or cast(pandas.Series, candidate_objects[sort_by]).isnull().any()
            )
        ):
            df_to_compute = (
                candidate_objects[cast(pandas.Series, candidate_objects[sort_by]).isnull()]
                if sort_by in candidate_objects.columns
                else candidate_objects
            )
            if not cast(pandas.DataFrame, df_to_compute).empty:
                self.compute(
                    calculation_date=self.calculation_date, df_to_compute=df_to_compute
                )
                # Update candidate_objects with the new computed values
                candidate_objects.update(self.objects.loc[cast(pandas.DataFrame, df_to_compute).index])

        visible_objects_indices = []
        for index, row in candidate_objects.iterrows():
            skyfield_object = self.get_skyfield_object(row)
            if skyfield_object is None:
                continue
            altaz_df = self.place.get_altaz_curve(skyfield_object, start, stop)

            altitude_values = altaz_df["Altitude"].apply(
                lambda x: x.magnitude if hasattr(x, "magnitude") else x
            )
            azimuth_values = altaz_df["Azimuth"].apply(
                lambda x: x.magnitude if hasattr(x, "magnitude") else x
            )

            altitude_condition = altitude_values > conditions.min_object_altitude
            azimuth_condition = self._is_azimuth_in_range(azimuth_values, conditions)

            if (altitude_condition & azimuth_condition).any():
                visible_objects_indices.append(index)

        if not visible_objects_indices:
            return pandas.DataFrame(columns=self.objects.columns)

        visible = self.objects.loc[visible_objects_indices].copy()

        # Sort objects by given order, handling potential NaNs
        if sort_by in visible.columns and not cast(pandas.Series, visible[sort_by]).isnull().all():
            visible = visible.sort_values(by=sort_by, ascending=True)

        return visible

    def _is_azimuth_in_range(self, azimuth_series, conditions):
        min_az = (
            conditions.min_object_azimuth.magnitude
            if hasattr(conditions.min_object_azimuth, "magnitude")
            else conditions.min_object_azimuth
        )
        max_az = (
            conditions.max_object_azimuth.magnitude
            if hasattr(conditions.max_object_azimuth, "magnitude")
            else conditions.max_object_azimuth
        )

        if min_az > max_az:
            return (azimuth_series >= min_az) | (azimuth_series <= max_az)
        else:
            return (azimuth_series >= min_az) & (azimuth_series <= max_az)

    @staticmethod
    def fixed_body(RA, Dec):
        # Create body at given coordinates
        return Star(ra_hours=RA, dec_degrees=Dec)

    def _compute_tranzit(self, skyfield_object, observer):
        if skyfield_object is None:
            return None
        # Return transit time in local time

        # Start search from the beginning of the UTC day to catch earlier transits
        current_dt = observer.date.utc_datetime()
        t0_dt = current_dt.replace(hour=0, minute=0, second=0, microsecond=0)

        # Search window extended to 2 days to catch transits happening next morning or late in the current day
        t0 = self.ts.utc(t0_dt)
        t1 = self.ts.utc(t0_dt + timedelta(days=2))
        f = almanac.meridian_transits(
            self.place.eph, skyfield_object, self.place.location
        )
        t, y = almanac.find_discrete(t0, t1, f)

        # Filter for upper culmination (y=1) AND relevant timing
        # We want a transit that results in the object being visible during the observation window (starting at observer.date).
        # A rough heuristic: Transit should be no earlier than 12 hours before observer.date.
        # (If it transited >12h ago, it likely set >6h ago and is gone).

        cutoff_time = current_dt - timedelta(hours=12)

        valid_transits = []
        for i, event in enumerate(y):
            if event == 1:  # Upper
                transit_dt = t[i].utc_datetime()
                if transit_dt > cutoff_time:
                    valid_transits.append(transit_dt)

        if valid_transits:
            # Return the first valid transit found
            return (
                valid_transits[0]
                .replace(tzinfo=pytz.UTC)
                .astimezone(observer.local_timezone)
            )

        return None
        upper_indices = [i for i, event in enumerate(y) if event == 1]

        if upper_indices:
            idx = upper_indices[0]
            return (
                t[idx]
                .utc_datetime()
                .replace(tzinfo=pytz.UTC)
                .astimezone(observer.local_timezone)
            )

        return None

    def _compute_rising_and_setting(self, skyfield_object, observer, transit_time):
        if skyfield_object is None or transit_time is None or pandas.isna(transit_time):
            return None, None

        f = almanac.risings_and_settings(
            self.place.eph, skyfield_object, self.place.location
        )

        # Find the latest rise time in the 24 hours before the transit
        t_transit = self.ts.utc(transit_time)
        t0_rise = self.ts.utc(transit_time - timedelta(days=1))
        t_rise, y_rise = find_discrete(t0_rise, t_transit, f)

        rising_time = None
        rise_events = [t for t, y in zip(t_rise, y_rise) if y == 1]
        if rise_events:
            rising_time = (
                rise_events[-1]
                .utc_datetime()
                .replace(tzinfo=pytz.UTC)
                .astimezone(observer.local_timezone)
            )

        # Find the earliest set time in the 24 hours after the transit
        t1_set = self.ts.utc(transit_time + timedelta(days=1))
        t_set, y_set = find_discrete(t_transit, t1_set, f)

        setting_time = None
        set_events = [t for t, y in zip(t_set, y_set) if y == 0]
        if set_events:
            setting_time = (
                set_events[0]
                .utc_datetime()
                .replace(tzinfo=pytz.UTC)
                .astimezone(observer.local_timezone)
            )

        return rising_time, setting_time

    def _altitude_at_transit(self, skyfield_object, transit, observer):
        # Calculate objects altitude at transit time
        if transit is None or pandas.isna(transit):
            return 0
        t = self.ts.utc(transit)
        alt, _, _ = (
            self.place.observer.at(t).observe(skyfield_object).apparent().altaz()
        )
        return alt.degrees
