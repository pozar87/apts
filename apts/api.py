from apts.observations import Observation
from apts.place import Place
from apts.equipment import Equipment

def get_events(lat: float, lon: float, elevation: int = 300, days: int = 365):
    place = Place(lat=lat, lon=lon, elevation=elevation)
    equipment = Equipment() # Dummy equipment
    observation = Observation(place, equipment)
    events = observation.get_astronomical_events(days=days)
    return events

if __name__ == '__main__':
    events_df = get_events(lat=52.2, lon=21.0)
    print(events_df)
