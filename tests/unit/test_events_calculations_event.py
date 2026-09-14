import math
from datetime import datetime, timezone

from apts.events.calculations.event import (
    DirectionData,
    _build_event_title,
    _extract_coordinates,
    _extract_event_objects,
    _format_angular_separation,
    _parse_event_datetime,
    build_event_description,
    get_direction_data,
    get_event_category,
    get_sky_brightness,
    get_step_by_step_guide,
)

utc = timezone.utc


def test_direction_data_to_dict():
    dd = DirectionData(code="NE", name="Look Northeast", azimuth_deg=45.123)
    d = dd.to_dict()
    assert d == {"code": "NE", "name": "Look Northeast", "azimuth_deg": 45.1}


def test_get_sky_brightness_classifications():
    # Day: sun alt >= -0.833
    assert get_sky_brightness(0.0) == "DAY"
    assert get_sky_brightness(-0.5) == "DAY"

    # Civil twilight: -6.0 <= sun alt < -0.833
    assert get_sky_brightness(-3.0) == "CIVIL_TWILIGHT"

    # Nautical twilight: -12.0 <= sun alt < -6.0
    assert get_sky_brightness(-9.0) == "NAUTICAL_TWILIGHT"

    # Astronomical twilight: -18.0 <= sun alt < -12.0
    assert get_sky_brightness(-15.0) == "ASTRONOMICAL_TWILIGHT"

    # Night moonlit vs dark
    assert get_sky_brightness(-25.0, moon_alt_deg=30.0, moon_phase_frac=0.5) == "NIGHT_MOONLIT"
    assert get_sky_brightness(-25.0, moon_alt_deg=-10.0, moon_phase_frac=0.5) == "NIGHT_DARK"
    assert get_sky_brightness(-25.0, moon_alt_deg=30.0, moon_phase_frac=0.1) == "NIGHT_DARK"
    assert get_sky_brightness(None) == "NIGHT_DARK"


def test_get_direction_data_cardinals():
    dir_e = get_direction_data(90.0)
    assert dir_e.code == "E"
    assert dir_e.azimuth_deg == 90.0

    dir_n = get_direction_data(0.0)
    assert dir_n.code == "N"

    dir_nnw = get_direction_data(330.0)
    assert dir_nnw.code == "NNW"

    dir_none = get_direction_data(None)
    assert dir_none.code == "E"

    dir_nan = get_direction_data(math.nan)
    assert dir_nan.code == "E"


def test_get_event_category_rules():
    assert get_event_category("Lunar occultation") == "OCCULTATION"
    assert get_event_category("Planetary Conjunction") == "CONJUNCTION"
    assert get_event_category("Perseids Meteor Shower") == "METEOR_SHOWER"
    assert get_event_category("Total Solar Eclipse") == "SOLAR_ECLIPSE"
    assert get_event_category("Falcon 9 Launch") == "ROCKET_LAUNCH"
    assert get_event_category("ISS Flyby") == "FLYBY"
    assert get_event_category("Vernal Equinox") == "EQUINOX_SOLSTICE"
    assert get_event_category("Full Moon") == "MOON_PHASE"
    assert get_event_category("Supermoon") == "SUPERMOON"
    assert get_event_category("Unknown Cosmic Motion") == "CELESTIAL_EVENT"


def test_get_step_by_step_guide_categories():
    guide_flyby = get_step_by_step_guide("FLYBY", title="ISS Pass")
    assert len(guide_flyby) >= 4

    guide_launch = get_step_by_step_guide("ROCKET_LAUNCH", title="Rocket Launch")
    assert len(guide_launch) >= 3

    guide_shower = get_step_by_step_guide("METEOR_SHOWER", title="Geminids")
    assert len(guide_shower) >= 4

    guide_eclipse = get_step_by_step_guide("SOLAR_ECLIPSE")
    assert any("solar filter" in g.lower() for g in guide_eclipse)

    guide_default = get_step_by_step_guide("CUSTOM", title="Random Event", objects=["Mars"])
    assert len(guide_default) >= 3


def test_build_event_description_formats():
    desc_occ = build_event_description("OCCULTATION", "Occultation", ["Moon", "Mars"], "2026-09-08T12:00:00Z", "Paris")
    assert "Moon" in desc_occ and "Mars" in desc_occ and "Paris" in desc_occ

    desc_conj = build_event_description("CONJUNCTION", "Conjunction", ["Venus", "Jupiter"], "2026-09-08T12:00:00Z", "Tokyo", angular_separation="0.5°")
    assert "Venus" in desc_conj and "Jupiter" in desc_conj and "0.5°" in desc_conj

    desc_shower = build_event_description("METEOR_SHOWER", "Perseids", ["Perseids"], "2026-09-08T12:00:00Z", "London")
    assert "Perseids" in desc_shower

    desc_gen = build_event_description("CELESTIAL_EVENT", "Comet Visit", ["Comet C/2023"], "2026-09-08T12:00:00Z", "Berlin")
    assert "Comet Visit" in desc_gen and "Berlin" in desc_gen


def test_event_extraction_helpers():
    # _parse_event_datetime
    dt_now = datetime.now(utc)
    parsed_iso = _parse_event_datetime({"date": "2026-09-08T15:30:00Z"})
    assert parsed_iso.year == 2026 and parsed_iso.month == 9 and parsed_iso.day == 8 and parsed_iso.hour == 15

    parsed_dt = _parse_event_datetime({"date": dt_now})
    assert parsed_dt == dt_now

    # _extract_event_objects
    objs1 = _extract_event_objects({"object1": "Moon", "object2": "Saturn"})
    assert objs1 == ["Moon", "Saturn"]

    objs2 = _extract_event_objects({"event": "Full Moon"})
    assert objs2 == ["Moon"]

    # _build_event_title
    t1 = _build_event_title({}, ["Moon", "Jupiter"], "OCCULTATION", "Occultation")
    assert t1 == "Moon occultation of Jupiter"

    t2 = _build_event_title({"title": "Custom Title"}, ["Moon"], "MOON_PHASE", "Full Moon")
    assert t2 == "Custom Title"

    # _format_angular_separation
    assert _format_angular_separation({"separation_degrees": 0.5}) == "30.0'"
    assert _format_angular_separation({"separation_degrees": 2.5}) == "2.5°"
    assert _format_angular_separation({"angular_separation": "15'"}) == "15'"

    # _extract_coordinates
    az, alt = _extract_coordinates({"azimuth": 180.0, "altitude": 45.0})
    assert az == 180.0 and alt == 45.0
