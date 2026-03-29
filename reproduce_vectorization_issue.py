import datetime
import numpy as np
from apts.utils import planetary
from apts.cache import get_timescale

ts = get_timescale()
times = ts.utc(2024, 1, [1, 2])

print("Testing get_planet_angular_diameter with vector time...")
try:
    diam = planetary.get_planet_angular_diameter("Jupiter", times)
    print(f"Result type: {type(diam)}")
    print(f"Result: {diam}")
except Exception as e:
    print(f"Error: {e}")

print("\nTesting get_saturn_ring_details with vector time...")
try:
    details = planetary.get_saturn_ring_details(times)
    print(f"Result: {details}")
except Exception as e:
    print(f"Error: {e}")
