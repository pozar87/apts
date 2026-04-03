from typing import Any, cast
import numpy as np
from skyfield import almanac
from skyfield.searchlib import find_minima
from ..cache import get_timescale
from ..constants import astronomy
from ..utils import planetary

def _get_jovian_moon_objects(eph):
    """
    Helper to get Galilean moon objects from ephemeris, handling different kernel IDs.
    """
    moon_map = {501: "Io", 502: "Europa", 503: "Ganymede", 504: "Callisto"}
    moon_objs = {}
    for moon_id in moon_map:
        try:
            moon_objs[moon_id] = eph[moon_id]
        except KeyError:
            # Fallback for jup300.bsp IDs
            jup300_ids = {501: 55061, 502: 55062, 503: 55063, 504: 55064}
            moon_objs[moon_id] = eph[jup300_ids[moon_id]]
    return moon_map, moon_objs

def find_jovian_mutual_events(observer, start_date, end_date):
    """
    Finds mutual events between Jovian moons:
    - Mutual Occultations: one moon occults another as seen from Earth.
    - Mutual Eclipses: one moon's shadow falls on another.
    """
    from ..cache import get_jovian_ephemeris

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_jovian_ephemeris())

    try:
        jupiter = eph["jupiter barycenter"]
        sun = eph["sun"]
        moon_map, moon_objs = _get_jovian_moon_objects(eph)
    except KeyError:
        return []

    events = []
    # Check all pairs of moons
    moon_ids = list(moon_map.keys())

    for i, id1 in enumerate(moon_ids):
        for id2 in moon_ids[i + 1 :]:
            m1_name = moon_map[id1]
            m2_name = moon_map[id2]
            m1_obj = moon_objs[id1]
            m2_obj = moon_objs[id2]

            def mutual_state(t):
                # Returns: 0: None, 1: m1 occults m2, 2: m2 occults m1,
                # 3: m1 eclipses m2, 4: m2 eclipses m1
                is_array = hasattr(t, "shape") and t.shape != ()
                res = np.zeros(len(t) if is_array else 1, dtype=int)

                # 1. Earth perspective (Occultations)
                # Oracle: use topocentric apparent positions for maximum precision
                m1_e = observer.at(t).observe(m1_obj).apparent(deflectors=(10, 599))
                m2_e = observer.at(t).observe(m2_obj).apparent(deflectors=(10, 599))
                sep_e = m1_e.separation_from(m2_e).degrees

                # Radii from constants (Galilean moons are spherical enough for this)
                moon_radii = {
                    501: astronomy.IO_RADIUS_KM,
                    502: astronomy.EUROPA_RADIUS_KM,
                    503: astronomy.GANYMEDE_RADIUS_KM,
                    504: astronomy.CALLISTO_RADIUS_KM,
                }
                r1 = np.degrees(np.arcsin(moon_radii[id1] / m1_e.distance().km))
                r2 = np.degrees(np.arcsin(moon_radii[id2] / m2_e.distance().km))

                occ = sep_e < (r1 + r2)
                # Determine who is in front (closer to Earth)
                m1_front = m1_e.distance().km < m2_e.distance().km

                # 2. Sun perspective (Eclipses)
                # Oracle: evaluated at t_emitted for retrospective accuracy
                # j_obs for light-time
                j_obs = observer.at(t).observe(jupiter).apparent(deflectors=(10, 599))
                t_emitted = ts.tt_jd(t.tt - j_obs.light_time)

                m1_s = sun.at(t_emitted).observe(m1_obj).apparent(deflectors=(10, 599))
                m2_s = sun.at(t_emitted).observe(m2_obj).apparent(deflectors=(10, 599))
                sep_s = m1_s.separation_from(m2_s).degrees

                # Angular radii as seen from Sun
                r1_s = np.degrees(np.arcsin(moon_radii[id1] / m1_s.distance().km))
                r2_s = np.degrees(np.arcsin(moon_radii[id2] / m2_s.distance().km))

                ecl = sep_s < (r1_s + r2_s)
                # Determine shadow caster (closer to Sun)
                m1_caster = m1_s.distance().km < m2_s.distance().km

                # Extract elevation from observer once
                observer_elevation = 0
                for vf in observer.vector_functions:
                    if hasattr(vf, "elevation"):
                        observer_elevation = vf.elevation.m
                        break

                # Visibility: Jupiter above horizon and Sun below -6
                # Special elevation -9999 bypasses topocentric checks for global indexing
                if observer_elevation == -9999:
                    visible = np.ones(len(t) if is_array else 1, dtype=bool)
                else:
                    alt, _, _ = j_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)
                    sun_alt = (
                        observer.at(t)
                        .observe(sun)
                        .apparent(deflectors=(10, 599))
                        .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                        .degrees
                    )
                    visible = (alt.degrees > 0) & (sun_alt <= -6)

                if is_array:
                    res[visible & occ & m1_front] = 1
                    res[visible & occ & ~m1_front] = 2
                    res[visible & ecl & m1_caster] = 3
                    res[visible & ecl & ~m1_caster] = 4
                else:
                    if visible:
                        if occ:
                            res[0] = 1 if m1_front else 2
                        elif ecl:
                            res[0] = 3 if m1_caster else 4
                return res

            # Step of 5 minutes is safe for fast-moving Jovian moons
            setattr(mutual_state, "step_days", 0.0035)
            t_events, y_events = almanac.find_discrete(t0, t1, mutual_state)

            if len(t_events) == 0:
                continue

            y_start = mutual_state(t0)
            y_prev = y_start[0] if hasattr(y_start, "shape") else y_start

            for te, ye in zip(t_events, y_events):
                if y_prev != 0:
                    caster, target = (m1_name, m2_name) if y_prev in [1, 3] else (m2_name, m1_name)
                    kind = "Occultation" if y_prev in [1, 2] else "Eclipse"
                    events.append({
                        "date": te.utc_datetime(),
                        "object1": caster,
                        "object2": target,
                        "event": f"Mutual {kind} End",
                        "type": f"Jovian Mutual {kind}",
                    })
                if ye != 0:
                    caster, target = (m1_name, m2_name) if ye in [1, 3] else (m2_name, m1_name)
                    kind = "Occultation" if ye in [1, 2] else "Eclipse"
                    events.append({
                        "date": te.utc_datetime(),
                        "object1": caster,
                        "object2": target,
                        "event": f"Mutual {kind} Start",
                        "type": f"Jovian Mutual {kind}",
                    })
                y_prev = ye

    return events

