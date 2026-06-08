from skyfield.api import load, Topos
from skyfield.api import Star
import numpy as np

ts = load.timescale()
eph = load('de421.bsp')
earth = eph['earth']
observer = earth + Topos('50.0 N', '20.0 E')
planets = [eph['mercury'], eph['venus'], eph['mars barycenter'], eph['jupiter barycenter']]
t = ts.now()

print("Testing individual observations:")
for p in planets:
    pos = observer.at(t).observe(p).apparent()
    alt, az, _ = pos.altaz()
    print(f"{p}: {alt.degrees}")

print("\nTesting vectorized observation attempt with multiple bodies:")
try:
    # Skyfield does NOT support a list of different bodies in observe()
    pos = observer.at(t).observe(planets)
    print("Vectorized planets work!")
except Exception as e:
    print(f"Vectorized planets failed: {e}")
