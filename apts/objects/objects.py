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
    ):
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
            or candidate_objects[ObjectTableLabels.TRANSIT].isnull().any()
        ):
            df_to_compute = (
                candidate_objects
                if ObjectTableLabels.TRANSIT not in self.objects.columns
                else candidate_objects[
                    candidate_objects[ObjectTableLabels.TRANSIT].isnull()
                ]
            )
            if not df_to_compute.empty:
                self.compute(
                    calculation_date=self.calculation_date, df_to_compute=df_to_compute
                )

        # Now that computations are done, filter from the updated self.objects
        magnitude_values = self.objects["Magnitude"].apply(
            lambda x: x.magnitude if hasattr(x, "magnitude") else x
        )
        visible = self.objects[magnitude_values < max_magnitude].copy()
        visible["ID"] = visible.index

        # Filter by transit time, ensuring Transit is not NaT
        visible = visible.loc[
            (visible[ObjectTableLabels.TRANSIT].notna())
            & (
                visible[ObjectTableLabels.TRANSIT]
                > start - timedelta(hours=hours_margin)
            )
            & (
                visible[ObjectTableLabels.TRANSIT]
                < stop + timedelta(hours=hours_margin)
            )
        ]

        if (
            conditions.min_object_azimuth == 0
            and conditions.max_object_azimuth == 360
        ):
            # Sort objects by given order
            visible = visible.sort_values(by=sort_by, ascending=True)  # pyright: ignore
            return visible

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
            if (altitude_condition & azimuth_condition).any():
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
        t0 = self.ts.utc(observer.date.utc_datetime())
        t1 = self.ts.utc(observer.date.utc_datetime() + timedelta(days=1))
        f = almanac.meridian_transits(self.place.eph, skyfield_object, self.place.location)
        t, y = almanac.find_discrete(t0, t1, f)
        if len(t) > 0:
            return (
                t[0]
                .utc_datetime()
                .replace(tzinfo=pytz.UTC)
                .astimezone(observer.local_timezone)
            )
        return None

    def _compute_rising_and_setting(self, skyfield_object, observer):
        if skyfield_object is None:
            return None, None
        # Return rising and setting time in local time
        t0 = self.ts.utc(observer.date.utc_datetime())
        t1 = self.ts.utc(observer.date.utc_datetime() + timedelta(days=1))
        f = almanac.risings_and_settings(self.place.eph, skyfield_object, self.place.location)
        t, y = find_discrete(t0, t1, f)

        rising_time = None
        setting_time = None

        for ti, yi in zip(t, y):
            local_time = (
                ti.utc_datetime()
                .replace(tzinfo=pytz.UTC)
                .astimezone(observer.local_timezone)
            )
            if yi == 1:  # Rising
                rising_time = local_time
            elif yi == 0:  # Setting
                setting_time = local_time
        return rising_time, setting_time

    def _altitude_at_transit(self, skyfield_object, transit, observer):
        # Calculate objects altitude at transit time
        if transit is None or pandas.isna(transit):
            return 0
        t = self.ts.utc(transit)
        alt, _, _ = self.place.observer.at(t).observe(skyfield_object).apparent().altaz()
        return alt.degrees
