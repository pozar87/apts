import unittest
from datetime import datetime, timezone
from unittest.mock import MagicMock

from apts.events.calculations.event import (
    DirectionData,
    build_event_description,
    build_event_title,
    extract_coordinates,
    extract_event_objects,
    format_angular_separation,
    get_direction_data,
    get_event_category,
    get_sky_brightness,
    get_step_by_step_guide,
    parse_event_datetime,
    resolve_event_topocentric_position,
)


class TestEventsCalculationsEvent(unittest.TestCase):

    def test_direction_data_to_dict(self):
        dd = DirectionData(code="NE", name="Look Northeast", azimuth_deg=45.123)
        self.assertEqual(
            dd.to_dict(),
            {"code": "NE", "name": "Look Northeast", "azimuth_deg": 45.1},
        )

    def test_get_sky_brightness(self):
        self.assertEqual(get_sky_brightness(None), "NIGHT_DARK")
        self.assertEqual(get_sky_brightness(0.0), "DAY")
        self.assertEqual(get_sky_brightness(-3.0), "CIVIL_TWILIGHT")
        self.assertEqual(get_sky_brightness(-10.0), "NAUTICAL_TWILIGHT")
        self.assertEqual(get_sky_brightness(-15.0), "ASTRONOMICAL_TWILIGHT")
        self.assertEqual(get_sky_brightness(-20.0, moon_alt_deg=10.0, moon_phase_frac=0.5), "NIGHT_MOONLIT")
        self.assertEqual(get_sky_brightness(-20.0, moon_alt_deg=10.0, moon_phase_frac=0.1), "NIGHT_DARK")

    def test_get_direction_data(self):
        d_east = get_direction_data(90.0)
        self.assertEqual(d_east.code, "E")

        d_north = get_direction_data(0.0)
        self.assertEqual(d_north.code, "N")

        d_nan = get_direction_data(float("nan"))
        self.assertEqual(d_nan.code, "E")

    def test_get_event_category(self):
        self.assertEqual(get_event_category("Lunar Occultation of Mars"), "OCCULTATION")
        self.assertEqual(get_event_category("Jupiter Conjunction"), "CONJUNCTION")
        self.assertEqual(get_event_category("Random Sky Event"), "CELESTIAL_EVENT")

    def test_get_step_by_step_guide(self):
        guide = get_step_by_step_guide("FLYBY", title="ISS Flyby")
        self.assertTrue(len(guide) > 0)

        guide_default = get_step_by_step_guide("UNKNOWN_CATEGORY", objects=["Mars"])
        self.assertTrue(len(guide_default) > 0)

    def test_build_event_description(self):
        desc = build_event_description(
            category="CONJUNCTION",
            title="Conjunction",
            objects=["Jupiter", "Saturn"],
            datetime_utc_str="2025-05-10T20:00:00Z",
            location_name="Warsaw",
            angular_separation="1.2°",
        )
        self.assertIn("Jupiter", desc)
        self.assertIn("Saturn", desc)

    def test_parse_event_datetime(self):
        dt = parse_event_datetime({"date": "2025-01-15T12:00:00Z"})
        self.assertEqual(dt.year, 2025)
        self.assertEqual(dt.tzinfo, timezone.utc)

    def test_extract_event_objects(self):
        objs = extract_event_objects({"object1": "Moon", "object2": "Venus"})
        self.assertEqual(objs, ["Moon", "Venus"])

    def test_build_event_title(self):
        title = build_event_title({}, ["Moon", "Mars"], "OCCULTATION", "Occultation")
        self.assertEqual(title, "Moon occultation of Mars")

    def test_format_angular_separation(self):
        sep_arcmin = format_angular_separation({"separation_degrees": 0.5})
        self.assertEqual(sep_arcmin, "30.0'")

        sep_deg = format_angular_separation({"separation_degrees": 2.5})
        self.assertEqual(sep_deg, "2.5°")

    def test_extract_coordinates(self):
        az, alt = extract_coordinates({"azimuth_deg": 180.0, "altitude_deg": 45.0})
        self.assertEqual(az, 180.0)
        self.assertEqual(alt, 45.0)

    def test_resolve_event_topocentric_position(self):
        place = MagicMock()
        ts_mock = MagicMock()
        place.ts = ts_mock
        place.get_altitude.side_effect = [15.0, 5.0, 30.0]
        place.get_azimuth.return_value = 120.0
        place.sun = "Sun"
        place.moon = "Moon"

        dt = datetime(2025, 5, 10, 20, 0, tzinfo=timezone.utc)
        sun_alt, moon_alt, alt, az = resolve_event_topocentric_position(
            place=place,
            dt_utc=dt,
            sun_alt=None,
            moon_alt=None,
            azimuth_deg=None,
            altitude_deg=None,
            objects=["Jupiter"],
        )
        self.assertEqual(sun_alt, 15.0)
        self.assertEqual(moon_alt, 5.0)
        self.assertEqual(alt, 30.0)
        self.assertEqual(az, 120.0)


if __name__ == "__main__":
    unittest.main()
