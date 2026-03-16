import unittest
from datetime import datetime, timezone
from apts.place import Place
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType

utc = timezone.utc

class TestStationaryPoints(unittest.TestCase):
    def test_mars_stationary_2025(self):
        # Mars becomes stationary (retrograde) around Dec 2024,
        # and stationary (direct) around Feb 24, 2025.
        place = Place(lat=52.2, lon=21.0)
        start_date = datetime(2025, 2, 20, tzinfo=utc)
        end_date = datetime(2025, 3, 1, tzinfo=utc)

        ae = AstronomicalEvents(place, start_date, end_date, events_to_calculate=[EventType.PLANET_STATIONARY_POINTS])
        df = ae.get_events()

        # Check for Mars stationary point
        mars_stationary = df[df['object'] == 'Mars']
        self.assertFalse(mars_stationary.empty)
        self.assertIn('Stationary', mars_stationary.iloc[0]['event'])
        # Precise date is Feb 24
        self.assertEqual(mars_stationary.iloc[0]['date'].day, 24)

if __name__ == '__main__':
    unittest.main()
