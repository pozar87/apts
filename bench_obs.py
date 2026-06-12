import time
import datetime
import pandas as pd
from apts.place import Place
from apts.observations.base import Observation
from apts.catalogs import Catalogs
from apts.opticalequipment import Telescope, Camera
from apts.optics import OpticalPath

def benchmark():
    place = Place(52.2297, 21.0122, "Warsaw")

    telescope = Telescope(100, 550)
    camera = Camera(23.5, 15.7, 6248, 4176)

    equipment = OpticalPath(telescope, [], [], [], [], camera)

    catalogs = Catalogs()

    target_date = datetime.date(2025, 3, 20)

    print("Benchmarking Observation initialization and catalog access...")

    start = time.time()
    obs = Observation(place, equipment, target_date=target_date)
    init_time = time.time() - start
    print(f"Observation init time: {init_time:.4f}s")

    start = time.time()
    visible_messier = obs.get_visible_messier()
    messier_time = time.time() - start
    print(f"get_visible_messier time: {messier_time:.4f}s ({len(visible_messier)} objects)")

    start = time.time()
    visible_planets = obs.get_visible_planets()
    planets_time = time.time() - start
    print(f"get_visible_planets time: {planets_time:.4f}s ({len(visible_planets)} objects)")

    # Test get_visible_ngc (this is usually the slowest)
    start = time.time()
    visible_ngc = obs.get_visible_ngc()
    ngc_time = time.time() - start
    print(f"get_visible_ngc time: {ngc_time:.4f}s ({len(visible_ngc)} objects)")

    # Repeat to check for lazy loading impact
    print("\nSecond pass (cached):")
    start = time.time()
    obs.get_visible_messier()
    print(f"get_visible_messier time: {time.time() - start:.4f}s")

if __name__ == "__main__":
    benchmark()