def find_jovian_moon_events(observer, start_date, end_date):
    """
    Finds Jovian moon events (Transits, Shadows, Occultations, Eclipses)
    for Io, Europa, Ganymede, and Callisto.
    """
    from ..cache import get_jovian_ephemeris

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_jovian_ephemeris())

    try:
        jupiter = eph["jupiter barycenter"]
        sun = eph["sun"]
        moon_map, moon_objs = _get_jovian_moon_objects(eph)
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

            # 1. Observation from Earth
            # j_obs gives Jupiter's position at t_emitted = t - light_time
            # We limit deflectors to avoid Saturn ephemeris dependency in some kernels.
            j_obs = observer.at(t).observe(jupiter).apparent(deflectors=(10, 599))
            m_obs = observer.at(t).observe(moon_obj).apparent(deflectors=(10, 599))

            # Time when light left Jupiter system
            t_emitted = ts.tt_jd(t.tt - j_obs.light_time)

            # Visibility check: Jupiter above horizon and Sun below -6 degrees
            alt, _, _ = j_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)
            sun_alt = (
                observer.at(t)
                .observe(sun)
                .apparent(deflectors=(10, 599))
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )
            visible = (alt.degrees > 0) & (sun_alt <= -6)

            # 2. Ellipsoidal body parameters
            re = astronomy.JUPITER_RADIUS_KM
            rp = astronomy.JUPITER_POLAR_RADIUS_KM

            # Jupiter's pole at emission time (IAU 2015 model)
            alpha0_deg, delta0_deg = planetary.get_planet_pole_coords("jupiter", t_emitted)
            alpha0 = np.radians(alpha0_deg)
            delta0 = np.radians(delta0_deg)
            z_pole = np.array([
                np.cos(delta0) * np.cos(alpha0),
                np.cos(delta0) * np.sin(alpha0),
                np.sin(delta0)
            ]) # (3, N) or (3,)

            def is_inside_ellipsoid_projection(p_vec, u_vec, z_pole):
                """
                Checks if point p is within the projection of an ellipsoid along direction u.
                p and u are (3, N), z_pole is (3, N) or (3,).
                """
                # Dots along z_pole
                if p_vec.ndim > 1:
                    p_z = np.sum(p_vec * z_pole, axis=0)
                    u_z = np.sum(u_vec * z_pole, axis=0)
                    p_u = np.sum(p_vec * u_vec, axis=0)
                    p_sq = np.sum(p_vec * p_vec, axis=0)
                else:
                    p_z = np.dot(p_vec, z_pole)
                    u_z = np.dot(u_vec, z_pole)
                    p_u = np.dot(p_vec, u_vec)
                    p_sq = np.dot(p_vec, p_vec)

                # Scaled space parameters
                p_prime_sq = (p_sq - p_z**2) / re**2 + p_z**2 / rp**2
                p_prime_u_prime = (p_u - p_z * u_z) / re**2 + (p_z * u_z) / rp**2
                u_prime_sq = (1.0 - u_z**2) / re**2 + u_z**2 / rp**2

                # Projected distance squared: |P'|^2 - (P' . U')^2 / |U'|^2
                return p_prime_sq - (p_prime_u_prime**2 / u_prime_sq) <= 1.000001

            # 3. Earth perspective (Transits and Occultations)
            # Vector from Jupiter to Earth
            p_j_e = -j_obs.position.km
            if is_array:
                u_e = p_j_e / np.linalg.norm(p_j_e, axis=0)
                p_m = m_obs.position.km - j_obs.position.km
                p_m_u_e = np.sum(p_m * u_e, axis=0)
            else:
                u_e = p_j_e / np.linalg.norm(p_j_e)
                p_m = m_obs.position.km - j_obs.position.km
                p_m_u_e = np.dot(p_m, u_e)

            in_projection_e = is_inside_ellipsoid_projection(p_m, u_e, z_pole)
            # Closer to Earth means p_m . u_e > 0
            in_transit = in_projection_e & (p_m_u_e > 0)
            in_occultation = in_projection_e & (p_m_u_e <= 0)

            # 4. Sun perspective (Shadows and Eclipses)
            # Oracle: evaluated at t_emitted to account for light-travel time
            sun_from_j = jupiter.at(t_emitted).observe(sun).apparent(deflectors=(10, 599))
            p_j_s = sun_from_j.position.km
            if is_array:
                u_s = p_j_s / np.linalg.norm(p_j_s, axis=0)
                p_m_u_s = np.sum(p_m * u_s, axis=0)
            else:
                u_s = p_j_s / np.linalg.norm(p_j_s)
                p_m = m_obs.position.km - j_obs.position.km
                p_m_u_s = np.dot(p_m, u_s)

            in_projection_s = is_inside_ellipsoid_projection(p_m, u_s, z_pole)
            # Between Sun and Jupiter (Shadow on Jupiter) means p_m . u_s > 0
            in_shadow = in_projection_s & (p_m_u_s > 0)
            in_eclipse = in_projection_s & (p_m_u_s <= 0)

            if is_array:
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

