from datetime import datetime, timedelta
from typing import Any, cast, List, Tuple, Optional, Dict

import numpy as np
from skyfield import almanac, eclipselib
from skyfield.api import load, Star
from skyfield.searchlib import find_maxima, find_minima

from .cache import get_ephemeris, get_timescale
from .constants import astronomy
from .utils import planetary


def find_solar_longitude_time(t0, t1, target_longitude, epoch=None):
    """
    Finds the exact time when the Sun reaches a specific ecliptic longitude.
    Default epoch is J2000.0 if not specified.
    """
    from typing import Any, cast
    eph = cast(Any, get_ephemeris())
    sun = eph["sun"]
    earth = eph["earth"]
    ts = get_timescale()
    target_epoch = epoch if epoch is not None else ts.utc(2000)

    def solar_longitude_at(t):
        # Solar longitude (λ⊙) is the ecliptic longitude of the Sun as seen from Earth.
        # It must be calculated for a geocentric observer (earth.at(t)) observing the Sun.
        # We use apparent position to include aberration and nutation, which is
        # the standard for λ⊙ used in meteor shower prediction (apparent geocentric).
        _, lon, _ = earth.at(t).observe(sun).apparent().ecliptic_latlon(target_epoch)
        return lon.degrees

    # We want to find where solar_longitude_at(t) == target_longitude
    # Since longitude wraps at 360, we use a difference function
    def longitude_difference(t):
        diff = solar_longitude_at(t) - target_longitude
        return (diff + 180) % 360 - 180

    def abs_diff(t):
        return abs(longitude_difference(t))

    setattr(abs_diff, "step_days", 1.0)
    times, _ = find_minima(t0, t1, abs_diff)

    return times[0] if len(times) > 0 else None


def _refine_conjunction(observer, obj1, obj2, rough_t):
    """
    Refines the time of a conjunction using iterative minimization.
    """
    ts = get_timescale()
    # Search within +/- 30 minutes of the rough time
    t0 = ts.from_datetime(rough_t.utc_datetime() - timedelta(minutes=30))
    t1 = ts.from_datetime(rough_t.utc_datetime() + timedelta(minutes=30))

    def separation_func(t):
        # We use .apparent() for maximum precision during refinement
        p1 = observer.at(t).observe(obj1).apparent()
        p2 = observer.at(t).observe(obj2).apparent()
        return p1.separation_from(p2).degrees

    setattr(separation_func, "step_days", 0.005)  # 7.2 minutes step for minimization
    times, separations = find_minima(t0, t1, separation_func)

    if len(times) > 0:
        return times[0], separations[0]
    return rough_t, separation_func(rough_t)


