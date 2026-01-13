import logging
import pytz
import pandas
from abc import ABC, abstractmethod

from datetime import timedelta
from ..constants import ObjectTableLabels
from skyfield.api import Star, load
from skyfield import almanac
from skyfield.searchlib import find_discrete

logger = logging.getLogger(__name__)


class Objects(ABC):
    @abstractmethod
    def get_skyfield_object(self, obj) -> object:
        pass

    @abstractmethod
    def compute(self, calculation_date=None, df_to_compute=None) -> pandas.DataFrame | None:
        pass

    def __init__(self, place, calculation_date=None):
        self.place = place
        self.objects: pandas.DataFrame = pandas.DataFrame()
        self.ts = load.timescale()
        self.calculation_date = calculation_date # Store it here

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
        candidate_objects = self.objects[magnitude_values < max_magnitude]

        if (
            ObjectTableLabels.TRANSIT not in candidate_objects.columns
            or candidate_objects[ObjectTableLabels.TRANSIT].isnull().any() # pyright: ignore
        ):
            df_to_compute = (
                candidate_objects
                if ObjectTableLabels.TRANSIT not in self.objects.columns
                else candidate_objects[
                    candidate_objects[ObjectTableLabels.TRANSIT].isnull() # pyright: ignore
                ]
            )
            if not df_to_compute.empty: # pyright: ignore
                self.compute(
                    calculation_date=self.calculation_date, df_to_compute=df_to_compute
                )

        # Now that computations are done, filter from the updated self.objects
        magnitude_values = self.objects["Magnitude"].apply(
            lambda x: x.magnitude if hasattr(x, "magnitude") else x
        )
        visible = self.objects[magnitude_values < max_magnitude].copy()
        visible["ID"] = visible.index

        # Filter objects based on visibility window (Rising/Setting) intersection with observation window
        # or Altitude at Transit if Rising/Setting are not available (e.g. circumpolar)
        
        # Helper boolean for existence of Rise/Set times
        has_rise_set = (visible[ObjectTableLabels.RISING].notna()) & (visible[ObjectTableLabels.SETTING].notna())
        
        # Case A: Rise < Set (Simple interval)
        # Visible if: (Rise <= Stop + margin) AND (Set >= Start - margin)
        # Note: We apply hours_margin to be safe, though overlap logic usually suffices.
        cond_A = (visible[ObjectTableLabels.RISING] <= visible[ObjectTableLabels.SETTING]) & \
                 (visible[ObjectTableLabels.RISING] <= stop + timedelta(hours=hours_margin)) & \
                 (visible[ObjectTableLabels.SETTING] >= start - timedelta(hours=hours_margin))
                 
        # Case B: Set < Rise (Crosses midnight/wrap-around)
        # Visible if: NOT (Set < Start - margin AND Rise > Stop + margin)
        # i.e. It is NOT the case that the "down time" covers the whole "observation time"
        cond_B = (visible[ObjectTableLabels.SETTING] < visible[ObjectTableLabels.RISING]) & \
                 ~((visible[ObjectTableLabels.SETTING] < start - timedelta(hours=hours_margin)) & \
                   (visible[ObjectTableLabels.RISING] > stop + timedelta(hours=hours_margin)))

        # Case C: No Rise/Set (Circumpolar or Always Down)
        # Check Altitude at Transit. If > min_alt, assume always visible (or at least up).
        if ObjectTableLabels.ALTITUDE in visible.columns:
             alt_values = visible[ObjectTableLabels.ALTITUDE].apply(lambda x: x.magnitude if hasattr(x, "magnitude") else x)
        else:
             alt_values = pandas.Series([0] * len(visible), index=visible.index)

        cond_always_up = (~has_rise_set) & (alt_values > conditions.min_object_altitude)
        
        # Apply filter
        visible = visible[ (has_rise_set & (cond_A | cond_B)) | cond_always_up ]

        # Filter by altitude at transit (if available) to reject impossible objects early
        if ObjectTableLabels.ALTITUDE in visible.columns and not visible[ObjectTableLabels.ALTITUDE].isnull().all():
             alt_values = visible[ObjectTableLabels.ALTITUDE].apply(lambda x: x.magnitude if hasattr(x, "magnitude") else x)
             visible = visible[alt_values > conditions.min_object_altitude]

        visible_objects_indices = []
        for index, row in visible.iterrows():
            skyfield_object = self.get_skyfield_object(row)
            altaz_df = self.place.get_altaz_curve(skyfield_object, start, stop)

            # Extract magnitude from Altitude and Azimuth Quantity objects
            altitude_values = altaz_df['Altitude'].apply(lambda x: x.magnitude if hasattr(x, 'magnitude') else x)
            azimuth_values = altaz_df['Azimuth'].apply(lambda x: x.magnitude if hasattr(x, 'magnitude') else x)

            # Combine altitude and azimuth conditions
            altitude_condition = altitude_values > conditions.min_object_altitude
            azimuth_condition = self._is_azimuth_in_range(azimuth_values, conditions)

            # Check if any time satisfies both conditions
            if (altitude_condition & azimuth_condition).any(): # pyright: ignore
                visible_objects_indices.append(index)

        visible = self.objects.loc[visible_objects_indices]
        # Sort objects by given order
        visible = visible.sort_values(by=sort_by, ascending=True)
        return visible

    def _is_azimuth_in_range(self, azimuth_series, conditions):
        min_az = conditions.min_object_azimuth.magnitude if hasattr(conditions.min_object_azimuth, 'magnitude') else conditions.min_object_azimuth
        max_az = conditions.max_object_azimuth.magnitude if hasattr(conditions.max_object_azimuth, 'magnitude') else conditions.max_object_azimuth

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
        f = almanac.meridian_transits(self.place.eph, skyfield_object, self.place.location)
        t, y = almanac.find_discrete(t0, t1, f)

        # Filter for upper culmination (y=1) AND relevant timing
        # We want a transit that results in the object being visible during the observation window (starting at observer.date).
        # A rough heuristic: Transit should be no earlier than 12 hours before observer.date.
        # (If it transited >12h ago, it likely set >6h ago and is gone).
        
        cutoff_time = current_dt - timedelta(hours=12)
        
        valid_transits = []
        for i, event in enumerate(y):
            if event == 1: # Upper
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
        alt, _, _ = self.place.observer.at(t).observe(skyfield_object).apparent().altaz()
        return alt.degrees
