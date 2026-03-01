from typing import Any, cast

import numpy as np
from skyfield import almanac, eclipselib
from skyfield.api import load, Star
from skyfield.positionlib import ICRF
from skyfield.searchlib import find_maxima, find_minima

from .cache import get_ephemeris, get_timescale
from .constants import astronomy
from .utils import planetary


def find_golden_blue_hours(observer, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = get_ephemeris()
    sun = eph["sun"]

    def sun_state(t):
        # We want to detect transitions at -6, -4, 6
        # Account for atmospheric refraction at standard conditions
        alt = (
            observer.at(t)
            .observe(sun)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )
        return (alt >= -6).astype(int) + (alt >= -4).astype(int) + (alt >= 6).astype(int)

    # Step size: must be small enough to catch all transitions.
    # A 2-degree interval (-6 to -4) takes about 8 minutes.
    sun_state.step_days = 0.005  # ~7.2 minutes

    t, y = almanac.find_discrete(t0, t1, sun_state)

    events = []
    y_prev = sun_state(t0)

    for ti, yi in zip(t, y):
        # Transitions:
        # 0 -> 1: Rising, Blue Hour Start (-6)
        # 1 -> 2: Rising, Blue Hour End / Golden Hour Start (-4)
        # 2 -> 3: Rising, Golden Hour End (6)
        # 3 -> 2: Setting, Golden Hour Start (6)
        # 2 -> 1: Setting, Golden Hour End / Blue Hour Start (-4)
        # 1 -> 0: Setting, Blue Hour End (-6)

        if y_prev == 0 and yi == 1:
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Blue Hour",
                    "phase": "Start",
                    "type": "Blue Hour",
                }
            )
        elif y_prev == 1 and yi == 2:
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Blue Hour",
                    "phase": "End",
                    "type": "Blue Hour",
                }
            )
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Golden Hour",
                    "phase": "Start",
                    "type": "Golden Hour",
                }
            )
        elif y_prev == 2 and yi == 3:
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Golden Hour",
                    "phase": "End",
                    "type": "Golden Hour",
                }
            )
        elif y_prev == 3 and yi == 2:
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Golden Hour",
                    "phase": "Start",
                    "type": "Golden Hour",
                }
            )
        elif y_prev == 2 and yi == 1:
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Golden Hour",
                    "phase": "End",
                    "type": "Golden Hour",
                }
            )
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Blue Hour",
                    "phase": "Start",
                    "type": "Blue Hour",
                }
            )
        elif y_prev == 1 and yi == 0:
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Blue Hour",
                    "phase": "End",
                    "type": "Blue Hour",
                }
            )

        y_prev = yi

    return events


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

    # Hourly check
    num_hours = int((t1 - t0) * 24)
    if num_hours < 2:
        return []
    times = ts.linspace(t0, t1, num_hours)

    # Vectorized observation for body1
    pos1 = observer.at(times).observe(body1)

    # Optimization: Observe fixed star once and broadcast to avoid repeated
    # coordinate transformations across the time array. Negligible accuracy loss.
    spos_single = observer.at(t0).observe(star_object)
    pos_star = ICRF(spos_single.position.au[:, np.newaxis], t=times)

    # Vectorized separation calculation
    separations = pos1.separation_from(pos_star).degrees

    # Find local minima where separation is below threshold
    # Using vectorized operations for comparison
    is_minima = (separations[1:-1] < separations[:-2]) & (
        separations[1:-1] < separations[2:]
    )
    is_below_threshold = separations[1:-1] < threshold_degrees

    minima_indices = np.where(is_minima & is_below_threshold)[0] + 1

    events = [
        {
            "date": times[idx].utc_datetime(),
            "separation_degrees": float(separations[idx]),
        }
        for idx in minima_indices
    ]

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

    stars_to_check = bright_stars[bright_stars["Name"].str.strip().isin(target_stars)]

    # Optimization: Pre-filter stars based on ecliptic latitude.
    # The Moon stays within ~5.3 degrees of the ecliptic.
    star_objs_all = stars_to_check["skyfield_object"].tolist()
    star_names_all = stars_to_check["Name"].tolist()

    # Observe all stars at once using a vectorized Star object
    stars_vector = Star(
        ra_hours=np.array([s.ra.hours for s in star_objs_all]),
        dec_degrees=np.array([s.dec.degrees for s in star_objs_all])
    )
    spos_at_t0_all = cast(Any, earth).at(t0).observe(stars_vector)
    lats, _, _ = spos_at_t0_all.ecliptic_latlon()

    # Filter using vectorized mask
    mask = np.abs(lats.degrees) < 10
    star_objects = [
        (star_names_all[i], star_objs_all[i])
        for i in np.where(mask)[0]
    ]

    # Check every 2 minutes for precision
    num_steps = int((t1 - t0) * 24 * 30)
    if num_steps < 2:
        return []
    times = ts.linspace(t0, t1, num_steps)

    # Topocentric position for accurate occultations
    mpos = observer.at(times).observe(moon)
    m_alt, _, m_dist = mpos.apparent().altaz()

    # Calculate Moon's angular radius
    moon_angular_radius = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_dist.km))

    for star_name, star_obj in star_objects:
        # Topocentric observation of star
        spos = observer.at(times).observe(star_obj)
        separations = mpos.separation_from(spos).degrees

        # Occultation check: separation < angular radius AND Moon above horizon
        occ_indices = np.where((separations < moon_angular_radius) & (m_alt.degrees > 0))[0]

        # We only want the moment of maximum occultation (minimum separation)
        # for each occultation event. An event can span multiple hours.
        if len(occ_indices) > 0:
            # Group consecutive indices as one event
            groups = np.split(occ_indices, np.where(np.diff(occ_indices) > 1)[0] + 1)
            for group in groups:
                # Find the index with the minimum separation in this group
                min_idx = group[np.argmin(separations[group])]
                events.append(
                    {
                        "date": times[min_idx].utc_datetime(),
                        "object1": "Moon",
                        "object2": star_name,
                    }
                )

    return events