def find_golden_blue_hours(observer, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
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

    setattr(sun_state, "step_days", 0.005)  # ~7.2 minutes

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


def find_jovian_moon_events(observer, start_date, end_date):
    """
    Finds Jovian moon events (Transits, Shadows, Occultations, Eclipses)
    for Io, Europa, Ganymede, and Callisto.
    """
    from .cache import get_jovian_ephemeris

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_jovian_ephemeris())

    try:
        jupiter = eph["jupiter barycenter"]
        sun = eph["sun"]
        # Map IDs to names
        moon_map = {501: "Io", 502: "Europa", 503: "Ganymede", 504: "Callisto"}
        moon_objs = {moon_id: eph[moon_id] for moon_id in moon_map}
    except KeyError:
        return []

    events = []

    # Process each moon
    for moon_id, moon_name in moon_map.items():
        moon_obj = moon_objs[moon_id]

        def state_func(t):
            # Vectorized state function for find_discrete
            # Returns: 0: None, 1: Transit, 2: Occultation, 3: Shadow, 4: Eclipse
            is_array = hasattr(t, "shape") and t.shape != ()
            res = np.zeros(len(t) if is_array else 1, dtype=int)

            # Jupiter observed from Earth
            j_obs = observer.at(t).observe(jupiter).apparent()
            alt, _, dist = j_obs.altaz()

            # Moon observed from Earth
            m_obs = observer.at(t).observe(moon_obj).apparent()
            sep_e = j_obs.separation_from(m_obs).degrees
            j_rad_e = np.degrees(np.arcsin(astronomy.JUPITER_RADIUS_KM / dist.km))

            # Earth perspective
            in_transit = (sep_e < j_rad_e) & (m_obs.distance().km < dist.km)
            in_occultation = (sep_e < j_rad_e) & (m_obs.distance().km >= dist.km)

            # Jupiter and Moon observed from Sun
            j_sun = sun.at(t).observe(jupiter).apparent()
            m_sun = sun.at(t).observe(moon_obj).apparent()
            sep_s = j_sun.separation_from(m_sun).degrees
            j_rad_s = np.degrees(
                np.arcsin(astronomy.JUPITER_RADIUS_KM / j_sun.distance().km)
            )

            # Sun perspective
            in_shadow = (sep_s < j_rad_s) & (m_sun.distance().km < j_sun.distance().km)
            in_eclipse = (sep_s < j_rad_s) & (m_sun.distance().km >= j_sun.distance().km)

            # Visibility from Earth (Jupiter above horizon)
            visible = alt.degrees > 0

            if hasattr(t, "shape"):
                res[visible & in_transit] = 1
                res[visible & in_occultation] = 2
                res[visible & in_shadow] = 3
                res[visible & in_eclipse] = 4
            else:
                if visible:
                    if in_transit:
                        res[0] = 1
                    elif in_occultation:
                        res[0] = 2
                    elif in_shadow:
                        res[0] = 3
                    elif in_eclipse:
                        res[0] = 4
            return res

        setattr(state_func, "step_days", 0.005)  # ~7.2 minutes
        t_events, y_events = almanac.find_discrete(t0, t1, state_func)

        if len(t_events) == 0:
            continue

        # Initial state
        y_start = state_func(t0)
        y_prev = y_start[0] if hasattr(y_start, "shape") else y_start
        state_names = {
            1: "Transit",
            2: "Occultation",
            3: "Shadow Transit",
            4: "Eclipse",
        }

        for te, ye in zip(t_events, y_events):
            if y_prev != 0:
                events.append(
                    {
                        "date": te.utc_datetime(),
                        "object": moon_name,
                        "event": f"{state_names[int(y_prev)]} End",
                        "type": "Jovian Moon Event",
                    }
                )
            if ye != 0:
                events.append(
                    {
                        "date": te.utc_datetime(),
                        "object": moon_name,
                        "event": f"{state_names[int(ye)]} Start",
                        "type": "Jovian Moon Event",
                    }
                )
            y_prev = ye

    return events


