import time
import cProfile
import pstats
import io
from datetime import datetime, timezone
from apts.place import Place
from apts.objects.solar_objects import SolarObjects
from apts.conditions import Conditions

def profile_planets():
    lat, lon = 52.2297, 21.0122  # Warsaw
    place = Place(lat, lon, name="Warsaw")
    conditions = Conditions()

    now = datetime.now(timezone.utc)

    print("Initializing SolarObjects...")
    start_time = time.time()
    planets = SolarObjects(place, calculation_date=now, lazy=True)
    print(f"SolarObjects init (lazy=True) took: {time.time() - start_time:.4f}s")

    print("\nProfiling SolarObjects.get_visible...")
    start = now
    stop = start.replace(hour=23, minute=59)
    if stop < start:
        from datetime import timedelta
        stop += timedelta(days=1)

    pr = cProfile.Profile()
    pr.enable()
    visible = planets.get_visible(conditions, start, stop)
    pr.disable()

    print(f"get_visible took: {time.time() - start_time:.4f}s")

    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats(20)
    print(s.getvalue())

if __name__ == "__main__":
    profile_planets()
