import unittest
from datetime import datetime, timezone
from typing import Any, cast
from unittest.mock import patch

import pandas as pd

from apts.constants.event_types import EventType
from apts.events import AstronomicalEvents
from apts.i18n import language_context
from apts.place import Place

utc = timezone.utc


class EventsTest(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=52.2, lon=21.0)  # Warsaw
        self.start_date = datetime(2023, 1, 1, tzinfo=utc)
        self.end_date = datetime(2023, 3, 15, tzinfo=utc)
        self.events = AstronomicalEvents(self.place, self.start_date, self.end_date)

    def tearDown(self):
        pass

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
        self.assertTrue(all(events_df["rarity"] == 1))

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
        assert venus_event is not None
        self.assertIsNotNone(venus_event)

        # Check if the event description is correct
        self.assertEqual(venus_event["event"], "Highest altitude")
        self.assertEqual(venus_event["rarity"], 2)

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
        self.assertEqual(jupiter_saturn_event.iloc[0]["rarity"], 4)  # Very close

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
        self.assertEqual(events_df.iloc[0]["rarity"], 3)

    def test_translate_events(self):
        # Create a sample DataFrame
        data = {
            "event": ["New Moon", "Full Moon"],
            "type": ["Moon Phase", "Moon Phase"],
        }
        events_df = pd.DataFrame(data)

        # Translate the events in Polish context
        with language_context("pl"):
            translated_df = self.events.translate_events(events_df)

        # Check if the events are translated
        self.assertEqual(translated_df.iloc[0]["event"], "Nów")
        self.assertEqual(translated_df.iloc[0]["type"], "Faza Księżyca")
        self.assertEqual(translated_df.iloc[1]["event"], "Pełnia")

    def test_calculate_meteor_showers(self):
        # Perseids in 2023: Peak around August 12-13, Start July 17, End Aug 24
        start_date = datetime(2023, 7, 15, tzinfo=utc)
        end_date = datetime(2023, 8, 25, tzinfo=utc)
        events_calculator = AstronomicalEvents(
            self.place,
            start_date,
            end_date,
            events_to_calculate=[EventType.METEOR_SHOWERS],
        )
        events_df = events_calculator.get_events()

        # Check for Perseids events
        perseids_events = events_df[events_df["shower_name"] == "Perseids"]

        # All 3 phases should be in range now
        self.assertEqual(len(perseids_events), 3)
        self.assertEqual(
            cast(Any, perseids_events[perseids_events["phase"] == "Peak"]).iloc[0][
                "rarity"
            ],
            3,
        )
        self.assertEqual(
            cast(Any, perseids_events[perseids_events["phase"] == "Start"]).iloc[0][
                "rarity"
            ],
            1,
        )
        self.assertTrue(any(perseids_events["phase"] == "Start"))
        self.assertTrue(any(perseids_events["phase"] == "Peak"))
        self.assertTrue(any(perseids_events["phase"] == "End"))

    def test_calculate_oppositions(self):
        # Mars opposition in 2022: December 8
        start_date = datetime(2022, 12, 1, tzinfo=utc)
        end_date = datetime(2022, 12, 15, tzinfo=utc)
        events_calculator = AstronomicalEvents(
            self.place,
            start_date,
            end_date,
            events_to_calculate=[EventType.OPPOSITIONS],
        )
        events_df = events_calculator.get_events()

        # Check for Mars opposition
        mars_opposition = events_df[
            (events_df["type"] == "Opposition") & (events_df["object"] == "Mars")
        ]

        self.assertEqual(len(mars_opposition), 1)
        self.assertEqual(mars_opposition.iloc[0]["rarity"], 3)
        # Check date: should be 2022-12-08
        event_date = mars_opposition.iloc[0]["date"]
        self.assertEqual(event_date.year, 2022)
        self.assertEqual(event_date.month, 12)
        self.assertEqual(event_date.day, 8)

    @patch("apts.events.skyfield_searches.find_conjunctions_with_star")
    def test_calculate_moon_messier_conjunctions(self, mock_find_conj):
        # Arrange
        mock_find_conj.return_value = [
            {
                "date": datetime(2023, 1, 20, 12, 0, 0, tzinfo=utc),
                "separation_degrees": 2.5,
            }
        ]

        # Act
        events_calculator = AstronomicalEvents(
            self.place,
            self.start_date,
            self.end_date,
            events_to_calculate=[EventType.MOON_MESSIER_CONJUNCTIONS],
        )
        events_df = events_calculator.get_events()

        # Assert
        # It should call find_conjunctions_with_star for several Messier objects
        self.assertGreater(mock_find_conj.call_count, 0)
        self.assertGreater(len(events_df), 0)
        messier_events = events_df[events_df["type"] == "Moon-Messier Conjunction"]
        self.assertGreater(len(messier_events), 0)
        self.assertEqual(messier_events.iloc[0]["object1"], "Moon")
        self.assertEqual(messier_events.iloc[0]["separation_degrees"], 2.5)
        self.assertEqual(messier_events.iloc[0]["rarity"], 2)

    def test_calculate_moon_star_conjunctions(self):
        # Moon-Antares conjunction in 2023: August 25 around 02:00-03:00 UTC
        start_date = datetime(2023, 8, 24, tzinfo=utc)
        end_date = datetime(2023, 8, 26, tzinfo=utc)

        events_calculator = AstronomicalEvents(
            self.place,
            start_date,
            end_date,
            events_to_calculate=[EventType.MOON_STAR_CONJUNCTIONS],
        )
        events_df = events_calculator.get_events()

        # Check for Moon-Antares conjunction
        antares_conjunction = events_df[
            (events_df["type"] == "Moon-Star Conjunction")
            & (events_df["object2"] == "Antares")
        ]

        self.assertGreater(len(antares_conjunction), 0)
        # Check date: should be 2023-08-25
        event_date = antares_conjunction.iloc[0]["date"]
        self.assertEqual(event_date.year, 2023)
        self.assertEqual(event_date.month, 8)
        self.assertEqual(event_date.day, 25)
        self.assertLess(antares_conjunction.iloc[0]["separation_degrees"], 2.0)
        self.assertEqual(antares_conjunction.iloc[0]["rarity"], 3)

    def test_planet_alignment(self):
        # Great planetary alignment of Feb 28, 2026
        # We use a window that covers the end of February to catch the alignment on Feb 28
        start_date = datetime(2026, 2, 20, tzinfo=utc)
        end_date = datetime(2026, 2, 28, 23, 59, 59, tzinfo=utc)
        events_calculator = AstronomicalEvents(
            self.place,
            start_date,
            end_date,
            events_to_calculate=[EventType.PLANET_ALIGNMENTS],
        )
        events_df = events_calculator.get_events()

        # Check for the alignment event
        alignment_events = events_df[events_df["type"] == "Planet Alignment"]
        self.assertGreaterEqual(len(alignment_events), 1)

        # Check if it correctly identified the number of planets
        # The Feb 28 alignment has 7 planets
        feb_28_alignment = alignment_events[
            cast(Any, alignment_events["date"]).dt.day == 28
        ]
        self.assertEqual(len(feb_28_alignment), 1)
        self.assertIn("7 planets", cast(Any, feb_28_alignment).iloc[0]["event"])
        self.assertEqual(cast(Any, feb_28_alignment).iloc[0]["rarity"], 5)

        # Check planets involved
        planets_involved = cast(Any, feb_28_alignment).iloc[0]["planets"]
        self.assertIn("Mercury", planets_involved)
        self.assertIn("Venus", planets_involved)
        self.assertIn("Mars", planets_involved)
        self.assertIn("Jupiter", planets_involved)
        self.assertIn("Saturn", planets_involved)
        self.assertIn("Uranus", planets_involved)
        self.assertIn("Neptune", planets_involved)


if __name__ == "__main__":
    unittest.main()