def find_lunar_planetary_occultations(observer, start_date, end_date):
    """
    Finds occultations of planets by the Moon for a specific observer.
    Provides precise ingress and egress times.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = planetary.get_skyfield_obj("moon")

    planets = ["mercury", "venus", "mars barycenter", "jupiter barycenter", "saturn barycenter", "uranus barycenter", "neptune barycenter"]
    events = []

    for p_name in planets:
        planet = planetary.get_skyfield_obj(p_name)
        simple_name = planetary.get_simple_name(p_name)

        def is_occulted(t):
            m = observer.at(t).observe(moon).apparent()
            p = observer.at(t).observe(planet).apparent()
            sep = m.separation_from(p).degrees
            rad = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m.distance().km))
            alt, _, _ = m.altaz(temperature_C=10.0, pressure_mbar=1013.25)
            return (sep < rad) & (alt.degrees > 0)

        setattr(is_occulted, "step_days", 0.05)
        t_occ, y_occ = almanac.find_discrete(t0, t1, is_occulted)

        for i in range(0, len(t_occ), 2):
            if i + 1 < len(t_occ):
                ingress_t = t_occ[i]
                egress_t = t_occ[i + 1]
                # Mid-point for conjunction refinement if needed
                mid_t = ts.from_datetime(ingress_t.utc_datetime() + (egress_t.utc_datetime() - ingress_t.utc_datetime()) / 2)
                refined_t, _ = _refine_conjunction(observer, moon, planet, mid_t)
                events.append({
                    "date": refined_t.utc_datetime(),
                    "object1": "Moon",
                    "object2": simple_name,
                    "ingress_time": ingress_t.utc_datetime(),
                    "egress_time": egress_t.utc_datetime(),
                    "type": "Lunar Planetary Occultation",
                    "event": "Lunar Planetary Occultation",
                })
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


def find_planet_messier_conjunctions(observer, start_date, end_date):
    """Finds conjunctions between major planets and Messier objects."""
    from .catalogs import Catalogs
    catalogs = Catalogs()
    planets = ["mercury", "venus", "mars barycenter", "jupiter barycenter", "saturn barycenter", "uranus barycenter", "neptune barycenter"]
    messier_data = [(row["Messier"], row["skyfield_object"]) for _, row in catalogs.MESSIER.iterrows()]

    events = []
    for p_name in planets:
        planet_obj = planetary.get_skyfield_obj(p_name)
        simple_name = planetary.get_simple_name(p_name)
        # 3.0 degrees threshold for planet-DSO conjunctions
        conjunctions = find_conjunctions_with_stars(observer, p_name, messier_data, start_date, end_date, threshold_degrees=3.0)
        for conj in conjunctions:
            events.append({
                "date": conj["date"],
                "event": "Conjunction",
                "object1": simple_name,
                "object2": conj["object2"],
                "separation_degrees": conj["separation_degrees"],
                "type": "Planet-Messier Conjunction",
            })
    return events


def find_saturn_ring_crossings(start_date, end_date):
    """
    Finds when Earth or the Sun crosses Saturn's ring plane.
    Earth crossing: rings appear edge-on as seen from Earth.
    Sun crossing: Sun illuminates rings edge-on (equinox on Saturn).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
    earth = eph["earth"]
    sun = eph["sun"]
    saturn = eph["saturn barycenter"]

    def get_tilt(t, observer_obj):
        # Geocentric observation of Saturn (ICRS)
        astrometric = observer_obj.at(t).observe(saturn)
        # Unit vector from Saturn to observer
        v_sat_obs = -astrometric.position.au / astrometric.distance().au

        # Saturn's pole in J2000.0
        alpha_p_deg, delta_p_deg = planetary.get_saturn_pole(t)
        alpha_p = np.radians(alpha_p_deg)
        delta_p = np.radians(delta_p_deg)

        # Pole unit vector
        p = np.array(
            [
                np.cos(delta_p) * np.cos(alpha_p),
                np.cos(delta_p) * np.sin(alpha_p),
                np.sin(delta_p),
            ]
        )

        # sin(B) is the dot product of the pole vector and the Saturn-observer vector
        # Handle both scalar and array 't'
        if hasattr(t, "shape") and t.shape != ():
            # p and v_sat_obs are vectors over time.
            # p is (3, N), v_sat_obs is (3, N)
            # Actually get_saturn_pole returns alpha, delta which might be scalars if t is Time object?
            # Let's be safe.
            sin_B = np.sum(p * v_sat_obs, axis=0)
        else:
            sin_B = np.dot(p, v_sat_obs)

        return sin_B

    def earth_tilt(t):
        return get_tilt(t, earth)

    def sun_tilt(t):
        return get_tilt(t, sun)

    # Use find_discrete to find zero crossings
    # We need a state function that changes sign at zero
    def earth_crossing_state(t):
        return (earth_tilt(t) > 0).astype(int)

    def sun_crossing_state(t):
        return (sun_tilt(t) > 0).astype(int)

    # Saturn's orbit is ~29 years, so these events are rare.
    # Step size of 30 days is safe for finding crossings.
    setattr(earth_crossing_state, "step_days", 30.0)
    setattr(sun_crossing_state, "step_days", 30.0)

    events = []

    t_e, y_e = almanac.find_discrete(t0, t1, earth_crossing_state)
    for ti in t_e:
        events.append(
            {
                "date": ti.utc_datetime(),
                "event": "Saturn Ring Plane Crossing (Earth)",
                "type": "Saturn Ring Crossing",
            }
        )

    t_s, y_s = almanac.find_discrete(t0, t1, sun_crossing_state)
    for ti in t_s:
        events.append(
            {
                "date": ti.utc_datetime(),
                "event": "Saturn Ring Plane Crossing (Sun)",
                "type": "Saturn Ring Crossing",
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
        # Use topocentric apparent positions to account for aberration and light deflection
        p1_obs = observer.at(t).observe(p1).apparent()
        p2_obs = observer.at(t).observe(p2).apparent()
        return p1_obs.separation_from(p2_obs).degrees

    # Dynamically adjust step size based on moving bodies
    # Moon moves ~13 deg/day, Mercury ~1.3 deg/day
    if "moon" in [p1_name.lower(), p2_name.lower()]:
        step = 0.05  # ~1.2 hours
    elif any(p in [p1_name.lower(), p2_name.lower()] for p in ["mercury", "venus"]):
        step = 0.2  # ~4.8 hours
    else:
        step = 0.5  # ~12 hours

    setattr(separation, "step_days", step)

    times, separations = find_minima(t0, t1, separation)

    events = []
    for t, s in zip(times, separations):
        if threshold_degrees is None or s < threshold_degrees:
            # Refine conjunction time and separation
            refined_t, refined_s = _refine_conjunction(observer, p1, p2, t)
            events.append(
                {"date": refined_t.utc_datetime(), "separation_degrees": float(refined_s)}
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
        planet_lon = observer.at(t).observe(planet).apparent().ecliptic_latlon()[1].degrees
        sun_lon = observer.at(t).observe(sun).apparent().ecliptic_latlon()[1].degrees
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
    """
    Finds conjunctions between a moving body and a fixed star.
    Wrapper around find_conjunctions_with_stars for single star case.
    """
    events = find_conjunctions_with_stars(
        observer,
        body1_name,
        [("Target", star_object)],
        start_date,
        end_date,
        threshold_degrees,
    )

    # Remove the object2 key for backward compatibility
    for event in events:
        if "object2" in event:
            del event["object2"]

    return events


def find_conjunctions_with_stars(
    observer,
    body_name,
    star_data,  # List of (name, Star object)
    start_date,
    end_date,
    threshold_degrees=1.0,
):
    """
    Finds conjunctions between a moving body and multiple fixed stars.
    Vectorized over both time and stars for maximum performance.
    """
    if not star_data:
        return []

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    body = planetary.get_skyfield_obj(body_name)

    # Hourly check
    num_hours = int((t1 - t0) * 24)
    if num_hours < 2:
        return []
    times = ts.linspace(t0, t1, num_hours)

    # Vectorized observation for moving body (e.g. Moon)
    pos_body = observer.at(times).observe(body).apparent()
    # Unit vectors for body at all times: (3, M)
    body_au = pos_body.position.au
    u_body = body_au / np.linalg.norm(body_au, axis=0)

    # Prepare vectorized Star objects
    star_names = [name for name, _ in star_data]
    star_objs = [obj for _, obj in star_data]

    # Vectorized observation for stars at all times to account for aberration and parallax
    # This results in a (3, N, M) array if we could observe all stars at all times vectorized.
    # Skyfield supports Star(ra, dec).at(times). However, we have N stars and M times.

    # To keep it efficient but accurate, we will process stars in a loop if N is small,
    # or use a more clever approach. Since we are looking for conjunctions with SPECIFIC stars,
    # let's observe the star vector at each time step.

    # Skyfield cannot observe a vector of stars at a vector of times if both have length > 1.
    # We must loop over stars but can still vectorize over time for each star.
    dot_products = np.zeros((len(star_objs), len(times)))
    for i, star_obj in enumerate(star_objs):
        pos_star = observer.at(times).observe(star_obj).apparent()
        u_star = pos_star.position.au / np.linalg.norm(pos_star.position.au, axis=0)
        dot_products[i] = np.einsum('kj,kj->j', u_star, u_body)

    # Angular separation in degrees: acos(dot_product)
    # Using clip to avoid NaNs due to floating point precision
    separations = np.degrees(np.arccos(np.clip(dot_products, -1.0, 1.0)))

    events = []
    for i, name in enumerate(star_names):
        star_separations = separations[i]

        # Identify local minima where separation is below threshold
        is_minima = (star_separations[1:-1] < star_separations[:-2]) & (
            star_separations[1:-1] < star_separations[2:]
        )
        is_below_threshold = star_separations[1:-1] < threshold_degrees

        minima_indices = np.where(is_minima & is_below_threshold)[0] + 1

        for idx in minima_indices:
            # Refine conjunction time and separation
            refined_t, refined_s = _refine_conjunction(
                observer, body, star_objs[i], times[idx]
            )
            events.append(
                {
                    "date": refined_t.utc_datetime(),
                    "object2": name,
                    "separation_degrees": float(refined_s),
                }
            )

    return events


def find_conjunctions_between_moving_bodies(
    observer,
    body1_name,
    bodies2_data,  # List of (name, Skyfield object)
    start_date,
    end_date,
    threshold_degrees=1.0,
    precomputed_positions=None,
):
    """
    Finds conjunctions between a moving body and multiple other moving bodies.
    Vectorized over time for each pair.
    """
    if not bodies2_data:
        return []

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    # Dynamically adjust step size based on moving bodies
    # Using 15-minute resolution for the Moon for better conjunction accuracy
    if "moon" == body1_name.lower() or any(
        "moon" == name.lower() for name, _ in bodies2_data
    ):
        step = 0.01  # ~14.4 minutes
    elif "mercury" == body1_name.lower() or any(
        "mercury" == name.lower() for name, _ in bodies2_data
    ):
        step = 0.1  # ~2.4 hours
    else:
        step = 0.2  # ~4.8 hours

    num_steps = int((t1 - t0) / step)
    if num_steps < 2:
        num_steps = 2
    times = ts.linspace(t0, t1, num_steps)

    # Use precomputed positions if available, otherwise observe
    if precomputed_positions and body1_name.lower() in precomputed_positions:
        # Check if length matches. Skyfield's Astrometric results store
        # their timestamps in '.t', which is a Time object with a .shape.
        pos1_all = precomputed_positions[body1_name.lower()]
        # Verify both 't' attribute and that the length of the vectorized time array matches
        if (
            hasattr(pos1_all, "t")
            and hasattr(pos1_all.t, "shape")
            and len(pos1_all.t.shape) > 0
            and pos1_all.t.shape[0] == len(times)
        ):
            pos1 = pos1_all
        else:
            body1 = planetary.get_skyfield_obj(body1_name)
            pos1 = observer.at(times).observe(body1)
    else:
        body1 = planetary.get_skyfield_obj(body1_name)
        pos1 = observer.at(times).observe(body1)

    events = []
    for name2, body2 in bodies2_data:
        if precomputed_positions and name2.lower() in precomputed_positions:
            pos2_all = precomputed_positions[name2.lower()]
            if (
                hasattr(pos2_all, "t")
                and hasattr(pos2_all.t, "shape")
                and len(pos2_all.t.shape) > 0
                and pos2_all.t.shape[0] == len(times)
            ):
                pos2 = pos2_all
            else:
                pos2 = observer.at(times).observe(body2)
        else:
            pos2 = observer.at(times).observe(body2)

        separations = pos1.separation_from(pos2).degrees

        # Identify local minima where separation is below threshold
        is_minima = (separations[1:-1] < separations[:-2]) & (
            separations[1:-1] < separations[2:]
        )
        is_below_threshold = separations[1:-1] < threshold_degrees

        minima_indices = np.where(is_minima & is_below_threshold)[0] + 1

        for idx in minima_indices:
            # Refine conjunction time and separation
            # If precomputed positions are used, we still refine using the actual objects
            # to ensure maximum precision.
            body1 = planetary.get_skyfield_obj(body1_name)
            refined_t, refined_s = _refine_conjunction(
                observer, body1, body2, times[idx]
            )
            events.append(
                {
                    "date": refined_t.utc_datetime(),
                    "object2": name2,
                    "separation_degrees": float(refined_s),
                }
            )

    return events


def find_lunar_occultations(observer, bright_stars, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = planetary.get_skyfield_obj("moon")
    earth = cast(Any, planetary.get_skyfield_obj("earth"))

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
    spos_at_t0_all = earth.at(t0).observe(stars_vector)
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

    for star_name, star_obj in star_objects:

        def is_occulted(t):
            m = observer.at(t).observe(moon).apparent()
            s = observer.at(t).observe(star_obj).apparent()
            sep = m.separation_from(s).degrees
            dist = m.distance().km
            rad = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / dist))
            alt, _, _ = m.altaz(temperature_C=10.0, pressure_mbar=1013.25)
            return (sep < rad) & (alt.degrees > 0)

        setattr(is_occulted, "step_days", 0.05)
        t_occ, y_occ = almanac.find_discrete(t0, t1, is_occulted)

        for i in range(0, len(t_occ), 2):
            if i + 1 < len(t_occ):
                ingress_t = t_occ[i]
                egress_t = t_occ[i + 1]
                mid_t = ts.from_datetime(
                    ingress_t.utc_datetime()
                    + (egress_t.utc_datetime() - ingress_t.utc_datetime()) / 2
                )
                refined_t, _ = _refine_conjunction(observer, moon, star_obj, mid_t)
                events.append(
                    {
                        "date": refined_t.utc_datetime(),
                        "object1": "Moon",
                        "object2": star_name,
                        "ingress_time": ingress_t.utc_datetime(),
                        "egress_time": egress_t.utc_datetime(),
                        "type": "Lunar Occultation",
                        "event": "Lunar Occultation",
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
        import logging
        logging.getLogger(__name__).warning(f"Could not load TLE for {satellite_name}: {e}")
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
        # If they are not in the 'times' list (because they fell outside the search window),
        # we try to find them by searching a small window around the culmination.
        if i > 0 and events[i - 1] == 0:
            event_data["rise_time"] = times[i - 1].utc_datetime()
        else:
            # Rise happened before start_date? Search up to 30 mins before culmination.
            t_search_start = ts.utc(culmination_time.utc_datetime() - timedelta(minutes=30))
            t_search_end = culmination_time
            r_times, r_events = satellite.find_events(
                topos_observer,
                t_search_start,
                t_search_end,
                altitude_degrees=rise_altitude_threshold,
            )
            r_indices = [idx for idx, code in enumerate(r_events) if code == 0]
            if r_indices:
                event_data["rise_time"] = r_times[r_indices[-1]].utc_datetime()
            else:
                event_data["rise_time"] = None

        if i < len(events) - 1 and events[i + 1] == 2:
            event_data["set_time"] = times[i + 1].utc_datetime()
        else:
            # Set will happen after end_date? Search up to 30 mins after culmination.
            t_search_start = culmination_time
            t_search_end = ts.utc(culmination_time.utc_datetime() + timedelta(minutes=30))
            s_times, s_events = satellite.find_events(
                topos_observer,
                t_search_start,
                t_search_end,
                altitude_degrees=rise_altitude_threshold,
            )
            s_indices = [idx for idx, code in enumerate(s_events) if code == 2]
            if s_indices:
                event_data["set_time"] = s_times[s_indices[0]].utc_datetime()
            else:
                event_data["set_time"] = None

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
    eph = cast(Any, get_ephemeris())
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
    """
    Finds solar eclipses for a specific observer, providing classification
    (Total, Annular, Partial), magnitude, and obscuration.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    sun = planetary.get_skyfield_obj("sun")
    moon = planetary.get_skyfield_obj("moon")

    def solar_separation(t):
        s = observer.at(t).observe(sun).apparent()
        m = observer.at(t).observe(moon).apparent()

        # Calculate topocentric angular radii
        s_dist = s.distance().km
        m_dist = m.distance().km

        s_radius = np.degrees(np.arcsin(astronomy.SUN_RADIUS_KM / s_dist))
        m_radius = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_dist))

        sep = s.separation_from(m).degrees
        return sep - (s_radius + m_radius)

    setattr(solar_separation, "step_days", 0.05)
    times, _ = find_minima(t0, t1, solar_separation)

    events = []
    for t in times:
        s_pos = observer.at(t).observe(sun).apparent()
        m_pos = observer.at(t).observe(moon).apparent()

        d = s_pos.separation_from(m_pos).degrees
        rs = np.degrees(np.arcsin(astronomy.SUN_RADIUS_KM / s_pos.distance().km))
        rm = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_pos.distance().km))

        if d < rs + rm:
            # Visibility check: Is the Sun above the horizon for this observer?
            # Account for atmospheric refraction for precise visibility check
            sun_alt = s_pos.altaz(temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
            if sun_alt <= 0:
                continue

            # Classification
            if d <= abs(rs - rm):
                if rm >= rs:
                    kind = "Total"
                else:
                    kind = "Annular"
            else:
                kind = "Partial"

            # Magnitude (fraction of solar diameter covered)
            mag = (rs + rm - d) / (2 * rs)

            # Obscuration (fraction of solar area covered)
            # Area of intersection of two circles
            if d <= abs(rs - rm):
                obs = 1.0 if rm >= rs else (rm / rs) ** 2
            else:
                # Formula for area of overlap of two circles
                # Source: http://mathworld.wolfram.com/Circle-CircleIntersection.html
                def area(r1, r2, d):
                    if d >= r1 + r2:
                        return 0.0
                    if d <= abs(r1 - r2):
                        return np.pi * min(r1, r2) ** 2
                    r1sq = r1**2
                    r2sq = r2**2
                    dsq = d**2
                    part1 = r1sq * np.arccos((dsq + r1sq - r2sq) / (2 * d * r1))
                    part2 = r2sq * np.arccos((dsq + r2sq - r1sq) / (2 * d * r2))
                    part3 = 0.5 * np.sqrt(
                        (-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2)
                    )
                    return part1 + part2 - part3

                overlap_area = area(rs, rm, d)
                sun_area = np.pi * rs**2
                obs = overlap_area / sun_area

            events.append(
                {
                    "date": t.utc_datetime(),
                    "type": "Solar Eclipse",
                    "eclipse_type": kind,
                    "magnitude": float(mag),
                    "obscuration": float(obs),
                    "separation_degrees": float(d),
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
            max_k = max(w[0] for w in window)

            best_j = -1
            min_arc = 360
            for j, (k, arc, _) in enumerate(window):
                if k == max_k:
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


def find_culminations(observer, start_date, end_date, sun_alt_threshold=-6):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
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

        setattr(altitude, "step_days", 0.5)  # Check twice a day
        times, altitudes = find_maxima(t0, t1, altitude)

        simple_name = planetary.get_simple_name(name)

        for t, alt in zip(cast(Any, times), altitudes):
            if alt > 0:
                # Visibility check: For non-solar objects, Sun must be below threshold
                sun_alt = (
                    observer.at(t)
                    .observe(sun)
                    .apparent()
                    .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                    .degrees
                )
                visible = True
                if simple_name != "Sun" and sun_alt > sun_alt_threshold:
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


def find_object_culminations(
    observer, objects_data, start_date, end_date, sun_alt_threshold=-12
):
    """
    Finds culminations for a list of objects (e.g. Messier catalog).
    Vectorized over objects using an analytical approach (LST == RA) for fixed objects.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
    sun = eph["sun"]

    events = []
    if not objects_data:
        return events

    # Separate fixed objects (e.g. Stars, DSOs) from moving objects (e.g. Planets)
    fixed_objects = []
    moving_objects = []
    for name, obj in objects_data:
        # Fixed objects are typically Star instances with a constant RA/Dec
        if hasattr(obj, "ra"):
            fixed_objects.append((name, obj))
        else:
            moving_objects.append((name, obj))

    # 1. Process fixed objects with vectorized analytical approach
    if fixed_objects:
        # Extract observer longitude from the VectorSum object (used for LST calculation)
        lon_hours = 0.0
        for vf in observer.vector_functions:
            if hasattr(vf, "longitude"):
                lon_hours = vf.longitude.hours
                break

        # Generate reference points for each day in the interval.
        # We include one extra day before and after to ensure we don't miss culminations
        # near the boundaries of the interval.
        num_days = int(t1 - t0) + 1
        day_offsets = np.arange(-1, num_days + 1)
        # Using 12:00 UTC as a stable reference point for each day
        t_refs = ts.utc(
            t0.utc_datetime().year,
            t0.utc_datetime().month,
            t0.utc_datetime().day + day_offsets,
            12,
        )

        names_fixed = [f[0] for f in fixed_objects]
        num_fixed = len(fixed_objects)
        ra_fixed = np.array([obj.ra.hours for _, obj in fixed_objects])
        dec_fixed = np.array([obj.dec.degrees for _, obj in fixed_objects])

        # Consolidate all fixed objects into a single vectorized Star object
        stars_vector = Star(ra_hours=ra_fixed, dec_degrees=dec_fixed)

        all_t_culm_tt = []

        # Optimization: Loop over days while vectorizing over all objects (N objects per day)
        for t_ref in t_refs:
            # Estimate apparent RA at mid-day for all objects (using epoch='date' for LST)
            ra_hours = (
                observer.at(t_ref)
                .observe(stars_vector)
                .apparent()
                .radec(epoch="date")[0]
                .hours
            )

            # At culmination: LST == RA => GAST + Lon == RA => GAST == RA - Lon
            target_gast = (ra_hours - lon_hours) % 24
            diff_gast = (target_gast - t_ref.gast) % 24

            # Convert sidereal interval to UT (approx. factor 1.0027379)
            t_est_tt = t_ref.tt + (diff_gast / 1.002737909) / 24.0
            t_est = ts.tt_jd(t_est_tt)

            # High-precision refinement (usually one iteration is enough for stars)
            refined_t_est_tt = np.zeros(num_fixed)
            for i in range(num_fixed):
                ti = t_est[i]
                si = fixed_objects[i][1]
                ra_now = (
                    observer.at(ti).observe(si).apparent().radec(epoch="date")[0].hours
                )
                target_gast_i = (ra_now - lon_hours) % 24
                diff = (target_gast_i - ti.gast + 12) % 24 - 12
                refined_t_est_tt[i] = ti.tt + (diff / 1.002737909) / 24.0

            all_t_culm_tt.append(refined_t_est_tt)

        # Flatten all potential culminations
        t_culms_all_tt = np.concatenate(all_t_culm_tt)
        obj_indices_all = np.tile(np.arange(num_fixed), len(t_refs))

        # Filter culminations that fall within the requested window
        mask_window = (t_culms_all_tt >= t0.tt) & (t_culms_all_tt <= t1.tt)

        t_final_tt = t_culms_all_tt[mask_window]
        t_final = ts.tt_jd(t_final_tt)
        obj_indices_final = obj_indices_all[mask_window]

        if len(t_final) > 0:
            # Observe each culmination for altitude and sun visibility check.
            # Since we have K different times and K different stars, we loop.
            # K is typically ~len(Messier catalog) * num_days, but many are below horizon.
            alts_final = np.zeros(len(t_final))
            sun_alts = np.zeros(len(t_final))

            for j in range(len(t_final)):
                tj = t_final[j]
                sj = fixed_objects[obj_indices_final[j]][1]
                alts_final[j] = (
                    observer.at(tj)
                    .observe(sj)
                    .apparent()
                    .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                    .degrees
                )
                sun_alts[j] = (
                    observer.at(tj)
                    .observe(sun)
                    .apparent()
                    .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                    .degrees
                )

            # Visibility threshold: Altitude > 15 deg and Sun below threshold
            valid_mask = (alts_final > 15) & (sun_alts <= sun_alt_threshold)

            final_names = [names_fixed[i] for i in obj_indices_final[valid_mask]]
            final_times = t_final[valid_mask]
            final_alts = alts_final[valid_mask]

            for t, name, alt in zip(final_times, final_names, final_alts):
                events.append(
                    {
                        "date": t.utc_datetime(),
                        "event": "Culmination",
                        "object": name,
                        "type": "Messier Culmination",
                        "altitude": float(alt),
                    }
                )

    # 2. Process moving objects with the traditional iterative solver
    for name, obj in moving_objects:

        def altitude_func(t):
            return (
                observer.at(t)
                .observe(obj)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

        setattr(altitude_func, "step_days", 0.5)
        times, altitudes = find_maxima(t0, t1, altitude_func)

        for t, alt in zip(cast(Any, times), altitudes):
            if alt > 15:
                sun_alt = (
                    observer.at(t)
                    .observe(sun)
                    .apparent()
                    .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                    .degrees
                )
                if sun_alt <= sun_alt_threshold:
                    events.append(
                        {
                            "date": t.utc_datetime(),
                            "event": "Culmination",
                            "object": name,
                            "type": "Messier Culmination",
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


def find_seasons(start_date, end_date):
    """
    Finds the start of seasons (equinoxes and solstices).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())

    t, y = almanac.find_discrete(t0, t1, almanac.seasons(eph))

    events = []
    for ti, yi in zip(t, y):
        events.append(
            {
                "date": ti.utc_datetime(),
                "event": almanac.SEASON_EVENTS[yi],
                "type": "Season",
            }
        )
    return events


def find_jupiter_grs_transits(observer, start_date, end_date):
    """
    Finds transits of Jupiter's Great Red Spot (GRS) across the central meridian.
    The GRS is visible for about 1 hour before and after the transit.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    jupiter = planetary.get_skyfield_obj("jupiter barycenter")
    target_lon = astronomy.JUPITER_GRS_LONGITUDE_SYSTEM_II

    def grs_longitude_difference(t):
        # We handle both scalar and array Time objects from Skyfield
        if hasattr(t, "shape") and t.shape != ():
            # For array, we must loop as planetary.get_jupiter_system_ii_longitude
            # uses ephem which is not vectorized for this.
            res = np.array([grs_longitude_difference(ti) for ti in t])
            return res

        current_lon = planetary.get_jupiter_system_ii_longitude(t)
        diff = current_lon - target_lon
        # Wrap to -180 to 180
        return (diff + 180) % 360 - 180

    def abs_diff(t):
        return abs(grs_longitude_difference(t))

    # Jupiter rotation period is ~9.9 hours. GRS transits every 9.9 hours.
    # Step size of 2 hours is safe to find the minimum.
    setattr(abs_diff, "step_days", 0.08)  # ~1.9 hours

    times, _ = find_minima(t0, t1, abs_diff)

    events = []
    for t in times:
        # Check if Jupiter is above horizon during transit
        j_obs = observer.at(t).observe(jupiter).apparent()
        alt, _, _ = j_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

        if alt.degrees > 0:
            events.append(
                {
                    "date": t.utc_datetime(),
                    "event": "Jupiter Great Red Spot Transit",
                    "object": "Jupiter",
                    "type": "Jupiter GRS Transit",
                    "altitude": float(alt.degrees),
                }
            )

    return events
