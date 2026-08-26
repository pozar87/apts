from datetime import datetime, timedelta
from typing import Any, Optional, Tuple

import pandas as pd
import pytz
from skyfield import almanac
from skyfield.api import Star
from skyfield.searchlib import find_discrete

from ...utils.astronomy.refraction import calculate_refraction


def calculate_transit(
    skyfield_object: Any,
    eph: Any,
    location: Any,
    lat_decimal: float,
    lon_decimal: float,
    observer_date_dt: datetime,
    observer_local_timezone: Any,
    ts: Any,
) -> Optional[datetime]:
    """
    Calculates the upper meridian transit of a celestial object.
    For stars, a fast sidereal time approximation is used.
    """
    if skyfield_object is None:
        return None

    # Optimization for stars: use sidereal time formula
    if isinstance(skyfield_object, Star):
        current_dt = observer_date_dt
        t0_dt = current_dt.replace(
            hour=0, minute=0, second=0, microsecond=0, tzinfo=pytz.UTC
        )
        t0 = ts.utc(t0_dt)

        ra_hours = skyfield_object.ra.hours
        lon_hours = lon_decimal / 15.0

        target_gmst = (ra_hours - lon_hours) % 24
        current_gmst = t0.gmst

        sidereal_to_solar = 0.99726957

        dt_sidereal = (target_gmst - current_gmst) % 24
        dt_solar = dt_sidereal * sidereal_to_solar

        transit_dt = t0_dt + timedelta(hours=dt_solar)

        if transit_dt < current_dt - timedelta(hours=12):
            transit_dt += timedelta(hours=24 * sidereal_to_solar)

        return transit_dt.astimezone(observer_local_timezone)

    # Fallback for moving objects (planets)
    current_dt = observer_date_dt
    t0_dt = current_dt.replace(hour=0, minute=0, second=0, microsecond=0)
    t0 = ts.utc(t0_dt)
    t1 = ts.utc(t0_dt + timedelta(days=2))
    f = almanac.meridian_transits(eph, skyfield_object, location)
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
            .astimezone(observer_local_timezone)
        )

    return None


def calculate_rising_and_setting(
    skyfield_object: Any,
    eph: Any,
    location: Any,
    transit_time: Optional[datetime],
    observer_local_timezone: Any,
    ts: Any,
) -> Tuple[Optional[datetime], Optional[datetime]]:
    """
    Calculates rising and setting times for a celestial object relative to its transit time.
    """
    if skyfield_object is None or transit_time is None or pd.isna(transit_time):
        return None, None

    f = almanac.risings_and_settings(eph, skyfield_object, location)

    t_transit = ts.utc(transit_time)
    t0_rise = ts.utc(transit_time - timedelta(days=1))
    t_rise, y_rise = find_discrete(t0_rise, t_transit, f)

    rising_time = None
    rise_events = [t for t, y in zip(t_rise, y_rise) if y == 1]
    if rise_events:
        rising_time = (
            rise_events[-1]
            .utc_datetime()
            .replace(tzinfo=pytz.UTC)
            .astimezone(observer_local_timezone)
        )

    t1_set = ts.utc(transit_time + timedelta(days=1))
    t_set, y_set = find_discrete(t_transit, t1_set, f)

    setting_time = None
    set_events = [t for t, y in zip(t_set, y_set) if y == 0]
    if set_events:
        setting_time = (
            set_events[0]
            .utc_datetime()
            .replace(tzinfo=pytz.UTC)
            .astimezone(observer_local_timezone)
        )

    return rising_time, setting_time


def calculate_altitude_at_transit(
    skyfield_object: Any,
    transit: Optional[datetime],
    lat_decimal: float,
    observer_skyfield_obj: Any,
    ts: Any,
) -> float:
    """
    Calculates altitude of a celestial object at transit time.
    """
    if transit is None or pd.isna(transit):
        return 0.0

    if isinstance(skyfield_object, Star):
        dec = skyfield_object.dec.degrees
        true_alt = 90.0 - abs(lat_decimal - dec)
        return true_alt + calculate_refraction(true_alt)

    t = ts.utc(transit)
    alt, _, _ = (
        observer_skyfield_obj.at(t)
        .observe(skyfield_object)
        .apparent()
        .altaz(temperature_C=10.0, pressure_mbar=1013.25)
    )
    return float(alt.degrees)
