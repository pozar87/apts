from datetime import datetime, timezone
from apts.events.calculations.event import (
    build_event_title,
    extract_coordinates,
    extract_event_objects,
    format_angular_separation,
    parse_event_datetime,
    resolve_event_topocentric_position,
)

utc = timezone.utc


def test_parse_event_datetime():
    data_str = {"date": "2025-05-10T20:00:00Z"}
    dt = parse_event_datetime(data_str)
    assert dt.year == 2025
    assert dt.month == 5
    assert dt.day == 10
    assert dt.hour == 20
    assert dt.tzinfo == utc

    data_dt = {"datetime_utc": datetime(2025, 6, 15, 12, 0, tzinfo=utc)}
    dt2 = parse_event_datetime(data_dt)
    assert dt2 == datetime(2025, 6, 15, 12, 0, tzinfo=utc)


def test_extract_event_objects():
    data1 = {"object1": "Moon", "object2": "Jupiter"}
    objs1 = extract_event_objects(data1)
    assert objs1 == ["Moon", "Jupiter"]

    data2 = {"event": "Full Moon"}
    objs2 = extract_event_objects(data2)
    assert objs2 == ["Moon"]

    data3 = {"shower_name": "Perseids"}
    objs3 = extract_event_objects(data3)
    assert objs3 == ["Perseids"]


def test_build_event_title():
    data = {"title": "Explicit Title"}
    assert build_event_title(data, ["Moon"], "MOON_PHASE", "Full Moon") == "Explicit Title"

    data_occultation = {}
    title_occ = build_event_title(data_occultation, ["Moon", "Jupiter"], "OCCULTATION", "Lunar Occultation")
    assert title_occ == "Moon occultation of Jupiter"


def test_format_angular_separation():
    data_deg = {"separation_degrees": 2.5}
    assert format_angular_separation(data_deg) == "2.5°"

    data_arcmin = {"separation_degrees": 0.25}
    assert format_angular_separation(data_arcmin) == "15.0'"

    data_explicit = {"angular_separation": "1° 30'"}
    assert format_angular_separation(data_explicit) == "1° 30'"


def test_extract_coordinates():
    data = {"azimuth": 180.5, "altitude": 45.0}
    az, alt = extract_coordinates(data)
    assert az == 180.5
    assert alt == 45.0


def test_resolve_event_topocentric_position():
    class DummyPlace:
        def __init__(self):
            self.sun = "Sun"
            self.moon = "Moon"
            self.ts = self

        def utc(self, y, m, d, h, min, s):
            return self

        def get_altitude(self, obj, t):
            if obj == "Sun":
                return -10.0
            if obj == "Moon":
                return 15.0
            if obj == "Jupiter":
                return 30.0
            return 0.0

        def get_azimuth(self, obj, t):
            if obj == "Jupiter":
                return 120.0
            return 0.0

    place = DummyPlace()
    dt = datetime(2025, 5, 1, 21, 0, tzinfo=utc)
    sun_alt, moon_alt, alt_deg, az_deg = resolve_event_topocentric_position(place, dt, ["Jupiter"])
    assert sun_alt == -10.0
    assert moon_alt == 15.0
    assert alt_deg == 30.0
    assert az_deg == 120.0