def find_jupiter_grs_transits(
    observer,
    start_date,
    end_date,
    grs_longitude=None,
):
    """
    Finds when Jupiter's Great Red Spot (GRS) transits the Central Meridian (System II).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    jupiter = planetary.get_skyfield_obj("jupiter barycenter")
    sun = planetary.get_skyfield_obj("sun")

    def cml_difference(t):
        # Use vectorized longitude calculations for better performance
        grs_lon = (
            grs_longitude
            if grs_longitude is not None
            else planetary.get_jupiter_grs_longitude(t)
        )
        sys_ii_lon = planetary.get_jupiter_system_ii_longitude(t)
        return (sys_ii_lon - grs_lon + 180) % 360 - 180

    def abs_diff(t):
        return np.abs(cml_difference(t))

    # Jupiter rotates every ~9.9 hours (~0.41 days).
    # A step of 0.1 days (~2.4 hours) is safe to find every transit.
    setattr(abs_diff, "step_days", 0.1)
    times, _ = find_minima(t0, t1, abs_diff)

    events = []
    for t in times:
        # Check visibility: Jupiter above horizon and Sun below -6 degrees
        j_obs = observer.at(t).observe(jupiter).apparent()
        alt, _, _ = j_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

        if alt.degrees > 0:
            sun_alt = (
                observer.at(t)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

            if sun_alt <= -6:
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
