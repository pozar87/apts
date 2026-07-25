import pandas as pd
import pytz
from datetime import timedelta
from skyfield import almanac
from skyfield.api import Star
from skyfield.searchlib import find_discrete
from .utils import calculate_refraction


class AlmanacMixIn:
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
            t0_dt = current_dt.replace(
                hour=0, minute=0, second=0, microsecond=0, tzinfo=pytz.UTC
            )
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
            # Add refraction for better accuracy
            true_alt = 90.0 - abs(lat - dec)
            return true_alt + calculate_refraction(true_alt)

        t = self.ts.utc(transit)
        alt, _, _ = (
            self.place.observer.at(t)
            .observe(skyfield_object)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)
        )
        return alt.degrees
