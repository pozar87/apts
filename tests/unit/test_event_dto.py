from datetime import datetime, timezone
import json
import pytest

from apts.events import Event, EventExportData, DirectionData
from apts.events.event import get_direction_data, get_event_category, get_step_by_step_guide


def test_direction_data():
    dir_e = get_direction_data(90.0)
    assert dir_e.code == "E"
    assert dir_e.name == "Look East"
    assert dir_e.azimuth_deg == 90.0
    assert dir_e.to_dict() == {"code": "E", "name": "Look East", "azimuth_deg": 90.0}

    dir_n = get_direction_data(0.0)
    assert dir_n.code == "N"
    assert dir_n.name == "Look North"

    dir_sw = get_direction_data(225.0)
    assert dir_sw.code == "SW"
    assert dir_sw.name == "Look Southwest"


def test_event_category_mapping():
    assert get_event_category("Lunar occultation of Jupiter") == "OCCULTATION"
    assert get_event_category("Conjunction of Moon and Venus") == "CONJUNCTION"
    assert get_event_category("Perseids Meteor Shower") == "METEOR_SHOWER"
    assert get_event_category("Solar Eclipse") == "SOLAR_ECLIPSE"


def test_step_by_step_guide():
    occultation_guide = get_step_by_step_guide("OCCULTATION")
    assert len(occultation_guide) >= 4
    assert "Verify that the occultation is visible from your location." in occultation_guide[0]

    conjunction_guide = get_step_by_step_guide("CONJUNCTION")
    assert len(conjunction_guide) >= 4


def test_event_dto_serialization():
    dt = datetime(2026, 9, 8, 5, 50, tzinfo=timezone.utc)
    event = Event(
        category="OCCULTATION",
        title="Lunar occultation of Jupiter",
        datetime_utc=dt,
        best_viewing_time_local="05:50",
        location_name="Chicago",
        description="The Moon will pass in front of Jupiter.",
        angular_separation="10.3°",
        azimuth_deg=90.0,
        objects=["Moon", "Jupiter"],
    )

    d = event.to_dict()
    assert d["category"] == "OCCULTATION"
    assert d["title"] == "Lunar occultation of Jupiter"
    assert d["datetime_utc"] == "2026-09-08T05:50:00Z"
    assert d["best_viewing_time_local"] == "05:50"
    assert d["location_name"] == "Chicago"
    assert d["angular_separation"] == "10.3°"
    assert d["direction"]["code"] == "E"
    assert d["direction"]["name"] == "Look East"
    assert d["direction"]["azimuth_deg"] == 90.0
    assert isinstance(d["step_by_step_guide"], list)

    json_str = event.to_json()
    parsed = json.loads(json_str)
    assert parsed["title"] == "Lunar occultation of Jupiter"


def test_event_from_dict_and_row():
    raw_dict = {
        "event": "Conjunction",
        "type": "planetary",
        "object1": "Moon",
        "object2": "Venus",
        "date": "2026-09-08T05:50:00Z",
        "separation_degrees": 0.5,
        "azimuth": 135.0,
        "altitude": 20.0,
    }

    event = Event.from_dict(raw_dict)
    assert event.category == "CONJUNCTION"
    assert event.title == "Conjunction of Moon and Venus"
    assert event.angular_separation == "30.0'"
    assert event.direction.code == "SE"
    assert event.direction.name == "Look Southeast"
