import time
from datetime import datetime, timedelta
import pytz
from apts.place import Place
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType

def benchmark_events_subset():
    place = Place(lat=52.2, lon=21.0, name="Warsaw")
    start = datetime.now(pytz.UTC)
    end = start + timedelta(days=30)

    # Only Moon Phase
    events_to_calc = [EventType.MOON_PHASES]

    # Warm up
    ae = AstronomicalEvents(place, start, end, events_to_calculate=events_to_calc)
    ae.get_events()

    start_t = time.perf_counter()
    for _ in range(10):
        ae = AstronomicalEvents(place, start, end, events_to_calculate=events_to_calc)
        ae.get_events()
    end_t = time.perf_counter()
    print(f"Time for 10 calls (Moon phases only): {end_t - start_t:.4f}s")

if __name__ == "__main__":
    benchmark_events_subset()
