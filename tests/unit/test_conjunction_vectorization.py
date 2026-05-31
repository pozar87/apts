import unittest
from datetime import datetime, timedelta, timezone
from apts import Place
from apts.events import AstronomicalEvents
from apts.skyfield_searches.conjunctions import (
    find_conjunctions_between_moving_bodies,
    find_all_pairs_conjunctions
)
from apts.utils import planetary

class TestConjunctionVectorization(unittest.TestCase):
    def setUp(self):
        self.place = Place(lat=50.0647, lon=19.9450, name="Krakow", elevation=200)
        self.start_date = datetime(2025, 1, 1, tzinfo=timezone.utc)
        self.end_date = self.start_date + timedelta(days=30)
        self.ae = AstronomicalEvents(self.place, self.start_date, self.end_date)

    def tearDown(self):
        self.ae.shutdown()

    def test_vectorized_matches_iterative_planets(self):
        # We'll compare the results of find_all_pairs_conjunctions with
        # repeated calls to find_conjunctions_between_moving_bodies
        planets = ["mercury", "venus", "mars barycenter"]
        planets_data = {p: planetary.get_skyfield_obj(p) for p in planets}

        # 1. New fully vectorized approach (via find_all_pairs_conjunctions)
        vectorized_events = find_all_pairs_conjunctions(
            self.ae.observer,
            list(planets_data.items()),
            self.start_date,
            self.end_date,
            threshold_degrees=5.0
        )

        # 2. Hybrid approach (vectorized over time but iterative over pairs)
        iterative_events = []
        p_list = list(planets_data.items())
        for i in range(len(p_list)):
            for j in range(i + 1, len(p_list)):
                found = find_conjunctions_between_moving_bodies(
                    self.ae.observer,
                    p_list[i][0],
                    [p_list[j]],
                    self.start_date,
                    self.end_date,
                    threshold_degrees=5.0
                )
                for e in found:
                    e["object1"] = planetary.get_simple_name(p_list[i][0])
                    iterative_events.append(e)

        self.assertEqual(len(vectorized_events), len(iterative_events))

        # Sort both by date and compare
        vectorized_events.sort(key=lambda x: x["date"])
        iterative_events.sort(key=lambda x: x["date"])

        for v, i in zip(vectorized_events, iterative_events):
            self.assertEqual(v["object1"], i["object1"])
            self.assertEqual(v["object2"], i["object2"])
            self.assertAlmostEqual(v["separation_degrees"], i["separation_degrees"], places=5)
            self.assertEqual(v["date"], i["date"])

    def test_calculate_conjunctions_results(self):
        # Ensure AE.calculate_conjunctions returns expected events
        events = self.ae.calculate_conjunctions()
        self.assertTrue(len(events) > 0)
        for event in events:
            self.assertEqual(event["type"], "Conjunction")
            self.assertIn("object1", event)
            self.assertIn("object2", event)
            self.assertIn("separation_degrees", event)
            self.assertIsInstance(event["date"], datetime)

if __name__ == "__main__":
    unittest.main()
