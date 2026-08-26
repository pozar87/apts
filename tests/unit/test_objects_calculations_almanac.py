from datetime import datetime
import pytz
from skyfield.api import Star, wgs84
from apts.cache import get_timescale, get_ephemeris
from apts.objects.calculations.almanac import (
    calculate_transit,
    calculate_rising_and_setting,
    calculate_altitude_at_transit,
)


def test_calculate_transit_none():
    ts = get_timescale()
    res = calculate_transit(
        skyfield_object=None,
        eph=None,
        location=None,
        lat_decimal=52.23,
        lon_decimal=21.01,
        observer_date_dt=datetime.now(pytz.UTC),
        observer_local_timezone=pytz.UTC,
        ts=ts,
    )
    assert res is None


def test_calculate_transit_star():
    ts = get_timescale()
    star = Star(ra_hours=6.75, dec_degrees=-16.72)  # Sirius
    dt = datetime(2025, 3, 1, 20, 0, 0, tzinfo=pytz.UTC)

    transit = calculate_transit(
        skyfield_object=star,
        eph=None,
        location=None,
        lat_decimal=52.23,
        lon_decimal=21.01,
        observer_date_dt=dt,
        observer_local_timezone=pytz.UTC,
        ts=ts,
    )
    assert transit is not None
    assert isinstance(transit, datetime)


def test_calculate_transit_planet():
    ts = get_timescale()
    eph = get_ephemeris()
    jupiter = eph["jupiter barycenter"]
    location = wgs84.latlon(52.23, 21.01)
    dt = datetime(2025, 3, 1, 20, 0, 0, tzinfo=pytz.UTC)

    transit = calculate_transit(
        skyfield_object=jupiter,
        eph=eph,
        location=location,
        lat_decimal=52.23,
        lon_decimal=21.01,
        observer_date_dt=dt,
        observer_local_timezone=pytz.UTC,
        ts=ts,
    )
    assert transit is not None
    assert isinstance(transit, datetime)


def test_calculate_rising_and_setting_none_transit():
    ts = get_timescale()
    star = Star(ra_hours=6.75, dec_degrees=-16.72)
    rise, set_time = calculate_rising_and_setting(
        skyfield_object=star,
        eph=None,
        location=None,
        transit_time=None,
        observer_local_timezone=pytz.UTC,
        ts=ts,
    )
    assert rise is None
    assert set_time is None


def test_calculate_rising_and_setting_planet():
    ts = get_timescale()
    eph = get_ephemeris()
    jupiter = eph["jupiter barycenter"]
    location = wgs84.latlon(52.23, 21.01)
    dt = datetime(2025, 3, 1, 20, 0, 0, tzinfo=pytz.UTC)

    transit = calculate_transit(
        skyfield_object=jupiter,
        eph=eph,
        location=location,
        lat_decimal=52.23,
        lon_decimal=21.01,
        observer_date_dt=dt,
        observer_local_timezone=pytz.UTC,
        ts=ts,
    )
    assert transit is not None

    rise, set_time = calculate_rising_and_setting(
        skyfield_object=jupiter,
        eph=eph,
        location=location,
        transit_time=transit,
        observer_local_timezone=pytz.UTC,
        ts=ts,
    )
    assert rise is not None or set_time is not None


def test_calculate_altitude_at_transit_none():
    ts = get_timescale()
    star = Star(ra_hours=6.75, dec_degrees=-16.72)
    alt = calculate_altitude_at_transit(
        skyfield_object=star,
        transit=None,
        lat_decimal=52.23,
        observer_skyfield_obj=None,
        ts=ts,
    )
    assert alt == 0.0


def test_calculate_altitude_at_transit_star():
    ts = get_timescale()
    star = Star(ra_hours=6.75, dec_degrees=50.0)
    lat_decimal = 50.0
    transit = datetime(2025, 3, 1, 20, 0, 0, tzinfo=pytz.UTC)

    alt = calculate_altitude_at_transit(
        skyfield_object=star,
        transit=transit,
        lat_decimal=lat_decimal,
        observer_skyfield_obj=None,
        ts=ts,
    )
    # At lat 50, dec 50, max alt is 90 + refraction
    assert alt > 89.9


def test_calculate_altitude_at_transit_planet():
    ts = get_timescale()
    eph = get_ephemeris()
    jupiter = eph["jupiter barycenter"]
    location = wgs84.latlon(52.23, 21.01)
    dt = datetime(2025, 3, 1, 20, 0, 0, tzinfo=pytz.UTC)

    transit = calculate_transit(
        skyfield_object=jupiter,
        eph=eph,
        location=location,
        lat_decimal=52.23,
        lon_decimal=21.01,
        observer_date_dt=dt,
        observer_local_timezone=pytz.UTC,
        ts=ts,
    )
    assert transit is not None

    observer_skyfield_obj = eph["earth"] + location
    alt = calculate_altitude_at_transit(
        skyfield_object=jupiter,
        transit=transit,
        lat_decimal=52.23,
        observer_skyfield_obj=observer_skyfield_obj,
        ts=ts,
    )
    assert isinstance(alt, float)
