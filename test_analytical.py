from skyfield.api import Star, load, Topos
from datetime import datetime, timezone, timedelta
import numpy as np

ts = load.timescale()
eph = load('de421.bsp')
observer = eph['earth'] + Topos(latitude_degrees=52.2297, longitude_degrees=21.0122)

# M31
m31 = Star(ra_hours=(0, 42, 44.3), dec_degrees=(41, 16, 9))
t0 = ts.utc(2025, 1, 1)
t1 = ts.utc(2025, 1, 8)

# Analytical
lon_hours = observer.target.longitude.hours
ra_hours = m31.ra.hours

# For each day
days = np.arange(7)
t_refs = ts.utc(2025, 1, 1 + days)
gmst_refs = t_refs.gmst
target_gmst = (ra_hours - lon_hours) % 24
diff_gmst = (target_gmst - gmst_refs) % 24
# The Earth rotates 360.9856 degrees per UT day
# 1 UT hour = 1.0027379 sidereal hours
# So Delta t (UT) = Delta GMST / 1.0027379
t_culms = ts.utc(2025, 1, 1 + days + (diff_gmst / 1.0027379) / 24.0)

# Check altitudes
alts = observer.at(t_culms).observe(m31).apparent().altaz()[0].degrees
print(f"Altitudes at analytical culminations: {alts}")

# Compare with find_maxima
from skyfield.searchlib import find_maxima
def alt_func(t):
    return observer.at(t).observe(m31).apparent().altaz()[0].degrees
setattr(alt_func, 'step_days', 0.5)
tm, am = find_maxima(t0, t1, alt_func)
print(f"Altitudes at find_maxima: {am}")
# Match counts
n = min(len(t_culms), len(tm))
print(f"Time differences (seconds): {(t_culms.tt[:n] - tm.tt[:n]) * 86400}")