def calculate_satellite_magnitude(
    satellite_name, sat_pos_km, sun_pos_km, observer_pos_km, distance_km
):
    """Calculates the apparent magnitude of a satellite."""
    # Vector from satellite to sun
    vec_sat_sun = sun_pos_km - sat_pos_km

    # Vector from satellite to observer
    vec_sat_obs = observer_pos_km - sat_pos_km

    # Calculate phase angle beta
    norm_sun = np.linalg.norm(vec_sat_sun)
    norm_obs = np.linalg.norm(vec_sat_obs)

    if norm_sun > 0 and norm_obs > 0:
        cos_beta = np.dot(vec_sat_sun, vec_sat_obs) / (norm_sun * norm_obs)
        beta = np.arccos(np.clip(cos_beta, -1.0, 1.0))

        # Phase function for diffuse sphere
        phi = (np.sin(beta) + (np.pi - beta) * np.cos(beta)) / np.pi

        # Standard magnitude (at 1000km, 0 phase)
        # ISS is approx -1.8, Tiangong is approx 0.0
        m_std = -1.8 if "ISS" in satellite_name else 0.0

        # Apparent magnitude
        return float(
            m_std + 5 * np.log10(distance_km / 1000.0) - 2.5 * np.log10(max(phi, 1e-9))
        )
    return 5.0


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

        # Check if satellite is sunlit
        if not sat.is_sunlit(get_ephemeris()):
            continue

        # Calculate apparent magnitude
        mag = calculate_satellite_magnitude(
            satellite_name,
            sat.position.km,
            cast(Any, sun).at(culmination_time).position.km,
            obs.position.km,
            distance.km,
        )

        if magnitude_threshold is not None and mag > magnitude_threshold:
            continue

        event_data = {
            "date": culmination_time.utc_datetime(),
            "event": event_name,
            "type": event_type,
            "rise_time": None,
            "culmination_time": culmination_time.utc_datetime(),
            "set_time": None,
            "peak_altitude": alt.degrees,
            "peak_magnitude": float(mag),
        }

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

    def solar_separation(t):
        s = observer.at(t).observe(sun).apparent()
        m = observer.at(t).observe(moon).apparent()

        # Calculate angular radii
        s_dist = s.distance().km
        m_dist = m.distance().km

        # Standard radii
        Rs = 695700.0  # Sun radius km
        Rm = 1737.4  # Moon radius km

        s_radius = np.degrees(np.arcsin(Rs / s_dist))
        m_radius = np.degrees(np.arcsin(Rm / m_dist))

        sep = s.separation_from(m).degrees
        return sep - (s_radius + m_radius)

    setattr(solar_separation, "step_days", 0.05)
    times, separations = find_minima(t0, t1, solar_separation)

    events = []
    for t, sep in zip(times, separations):
        if sep < 0:
            # Visibility check: Is the Sun above the horizon for this observer?
            sun_alt = observer.at(t).observe(sun).apparent().altaz()[0].degrees
            if sun_alt > 0:
                events.append(
                    {
                        "date": t.utc_datetime(),
                        "type": "Solar Eclipse",
                        "separation_degrees": float(sep),
                    }
                )
    return events


