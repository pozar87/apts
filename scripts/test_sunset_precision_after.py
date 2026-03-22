import datetime
from apts.place import Place
from apts.cache import get_ephemeris, get_timescale

ts = get_timescale()
eph = get_ephemeris()
p = Place(52.2, 21.0) # Warsaw
start = datetime.datetime(2024, 6, 21, tzinfo=datetime.timezone.utc)

# 0 degrees horizon
sunset_0 = p.sunset_time(target_date=start.date(), horizon_degrees=0.0)
print(f"Sunset (0 deg): {sunset_0}")

# -0.8333 degrees horizon (new default)
sunset_ref = p.sunset_time(target_date=start.date())
print(f"Sunset (-0.8333 deg): {sunset_ref}")

if sunset_ref is not None and sunset_0 is not None:
    diff = (sunset_ref - sunset_0).total_seconds()
    print(f"Difference: {diff} seconds ({diff/60:.2f} minutes)")
else:
    print("Could not calculate sunset.")
