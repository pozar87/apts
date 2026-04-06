import unittest
from datetime import datetime, timezone
from unittest.mock import patch, MagicMock
from apts.utils import planetary
from apts.events import AstronomicalEvents
from apts.place import Place
from apts.constants.event_types import EventType


class TestAstronomicalEvents(unittest.TestCase):
    def setUp(self):
        self.place = Place(
            name="Test Place",
            lat=34.0522,
            lon=-118.2437,
            elevation=100,
            date=datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
        )
        self.start_date = datetime(2024, 1, 1, tzinfo=timezone.utc)
        self.end_date = datetime(2024, 1, 31, tzinfo=timezone.utc)

    @patch("apts.events.coordinator.as_completed")
    @patch("apts.events.coordinator.get_event_settings")
    def test_get_events_parallelization(
        self, mock_get_event_settings, mock_as_completed
    ):
        # Configure mock_get_event_settings to return all events enabled
        mock_get_event_settings.return_value = {
            "moon_phases": True,
            "conjunctions": True,
            "oppositions": True,
            "meteor_showers": True,
            "highest_altitudes": True,
            "lunar_occultations": True,
            "aphelion_perihelion": True,
            "moon_apogee_perigee": True,
            "mercury_inferior_conjunctions": True,
            "moon_messier_conjunctions": True,
            "moon_star_conjunctions": True,
            "space_launches": True,
            "space_events": True,
            "iss_flybys": True,
            "tiangong_flybys": True,
            "solar_eclipses": True,
            "lunar_eclipses": True,
            "nasa_comets": True,
            "planet_alignments": True,
            "lunar_planetary_occultations": True,
            "messier_culminations": True,
            "golden_hour": True,
            "blue_hour": True,
            "culminations": True,
            "greatest_elongations": True,
            "seasons": True,
            "jovian_moon_events": True,
            "saturn_ring_crossings": True,
            "jupiter_grs_transits": True,
            "planet_messier_conjunctions": True,
            "planet_star_conjunctions": True,
            "planet_stationary_points": True,
            "planet_solar_conjunctions": True,
            "lunar_features": True,
            "planet_planet_occultations": True,
            "mars_closest_approach": True,
            "jovian_mutual_events": True,
            "moon_libration_maxima": True,
            "venus_great_brilliancy": True,
            "supermoons": True,
            "planetary_dichotomy": True,
        }

        # Instantiate AstronomicalEvents AFTER patching
        events_instance = AstronomicalEvents(self.place, self.start_date, self.end_date)

        # Mock the executor instance that the 'with' statement will use
        events_instance.executor = MagicMock()
        mock_executor_instance = events_instance.executor

        # Create a list of mock futures for all calculation methods
        # Counting how many 'if self.event_settings.get(...):' are in get_events()
        # Blocks:
        # 1-20: basic events
        # 21: messier_culminations
        # 22: jovian_moon_events
        # 23: saturn_ring_crossings
        # 24: jupiter_grs_transits
        # 25: planet_messier_conjunctions
        # 26: planet_star_conjunctions
        # 27: planet_stationary_points
        # 28: planet_solar_conjunctions
        # 29: golden_blue_hours
        # 30: culminations
        # 31: greatest_elongations
        # 32: seasons
        # 33: lunar_features
        # 34: planet_planet_occultations
        # 35: venus_greatest_brilliancy
        # 36: supermoons
        # 37: planetary_dichotomy
        # 38: mars_closest_approach
        # 39: jovian_mutual_events
        # 40: moon_libration_maxima
        num_events = 40
        mock_futures = [MagicMock() for _ in range(num_events)]
        for future in mock_futures:
            future.result.return_value = []

        # Have the submit method return a different mock future each time
        mock_executor_instance.submit.side_effect = mock_futures

        # Pre-computation futures (for the 8 bodies)
        num_precompute = 8
        precompute_mock_futures = [MagicMock() for _ in range(num_precompute)]
        for i, (future, name) in enumerate(
            zip(
                precompute_mock_futures,
                list(planetary.CONJUNCTION_PLANETS.keys()) + ["moon"],
            )
        ):
            future.result.return_value = (name.lower(), MagicMock())

        # Combine pre-computation and main event futures
        all_mock_futures = precompute_mock_futures + mock_futures
        mock_executor_instance.submit.side_effect = all_mock_futures

        # have as_completed return all mock futures in two separate batches as expected by get_events
        def mock_as_completed_side_effect(futures_list):
            return iter(futures_list)

        mock_as_completed.side_effect = mock_as_completed_side_effect

        events_instance.get_events()

        # Check that submit was called for each calculation method + precompute
        self.assertEqual(
            mock_executor_instance.submit.call_count, num_events + num_precompute
        )
        # Check that as_completed was called twice
        self.assertEqual(mock_as_completed.call_count, 2)

    @patch("apts.events.coordinator.as_completed")
    def test_get_events_with_enum_selection(self, mock_as_completed):
        # Instantiate AstronomicalEvents with a selection of events
        events_instance = AstronomicalEvents(
            self.place,
            self.start_date,
            self.end_date,
            events_to_calculate=[EventType.CONJUNCTIONS, EventType.OPPOSITIONS],
        )

        events_instance.executor = MagicMock()
        mock_executor_instance = events_instance.executor

        mock_futures = [MagicMock(), MagicMock()]
        for future in mock_futures:
            future.result.return_value = []

        mock_executor_instance.submit.side_effect = mock_futures
        mock_as_completed.return_value = iter(mock_futures)

        events_instance.get_events()

        # Check that submit was called only for the selected events
        self.assertEqual(mock_executor_instance.submit.call_count, 2)
        mock_as_completed.assert_called_once()
        self.assertEqual(len(mock_as_completed.call_args[0][0]), 2)


if __name__ == "__main__":
    unittest.main()
