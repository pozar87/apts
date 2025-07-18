from skyfield.api import load
from skyfield import almanac
import numpy as np
import pandas as pd

def find_aphelion_perihelion(eph, planet_name, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    body = eph[planet_name]
    sun = eph['sun']

    def distance_to_sun(t):
        return body.at(t).observe(sun).distance().km

    distance_to_sun.rough_period = 365.0 if 'barycenter' in planet_name else 27.0

    t, y = almanac.find_extrema(t0, t1, distance_to_sun)

    events = []
    for ti, yi in zip(t, y):
        event_type = 'Aphelion' if yi else 'Perihelion'
        events.append({'date': ti.utc_datetime(), 'event': f'{planet_name.capitalize()} {event_type}'})

    return events


def find_moon_apogee_perigee(eph, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    moon = eph['moon']
    earth = eph['earth']

    def distance_to_earth(t):
        return earth.at(t).observe(moon).distance().km

    distance_to_earth.rough_period = 27.0

    t, y = almanac.find_extrema(t0, t1, distance_to_earth)

    events = []
    for ti, yi in zip(t, y):
        event_type = 'Apogee' if yi else 'Perigee'
        events.append({'date': ti.utc_datetime(), 'event': f'Moon {event_type}'})

    return events


def find_conjunctions(eph, p1_name, p2_name, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    p1 = eph[p1_name]
    p2 = eph[p2_name]

    def separation(t):
        return p1.at(t).separation_from(p2.at(t)).degrees

    separation.rough_period = 180.0

    t, y = almanac.find_minima(t0, t1, separation)

    events = []
    for ti, yi in zip(t, y):
        if yi < 1.0:
            events.append({'date': ti.utc_datetime(), 'event': f'{p1_name.capitalize()} conjunct {p2_name.capitalize()}'})

    return events

def find_mercury_inferior_conjunctions(eph, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    t, y = almanac.find_discrete(t0, t1, almanac.mercury_inferior_conjunctions(eph))

    events = []
    for ti in t:
        events.append({'date': ti.utc_datetime(), 'event': 'Mercury Inferior Conjunction'})

    return events


def find_highest_altitude(observer, planet, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    def altitude(t):
        return observer.at(t).observe(planet).apparent().altaz()[0].degrees

    altitude.rough_period = 0.5

    t, y = almanac.find_maxima(t0, t1, altitude)

    if len(t) > 0:
        max_alt = max(y)
        max_alt_time = t[np.argmax(y)]
        return max_alt_time.utc_datetime(), max_alt
    else:
        return None, 0

def find_lunar_occultations(observer, eph, bright_stars, start_date, end_date):
    # This remains a complex problem.
    return []
