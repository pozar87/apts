from skyfield.api import Star, load, Topos
import numpy as np

ts = load.timescale()
eph = load('de421.bsp')
observer = eph['earth'] + Topos(latitude_degrees=52.2297, longitude_degrees=21.0122)

stars = Star(ra_hours=np.array([1.0, 2.0]), dec_degrees=np.array([10.0, 20.0]))
times = ts.utc(2025, 1, [1, 2, 3])

print(f"Number of stars: {len(stars.ra.hours)}")
print(f"Number of times: {len(times)}")

try:
    pos = observer.at(times).observe(stars)
    print("Vectorized observation successful")
except Exception as e:
    print(f"Vectorized observation failed: {e}")

for t in times:
    pos = observer.at(t).observe(stars)
    print(f"Observation at {t} successful, shape: {pos.position.au.shape}")
