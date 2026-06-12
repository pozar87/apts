import time
from apts.place import Place
from apts.catalogs import Catalogs
from apts.objects.messier import Messier
from skyfield.api import load
import numpy as np

def test():
    place = Place(52.2297, 21.0122, "Warsaw")
    catalogs = Catalogs()
    messier = Messier(place, catalogs)

    stars = messier.objects

    # Simulate extraction in get_visible_stars
    start = time.time()
    for _ in range(100):
        stars_ras = [obj.ra.hours for obj in stars["skyfield_object"]]
        stars_decs = [obj.dec.degrees for obj in stars["skyfield_object"]]
    print(f"List comprehension extraction x 100: {time.time() - start:.4f}s")

    start = time.time()
    for _ in range(100):
        stars_ras = stars["ra_hours"].to_numpy()
        stars_decs = stars["dec_degrees"].to_numpy()
    print(f"Vectorized extraction x 100: {time.time() - start:.4f}s")

if __name__ == "__main__":
    test()
