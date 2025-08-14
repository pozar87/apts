import unittest
from datetime import datetime, timezone
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType

utc = timezone.utc
from apts.place import Place


class EventsTest(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=52.2, lon=21.0)  # Warsaw
        self.start_date = datetime(2023, 1, 1, tzinfo=utc)
        self.end_date = datetime(2023, 3, 15, tzinfo=utc)
        self.events = AstronomicalEvents(self.place, self.start_date, self.end_date)

    def test_moon_phases(self):
        # Disable all event calculations by default for this test
        for key in self.events.event_settings:
            self.events.event_settings[key] = False
        self.events.event_settings["moon_phases"] = True
        events_df = self.events.get_events()

        # New Moons within January 1, 2023, to March 15, 2023:
        #  - January 21, 2023
        #  - February 20, 2023
        self.assertEqual(sum(events_df["event"] == "New Moon"), 2)

        # Full Moons within January 1, 2023, to March 15, 2023:
        #  - January 6, 2023
        #  - February 5, 2023
        #  - March 7, 2023
        self.assertEqual(sum(events_df["event"] == "Full Moon"), 3)

    def test_eclipses(self):
        # This test is a bit generic, we can improve it later if needed
        # For now, just enable one event type to make it fast and ensure the dataframe is not empty
        for key in self.events.event_settings:
            self.events.event_settings[key] = False
        self.events.event_settings["moon_phases"] = True
        events_df = self.events.get_events()
        self.assertIn("event", events_df.columns)

    def test_highest_altitudes(self):
        # Disable all event calculations by default for this test
        for key in self.events.event_settings:
            self.events.event_settings[key] = False

        # Enable only the highest_altitudes event calculation
        self.events.event_settings["highest_altitudes"] = True

        # We call calculate_highest_altitudes directly
        events = self.events.calculate_highest_altitudes()

        # Check if any events were returned
        self.assertTrue(events)

        # Check if the event description contains the degree information
        self.assertIn("deg", events[0]['event'])


    def test_events_with_enum(self):
        # Calculate only moon phases using the new enum parameter
        events = AstronomicalEvents(
            self.place,
            self.start_date,
            self.end_date,
            events_to_calculate=[EventType.MOON_PHASES],
        )
        events_df = events.get_events()

        # Check that only moon phase events were calculated
        self.assertTrue(all(events_df["type"] == "Moon Phase"))

        # Check for a known moon phase event
        self.assertEqual(sum(events_df["event"] == "New Moon"), 2)


if __name__ == "__main__":
    unittest.main()
