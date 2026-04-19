from typing import Any, cast
import numpy as np
from skyfield import almanac, magnitudelib
from skyfield.searchlib import find_maxima, find_minima
from ..cache import get_timescale, get_ephemeris
from ..utils import planetary
from ..constants import astronomy

def find_planetary_dichotomy(
    observer,
    start_date,
    end_date,
    precomputed_positions=None,
):
    """
    Finds when Mercury or Venus reach exactly 50% illumination (phase angle = 90°).
    This event is known as dichotomy.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    sun = planetary.get_skyfield_obj("sun")

    planets = ["mercury", "venus"]
    events = []

    for p_name in planets:
        planet_obj = planetary.get_skyfield_obj(p_name)
        simple_name = planetary.get_simple_name(p_name)

        def phase_angle_state(t):
            # We want to find when phase angle crosses 90 degrees.
            # Use geocentric position for standard dichotomy calculation.
            # Geocentric Earth position is used as the reference for astronomical dichotomy.
            eph = get_ephemeris()
            earth = cast(Any, eph["earth"])
            astrometric = earth.at(t).observe(planet_obj)

            # Phase angle Sun-Planet-Earth
            phase_angle = astrometric.phase_angle(sun).degrees
            return (phase_angle > 90).astype(int)

        # Dichotomy happens twice per synodic period.
        # Step of 5 days is safe for Mercury (~116d synodic) and Venus (~584d synodic).
        setattr(phase_angle_state, "step_days", 5.0)
        times, codes = almanac.find_discrete(t0, t1, phase_angle_state)

        for t in times:
            # High-precision observation at the event time
            astrometric = observer.at(t).observe(planet_obj).apparent()
            alt, _, _ = astrometric.altaz(temperature_C=10.0, pressure_mbar=1013.25)

            # Visibility check: Planet above horizon and Sun below -6 degrees
            sun_alt = (
                observer.at(t)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

            events.append(
                {
                    "date": t.utc_datetime(),
                    "event": f"{simple_name} Dichotomy (50% Illumination)",
                    "object": simple_name,
                    "type": "Planetary Dichotomy",
                    "altitude": float(alt.degrees),
                    "is_visible": bool(alt.degrees > 0 and sun_alt <= -6),
                }
            )

    return events

def find_venus_greatest_brilliancy(observer: Any, start_date: Any, end_date: Any):
    """
    Finds when Venus reaches its greatest brilliancy (minimum apparent magnitude).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    venus = planetary.get_skyfield_obj("venus")

    # For planetary magnitude, we use geocentric position (earth.at(t))
    # to match standard almanac definitions for greatest brilliancy.
    earth = cast(Any, get_ephemeris()["earth"])

    def magnitude(t):
        astrometric = earth.at(t).observe(venus)
        return magnitudelib.planetary_magnitude(astrometric)

    # Venus greatest brilliancy occurs every ~584 days.
    # A step of 30 days is safe to find the minimum.
    setattr(magnitude, "step_days", 30.0)
    times, values = find_minima(t0, t1, magnitude)

    events = []
    for t, mag in zip(times, values):
        # Calculate altitude and visibility at the observer's location
        v_obs = observer.at(t).observe(venus).apparent()
        alt, _, _ = v_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

        # Sun altitude for visibility check
        sun = planetary.get_skyfield_obj("sun")
        sun_alt = (
            observer.at(t)
            .observe(sun)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )

        events.append(
            {
                "date": t.utc_datetime(),
                "event": "Venus Greatest Brilliancy",
                "object": "Venus",
                "type": "Venus Greatest Brilliancy",
                "magnitude": float(mag),
                "altitude": float(alt.degrees),
                "sun_altitude": float(sun_alt),
            }
        )

    return events

def find_stationary_points(observer, planet_name, start_date, end_date):
    """
    Finds when a planet becomes stationary in Right Ascension (transitioning
    between direct and retrograde motion).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    planet = planetary.get_skyfield_obj(planet_name)

    def ra_velocity(t):
        # We want to find where d(RA)/dt = 0
        # Use a small delta for numerical differentiation
        dt = 0.001  # ~1.4 minutes
        t_minus = ts.tt_jd(t.tt - dt)
        t_plus = ts.tt_jd(t.tt + dt)

        ra1 = observer.at(t_minus).observe(planet).apparent().radec(epoch="date")[0].hours
        ra2 = observer.at(t_plus).observe(planet).apparent().radec(epoch="date")[0].hours

        # Handle wrap-around at 24h
        diff = (ra2 - ra1 + 12) % 24 - 12
        return diff / (2 * dt)

    # Stationary points occur when RA velocity is zero.
    # We search for zero-crossings of the velocity.
    def ra_state(t):
        return (ra_velocity(t) > 0).astype(int)

    # Planets stay retrograde for weeks/months, so 2 days step is safe.
    setattr(ra_state, "step_days", 2.0)
    times, codes = almanac.find_discrete(t0, t1, ra_state)

    events = []
    simple_name = planetary.get_simple_name(planet_name)
    for t, code in zip(times, codes):
        direction = "Stationary (Direct)" if code == 1 else "Stationary (Retrograde)"
        events.append(
            {
                "date": t.utc_datetime(),
                "event": f"{simple_name} {direction}",
                "object": simple_name,
                "type": "Planet Stationary Point",
            }
        )
    return events

def find_highest_altitude(observer, planet, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    def altitude(t):
        # Account for atmospheric refraction for high-precision altitude
        return (
            observer.at(t)
            .observe(planet)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )

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
        dist_km = planetary.get_planet_distance_km(planet_name, t, astrometric=astrometric)
        diam = planetary.get_planet_angular_diameter(planet_name, t, observer=observer)

        events.append({
            "date": t.utc_datetime(),
            "planet": planet_name,
            "magnitude": float(mag),
            "distance_au": float(dist_km / astronomy.AU_KM),
            "angular_diameter_arcsec": float(diam)
        })

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

def find_greatest_elongations(observer, start_date, end_date):
    """
    Finds greatest elongations for Mercury and Venus.
    Greatest Eastern Elongation is in the evening sky.
    Greatest Western Elongation is in the morning sky.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
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

        setattr(elongation, "step_days", 2.0)  # Elongations change slowly
        times, separations = find_maxima(t0, t1, elongation)

        for t, sep in zip(cast(Any, times), separations):
            # Determine if it's Eastern or Western elongation
            # Eastern elongation: planet is east of the Sun (evening sky)
            # Western elongation: planet is west of the Sun (morning sky)
            s_lon = cast(Any, earth).at(t).observe(sun).ecliptic_latlon()[1].degrees
            p_lon = cast(Any, earth).at(t).observe(planet).ecliptic_latlon()[1].degrees

            diff = (p_lon - s_lon + 180) % 360 - 180
            direction = "Eastern" if diff > 0 else "Western"

            events.append(
                {
                    "date": t.utc_datetime(),
                    "event": f"{planetary.get_simple_name(p_name)} Greatest {direction} Elongation",
                    "object": planetary.get_simple_name(p_name),
                    "type": "Greatest Elongation",
                    "separation_degrees": float(sep),
                    "direction": direction,
                }
            )

    return events

