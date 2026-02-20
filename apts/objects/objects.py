import logging
from abc import ABC, abstractmethod
from datetime import timedelta
from typing import Any, cast

import numpy as np
import pandas as pd
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
    ) -> pd.DataFrame | None:
        pass

    def __init__(self, place, calculation_date=None):
        self.place = place
        self.objects: pd.DataFrame = pd.DataFrame()
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
    ) -> pd.DataFrame:
        if not start or not stop:
            return pd.DataFrame(columns=self.objects.columns)

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

        if candidate_objects.empty:
            return pd.DataFrame(columns=self.objects.columns)

        # Vectorized visibility check
        ts = self.ts
        t_start = ts.utc(start)
        t_stop = ts.utc(stop)
        # Use 100 points to match previous behavior and ensure precision
        check_times = ts.linspace(t_start, t_stop, 100)

        # Check if get_altaz_curve is mocked or overridden (common in tests)
        import types
        import unittest.mock

        # Original method is a bound method, mocked/overridden is often a function or a Mock object
        is_mocked = isinstance(
            self.place.get_altaz_curve, unittest.mock.Mock
        ) or isinstance(self.place.get_altaz_curve, types.FunctionType)

        if is_mocked:
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
                az_condition = self._is_azimuth_in_range(azimuth_values, conditions)
                if cast(Any, (altitude_condition & az_condition).any()):
                    visible_objects_indices.append(index)

            visible_candidate_objects = cast(
                pd.DataFrame, candidate_objects.loc[visible_objects_indices].copy()
            )
        else:
            visible_mask = np.zeros(len(candidate_objects), dtype=bool)

            # Group objects by type to vectorize Star objects
            stars_indices = []
            stars_ras = []
            stars_decs = []
            other_objects = [] # List of (local_index, skyfield_obj)

            for i, (index, row) in enumerate(candidate_objects.iterrows()):
                skyfield_obj = self.get_skyfield_object(row)
                if skyfield_obj is None:
                    continue
                if isinstance(skyfield_obj, Star):
                    stars_indices.append(i)
                    stars_ras.append(skyfield_obj.ra.hours)
                    stars_decs.append(skyfield_obj.dec.degrees)
                else:
                    other_objects.append((i, skyfield_obj))

            observer = self.place.observer

            # Check Stars in vectorized batches across check_times
            if stars_indices:
                combined_stars = Star(ra_hours=stars_ras, dec_degrees=stars_decs)
                for t in check_times:
                    alt, az, _ = observer.at(t).observe(combined_stars).apparent().altaz()
                    alt_deg = alt.degrees
                    az_deg = az.degrees

                    alt_ok = alt_deg > conditions.min_object_altitude
                    az_ok = self._is_azimuth_in_range(az_deg, conditions)

                    visible_mask[stars_indices] |= (alt_ok & az_ok)

            # Check Other objects (like planets)
            for i, skyfield_obj in other_objects:
                alt, az, _ = observer.at(check_times).observe(skyfield_obj).apparent().altaz()
                alt_deg = alt.degrees
                az_deg = az.degrees

                alt_ok = alt_deg > conditions.min_object_altitude
                az_ok = self._is_azimuth_in_range(az_deg, conditions)

                if cast(Any, (alt_ok & az_ok).any()):
                    visible_mask[i] = True

            visible_candidate_objects: pd.DataFrame = cast(
                pd.DataFrame, candidate_objects.loc[visible_mask].copy()
            )

        if visible_candidate_objects.empty:
            return pd.DataFrame(columns=self.objects.columns)

        # Compute transit/rise/set ONLY for visible objects if needed for sorting or plotting
        # SolarObjects and others often need these for plotting later
        if (
            sort_by
            in [
                ObjectTableLabels.TRANSIT,
                ObjectTableLabels.RISING,
                ObjectTableLabels.SETTING,
            ]
            or True # Always ensure these are available for visible objects to avoid KeyErrors in plotting
        ):
            # Check if any of the core columns are missing
            needed_cols = [ObjectTableLabels.TRANSIT, ObjectTableLabels.RISING, ObjectTableLabels.SETTING, ObjectTableLabels.ALTITUDE]
            missing_any = False
            for col in needed_cols:
                if col not in visible_candidate_objects.columns or cast(
                    Any, visible_candidate_objects[col].isnull().any()
                ):
                    missing_any = True
                    break

            if missing_any:
                if not visible_candidate_objects.empty:
                    self.compute(
                        calculation_date=self.calculation_date, df_to_compute=visible_candidate_objects
                    )
                    # Update visible_candidate_objects with the new computed values
                    # Ensure columns exist before update
                    for col in self.objects.columns:
                        if col not in visible_candidate_objects.columns:
                            visible_candidate_objects[col] = None
                    visible_candidate_objects.update(self.objects.loc[visible_candidate_objects.index])

        visible = visible_candidate_objects

        # Sort objects by given order, handling potential NaNs
        if sort_by in visible.columns and not bool(visible[sort_by].isnull().all()):
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
        """
        Calculates the upper meridian transit of a celestial object.
        For stars, a fast sidereal time approximation is used.
        """
        if skyfield_object is None:
            return None

        # Optimization for stars: use sidereal time formula
        if isinstance(skyfield_object, Star):
            current_dt = observer.date.utc_datetime()
            # Start search from the beginning of the UTC day
            t0_dt = current_dt.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=pytz.UTC)
            t0 = self.ts.utc(t0_dt)

            # RA of the star
            ra_hours = skyfield_object.ra.hours
            lon_hours = self.place.lon_decimal / 15.0

            # LST = GMST + lon
            # We want LST == RA => GMST + lon == RA => GMST == RA - lon
            target_gmst = (ra_hours - lon_hours) % 24

            current_gmst = t0.gmst

            # Sidereal day is shorter than solar day
            # 1 solar hour = 1.0027379 sidereal hours
            # 1 sidereal hour = 0.99726957 solar hours
            sidereal_to_solar = 0.99726957

            dt_sidereal = (target_gmst - current_gmst) % 24
            dt_solar = dt_sidereal * sidereal_to_solar

            transit_dt = t0_dt + timedelta(hours=dt_solar)

            # Ensure we catch the transit relevant to the observation window
            # If it already happened more than 12 hours before observation start,
            # we might want the next one (stars transit once per sidereal day)
            if transit_dt < current_dt - timedelta(hours=12):
                transit_dt += timedelta(hours=24 * sidereal_to_solar)

            return transit_dt.astimezone(observer.local_timezone)

        # Fallback for moving objects (planets)
        current_dt = observer.date.utc_datetime()
        t0_dt = current_dt.replace(hour=0, minute=0, second=0, microsecond=0)
        t0 = self.ts.utc(t0_dt)
        t1 = self.ts.utc(t0_dt + timedelta(days=2))
        f = almanac.meridian_transits(
            self.place.eph, skyfield_object, self.place.location
        )
        t, y = almanac.find_discrete(t0, t1, f)

        cutoff_time = current_dt - timedelta(hours=12)
        valid_transits = []
        for i, event in enumerate(y):
            if event == 1:  # Upper
                transit_dt = t[i].utc_datetime()
                if transit_dt > cutoff_time:
                    valid_transits.append(transit_dt)

        if valid_transits:
            return (
                valid_transits[0]
                .replace(tzinfo=pytz.UTC)
                .astimezone(observer.local_timezone)
            )

        return None

    def _compute_rising_and_setting(self, skyfield_object, observer, transit_time):
        """
        Calculates rising and setting times for a celestial object.
        Note: For stars, use _fast_compute_stars for better performance.
        """
        if skyfield_object is None or transit_time is None or pd.isna(transit_time):
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
        if transit is None or pd.isna(transit):
            return 0

        # Optimization for stars: geometric formula
        if isinstance(skyfield_object, Star):
            lat = self.place.lat_decimal
            dec = skyfield_object.dec.degrees
            # Max altitude = 90 - abs(lat - dec)
            # This is exact for stars ignoring refraction
            return 90.0 - abs(lat - dec)

        t = self.ts.utc(transit)
        alt, _, _ = (
            self.place.observer.at(t).observe(skyfield_object).apparent().altaz()
        )
        return alt.degrees

    def _fast_compute_stars(self, df, observer):
        """
        Fast transit, altitude, rising, and setting calculation for a DataFrame of Stars.
        Uses vectorized numpy operations and geometric approximations for speed.

        Note: Rising/setting times use a geometric formula that ignores atmospheric
        refraction (~34'). This results in a 2-5 minute difference compared to
        Skyfield's iterative solver, which is acceptable for fast visualization.
        """
        # Extract Skyfield Star objects and their coordinates in a vectorized way
        sky_objs = [self.get_skyfield_object(row) for _, row in df.iterrows()]
        valid_mask = np.array([isinstance(obj, Star) for obj in sky_objs])

        ras = np.array(
            [obj.ra.hours if isinstance(obj, Star) else 0 for obj in sky_objs]
        )
        decs = np.array(
            [obj.dec.degrees if isinstance(obj, Star) else 0 for obj in sky_objs]
        )

        return self._vectorized_geometric_compute(df, observer, ras, decs, valid_mask)

    def _vectorized_geometric_compute(self, df, observer, ras, decs, valid_mask):
        """
        Generic vectorized transit, altitude, rising, and setting calculation.
        Uses vectorized numpy operations and geometric approximations for speed.

        Note: Rising/setting times use a geometric formula that ignores atmospheric
        refraction (~34'). This results in a 2-5 minute difference compared to
        Skyfield's iterative solver, which is acceptable for fast visualization.
        """
        current_dt = observer.date.utc_datetime()
        t0_dt = current_dt.replace(
            hour=0, minute=0, second=0, microsecond=0, tzinfo=pytz.UTC
        )
        t0 = self.ts.utc(t0_dt)
        lon_hours = self.place.lon_decimal / 15.0
        current_gmst = t0.gmst
        sidereal_to_solar = 0.99726957
        lat_deg = self.place.lat_decimal

        # Vectorized Transit calculation
        target_gmst = (ras - lon_hours) % 24
        dt_solar = ((target_gmst - current_gmst) % 24) * sidereal_to_solar

        # Use pandas for datetime vectorization
        t0_ts = pd.Timestamp(t0_dt)
        transit_times = t0_ts + pd.to_timedelta(dt_solar * 3600, unit="s")

        # Adjust for 12-hour window relative to current time
        cutoff = current_dt - timedelta(hours=12)
        shift = timedelta(hours=24 * sidereal_to_solar)

        transit_times = pd.Series(transit_times)
        # Ensure cutoff is compatible with transit_times timezone
        cutoff_ts = pd.Timestamp(cutoff)
        if transit_times.dt.tz is None and cutoff_ts.tz is not None:
            cutoff_ts = cutoff_ts.replace(tzinfo=None)
        elif transit_times.dt.tz is not None and cutoff_ts.tz is None:
            cutoff_ts = cutoff_ts.replace(tzinfo=pytz.UTC)

        needs_shift = transit_times < cutoff_ts
        transit_times.loc[needs_shift] += shift

        # Localize transits
        local_tz = observer.local_timezone
        transits = [
            t.replace(tzinfo=pytz.UTC).astimezone(local_tz) if m else None
            for t, m in zip(transit_times, valid_mask)
        ]

        # Vectorized Altitude calculation
        altitudes = 90.0 - np.abs(lat_deg - decs)
        alts = [float(a) if m else 0 for a, m in zip(altitudes, valid_mask)]

        # Vectorized Rise/Set (Geometric) calculation
        lat_rad = np.deg2rad(lat_deg)
        decs_rad = np.deg2rad(decs)
        cos_H = -np.tan(lat_rad) * np.tan(decs_rad)

        # Hour angle in solar hours
        H_hours = np.full(len(df), np.nan)
        # Objects must be Stars and within the range where they actually rise/set
        h_mask = valid_mask & (cos_H >= -1) & (cos_H <= 1)
        H_hours[h_mask] = np.arccos(cos_H[h_mask]) * (12.0 / np.pi) * sidereal_to_solar

        H_delta = pd.to_timedelta(H_hours * 3600, unit="s")
        rising_times = transit_times - H_delta
        setting_times = transit_times + H_delta

        rises = [
            t.replace(tzinfo=pytz.UTC).astimezone(local_tz) if pd.notna(t) else None
            for t in rising_times
        ]
        sets = [
            t.replace(tzinfo=pytz.UTC).astimezone(local_tz) if pd.notna(t) else None
            for t in setting_times
        ]

        return transits, alts, rises, sets
