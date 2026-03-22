import unittest
from datetime import datetime, timezone
from apts.place import Place
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType

utc = timezone.utc

class MeteorVisibilityTest(unittest.TestCase):
    def setUp(self):
        # Place in Southern Hemisphere to check Perseids visibility (radiant is far North)
        self.place_south = Place(lat=-45.0, lon=170.0) # New Zealand
        # Place in Northern Hemisphere
        self.place_north = Place(lat=52.0, lon=21.0) # Warsaw

    def test_perseids_visibility_2024(self):
        # Perseids peak around Aug 12, 2024
        start_date = datetime(2024, 8, 11, tzinfo=utc)
        end_date = datetime(2024, 8, 13, tzinfo=utc)

        # North visibility check
        events_north = AstronomicalEvents(self.place_north, start_date, end_date,
                                          events_to_calculate=[EventType.METEOR_SHOWERS])
        df_north = events_north.get_events()
        perseids_peak_north = df_north[(df_north['shower_name'] == 'Perseids') & (df_north['phase'] == 'Peak')]
        self.assertFalse(perseids_peak_north.empty)
        # Perseids radiant is at +58 Dec, so it's always up in Warsaw or at least visible at peak if peak is at night
        # We need to check if it's visible at the exact peak time

        # South visibility check
        events_south = AstronomicalEvents(self.place_south, start_date, end_date,
                                          events_to_calculate=[EventType.METEOR_SHOWERS])
        df_south = events_south.get_events()
        perseids_peak_south = df_south[(df_south['shower_name'] == 'Perseids') & (df_south['phase'] == 'Peak')]

        # In NZ (-45 lat), Perseids (+58 Dec) radiant is never above horizon (max alt = -45 + (90-58) = -13 approx)
        # So it should be invisible.
        if not perseids_peak_south.empty:
            self.assertEqual(perseids_peak_south.iloc[0]['is_visible'], False)
            self.assertLess(perseids_peak_south.iloc[0]['altitude'], 0)

if __name__ == '__main__':
    unittest.main()