def find_planet_alignments(observer, start_date, end_date):
    """
    Finds planetary alignments (multiple planets close together in ecliptic longitude).
    Takes into account visibility from the observer's location to highlight "planet parades".
    """
    from datetime import timedelta

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
    eph = get_ephemeris()
    earth = eph["earth"]
    sun = planetary.get_skyfield_obj("sun")

    # Thresholds for different numbers of planets
    thresholds = {
        3: 10,
        4: 25,
        5: 45,
        6: 90,
        7: 150,
    }

    # Use 1-hour steps to find best visibility and alignment
    duration_days = float(t_end - t_start)
    if duration_days <= 0:
        return []

    num_steps = int(duration_days * 24) + 1
    t_list = [
        t_start.utc_datetime() + timedelta(hours=i) for i in range(num_steps)
    ]
    times = ts.from_datetimes(t_list)

    # Pre-calculate longitudes, altitudes and sun altitude vectorized
    longitudes = []
    altitudes = []
    for _, obj in planet_objs:
        # Longitudes are geocentric ecliptic
        lons = cast(Any, earth).at(times).observe(obj).ecliptic_latlon()[1].degrees
        longitudes.append(lons)

        # Altitudes are topocentric (from observer)
        alts = observer.at(times).observe(obj).apparent().altaz()[0].degrees
        altitudes.append(alts)

    longitudes = np.array(longitudes)  # (n_planets, n_times)
    altitudes = np.array(altitudes)  # (n_planets, n_times)

    sun_alts = observer.at(times).observe(sun).apparent().altaz()[0].degrees
    is_dark = sun_alts < -6

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

    # Calculate stats for every hour
    step_results = []
    for i in range(len(times)):
        k, arc, indices = get_best_k_and_arc(longitudes[:, i])

        # Count visible planets among those in the alignment
        visible_in_alignment = 0
        visible_indices = []
        if k >= 3:
            for idx in indices:
                if altitudes[idx, i] > 0 and is_dark[i]:
                    visible_in_alignment += 1
                    visible_indices.append(idx)

        step_results.append(
            {
                "k": k,
                "arc": arc,
                "indices": indices,
                "num_visible": visible_in_alignment,
                "visible_indices": visible_indices,
            }
        )

    # Aggregate to daily results to maintain consistent grouping
    from collections import defaultdict

    by_day = defaultdict(list)
    for i, res in enumerate(step_results):
        day = times[i].utc_datetime().date()
        by_day[day].append((times[i], res))

    daily_results = []
    sorted_days = sorted(by_day.keys())
    for day in sorted_days:
        day_steps = by_day[day]
        # Best day means: max k, then max num_visible, then min arc
        best_step = max(
            day_steps, key=lambda x: (x[1]["k"], x[1]["num_visible"], -x[1]["arc"])
        )
        daily_results.append(best_step)

    events = []
    i = 0
    while i < len(daily_results):
        if daily_results[i][1]["k"] >= 3:
            # Start of an alignment period
            start_i = i
            while i < len(daily_results) and daily_results[i][1]["k"] >= 3:
                i += 1
            end_i = i

            # Find the best representative day in the window
            window = daily_results[start_i:end_i]
            best_day_tuple = max(
                window, key=lambda x: (x[1]["k"], x[1]["num_visible"], -x[1]["arc"])
            )

            t_best, res = best_day_tuple
            k = res["k"]
            arc = res["arc"]
            indices = res["indices"]
            num_visible = res["num_visible"]
            visible_indices = res["visible_indices"]

            aligned_planets = [
                planetary.get_simple_name(planets[idx]) for idx in indices
            ]
            visible_names = [
                planetary.get_simple_name(planets[idx]) for idx in visible_indices
            ]

            event_label = f"Alignment of {k} planets"
            if num_visible >= 3:
                event_label += f" ({num_visible} visible)"

            events.append(
                {
                    "date": t_best.utc_datetime(),
                    "event": event_label,
                    "planets": aligned_planets,
                    "visible_planets": visible_names,
                    "arc_degrees": arc,
                    "num_visible": num_visible,
                }
            )
        else:
            i += 1

    return events
