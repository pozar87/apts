from skyfield.api import load
from skyfield import eclipselib
from skyfield.searchlib import find_maxima, find_minima
import numpy as np
import pandas as pd
from typing import Any, cast
from .cache import get_timescale, get_ephemeris
from .utils import planetary
from .constants import astronomy


def find_highest_altitude(observer, planet, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    def altitude(t):
        return observer.at(t).observe(planet).apparent().altaz()[0].degrees

    setattr(altitude, "step_days", 0.1)
    times, altitudes = find_maxima(t0, t1, altitude)

    if len(times) == 0:
        return None, 0

    # find the index of the highest altitude
    max_altitude_index = np.argmax(altitudes)

    return times[max_altitude_index].utc_datetime(), altitudes[max_altitude_index]


def find_aphelion_perihelion(planet_name, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    body = planetary.get_skyfield_obj(planet_name)
    sun = planetary.get_skyfield_obj("sun")

    def distance_to_sun(t):
        return cast(Any, body).at(t).observe(sun).distance().km

    setattr(distance_to_sun, "step_days", 180)

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


def find_moon_apogee_perigee(start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    moon = planetary.get_skyfield_obj("moon")
    earth = planetary.get_skyfield_obj("earth")

    def distance_to_earth(t):
        return cast(Any, earth).at(t).observe(moon).distance().km

    setattr(distance_to_earth, "step_days", 13)

    max_times, _ = find_maxima(t0, t1, distance_to_earth)
    min_times, _ = find_minima(t0, t1, distance_to_earth)

    events = []
    for t in max_times:
        events.append({"date": t.utc_datetime(), "event": "Apogee", "object": "Moon"})
    for t in min_times:
        events.append({"date": t.utc_datetime(), "event": "Perigee", "object": "Moon"})

    return events


def find_conjunctions(
    observer,
    p1_name,
    p2_name,
    start_date,
    end_date,
    threshold_degrees=None,
):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    p1 = planetary.get_skyfield_obj(p1_name)
    p2 = planetary.get_skyfield_obj(p2_name)

    def separation(t):
        return (
            observer.at(t)
            .observe(p1)
            .separation_from(observer.at(t).observe(p2))
            .degrees
        )

    setattr(separation, "step_days", 1.0)

    times, separations = find_minima(t0, t1, separation)

    events = []
    for t, s in zip(times, separations):
        if threshold_degrees is None or s < threshold_degrees:
            events.append({"date": t.utc_datetime(), "separation_degrees": s})

    return events


def find_oppositions(observer, planet_name, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    planet = planetary.get_skyfield_obj(planet_name)
    sun = planetary.get_skyfield_obj("sun")

    def ecliptic_longitude_difference(t):
        planet_lon = observer.at(t).observe(planet).ecliptic_latlon()[1].degrees
        sun_lon = observer.at(t).observe(sun).ecliptic_latlon()[1].degrees
        diff = sun_lon - planet_lon
        return (diff + 180) % 360 - 180

    def opposition_angle_difference(t):
        return abs(abs(ecliptic_longitude_difference(t)) - 180)

    setattr(opposition_angle_difference, "step_days", 180)

    times, _ = find_minima(t0, t1, opposition_angle_difference)

    events = []
    for t in times:
        events.append({"date": t.utc_datetime(), "planet": planet_name})

    return events


def find_mercury_inferior_conjunctions(
    observer, start_date, end_date, threshold_degrees=1.0
):
    conjunctions = find_conjunctions(
        observer, "mercury", "sun", start_date, end_date, threshold_degrees
    )

    mercury = planetary.get_skyfield_obj("mercury")
    sun = planetary.get_skyfield_obj("sun")
    ts = get_timescale()

    inferior_events = []
    for event in conjunctions:
        t = ts.from_datetime(event["date"])
        mercury_obs = observer.at(t).observe(mercury)
        sun_obs = observer.at(t).observe(sun)

        mercury_dist = mercury_obs.distance().au
        sun_dist = sun_obs.distance().au

        if mercury_dist < sun_dist:
            # It is an inferior conjunction
            # Calculate angular radii
            mercury_angular_radius = np.degrees(
                np.arctan2(astronomy.MERCURY_RADIUS_KM / astronomy.AU_KM, mercury_dist)
            )
            sun_angular_radius = np.degrees(
                np.arctan2(astronomy.SUN_RADIUS_KM / astronomy.AU_KM, sun_dist)
            )

            event["is_transit"] = event["separation_degrees"] < (
                mercury_angular_radius + sun_angular_radius
            )
            inferior_events.append(event)

    return inferior_events


def find_conjunctions_with_star(
    observer,
    body1_name,
    star_object,
    start_date,
    end_date,
    threshold_degrees=1.0,
):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    body1 = planetary.get_skyfield_obj(body1_name)

    times = ts.linspace(t0, t1, int((t1 - t0) * 24))  # Hourly check

    events = []

    separations = []
    for t in times:
        pos1 = observer.at(t).observe(body1)
        pos_star = observer.at(t).observe(star_object)
        separations.append(pos1.separation_from(pos_star).degrees.item())

    for i in range(1, len(separations) - 1):
        if (
            separations[i] < separations[i - 1]
            and separations[i] < separations[i + 1]
            and separations[i] < threshold_degrees
        ):
            events.append(
                {
                    "date": times[i].utc_datetime(),
                    "separation_degrees": separations[i],
                }
            )

    return events


def find_lunar_occultations(observer, bright_stars, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = planetary.get_skyfield_obj("moon")
    earth = planetary.get_skyfield_obj("earth")

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
            index=pd.Index([0]),
        )
        star_objects.append((star_data["Name"], Star.from_dataframe(star_df)))

    ts = get_timescale()
    times = ts.linspace(t0, t1, int((t1 - t0) * 24))  # Hourly check

    for t in times:
        mpos = cast(Any, earth).at(t).observe(moon)
        for star_name, star in star_objects:
            spos = cast(Any, earth).at(t).observe(star)

            if mpos.separation_from(spos).degrees < 0.5:
                events.append(
                    {
                        "date": t.utc_datetime(),
                        "object1": "Moon",
                        "object2": star_name,
                    }
                )

    return events


def _find_satellite_flybys(
    topos_observer,
    vector_observer,
    start_date,
    end_date,
    satellite_name,
    event_name,
    event_type,
    magnitude_threshold=None,
    peak_altitude_threshold=40,
    rise_altitude_threshold=10,
):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    try:
        stations_url = "https://celestrak.org/NORAD/elements/stations.txt"
        # Load TLE file - no ephemeris needed for satellite data
        # Skyfield will cache this file by default
        satellites = load.tle_file(stations_url)
        satellite = next(s for s in satellites if s.name == satellite_name)
    except Exception as e:
        # Could be network error, or satellite not in file
        print(f"Could not load TLEs for {satellite_name}: {e}")
        return []

    # Find rise/culmination/set events above `rise_altitude_threshold`
    times, events = satellite.find_events(
        topos_observer, t0, t1, altitude_degrees=rise_altitude_threshold
    )

    events_list = []
    sun = planetary.get_skyfield_obj("sun")

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

        # Topocentric satellite position
        sat = cast(Any, satellite).at(culmination_time)
        obs = cast(Any, topos_observer).at(culmination_time)
        topocentric = sat - obs

        # Altitude, azimuth, distance
        alt, az, distance = topocentric.altaz()
        if alt.degrees < peak_altitude_threshold:
            continue

        event_data = {
            "date": culmination_time.utc_datetime(),
            "event": event_name,
            "type": event_type,
            "rise_time": None,
            "culmination_time": culmination_time.utc_datetime(),
            "set_time": None,
            "peak_altitude": alt.degrees,
        }

        if magnitude_threshold is not None:
            # Apparent magnitude (Skyfield computes it for satellites directly)
            mag = -3.0
            if mag is not None and mag > magnitude_threshold:
                continue
            event_data["peak_magnitude"] = mag

        # Find rise and set times for this pass
        if i > 0 and events[i - 1] == 0:
            event_data["rise_time"] = times[i - 1].utc_datetime()
        else:
            continue

        if i < len(events) - 1 and events[i + 1] == 2:
            event_data["set_time"] = times[i + 1].utc_datetime()
        else:
            continue

        events_list.append(event_data)

    return events_list


def find_iss_flybys(
    topos_observer,
    vector_observer,
    start_date,
    end_date,
    magnitude_threshold=-1.5,
    peak_altitude_threshold=40,
    rise_altitude_threshold=10,
):
    return _find_satellite_flybys(
        topos_observer,
        vector_observer,
        start_date,
        end_date,
        "ISS (ZARYA)",
        "Bright ISS Flyby",
        "ISS Flyby",
        magnitude_threshold,
        peak_altitude_threshold,
        rise_altitude_threshold,
    )


def find_tiangong_flybys(
    topos_observer,
    vector_observer,
    start_date,
    end_date,
    peak_altitude_threshold=40,
    rise_altitude_threshold=10,
):
    return _find_satellite_flybys(
        topos_observer,
        vector_observer,
        start_date,
        end_date,
        "CSS (TIANHE)",
        "Bright Tiangong Flyby",
        "Tiangong Flyby",
        None,  # No magnitude threshold for Tiangong
        peak_altitude_threshold,
        rise_altitude_threshold,
    )


def find_lunar_eclipses(start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = get_ephemeris()
    t, y, details = eclipselib.lunar_eclipses(t0, t1, eph)
    events = []
    for i, (ti, yi) in enumerate(zip(t, y)):
        events.append(
            {
                "date": ti.utc_datetime(),
                "type": "Lunar Eclipse",
                "eclipse_kind": eclipselib.LUNAR_ECLIPSES[yi],
                "penumbral_magnitude": details["penumbral_magnitude"][i],
                "umbral_magnitude": details["umbral_magnitude"][i],
            }
        )
    return events


def find_solar_eclipses(observer, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    sun = planetary.get_skyfield_obj("sun")
    moon = planetary.get_skyfield_obj("moon")
    earth = planetary.get_skyfield_obj("earth")

    Rs = 695700  # km
    rm = 1737.4  # km
    re = 6378  # km

    def eclipse_separation(t):
        s = cast(Any, earth).at(t).observe(sun)
        m = cast(Any, earth).at(t).observe(moon)
        Ds = s.distance().km
        dm = m.distance().km
        mu = s.separation_from(m).radians
        threshold = np.arcsin((rm + re) / dm) + np.arcsin((Rs - re) / Ds)
        return mu - threshold

    setattr(eclipse_separation, "step_days", 0.1)
    times, separations = find_minima(t0, t1, eclipse_separation)
    events = []
    for t, sep in zip(times, separations):
        if sep < 0:
            events.append(
                {"date": t.utc_datetime(), "type": "Solar Eclipse", "separation": sep}
            )
    return events
