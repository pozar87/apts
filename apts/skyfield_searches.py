from skyfield.api import load
import numpy as np
import pandas as pd

def find_extrema(f, t0, t1, num_points=5000):
    """
    Finds the extrema of a function f over the interval [t0, t1]
    by finding the sign changes in its derivative.
    Returns a list of tuples (time, value, is_max).
    """
    ts = load.timescale()
    times = ts.linspace(t0, t1, num_points)

    values = np.array([f(t) for t in times])
    values = np.squeeze(values)

    if values.ndim == 0:
        return []

    if values.shape[0] < 2:
        return []

    deriv = np.gradient(values)

    # Find sign changes in the derivative
    sign_changes = np.where(np.diff(np.sign(deriv)))[0]

    extrema = []
    for i in sign_changes:
        t_extremum = times[i]
        v_extremum = values[i]
        is_max = deriv[i] > 0 and deriv[i+1] < 0
        extrema.append((t_extremum, v_extremum, is_max))

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


def find_conjunctions(eph, p1_name, p2_name, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    p1 = eph[p1_name]
    p2 = eph[p2_name]

    def separation(t):
        return p1.at(t).separation_from(p2.at(t)).degrees

    extrema = find_extrema(lambda t: -separation(t), t0, t1) # Find maxima of negative separation

    events = []
    for t, v, is_max in extrema:
        if is_max and -v < 1.0:
            events.append({'date': t.utc_datetime(), 'event': f'{p1_name.capitalize()} conjunct {p2_name.capitalize()}'})

    return events


def find_oppositions(eph, planet_name, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    planet = eph[planet_name]
    sun = eph['sun']
    earth = eph['earth']

    def ecliptic_longitude_difference(t):
        planet_lon = earth.at(t).observe(planet).ecliptic_latlon()[1].degrees
        sun_lon = earth.at(t).observe(sun).ecliptic_latlon()[1].degrees
        return abs(planet_lon - sun_lon)

    extrema = find_extrema(lambda t: -abs(ecliptic_longitude_difference(t) - 180), t0, t1)

    events = []
    for t, v, is_max in extrema:
        if is_max:
            events.append({'date': t.utc_datetime(), 'event': f'{planet_name.capitalize()} at opposition'})

    return events

def find_mercury_inferior_conjunctions(eph, start_date, end_date):
    return find_conjunctions(eph, 'mercury', 'sun', start_date, end_date)

def find_conjunctions_with_star(eph, body1_name, star_object, start_date, end_date, threshold_degrees=1.0):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    body1 = eph[body1_name]

    def separation(t):
        pos1 = eph['earth'].at(t).observe(body1)
        if hasattr(t, 'shape') and t.shape:
            star_object.epoch = t.tt
        pos_star = eph['earth'].at(t).observe(star_object)
        return pos1.separation_from(pos_star).degrees

    # We are looking for minima of separation, so we find maxima of negative separation
    extrema = find_extrema(lambda t: -separation(t), t0, t1)

    events = []
    for t, v, is_max in extrema:
        # If it's a maximum of negative separation, it's a minimum of positive separation
        if is_max and -v < threshold_degrees:
            events.append({'date': t.utc_datetime(), 'separation_degrees': -v})

    return events

def find_lunar_occultations(observer, eph, bright_stars, start_date, end_date):
    ts = load.timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = eph['moon']

    target_stars = [
        "Sirius", "Arcturus", "Rigel", "Procyon", "Betelgeuse", "Altair",
        "Aldebaran", "Antares", "Spica", "Pollux", "Fomalhaut", "Regulus",
        "Adhara", "Bellatrix", "El Nath", "Alnilam", "Alnitak", "Wezen",
        "Alhena", "Mirzam", "Alphard", "Hamal", "Beta Tauri"
    ]

    events = []

    from skyfield.api import Star
    stars_to_check = bright_stars[bright_stars['Name'].str.strip().isin(target_stars)]

    star_objects = []
    for index, star_data in stars_to_check.iterrows():
        star_df = pd.DataFrame({
            'ra_hours': [star_data['RA'].to('hour').magnitude],
            'dec_degrees': [star_data['Dec'].to('degree').magnitude],
            'ra_mas_per_year': [0],
            'dec_mas_per_year': [0],
            'parallax_mas': [0],
            'radial_km_per_s': [0],
            'epoch_year': [2000.0]
        }, index=[0])
        star_objects.append((star_data['Name'], Star.from_dataframe(star_df)))

    times = ts.linspace(t0, t1, int((t1 - t0) * 24)) # Hourly check

    for t in times:
        mpos = eph['earth'].at(t).observe(moon)
        for star_name, star in star_objects:
            spos = eph['earth'].at(t).observe(star)

            if mpos.separation_from(spos).degrees < 0.5:
                events.append({'date': t.utc_datetime(), 'event': f'Moon occults {star_name}'})

    return events
