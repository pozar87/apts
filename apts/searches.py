from skyfield.api import load
import numpy as np
import pandas as pd
from scipy.optimize import brentq

def find_extrema(f, t0, t1, num_points=1000):
    """
    Finds the extrema of a function f over the interval [t0, t1]
    by finding the roots of its derivative.
    Returns a list of tuples (time, value, is_max).
    """
    ts = load.timescale()
    times = ts.linspace(t0, t1, num_points)

    # Approximate derivative
    dt = (t1 - t0) / num_points
    values = f(times)
    deriv = np.gradient(values, dt)

    # Find roots of the derivative
    root_indices = np.where(np.diff(np.sign(deriv)))[0]

    extrema = []
    for i in root_indices:
        try:
            # Refine root location
            def deriv_at(t):
                # Ensure t is float
                t_val = float(t)
                return np.gradient(f(ts.tt(jd=[t_val - 0.01, t_val, t_val + 0.01])), 0.01)[1]

            t_root = brentq(
                deriv_at, float(times[i].tt), float(times[i + 1].tt)
            )
            t_extremum = ts.tt(jd=t_root)
            v_extremum = f(t_extremum)

            # Check second derivative to determine if max or min
            def second_deriv_at(t):
                t_val = float(t)
                return np.gradient(
                    np.gradient(f(ts.tt(jd=[t_val - 0.01, t_val, t_val + 0.01])), 0.01),
                    0.01,
                )[1]

            is_max = second_deriv_at(t_root) < 0

            extrema.append((t_extremum, v_extremum, is_max))
        except (RuntimeError, ValueError):
            # brentq can fail if the root is not bracketed
            continue

    return extrema


def find_highest_altitude(observer, planet, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    def altitude(t):
        return observer.at(t).observe(planet).apparent().altaz()[0].degrees

    extrema = find_extrema(altitude, t0, t1)
    maxima = [e for e in extrema if e[2]]

    if not maxima:
        return None, 0

    highest = max(maxima, key=lambda x: x[1])
    return highest[0].utc_datetime(), highest[1]


def find_aphelion_perihelion(eph, planet_name, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    body = eph[planet_name]
    sun = eph['sun']

    def distance_to_sun(t):
        return body.at(t).observe(sun).distance().km

    extrema = find_extrema(distance_to_sun, t0, t1)

    events = []
    for t, v, is_max in extrema:
        event_type = 'Aphelion' if is_max else 'Perihelion'
        events.append({'date': t.utc_datetime(), 'event': f'{planet_name.capitalize()} {event_type}'})

    return events


def find_moon_apogee_perigee(eph, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    moon = eph['moon']
    earth = eph['earth']

    def distance_to_earth(t):
        return earth.at(t).observe(moon).distance().km

    extrema = find_extrema(distance_to_earth, t0, t1)

    events = []
    for t, v, is_max in extrema:
        event_type = 'Apogee' if is_max else 'Perigee'
        events.append({'date': t.utc_datetime(), 'event': f'Moon {event_type}'})

    return events


def find_conjunctions(eph, p1_name, p2_name, start_date, end_date, threshold_degrees=None):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    p1 = eph[p1_name]
    p2 = eph[p2_name]

    def separation(t):
        return p1.at(t).separation_from(p2.at(t)).degrees

    extrema = find_extrema(separation, t0, t1)

    events = []
    for t, v, is_max in extrema:
        if not is_max:
            separation_val = v
            if threshold_degrees is None or separation_val < threshold_degrees:
                events.append({
                    'date': t.utc_datetime(),
                    'event': f'{p1_name.capitalize()} conjunct {p2_name.capitalize()}',
                    'separation_degrees': separation_val
                })

    return events

def find_mercury_inferior_conjunctions(eph, start_date, end_date, threshold_degrees=5.0):
    return find_conjunctions(eph, 'mercury', 'sun', start_date, end_date, threshold_degrees)


def find_lunar_occultations(observer, eph, bright_stars, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = eph['moon']

    events = []

    from skyfield.api import Star
    for index, star_data in bright_stars.iterrows():
        star_df = pd.DataFrame({
            'ra_hours': [star_data['RA'].to('hour').magnitude],
            'dec_degrees': [star_data['Dec'].to('degree').magnitude],
            'ra_mas_per_year': [0],
            'dec_mas_per_year': [0],
            'parallax_mas': [0],
            'radial_km_per_s': [0],
            'epoch_year': [2000.0]
        }, index=pd.Index([0]))
        star = Star.from_dataframe(star_df)

        times = ts.linspace(t0, t1, int((t1 - t0) * 24)) # Hourly check
        for t in times:
            mpos = eph['earth'].at(t).observe(moon)
            spos = eph['earth'].at(t).observe(star)

            if mpos.separation_from(spos).degrees < 0.5:
                events.append({'date': t.utc_datetime(), 'event': f'Moon occults {star_data["Name"]}'})

    return events
