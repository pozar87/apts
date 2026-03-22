import unittest
from datetime import datetime, timezone
from apts.place import Place
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType

utc = timezone.utc

class VenusBrilliancyTest(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=52.2, lon=21.0) # Warsaw

    def test_venus_greatest_brilliancy_2025(self):
        # Venus greatest brilliancy occurs around Feb 15-20, 2025
        start_date = datetime(2025, 2, 1, tzinfo=utc)
        end_date = datetime(2025, 3, 1, tzinfo=utc)

        events = AstronomicalEvents(self.place, start_date, end_date,
                                   events_to_calculate=[EventType.VENUS_GREAT_BRILLIANCY])
        df = events.get_events()

        self.assertFalse(df.empty)
        brilliancy_event = df[df['type'] == 'Venus Greatest Brilliancy']
        self.assertFalse(brilliancy_event.empty)

        event_date = brilliancy_event.iloc[0]['date']
        self.assertEqual(event_date.year, 2025)
        self.assertEqual(event_date.month, 2)
        # Expected around Feb 18 based on my previous calculation
        self.assertIn(event_date.day, [15, 16, 17, 18, 19, 20])
        self.assertLess(brilliancy_event.iloc[0]['magnitude'], -4.8)

if __name__ == '__main__':
    unittest.main()
