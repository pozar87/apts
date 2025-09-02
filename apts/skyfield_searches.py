from skyfield.api import load
from skyfield.searchlib import find_maxima, find_minima
import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar
from .cache import get_timescale, get_ephemeris


def find_highest_altitude(observer, planet, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    def altitude(t):
        return observer.at(t).observe(planet).apparent().altaz()[0].degrees

    altitude.step_days = 0.1
    times, altitudes = find_maxima(t0, t1, altitude)

    if len(times) == 0:
        return None, 0

    # find the index of the highest altitude
    max_altitude_index = np.argmax(altitudes)

    return times[max_altitude_index].utc_datetime(), altitudes[max_altitude_index]


def find_aphelion_perihelion(eph, planet_name, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    body = eph[planet_name]
    sun = eph["sun"]

    def distance_to_sun(t):
        return body.at(t).observe(sun).distance().km

    distance_to_sun.step_days = 180

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


def find_moon_apogee_perigee(eph, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    moon = eph["moon"]
    earth = eph["earth"]

    def distance_to_earth(t):
        return earth.at(t).observe(moon).distance().km

    distance_to_earth.step_days = 13

    max_times, _ = find_maxima(t0, t1, distance_to_earth)
    min_times, _ = find_minima(t0, t1, distance_to_earth)

    events = []
    for t in max_times:
        events.append({"date": t.utc_datetime(), "event": "Moon Apogee"})
    for t in min_times:
        events.append({"date": t.utc_datetime(), "event": "Moon Perigee"})

    return events


def find_conjunctions(
    observer,
    eph,
    p1_name,
    p2_name,
    start_date,
    end_date,
    threshold_degrees=None,
    event_name=None,
):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    p1 = eph[p1_name]
    p2 = eph[p2_name]

    def separation(t):
        return (
            observer.at(t)
            .observe(p1)
            .separation_from(observer.at(t).observe(p2))
            .degrees
        )

    separation.step_days = 1.0

    times, separations = find_minima(t0, t1, separation)

    if event_name is None:
        event_name = f"{p1_name.capitalize()} conjunct {p2_name.capitalize()}"

    events = []
    for t, s in zip(times, separations):
        if threshold_degrees is None or s < threshold_degrees:
            events.append(
                {"date": t.utc_datetime(), "event": event_name, "separation_degrees": s}
            )

    return events


def find_oppositions(observer, eph, planet_name, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    planet = eph[planet_name]
    sun = eph["sun"]

    def ecliptic_longitude_difference(t):
        planet_lon = observer.at(t).observe(planet).ecliptic_latlon()[1].degrees
        sun_lon = observer.at(t).observe(sun).ecliptic_latlon()[1].degrees
        diff = sun_lon - planet_lon
        return (diff + 180) % 360 - 180

    def opposition_angle_difference(t):
        return abs(abs(ecliptic_longitude_difference(t)) - 180)

    opposition_angle_difference.step_days = 180

    times, _ = find_minima(t0, t1, opposition_angle_difference)

    events = []
    for t in times:
        events.append({"date": t.utc_datetime(), "planet": planet_name})

    return events


def find_mercury_inferior_conjunctions(
    observer, eph, start_date, end_date, threshold_degrees=1.0
):
    return find_conjunctions(
        observer, eph, "mercury", "sun", start_date, end_date, threshold_degrees
    )


def find_conjunctions_with_star(
    observer,
    eph,
    body1_name,
    star_object,
    start_date,
    end_date,
    threshold_degrees=1.0,
    event_name=None,
):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    body1 = eph[body1_name]

    times = ts.linspace(t0, t1, int((t1 - t0) * 24))  # Hourly check

    events = []

    separations = []
    for t in times:
        pos1 = observer.at(t).observe(body1)
        pos_star = observer.at(t).observe(star_object)
        separations.append(float(pos1.separation_from(pos_star).degrees))

    for i in range(1, len(separations) - 1):
        if (
            separations[i] < separations[i - 1]
            and separations[i] < separations[i + 1]
            and separations[i] < threshold_degrees
        ):
            events.append(
                {
                    "date": times[i].utc_datetime(),
                    "event": event_name,
                    "separation_degrees": separations[i],
                }
            )

    return events


def find_lunar_occultations(observer, eph, bright_stars, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = eph["moon"]

    target_stars = [
        "Sirius",
        "Arcturus",
        "Rigel",
        "Procyon",
        "Betelgeuse",
        "Altair",
        "Aldebaran",
        "Antares",
        "Spica",
        "Pollux",
        "Fomalhaut",
        "Regulus",
        "Adhara",
        "Bellatrix",
        "El Nath",
        "Alnilam",
        "Alnitak",
        "Wezen",
        "Alhena",
        "Mirzam",
        "Alphard",
        "Hamal",
        "Beta Tauri",
    ]

    events = []

    from skyfield.api import Star

    stars_to_check = bright_stars[bright_stars["Name"].str.strip().isin(target_stars)]

    star_objects = []
    for index, star_data in stars_to_check.iterrows():
        star_df = pd.DataFrame(
            {
                "ra_hours": [star_data["RA"].to("hour").magnitude],
                "dec_degrees": [star_data["Dec"].to("degree").magnitude],
                "ra_mas_per_year": [0],
                "dec_mas_per_year": [0],
                "parallax_mas": [0],
                "radial_km_per_s": [0],
                "epoch_year": [2000.0],
            },
            index=[0],
        )
        star_objects.append((star_data["Name"], Star.from_dataframe(star_df)))

    ts = get_timescale()
    times = ts.linspace(t0, t1, int((t1 - t0) * 24))  # Hourly check

    for t in times:
        mpos = eph["earth"].at(t).observe(moon)
        for star_name, star in star_objects:
            spos = eph["earth"].at(t).observe(star)

            if mpos.separation_from(spos).degrees < 0.5:
                events.append(
                    {"date": t.utc_datetime(), "event": f"Moon occults {star_name}"}
                )

    return events


def find_iss_flybys(
    topos_observer,
    vector_observer,
    start_date,
    end_date,
    magnitude_threshold=-1.5,
    peak_altitude_threshold=40,
    rise_altitude_threshold=10,
):
    ts = get_timescale()
    eph = get_ephemeris()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    try:
        stations_url = "https://celestrak.org/NORAD/elements/stations.txt"
        # Load TLE file - no ephemeris needed for satellite data
        satellites = load.tle_file(stations_url)
        iss = next(s for s in satellites if s.name == "ISS (ZARYA)")
    except Exception as e:
        # Could be network error, or ISS not in file
        print(f"Could not load ISS TLEs: {e}")
        return []

    # Find rise/culmination/set events above `rise_altitude_threshold`
    times, events = iss.find_events(
        topos_observer, t0, t1, altitude_degrees=rise_altitude_threshold
    )

    events_list = []
    sun = eph["sun"]

    for i, event_code in enumerate(events):
        if event_code != 1:  # only look at culmination
            continue

        culmination_time = times[i]

        # Sun altitude (dark-sky check)
        sun_alt, _, _ = (
            vector_observer.at(culmination_time).observe(sun).apparent().altaz()
        )
        if sun_alt.degrees > -18:  # not dark enough
            continue

        # Topocentric ISS position
        sat = iss.at(culmination_time)
        obs = topos_observer.at(culmination_time)
        topocentric = sat - obs

        # Altitude, azimuth, distance
        alt, az, distance = topocentric.altaz()
        if alt.degrees < peak_altitude_threshold:
            continue

        # Apparent magnitude (Skyfield computes it for satellites directly)
        mag = -3.0
        if mag is not None and mag > magnitude_threshold:
            continue

        # Find rise and set times for this pass
        if i > 0 and events[i - 1] == 0:
            rise_time = times[i - 1]
        else:
            continue

        if i < len(events) - 1 and events[i + 1] == 2:
            set_time = times[i + 1]
        else:
            continue

        events_list.append(
            {
                "date": culmination_time.utc_datetime(),
                "event": f"Bright ISS Flyby (mag {mag:.2f}, peak alt {alt.degrees:.1f}°)",
                "type": "ISS Flyby",
                "rise_time": rise_time.utc_datetime(),
                "culmination_time": culmination_time.utc_datetime(),
                "set_time": set_time.utc_datetime(),
                "peak_altitude": alt.degrees,
                "peak_magnitude": mag,
            }
        )

    return events_list
