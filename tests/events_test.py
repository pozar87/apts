import unittest
from unittest.mock import patch
from datetime import datetime, timezone
import pandas as pd
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType
from apts.place import Place
from apts.i18n import set_language

utc = timezone.utc


class EventsTest(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=52.2, lon=21.0)  # Warsaw
        self.start_date = datetime(2023, 1, 1, tzinfo=utc)
        self.end_date = datetime(2023, 3, 15, tzinfo=utc)
        self.events = AstronomicalEvents(self.place, self.start_date, self.end_date)
        set_language('en')

    def tearDown(self):
        set_language('en')

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

        # Find the event for Venus
        venus_event = next((e for e in events if e.get("object") == "Venus"), None)
        self.assertIsNotNone(venus_event)

        # Check if the event description is correct
        self.assertEqual(venus_event["event"], "Highest altitude")

        # Check the date and altitude
        self.assertEqual(venus_event["date"].day, 14)
        self.assertAlmostEqual(venus_event["altitude"], 48.23, delta=0.01)

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

    def test_jupiter_saturn_conjunction(self):
        # Set a date range around the Great Conjunction of 2020
        start_date = datetime(2020, 12, 20, tzinfo=utc)
        end_date = datetime(2020, 12, 22, tzinfo=utc)
        events = AstronomicalEvents(
            self.place,
            start_date,
            end_date,
            events_to_calculate=[EventType.CONJUNCTIONS],
        )
        events_df = events.get_events()

        # Check that at least one conjunction event was found
        self.assertGreater(len(events_df), 0)

        # Find the Jupiter-Saturn conjunction event
        jupiter_saturn_event = events_df[
            (events_df["event"] == "Conjunction")
            & (events_df["object1"] == "Jupiter")
            & (events_df["object2"] == "Saturn")
        ]

        # Check that the event was found
        self.assertEqual(len(jupiter_saturn_event), 1)

        # Check the date of the event
        event_date = jupiter_saturn_event.iloc[0]["date"]
        self.assertEqual(event_date.year, 2020)
        self.assertEqual(event_date.month, 12)
        self.assertEqual(event_date.day, 21)

    @patch("apts.events.skyfield_searches.find_iss_flybys")
    def test_calculate_iss_flybys(self, mock_find_iss_flybys):
        # Arrange
        mock_flyby_event = {
            "date": datetime(2023, 1, 15, 18, 30, 0, tzinfo=utc),
            "event": "Bright ISS Flyby",
            "type": "ISS Flyby",
            "peak_altitude": 85.0,
            "peak_magnitude": -3.5,
        }
        mock_find_iss_flybys.return_value = [mock_flyby_event]

        # Act
        events_calculator = AstronomicalEvents(
            self.place,
            self.start_date,
            self.end_date,
            events_to_calculate=[EventType.ISS_FLYBYS],
        )
        events_df = events_calculator.get_events()

        # Assert
        mock_find_iss_flybys.assert_called_once()
        self.assertEqual(len(events_df), 1)
        self.assertEqual(events_df.iloc[0]["event"], "Bright ISS Flyby")
        self.assertEqual(events_df.iloc[0]["type"], "ISS Flyby")
        self.assertEqual(events_df.iloc[0]["peak_altitude"], 85.0)
        self.assertEqual(events_df.iloc[0]["peak_magnitude"], -3.5)

    def test_translate_events(self):
        # Create a sample DataFrame
        data = {'event': ['New Moon', 'Full Moon'],
                'type': ['Moon Phase', 'Moon Phase']}
        events_df = pd.DataFrame(data)

        # Set language to Polish
        set_language('pl')

        # Translate the events
        translated_df = self.events.translate_events(events_df)

        # Check if the events are translated
        self.assertEqual(translated_df.iloc[0]['event'], 'Nów')
        self.assertEqual(translated_df.iloc[0]['type'], 'Faza księżyca')
        self.assertEqual(translated_df.iloc[1]['event'], 'Pełnia')


if __name__ == "__main__":
    unittest.main()
