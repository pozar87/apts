import unittest
from datetime import datetime, timezone
from apts.events import AstronomicalEvents
from apts.place import Place
from apts.constants.event_types import EventType

utc = timezone.utc

class PlanetaryDichotomyTest(unittest.TestCase):
    def setUp(self):
        # Observer at Greenwich
        self.place = Place(lat=51.4778, lon=-0.0015)
        # Venus dichotomy occurs around January 11, 2025 (Western Elongation/Evening sky)
        # and again around June 1, 2025 (Eastern Elongation/Morning sky)
        self.start_date = datetime(2025, 1, 1, tzinfo=utc)
        self.end_date = datetime(2025, 2, 1, tzinfo=utc)

    def test_venus_dichotomy_2025(self):
        events_calculator = AstronomicalEvents(
            self.place,
            self.start_date,
            self.end_date,
            events_to_calculate=[EventType.PLANETARY_DICHOTOMY],
        )
        events_df = events_calculator.get_events()

        # Find Venus dichotomy events
        venus_dichotomies = events_df[
            (events_df["type"] == "Planetary Dichotomy") &
            (events_df["object"] == "Venus")
        ]

        self.assertGreaterEqual(len(venus_dichotomies), 1)

        # Verify approximate date (around January 11, 2025)
        event_date = venus_dichotomies.iloc[0]["date"]
        self.assertEqual(event_date.year, 2025)
        self.assertEqual(event_date.month, 1)
        self.assertTrue(8 <= event_date.day <= 15)

        # Verify event name
        self.assertIn("Venus Dichotomy", venus_dichotomies.iloc[0]["event"])

    def test_precomputation_integration(self):
        # This test ensures that enabling dichotomy triggers pre-computation
        # (indirectly verified by ensuring it doesn't crash and returns results)
        events_calculator = AstronomicalEvents(
            self.place,
            self.start_date,
            self.end_date,
            events_to_calculate=[EventType.PLANETARY_DICHOTOMY],
        )
        # We can also check if CONJUNCTION_EVENTS includes it
        self.assertIn("planetary_dichotomy", events_calculator.CONJUNCTION_EVENTS)

        events_df = events_calculator.get_events()
        self.assertFalse(events_df.empty)

if __name__ == "__main__":
    unittest.main()
