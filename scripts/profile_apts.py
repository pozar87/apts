import time
from datetime import datetime
from apts.place import Place
from apts.equipment import Equipment
from apts.observations import Observation
from apts.conditions import Conditions


def profile():
    lat, lon = 52.2297, 21.0122  # Warsaw
    place = Place(lat, lon, name="Warsaw")
    equipment = Equipment()  # Default equipment
    conditions = Conditions()

    start_time = time.time()
    obs = Observation(place, equipment, conditions, target_date=datetime.now().date())
    print(f"Observation init took: {time.time() - start_time:.4f}s")

    start_time = time.time()
    messier = obs.get_visible_messier()
    print(
        f"get_visible_messier took: {time.time() - start_time:.4f}s (found {len(messier)})"
    )

    start_time = time.time()
    planets = obs.get_visible_planets()
    print(
        f"get_visible_planets took: {time.time() - start_time:.4f}s (found {len(planets)})"
    )
    print(f"Visible planets: {planets['Name'].tolist()}")

    start_time = time.time()
    # NGC might be slow if not filtered
    ngc = obs.get_visible_ngc()
    print(f"get_visible_ngc took: {time.time() - start_time:.4f}s (found {len(ngc)})")

    start_time = time.time()
    obs.get_weather_analysis()
    print(f"get_weather_analysis took: {time.time() - start_time:.4f}s")


if __name__ == "__main__":
    profile()
