import os
import sys
import datetime
import time
import pandas as pd

# Add the project root to sys.path to import apts
sys.path.append(os.getcwd())

from apts.events import AstronomicalEvents
from apts.place import Place
from apts.constants.event_types import EventType

def main():
    place = Place(52.2297, 21.0122, name="Warsaw")
    start_date = datetime.datetime(2024, 1, 1, tzinfo=datetime.timezone.utc)
    end_date = datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc)
    
    events_to_check = [
        EventType.MOON_PHASES,
        EventType.CONJUNCTIONS,
        EventType.OPPOSITIONS,
        EventType.METEOR_SHOWERS,
        EventType.HIGHEST_ALTITUDES,
        EventType.LUNAR_OCCULTATIONS,
        EventType.APHELION_PERIHELION,
        EventType.MOON_APOGEE_PERIGEE,
        EventType.MERCURY_INFERIOR_CONJUNCTIONS,
        EventType.MOON_MESSIER_CONJUNCTIONS,
        EventType.SOLAR_ECLIPSES,
        EventType.LUNAR_ECLIPSES,
        EventType.MOON_STAR_CONJUNCTIONS,
        EventType.PLANET_ALIGNMENTS,
    ]
    
    print("Profiling one year (2024) for Warsaw...")
    
    ae = AstronomicalEvents(place, start_date, end_date, events_to_calculate=events_to_check)
    
    results = []
    
    # We'll test them one by one
    test_methods = {
        "Moon Phases": ae.calculate_moon_phases,
        "Conjunctions": ae.calculate_conjunctions,
        "Oppositions": ae.calculate_oppositions,
        "Meteor Showers": ae.calculate_meteor_showers,
        "Highest Altitudes": ae.calculate_highest_altitudes,
        "Lunar Occultations": ae.calculate_lunar_occultations,
        "Aphelion/Perihelion": ae.calculate_aphelion_perihelion,
        "Moon Apogee/Perigee": ae.calculate_moon_apogee_perigee,
        "Mercury Inferior": ae.calculate_mercury_inferior_conjunctions,
        "Moon-Messier Conj": ae.calculate_moon_messier_conjunctions,
        "Solar Eclipses": ae.calculate_solar_eclipses,
        "Lunar Eclipses": ae.calculate_lunar_eclipses,
        "Moon-Star Conj": ae.calculate_moon_star_conjunctions,
        "Planet Alignments": ae.calculate_planet_alignments,
    }
    
    for name, method in test_methods.items():
        print(f"Testing {name}...", end="", flush=True)
        start = time.time()
        try:
            res = method()
            duration = time.time() - start
            print(f" {duration:.2f}s ({len(res)} events)")
            results.append({"name": name, "duration": duration, "count": len(res)})
        except Exception as e:
            print(f" Failed: {e}")
            
    ae.shutdown()
    
    df = pd.DataFrame(results).sort_values(by="duration", ascending=False)
    print("\nSummary:")
    print(df.to_string())

if __name__ == "__main__":
    main()
