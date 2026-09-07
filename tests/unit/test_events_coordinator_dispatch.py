import unittest
from unittest.mock import MagicMock

from apts.events.coordinator.dispatch import build_event_dispatch_map


class TestEventsCoordinatorDispatch(unittest.TestCase):
    def test_build_event_dispatch_map(self):
        mock_events = MagicMock()
        mock_precomputed = {"mars": MagicMock()}

        dispatch_map = build_event_dispatch_map(mock_events, mock_precomputed)

        # Ensure dispatch_map is a dictionary with expected keys
        self.assertIsInstance(dispatch_map, dict)
        expected_keys = [
            "moon_phases",
            "conjunctions",
            "oppositions",
            "meteor_showers",
            "highest_altitudes",
            "lunar_occultations",
            "aphelion_perihelion",
            "moon_apogee_perigee",
            "mercury_inferior_conjunctions",
            "moon_messier_conjunctions",
            "moon_star_conjunctions",
            "space_launches",
            "space_events",
            "iss_flybys",
            "tiangong_flybys",
            "solar_eclipses",
            "lunar_eclipses",
            "nasa_comets",
            "planet_alignments",
            "lunar_planetary_occultations",
            "messier_culminations",
            "jovian_moon_events",
            "saturn_ring_crossings",
            "jupiter_grs_transits",
            "planet_messier_conjunctions",
            "planet_star_conjunctions",
            "planet_stationary_points",
            "planet_solar_conjunctions",
            "lunar_features",
            "moon_libration_maxima",
            "planet_planet_occultations",
            "venus_great_brilliancy",
            "supermoons",
            "mars_closest_approach",
            "jovian_mutual_events",
            "greatest_elongations",
            "planetary_dichotomy",
            "seasons",
            "culminations",
            "celestial_configurations",
        ]

        for key in expected_keys:
            self.assertIn(key, dispatch_map)
            self.assertTrue(callable(dispatch_map[key]))

        # Test execution of lambda/wrapped dispatchers
        dispatch_map["conjunctions"]()
        mock_events.calculate_conjunctions.assert_called_once_with(mock_precomputed)

        dispatch_map["planetary_dichotomy"]()
        mock_events.calculate_planetary_dichotomy.assert_called_once_with(mock_precomputed)


if __name__ == "__main__":
    unittest.main()
