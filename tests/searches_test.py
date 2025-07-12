import unittest
from datetime import datetime
from apts.events import AstronomicalEvents
from apts.place import Place

class SearchesTest(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=52.2, lon=21.0) # Warsaw
        self.start_date = datetime(2023, 1, 1)
        self.end_date = datetime(2023, 12, 31)
        self.events = AstronomicalEvents(self.place, self.start_date, self.end_date)

    def test_conjunctions(self):
        events_df = self.events.get_events()
        self.assertIn('event', events_df.columns)

    def test_oppositions(self):
        events_df = self.events.get_events()
        self.assertIn('event', events_df.columns)

if __name__ == '__main__':
    unittest.main()
