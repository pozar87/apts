import datetime
import pytz
from skyfield import almanac
from skyfield.api import Topos, Time
from ...cache import get_timescale, get_ephemeris

def previous_setting_time_utc(lat, lon, elevation, obj_name, start, horizon_degrees=None):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))
    obj = eph[obj_name]

    if isinstance(start, Time):
        t1 = start
        t0 = ts.tt_jd(t1.tt - 2.0)
    else:
        t1 = ts.utc(start)
        t0 = ts.utc(start - datetime.timedelta(days=2))

    if horizon_degrees is not None:
        f = almanac.risings_and_settings(eph, obj, location, horizon_degrees=horizon_degrees)
    else:
        f = almanac.risings_and_settings(eph, obj, location)
    t, y = almanac.find_discrete(t0, t1, f)

    if t is None:
        return None

    settings = [ti for ti, yi in zip(t, y) if yi == 0]
    if settings:
        return settings[-1].utc_datetime().replace(tzinfo=pytz.UTC)
    return None

def next_rising_time_utc(lat, lon, elevation, obj_name, start, horizon_degrees=None):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))
    obj = eph[obj_name]

    if isinstance(start, Time):
        t0 = start
        t1 = ts.tt_jd(t0.tt + 2.0)
    else:
        t0 = ts.utc(start)
        t1 = ts.utc(start + datetime.timedelta(days=2))

    if horizon_degrees is not None:
        f = almanac.risings_and_settings(eph, obj, location, horizon_degrees=horizon_degrees)
    else:
        f = almanac.risings_and_settings(eph, obj, location)
    t, y = almanac.find_discrete(t0, t1, f)

    if t is not None:
        for ti, yi in zip(t, y):
            if yi == 1:  # Rising
                return ti.utc_datetime().replace(tzinfo=pytz.UTC)
    return None

def next_setting_time_utc(lat, lon, elevation, obj_name, start, horizon_degrees=None):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))
    obj = eph[obj_name]

    if isinstance(start, Time):
        t0 = start
        t1 = ts.tt_jd(t0.tt + 2.0)
    else:
        t0 = ts.utc(start)
        t1 = ts.utc(start + datetime.timedelta(days=2))

    if horizon_degrees is not None:
        f = almanac.risings_and_settings(eph, obj, location, horizon_degrees=horizon_degrees)
    else:
        f = almanac.risings_and_settings(eph, obj, location)
    t, y = almanac.find_discrete(t0, t1, f)

    if t is not None:
        for ti, yi in zip(t, y):
            if yi == 0:  # Setting
                return ti.utc_datetime().replace(tzinfo=pytz.UTC)
    return None

def previous_rising_time_utc(lat, lon, elevation, obj_name, start, horizon_degrees=None):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))
    obj = eph[obj_name]

    if isinstance(start, Time):
        t1 = start
        t0 = ts.tt_jd(t1.tt - 2.0)
    else:
        t1 = ts.utc(start)
        t0 = ts.utc(start - datetime.timedelta(days=2))

    if horizon_degrees is not None:
        f = almanac.risings_and_settings(eph, obj, location, horizon_degrees=horizon_degrees)
    else:
        f = almanac.risings_and_settings(eph, obj, location)
    t, y = almanac.find_discrete(t0, t1, f)

    if t is None:
        return None

    risings = [ti for ti, yi in zip(t, y) if yi == 1]
    if risings:
        return risings[-1].utc_datetime().replace(tzinfo=pytz.UTC)
    return None
