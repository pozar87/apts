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
        self, conditions, start, stop, hours_margin=0, sort_by=ObjectTableLabels.TRANSIT
    ):
        # Check if 'TRANSIT' and 'ALTITUDE' columns exist. If not, compute them.
        if ObjectTableLabels.TRANSIT not in self.objects.columns or \
           ObjectTableLabels.ALTITUDE not in self.objects.columns:
            self.compute(self.calculation_date)

        visible = self.objects
        # Add ID collumn
        visible["ID"] = visible.index
        visible = visible[
            # Filter objects by they transit
            (visible.Transit > start - timedelta(hours=hours_margin))
            & (visible.Transit < stop + timedelta(hours=hours_margin))
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

            # Filter for times when altitude is sufficient
            above_horizon_df = altaz_df[altaz_df['Altitude'] > conditions.min_object_altitude]

            if not above_horizon_df.empty:
                # Check if azimuth is within range for any of these times
                az_conditions_met = self._is_azimuth_in_range(above_horizon_df['Azimuth'], conditions)
                if az_conditions_met.any():
                    visible_objects_indices.append(index)

        visible = self.objects.loc[visible_objects_indices]
        # Sort objects by given order
        visible = visible.sort_values(by=sort_by, ascending=True)
        return visible

    def _is_azimuth_in_range(self, azimuth_series, conditions):
        if conditions.min_object_azimuth > conditions.max_object_azimuth:
            return (azimuth_series >= conditions.min_object_azimuth) | (azimuth_series <= conditions.max_object_azimuth)
        else:
            return (azimuth_series >= conditions.min_object_azimuth) & (azimuth_series <= conditions.max_object_azimuth)

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
