from datetime import datetime, timezone
from skyfield.api import Topos
from apts.place import Place
from apts.skyfield_searches import find_golden_blue_hours
from apts.cache import get_ephemeris

place = Place(lat=52.2, lon=21.0) # Warsaw
start_date = datetime(2023, 6, 20, tzinfo=timezone.utc)
end_date = datetime(2023, 6, 22, tzinfo=timezone.utc)

# Mock observer for find_golden_blue_hours
eph = get_ephemeris()
observer = eph['earth'] + Topos(latitude_degrees=place.lat_decimal, longitude_degrees=place.lon_decimal)

events = find_golden_blue_hours(observer, start_date, end_date)
for e in events:
    print(f"{e['date']} - {e['event']} {e['phase']}")
