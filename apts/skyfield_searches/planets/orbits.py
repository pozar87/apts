from typing import Any, cast
from ...cache import get_timescale
from ...utils import planetary

def find_aphelion_perihelion(planet_name, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    body = planetary.get_skyfield_obj(planet_name)
    sun = planetary.get_skyfield_obj("sun")

    def distance_to_sun(t):
        return cast(Any, body).at(t).observe(sun).distance().km

    # Set step size based on orbital period to avoid missing extrema.
    # Mercury (~88 days), Venus (~225 days), Earth (~365 days).
    if "mercury" in planet_name.lower():
        step = 20.0
    elif "venus" in planet_name.lower():
        step = 50.0
    elif any(p in planet_name.lower() for p in ["earth", "moon"]):
        step = 90.0
    else:
        step = 180.0

    from skyfield.searchlib import find_maxima, find_minima
    setattr(distance_to_sun, "step_days", step)

    max_times, _ = find_maxima(t0, t1, distance_to_sun)
    min_times, _ = find_minima(t0, t1, distance_to_sun)

    events = []
    for t in max_times:
        events.append(
            {"date": t.utc_datetime(), "event_type": "Aphelion", "planet": planet_name}
        )
    for t in min_times:
        events.append(
            {
                "date": t.utc_datetime(),
                "event_type": "Perihelion",
                "planet": planet_name,
            }
        )
    return events
