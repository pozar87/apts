from datetime import datetime, timezone
import numpy as np
from apts.place import Place
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType
from apts.skyfield_searches import find_conjunctions_between_moving_bodies
from apts.cache import get_timescale, get_ephemeris
from skyfield.api import Topos

utc = timezone.utc

def check_conjunction_precision():
    place = Place(lat=52.2, lon=21.0)
    ts = get_timescale()
    eph = get_ephemeris()
    observer = eph['earth'] + Topos(latitude_degrees=place.lat_decimal, longitude_degrees=place.lon_decimal)

    # Great Conjunction of 2020
    start_date = datetime(2020, 12, 21, 0, 0, tzinfo=utc)
    end_date = datetime(2020, 12, 22, 0, 0, tzinfo=utc)

    events = AstronomicalEvents(place, start_date, end_date, events_to_calculate=[EventType.CONJUNCTIONS])
    df = events.get_events()

    print("Events found:")
    print(df[['date', 'object1', 'object2', 'separation_degrees']])

    if not df.empty:
        event_time = df.iloc[0]['date']
        print(f"Predicted time: {event_time}")

        # Now let's check with higher resolution
        t = ts.from_datetime(event_time)
        jupiter = eph['jupiter barycenter']
        saturn = eph['saturn barycenter']

        def get_sep(ti):
            p1 = observer.at(ti).observe(jupiter).apparent()
            p2 = observer.at(ti).observe(saturn).apparent()
            return p1.separation_from(p2).degrees

        sep_at_predicted = get_sep(t)
        print(f"Separation at predicted time: {sep_at_predicted:.6f} degrees")

        # Check nearby times
        times = ts.utc(2020, 12, 21, 18, 20 + np.linspace(-30, 30, 601) / 60.0)
        seps = [get_sep(ti) for ti in times]
        min_sep = min(seps)
        min_time = times[np.argmin(seps)].utc_datetime()

        print(f"True minimum separation: {min_sep:.6f} degrees at {min_time}")
        print(f"Difference: {(event_time - min_time).total_seconds():.1f} seconds")

if __name__ == "__main__":
    check_conjunction_precision()
