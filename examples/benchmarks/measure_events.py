import time
from datetime import datetime, timedelta
from apts import Place
from apts.events import AstronomicalEvents

def benchmark_events():
    place = Place(lat=50.0647, lon=19.9450, name="Krakow", elevation=200)
    start_date = datetime(2025, 1, 1)
    end_date = start_date + timedelta(days=30)

    events_coord = AstronomicalEvents(place, start_date, end_date)

    # We want to measure individual calculation methods
    methods = [
        ("Culminations", events_coord.calculate_culminations),
        ("Messier Culminations", events_coord.calculate_messier_culminations),
        ("Jovian Moon Events", events_coord.calculate_jovian_moon_events),
        ("Jovian Mutual Events", events_coord.calculate_jovian_mutual_events),
        ("Lunar Occultations", events_coord.calculate_lunar_occultations),
        ("Lunar Planetary Occultations", events_coord.calculate_lunar_planetary_occultations),
        ("Conjunctions", events_coord.calculate_conjunctions),
        ("Planet-Star Conjunctions", events_coord.calculate_planet_star_conjunctions),
        ("Planet Stationary Points", events_coord.calculate_planet_stationary_points),
        ("NASA Comets", events_coord.calculate_nasa_comets),
    ]

    print(f"{'Event Type':<30} | {'Duration (s)':<15}")
    print("-" * 48)

    for name, method in methods:
        start = time.time()
        try:
            method()
            duration = time.time() - start
            print(f"{name:<30} | {duration:<15.4f}")
        except Exception as e:
            print(f"{name:<30} | FAILED: {e}")

if __name__ == "__main__":
    benchmark_events()