def find_planet_alignments(observer, start_date, end_date):
    ts = get_timescale()
    t_start = ts.utc(start_date)
    t_end = ts.utc(end_date)

    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]
    planet_objs = [(p, planetary.get_skyfield_obj(p)) for p in planets]
    earth = get_ephemeris()["earth"]

    # Thresholds for different numbers of planets
    thresholds = {
        3: 10,
        4: 25,
        5: 45,
        6: 90,
        7: 150,
    }

    # We'll check every day.
    num_days = int(t_end - t_start) + 1
    if num_days <= 0:
        return []

    t_utc = cast(Any, t_start.utc_datetime())
    times = ts.utc(
        t_utc.year,
        t_utc.month,
        t_utc.day + np.arange(num_days),
    )

    # Pre-calculate longitudes for all planets at all times
    longitudes = []
    for _, obj in planet_objs:
        lons = cast(Any, earth).at(times).observe(obj).ecliptic_latlon()[1].degrees
        longitudes.append(lons)

    longitudes = np.array(longitudes)  # (n_planets, n_times)

    def get_best_k_and_arc(lons_at_t):
        sorted_indices = np.argsort(lons_at_t)
        sorted_lons = lons_at_t[sorted_indices]
        n = len(sorted_lons)
        lons_extended = np.concatenate([sorted_lons, sorted_lons + 360])

        best_k = 0
        best_arc = 360
        best_indices = []

        for k in range(3, n + 1):
            min_arc_k = 360
            min_indices_k = []
            for i in range(n):
                arc = lons_extended[i + k - 1] - lons_extended[i]
                if arc < min_arc_k:
                    min_arc_k = arc
                    # Indices of planets in the arc
                    min_indices_k = [sorted_indices[j % n] for j in range(i, i + k)]

            if min_arc_k < thresholds.get(k, 360):
                best_k = k
                best_arc = min_arc_k
                best_indices = min_indices_k

        return best_k, best_arc, best_indices

    daily_results = []
    for i in range(len(times)):
        k, arc, indices = get_best_k_and_arc(longitudes[:, i])
        daily_results.append((k, arc, indices))

    events = []
    i = 0
    while i < len(daily_results):
        if daily_results[i][0] >= 3:
            # Start of an alignment period
            start_i = i
            while i < len(daily_results) and daily_results[i][0] >= 3:
                i += 1
            end_i = i

            # Find the best day in [start_i, end_i)
            # "Best" means max k, then min arc
            window = daily_results[start_i:end_i]
            max_k_in_window = max(w[0] for w in window)

            best_j = -1
            min_arc = 360
            for j, (k, arc, _) in enumerate(window):
                if k == max_k_in_window:
                    if arc < min_arc:
                        min_arc = arc
                        best_j = j

            best_i = start_i + best_j
            k, arc, indices = daily_results[best_i]
            aligned_planets = [
                planetary.get_simple_name(planets[idx]) for idx in indices
            ]

            events.append(
                {
                    "date": times[best_i].utc_datetime(),
                    "event": f"Alignment of {k} planets",
                    "planets": aligned_planets,
                    "arc_degrees": arc,
                }
            )
        else:
            i += 1

    return events


def find_culminations(observer, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = get_ephemeris()
    sun = eph["sun"]

    planets = [
        "sun",
        "moon",
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]
    planet_objs = [(p, planetary.get_skyfield_obj(p)) for p in planets]

    events = []

    for name, obj in planet_objs:

        def altitude(t):
            # Account for atmospheric refraction for high-precision culmination altitude
            return (
                observer.at(t)
                .observe(obj)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

        altitude.step_days = 0.5  # Check twice a day
        times, altitudes = find_maxima(t0, t1, altitude)

        simple_name = planetary.get_simple_name(name)

        for t, alt in zip(times, altitudes):
            if alt > 0:
                # Visibility check: For non-solar objects, Sun must be below -6 degrees
                sun_alt = observer.at(t).observe(sun).apparent().altaz()[0].degrees
                visible = True
                if simple_name != "Sun" and sun_alt > -6:
                    visible = False

                if visible:
                    events.append(
                        {
                            "date": t.utc_datetime(),
                            "event": "Culmination",
                            "object": simple_name,
                            "type": "Culmination",
                            "altitude": float(alt),
                        }
                    )

    return events


def find_greatest_elongations(observer, start_date, end_date):
    """
    Finds greatest elongations for Mercury and Venus.
    Greatest Eastern Elongation is in the evening sky.
    Greatest Western Elongation is in the morning sky.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = get_ephemeris()
    sun = eph["sun"]
    earth = eph["earth"]

    planets = ["mercury", "venus"]
    events = []

    for p_name in planets:
        planet = planetary.get_skyfield_obj(p_name)

        def elongation(t):
            # Elongation is the angle between the Sun and the planet as seen from Earth
            # We use Earth center (barycentric) for standard elongation values
            s = earth.at(t).observe(sun)
            p = earth.at(t).observe(planet)
            return s.separation_from(p).degrees

        elongation.step_days = 2.0  # Elongations change slowly
        times, separations = find_maxima(t0, t1, elongation)

        for t, sep in zip(times, separations):
            # Determine if it's Eastern or Western elongation
            # Eastern elongation: planet is east of the Sun (evening sky)
            # Western elongation: planet is west of the Sun (morning sky)
            s_lon = earth.at(t).observe(sun).ecliptic_latlon()[1].degrees
            p_lon = earth.at(t).observe(planet).ecliptic_latlon()[1].degrees

            diff = (p_lon - s_lon + 180) % 360 - 180
            direction = "Eastern" if diff > 0 else "Western"

            events.append(
                {
                    "date": t.utc_datetime(),
                    "event": f"Greatest {direction} Elongation",
                    "object": planetary.get_simple_name(p_name),
                    "type": "Greatest Elongation",
                    "separation_degrees": float(sep),
                    "direction": direction,
                }
            )

    return events
