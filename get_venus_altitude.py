from skyfield.api import load, Topos, utc
from datetime import datetime

ts = load.timescale()
eph = load('de421.bsp')
observer = eph['earth'] + Topos(latitude_degrees=52.2, longitude_degrees=21.0)
start_date = datetime(2023, 1, 1, tzinfo=utc)
end_date = datetime(2023, 3, 15, tzinfo=utc)
planet = eph['venus']

def altitude(t):
    return observer.at(t).observe(planet).apparent().altaz()[0].degrees

altitude.rough_period = 1.0

from skyfield.searchlib import find_maxima
times, altitudes = find_maxima(ts.utc(start_date), ts.utc(end_date), altitude)

max_altitude_index = altitudes.argmax()
print(f"Time: {times[max_altitude_index].utc_iso()}")
print(f"Altitude: {altitudes[max_altitude_index]}")
