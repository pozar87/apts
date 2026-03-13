import unittest
from datetime import datetime, timezone
from apts.place import Place
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType
from apts.cache import get_timescale, get_ephemeris
from skyfield.api import Topos
import numpy as np

utc = timezone.utc

class OraclePrecisionTest(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=52.2, lon=21.0) # Warsaw
        self.ts = get_timescale()
        self.eph = get_ephemeris()
        self.observer = self.eph['earth'] + Topos(
            latitude_degrees=self.place.lat_decimal,
            longitude_degrees=self.place.lon_decimal
        )

    def test_conjunction_precision_refinement(self):
        # Great Conjunction of 2020
        start_date = datetime(2020, 12, 21, 0, 0, tzinfo=utc)
        end_date = datetime(2020, 12, 22, 0, 0, tzinfo=utc)

        events = AstronomicalEvents(self.place, start_date, end_date, events_to_calculate=[EventType.CONJUNCTIONS])
        df = events.get_events()

        # Filter for Jupiter-Saturn
        js_event = df[(df['object1'] == 'Jupiter') & (df['object2'] == 'Saturn')]
        self.assertFalse(js_event.empty)

        event_time = js_event.iloc[0]['date']

        # Reference high-precision check
        jupiter = self.eph['jupiter barycenter']
        saturn = self.eph['saturn barycenter']

        def get_sep(t_dt):
            t = self.ts.from_datetime(t_dt)
            p1 = self.observer.at(t).observe(jupiter).apparent()
            p2 = self.observer.at(t).observe(saturn).apparent()
            return p1.separation_from(p2).degrees

        # Check that we are indeed very close to the minimum
        sep_at_event = get_sep(event_time)

        # Check 1 minute before and after in 1-second steps
        offsets = np.linspace(-60, 60, 121)
        for offset in offsets:
            t_test = datetime.fromtimestamp(event_time.timestamp() + offset, tz=utc)
            sep_test = get_sep(t_test)
            # Separation at predicted time should be <= any nearby time (within numerical precision)
            self.assertGreaterEqual(sep_test, sep_at_event - 1e-7)

    def test_planet_messier_conjunction(self):
        # Mars passing through the Pleiades (M45) in early March 2021
        start_date = datetime(2021, 3, 1, tzinfo=utc)
        end_date = datetime(2021, 3, 10, tzinfo=utc)

        events = AstronomicalEvents(self.place, start_date, end_date, events_to_calculate=[EventType.PLANET_MESSIER_CONJUNCTIONS])
        df = events.get_events()

        # Check for Mars-M45 conjunction
        m45_conj = df[(df['object1'] == 'Mars') & (df['object2'] == 'M45')]
        self.assertFalse(m45_conj.empty)

        # Should be around March 4, 2021
        self.assertEqual(m45_conj.iloc[0]['date'].day, 4)
        self.assertLess(m45_conj.iloc[0]['separation_degrees'], 3.0)

    def test_occultation_ingress_egress(self):
        # Lunar occultation of Mars: Dec 8, 2022 (visible from Warsaw)
        start_date = datetime(2022, 12, 8, 0, 0, tzinfo=utc)
        end_date = datetime(2022, 12, 8, 12, 0, tzinfo=utc)

        events = AstronomicalEvents(self.place, start_date, end_date, events_to_calculate=[EventType.LUNAR_PLANETARY_OCCULTATIONS])
        df = events.get_events()

        # Check for Mars occultation
        mars_occ = df[df['object2'] == 'Mars']
        self.assertFalse(mars_occ.empty)

        event = mars_occ.iloc[0]
        self.assertIn('ingress_time', event)
        self.assertIn('egress_time', event)
        self.assertIsNotNone(event['ingress_time'])
        self.assertIsNotNone(event['egress_time'])

        # Ingress around 05:00 UTC, Egress around 05:55 UTC
        self.assertEqual(event['ingress_time'].hour, 5)
        self.assertEqual(event['egress_time'].hour, 5)

if __name__ == '__main__':
    unittest.main()
