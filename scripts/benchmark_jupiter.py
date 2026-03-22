import time
import numpy as np
from datetime import datetime, timezone
from apts.cache import get_timescale
from apts.utils.planetary import get_jupiter_system_ii_longitude

def benchmark():
    ts = get_timescale()
    # 1000 points over 10 days
    t0 = ts.utc(2026, 3, 1)
    t1 = ts.utc(2026, 3, 11)
    times = ts.linspace(t0, t1, 1000)

    print(f"Benchmarking get_jupiter_system_ii_longitude with {len(times)} points...")

    start = time.time()
    res = get_jupiter_system_ii_longitude(times)
    end = time.time()

    print(f"Time taken: {end - start:.4f} seconds")
    print(f"First 5 results: {res[:5]}")

if __name__ == "__main__":
    benchmark()
