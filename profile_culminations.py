import time
from datetime import datetime, timezone, timedelta
from apts.place import Place
from apts.events import AstronomicalEvents
import logging

# Disable logging for cleaner output
logging.getLogger("apts").setLevel(logging.WARNING)

def profile_messier_culminations():
    place = Place(lat=52.2297, lon=21.0122, name="Warsaw")
    start_date = datetime(2025, 1, 1, tzinfo=timezone.utc)
    end_date = start_date + timedelta(days=7)

    events_calc = AstronomicalEvents(place, start_date, end_date)

    print(f"Profiling calculate_messier_culminations for 7 days...")

    # Original iterative approach (simulated by disabling fixed object optimization or using moving objects)
    # But wait, I want to compare with the PREVIOUS state of the code.
    # Since I already changed it, I can't easily run the old one unless I revert.
    # Alternatively, I can mock fixed objects as moving objects.

    # Mock messier objects as non-Stars to force iterative solver
    objects_data = [
        (row["Messier"], row["skyfield_object"])
        for _, row in events_calc.catalogs.MESSIER.iterrows()
    ]

    # To force iterative, we can use a proxy object that delegates everything but has no 'ra'
    class NonFixedProxy:
        def __init__(self, obj): self._obj = obj
        def __getattr__(self, name):
            if name == "ra": raise AttributeError("No RA")
            return getattr(self._obj, name)
        def _observe_from_bcrs(self, observer): return self._obj._observe_from_bcrs(observer)

    iterative_data = []
    for name, obj in objects_data:
        nf = NonFixedProxy(obj)
        iterative_data.append((name, nf))

    from apts import skyfield_searches

    print("Running iterative approach...")
    start_iter = time.time()
    events_iter = skyfield_searches.find_object_culminations(
        events_calc.observer, iterative_data, start_date, end_date
    )
    end_iter = time.time()
    print(f"Iterative: Found {len(events_iter)} events in {end_iter - start_iter:.4f}s")

    print("Running optimized approach...")
    start_opt = time.time()
    events_opt = events_calc.calculate_messier_culminations()
    end_opt = time.time()
    print(f"Optimized: Found {len(events_opt)} events in {end_opt - start_opt:.4f}s")

if __name__ == "__main__":
    profile_messier_culminations()
