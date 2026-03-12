from skyfield.api import Star, load, Topos
from datetime import datetime, timezone, timedelta
import numpy as np

ts = load.timescale()
eph = load('de421.bsp')
observer = eph['earth'] + Topos(latitude_degrees=52.2297, longitude_degrees=21.0122)

m31 = Star(ra_hours=(0, 42, 44.3), dec_degrees=(41, 16, 9))
t0 = ts.utc(2025, 1, 1)

lon_hours = observer.target.longitude.hours

def get_culm_for_time(t_ref):
    # Apparent RA at t_ref
    ra_hours = observer.at(t_ref).observe(m31).apparent().radec()[0].hours
    target_gast = (ra_hours - lon_hours) % 24
    diff_gast = (target_gast - t_ref.gast) % 24
    t_culm_tt = t_ref.tt + (diff_gast / 1.0027379) / 24.0
    t_culm = ts.tt_jd(t_culm_tt)
    # Refine
    for _ in range(2):
        ra_hours = observer.at(t_culm).observe(m31).apparent().radec()[0].hours
        target_gast = (ra_hours - lon_hours) % 24
        gast_now = t_culm.gast
        diff = (target_gast - gast_now + 12) % 24 - 12
        t_culm_tt = t_culm.tt + (diff / 1.0027379) / 24.0
        t_culm = ts.tt_jd(t_culm_tt)
    return t_culm

days = np.arange(7)
t_refs = ts.utc(2025, 1, 1 + days)
t_culms = get_culm_for_time(t_refs)

# Compare with find_maxima
from skyfield.searchlib import find_maxima
def alt_func(t):
    return observer.at(t).observe(m31).apparent().altaz()[0].degrees
setattr(alt_func, 'step_days', 0.5)
tm, am = find_maxima(t0, ts.utc(2025,1,8), alt_func)

print(f"Analytical altitudes: {observer.at(t_culms).observe(m31).apparent().altaz()[0].degrees}")
print(f"find_maxima altitudes: {am}")
n = min(len(t_culms), len(tm))
print(f"Time differences (seconds): {(t_culms.tt[:n] - tm.tt[:n]) * 86400}")
