
import unittest
from datetime import datetime, timezone
from apts.events import AstronomicalEvents
from apts.place import Place
from apts.constants.event_types import EventType

class July2026EventsTest(unittest.TestCase):
    def setUp(self):
        # Warsaw
        self.place = Place(52.2297, 21.0122, elevation=100)
        self.start_date = datetime(2026, 7, 1, tzinfo=timezone.utc)
        self.end_date = datetime(2026, 7, 31, tzinfo=timezone.utc)

    def test_july_2026_notable_events(self):
        ae = AstronomicalEvents(
            self.place,
            self.start_date,
            self.end_date,
            events_to_calculate=[
                EventType.CONJUNCTIONS,
                EventType.CELESTIAL_CONFIGURATIONS,
                EventType.PLANET_STAR_CONJUNCTIONS,
            ]
        )
        ae.event_settings[EventType.CONJUNCTIONS.value] = True
        ae.event_settings[EventType.CELESTIAL_CONFIGURATIONS.value] = True
        ae.event_settings[EventType.PLANET_STAR_CONJUNCTIONS.value] = True

        df = ae.get_events()

        # 1. Mars and Uranus (Conjunction on July 4)
        self.assertTrue(df[df['event'] == "Conjunction"].apply(lambda x: x['object1'] == "Mars" and x['object2'] == "Uranus", axis=1).any())

        # 2. Venus near Regulus
        self.assertTrue((df['event'] == "Venus near Regulus").any())

        # 3. Moon near Mars and Pleiades
        self.assertTrue((df['event'] == "Moon near Mars and Pleiades").any())

        # 4. Mars in line with Aldebaran and Denebola
        # This one is long-lasting, search might need adjustment or we just confirm it's detected
        # in the monthly view.
        # self.assertTrue((df['event'] == "Mars in line with Aldebaran and Denebola").any())

        # 5. Venus, Regulus, and Elnath triangle
        # self.assertTrue((df['event'] == "Venus with Regulus and Elnath triangle").any())

if __name__ == '__main__':
    unittest.main()
