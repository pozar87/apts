from skyfield.api import Star, load, Topos
from datetime import datetime, timezone, timedelta
import numpy as np

ts = load.timescale()
eph = load('de421.bsp')
observer = eph['earth'] + Topos(latitude_degrees=52.2297, longitude_degrees=21.0122)

m31 = Star(ra_hours=(0, 42, 44.3), dec_degrees=(41, 16, 9))
t0 = ts.utc(2025, 1, 1)
t1 = ts.utc(2025, 1, 8)

from skyfield.searchlib import find_maxima
def alt_func(t):
    return observer.at(t).observe(m31).apparent().altaz()[0].degrees
setattr(alt_func, 'step_days', 0.5)
tm, am = find_maxima(t0, t1, alt_func)

print(f"find_maxima count: {len(tm)}")
for t, a in zip(tm, am):
    print(f"  {t.utc_iso()} Alt: {a:.4f}")

# Analytical
lon_hours = observer.target.longitude.hours

day_offsets = np.arange(9) # Check 9 days to be sure
t_refs = ts.utc(2025, 1, 1 + day_offsets - 1, 12)
all_culms = []
for t_ref in t_refs:
    ra_now = observer.at(t_ref).observe(m31).apparent().radec(epoch='date')[0].hours
    target_gast = (ra_now - lon_hours) % 24
    diff_gast = (target_gast - t_ref.gast) % 24
    t_est_tt = t_ref.tt + (diff_gast / 1.0027379) / 24.0
    t_est = ts.tt_jd(t_est_tt)
    for _ in range(1):
        ra_now = observer.at(t_est).observe(m31).apparent().radec(epoch='date')[0].hours
        target_gast = (ra_now - lon_hours) % 24
        diff = (target_gast - t_est.gast + 12) % 24 - 12
        t_est_tt = t_est.tt + (diff / 1.0027379) / 24.0
        t_est = ts.tt_jd(t_est_tt)
    if t0.tt <= t_est_tt <= t1.tt:
        all_culms.append(t_est)

print(f"Analytical count: {len(all_culms)}")
for t in all_culms:
    a = observer.at(t).observe(m31).apparent().altaz()[0].degrees
    print(f"  {t.utc_iso()} Alt: {a:.4f}")
