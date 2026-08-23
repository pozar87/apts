from datetime import datetime, timezone
import unittest

from apts.events.calculations import (
    calculate_event_duration,
    calculate_event_rarity,
    get_duration,
    get_rarity,
)


class TestEventCalculationsEvaluations(unittest.TestCase):

    def test_calculate_event_rarity_conjunctions(self):
        self.assertEqual(calculate_event_rarity("Conjunction", {"separation_degrees": 0.10}), 5)
        self.assertEqual(calculate_event_rarity("Conjunction", {"separation_degrees": 0.30}), 4)
        self.assertEqual(calculate_event_rarity("Conjunction", {"separation_degrees": 0.80}), 3)
        self.assertEqual(calculate_event_rarity("Conjunction", {"separation_degrees": 1.80}), 2)
        self.assertEqual(calculate_event_rarity("Conjunction", {"separation_degrees": 3.50}), 1)
        self.assertEqual(calculate_event_rarity("Conjunction", {}), 1)

    def test_calculate_event_rarity_oppositions_and_alignments(self):
        self.assertEqual(calculate_event_rarity("Opposition", {"object": "Mars"}), 4)
        self.assertEqual(calculate_event_rarity("Opposition", {"object": "Moon"}), 3)
        self.assertEqual(calculate_event_rarity("Planet Alignment", {"planets": ["A", "B", "C", "D", "E", "F"]}), 5)
        self.assertEqual(calculate_event_rarity("Planet Alignment", {"planets": ["A", "B", "C", "D", "E"]}), 4)
        self.assertEqual(calculate_event_rarity("Planet Alignment", {"planets": ["A", "B", "C", "D"]}), 3)
        self.assertEqual(calculate_event_rarity("Planet Alignment", {"planets": ["A", "B", "C"]}), 2)

    def test_calculate_event_rarity_eclipses_and_transits(self):
        self.assertEqual(calculate_event_rarity("Solar Eclipse", {"eclipse_type": "Total Solar Eclipse"}), 5)
        self.assertEqual(calculate_event_rarity("Solar Eclipse", {"eclipse_type": "Partial Solar Eclipse"}), 4)
        self.assertEqual(calculate_event_rarity("Lunar Eclipse", {"eclipse_kind": "Total Lunar Eclipse"}), 5)
        self.assertEqual(calculate_event_rarity("Lunar Eclipse", {"eclipse_kind": "Partial Lunar Eclipse"}), 4)
        self.assertEqual(calculate_event_rarity("Lunar Eclipse", {"eclipse_kind": "Penumbral"}), 3)
        self.assertEqual(calculate_event_rarity("Inferior Conjunction", {"is_transit": True}), 5)
        self.assertEqual(calculate_event_rarity("Inferior Conjunction", {"is_transit": False}), 3)

    def test_calculate_event_rarity_flybys_and_unknown(self):
        self.assertEqual(calculate_event_rarity("ISS Flyby", {"peak_magnitude": -4.0}), 4)
        self.assertEqual(calculate_event_rarity("ISS Flyby", {"peak_magnitude": -2.0}), 3)
        self.assertEqual(calculate_event_rarity("ISS Flyby", {"peak_magnitude": 1.0}), 1)
        self.assertEqual(calculate_event_rarity("Unknown Event Type", {}), 1)

    def test_calculate_event_duration_dynamic(self):
        t1 = datetime(2025, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        t2 = datetime(2025, 1, 1, 12, 10, 0, tzinfo=timezone.utc)

        self.assertEqual(
            calculate_event_duration("ISS Flyby", {"rise_time": t1, "set_time": t2}),
            600,
        )
        self.assertEqual(
            calculate_event_duration("Lunar Occultation", {"ingress_time": t1, "egress_time": t2}),
            600,
        )

    def test_calculate_event_duration_defaults(self):
        self.assertEqual(calculate_event_duration("ISS Flyby", {}), 600)
        self.assertEqual(calculate_event_duration("Lunar Occultation", {}), 3600)
        self.assertEqual(calculate_event_duration("Solar Eclipse", {}), 7200)
        self.assertEqual(calculate_event_duration("Lunar Eclipse", {}), 14400)
        self.assertEqual(calculate_event_duration("Moon-Star Conjunction", {}), 172800)
        self.assertEqual(calculate_event_duration("Opposition", {}), 259200)
        self.assertEqual(calculate_event_duration("Moon Phase", {}), 86400)

    def test_backward_compatibility_aliases(self):
        self.assertEqual(get_rarity("Comet", {}), 5)
        self.assertEqual(get_duration("Golden Hour", {}), 3600)


if __name__ == "__main__":
    unittest.main()
