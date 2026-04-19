from typing import Any, cast
from skyfield.searchlib import find_maxima, find_minima

from ...cache import get_timescale, get_ephemeris
from ...utils import planetary
from ...constants import astronomy


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


def find_oppositions(observer, planet_name, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    planet = planetary.get_skyfield_obj(planet_name)
    sun = planetary.get_skyfield_obj("sun")

    def ecliptic_longitude_difference(t):
        # Use apparent topocentric positions for maximum observational accuracy
        planet_lon = (
            observer.at(t).observe(planet).apparent().ecliptic_latlon()[1].degrees
        )
        sun_lon = observer.at(t).observe(sun).apparent().ecliptic_latlon()[1].degrees
        diff = sun_lon - planet_lon
        return (diff + 180) % 360 - 180

    def opposition_angle_difference(t):
        return abs(abs(ecliptic_longitude_difference(t)) - 180)

    setattr(opposition_angle_difference, "step_days", 180)

    times, _ = find_minima(t0, t1, opposition_angle_difference)

    events = []
    for t in times:
        # Calculate physical data at the moment of opposition
        astrometric = observer.at(t).observe(planet).apparent()

        mag = planetary.get_planet_magnitude(planet_name, t, astrometric=astrometric)
        dist_km = planetary.get_planet_distance_km(
            planet_name, t, astrometric=astrometric
        )
        diam = planetary.get_planet_angular_diameter(planet_name, t, observer=observer)

        events.append(
            {
                "date": t.utc_datetime(),
                "planet": planet_name,
                "magnitude": float(mag),
                "distance_au": float(dist_km / astronomy.AU_KM),
                "angular_diameter_arcsec": float(diam),
            }
        )

    return events


def find_mars_closest_approach(start_date, end_date, observer=None):
    """
    Finds when Mars is at its closest point to Earth (perigee).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = get_ephemeris()
    earth = eph["earth"]
    mars = eph["mars barycenter"]
    sun = eph["sun"]

    def distance_to_earth(t):
        return cast(Any, earth).at(t).observe(mars).distance().au

    # Mars closest approach happens every ~780 days.
    # Step of 30 days is safe for find_minima.
    setattr(distance_to_earth, "step_days", 30.0)
    times, values = find_minima(t0, t1, distance_to_earth)

    events = []
    for t, dist in zip(times, values):
        event = {
            "date": t.utc_datetime(),
            "event": "Mars Closest Approach",
            "object": "Mars",
            "type": "Mars Closest Approach",
            "distance_au": float(dist),
        }

        if observer is not None:
            v_obs = observer.at(t).observe(mars).apparent()
            alt, _, _ = v_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

            sun_alt = (
                observer.at(t)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

            event.update(
                {
                    "altitude": float(alt.degrees),
                    "sun_altitude": float(sun_alt),
                    "is_visible": bool(alt.degrees > 0 and sun_alt <= -6),
                }
            )

        events.append(event)

    return events
