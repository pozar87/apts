from typing import Any, cast
import numpy as np
from skyfield import almanac
from ...cache import get_timescale
from ...constants import astronomy
from .utils import _get_jovian_moon_objects

def find_jovian_mutual_events(observer, start_date, end_date):
    """
    Finds mutual events between Jovian moons:
    - Mutual Occultations: one moon occults another as seen from Earth.
    - Mutual Eclipses: one moon's shadow falls on another.
    """
    from ...cache import get_jovian_ephemeris

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
                        "event": f"{caster} Mutual {kind} of {target} End",
                        "type": f"Jovian Mutual {kind}",
                    })
                if ye != 0:
                    caster, target = (m1_name, m2_name) if ye in [1, 3] else (m2_name, m1_name)
                    kind = "Occultation" if ye in [1, 2] else "Eclipse"
                    events.append({
                        "date": te.utc_datetime(),
                        "object1": caster,
                        "object2": target,
                        "event": f"{caster} Mutual {kind} of {target} Start",
                        "type": f"Jovian Mutual {kind}",
                    })
                y_prev = ye

    return events
