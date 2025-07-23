from apts.observations import Observation
from apts.place import Place
from apts.equipment import Equipment
from datetime import datetime, timedelta
from skyfield.api import utc

def get_events(lat: float, lon: float, start_date: datetime, end_date: datetime, elevation: int = 300):
    place = Place(lat=lat, lon=lon, elevation=elevation)
    equipment = Equipment() # Dummy equipment
    observation = Observation(place, equipment)
    # Ensure dates are UTC for apts
    start_date_utc = start_date.astimezone(utc)
    end_date_utc = end_date.astimezone(utc)
    # Calculate days from start_date_utc and end_date_utc
    days = (end_date_utc - start_date_utc).days
    events = observation.get_astronomical_events(days=days)
    return events

if __name__ == 'main':
    # Example usage for testing
    from datetime import date
    start = datetime.combine(date.today(), datetime.min.time()).replace(tzinfo=utc)
    end = datetime.combine(date.today() + timedelta(days=30), datetime.max.time()).replace(tzinfo=utc)
    events_df = get_events(lat=52.2, lon=21.0, start_date=start, end_date=end)
    print(events_df)
