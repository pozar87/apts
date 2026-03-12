from skyfield.api import Star, load, Topos
from datetime import datetime, timezone, timedelta
import numpy as np

ts = load.timescale()
eph = load('de421.bsp')
observer = eph['earth'] + Topos(latitude_degrees=52.2297, longitude_degrees=21.0122)

m31 = Star(ra_hours=(0, 42, 44.3), dec_degrees=(41, 16, 9))

t_ref = ts.utc(2025, 1, 1, 12)
pos = observer.at(t_ref).observe(m31).apparent()
# LST = RA is for local RA.
ra, dec, dist = pos.radec(epoch='date')
print(f"Apparent RA (epoch date): {ra.hours}")

# Analytical using apparent RA
lon_hours = observer.target.longitude.hours
target_gast = (ra.hours - lon_hours) % 24
diff_gast = (target_gast - t_ref.gast) % 24
t_culm_tt = t_ref.tt + (diff_gast / 1.0027379) / 24.0
t_culm = ts.tt_jd(t_culm_tt)

alt = observer.at(t_culm).observe(m31).apparent().altaz()[0].degrees
print(f"Altitude at analytical culm: {alt}")

# Check with slightly different times
for offset in [-60, -30, -10, -1, 0, 1, 10, 30, 60]:
    t = ts.tt_jd(t_culm.tt + offset/86400.0)
    a = observer.at(t).observe(m31).apparent().altaz()[0].degrees
    print(f"  Offset {offset}s: {a}")
