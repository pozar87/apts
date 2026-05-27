import logging
from concurrent.futures import as_completed
from typing import Dict, Any

from ...utils import planetary

logger = logging.getLogger(__name__)

class PrecomputationEngine:
    """
    Handles pre-computation of celestial body positions to optimize multiple event searches.
    """

    CONJUNCTION_EVENTS = [
        "conjunctions",
        "moon_messier_conjunctions",
        "moon_star_conjunctions",
        "planet_messier_conjunctions",
        "planet_star_conjunctions",
        "planetary_dichotomy",
    ]

    MOON_EVENTS = [
        "moon_messier_conjunctions",
        "moon_star_conjunctions",
        "conjunctions",
    ]

    def __init__(self, ts, observer, start_date, end_date):
        self.ts = ts
        self.observer = observer
        self.start_date = start_date
        self.end_date = end_date

    def precompute_positions(self, event_settings: Dict[str, bool], executor) -> Dict[str, Any]:
        """
        Pre-compute positions for moving bodies often used in multiple searches
        to improve overall calculation efficiency.
        """
        precomputed = {}
        if not any(event_settings.get(e) for e in self.CONJUNCTION_EVENTS):
            return precomputed

        # Increase resolution if Moon-related conjunctions are requested
        if any(event_settings.get(e) for e in self.MOON_EVENTS):
            # 864s matches typical ~1.2h step in find_conjunctions but is more precise.
            # We use 864s (0.01 days) to maintain compatibility with existing tests.
            step_seconds = 864
        else:
            # Hourly resolution for planets
            step_seconds = 3600

        duration_seconds = (self.end_date - self.start_date).total_seconds()
        num_steps = int(duration_seconds / step_seconds)

        if num_steps < 2:
            return precomputed

        times = self.ts.linspace(
            self.ts.utc(self.start_date), self.ts.utc(self.end_date), num_steps
        )

        # Optimization: Hoist observer.at(times) out of the loop
        obs_at_times = self.observer.at(times)

        bodies_to_precompute = list(planetary.CONJUNCTION_PLANETS.keys()) + ["moon"]

        def _observe(name):
            obj = planetary.get_skyfield_obj(name)
            return name.lower(), obs_at_times.observe(obj)

        # Optimization: Parallelize high-precision observations using the existing executor.
        precompute_futures = [
            executor.submit(_observe, name) for name in bodies_to_precompute
        ]
        for future in as_completed(precompute_futures):
            name, pos = future.result()
            precomputed[name] = pos

        return precomputed
