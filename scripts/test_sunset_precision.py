import datetime
from apts.place import Place
from skyfield import almanac
from apts.cache import get_ephemeris, get_timescale

ts = get_timescale()
eph = get_ephemeris()
p = Place(52.2, 21.0) # Warsaw
start = datetime.datetime(2024, 6, 21, tzinfo=datetime.timezone.utc)
t0 = ts.utc(start)
t1 = ts.utc(start + datetime.timedelta(days=1))
location = p.location
sun = eph['sun']

f0 = almanac.risings_and_settings(eph, sun, location)
t, y = almanac.find_discrete(t0, t1, f0)
t_set0 = [ti for ti, yi in zip(t, y) if yi == 0]
print(f"Sunset (0 deg): {t_set0[0].utc_datetime()}")

f_ref = almanac.risings_and_settings(eph, sun, location, horizon_degrees=-0.8333)
t, y = almanac.find_discrete(t0, t1, f_ref)
t_set_ref = [ti for ti, yi in zip(t, y) if yi == 0]
print(f"Sunset (-0.8333 deg): {t_set_ref[0].utc_datetime()}")

diff = (t_set_ref[0].utc_datetime() - t_set0[0].utc_datetime()).total_seconds()
print(f"Difference: {diff} seconds ({diff/60:.2f} minutes)")
