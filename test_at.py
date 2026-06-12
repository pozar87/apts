import time
from apts.place import Place
from skyfield.api import load

def test():
    place = Place(52.2297, 21.0122, "Warsaw")
    ts = load.timescale()
    t_start = ts.utc(2025, 3, 20, 18, 0)
    t_stop = ts.utc(2025, 3, 21, 6, 0)
    check_times = ts.linspace(t_start, t_stop, 100)

    start = time.time()
    for _ in range(100):
        _ = place.observer.at(check_times)
    print(f"observer.at(100 points) x 100: {time.time() - start:.4f}s")

if __name__ == "__main__":
    test()
