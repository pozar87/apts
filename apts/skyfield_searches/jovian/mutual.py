from typing import Any, cast
import numpy as np
from skyfield import almanac
from ...cache import get_timescale
from ...constants import astronomy
from .utils import _get_jovian_moon_objects

# Radii from constants (Galilean moons are spherical enough for this)
GALILEAN_MOON_RADII = {
    501: astronomy.IO_RADIUS_KM,
    502: astronomy.EUROPA_RADIUS_KM,
    503: astronomy.GANYMEDE_RADIUS_KM,
    504: astronomy.CALLISTO_RADIUS_KM,
}


def _get_observer_elevation(observer):
    """Extracts elevation from observer vector functions."""
    observer_elevation = 0
    for vf in observer.vector_functions:
        if hasattr(vf, "elevation"):
            observer_elevation = vf.elevation.m
            break
    return observer_elevation


def _get_moon_angular_radius(moon_id, distance_km):
    """Calculates the apparent angular radius of a moon in degrees."""
    return np.degrees(np.arcsin(GALILEAN_MOON_RADII[moon_id] / distance_km))


def _is_jovian_event_visible(observer, t, j_obs, sun, observer_elevation, is_array):
    """Checks if Jupiter is above horizon and Sun is below -6 degrees."""
    # Visibility: Jupiter above horizon and Sun below -6
    # Special elevation -9999 bypasses topocentric checks for global indexing
    if observer_elevation == -9999:
        return np.ones(len(t) if is_array else 1, dtype=bool)

    alt, _, _ = j_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)
    sun_alt = (
        observer.at(t)
        .observe(sun)
        .apparent(deflectors=(10, 599))
        .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
        .degrees
    )
    return (alt.degrees > 0) & (sun_alt <= -6)


def _append_jovian_mutual_event(events, te, state_val, m1_name, m2_name, is_start):
    """Creates and appends a Jovian mutual event dictionary to the events list."""
    if state_val == 0:
        return

    caster, target = (m1_name, m2_name) if state_val in [1, 3] else (m2_name, m1_name)
    kind = "Occultation" if state_val in [1, 2] else "Eclipse"
    suffix = "Start" if is_start else "End"

    events.append(
        {
            "date": te.utc_datetime(),
            "object1": caster,
            "object2": target,
            "event": f"{caster} Mutual {kind} of {target} {suffix}",
            "type": f"Jovian Mutual {kind}",
        }
    )


class JovianMutualState:
    """Calculates the mutual state (occultation/eclipse) between two Jovian moons."""

    def __init__(self, observer, jupiter, sun, m1_obj, m2_obj, id1, id2, ts, elevation):
        self.observer = observer
        self.jupiter = jupiter
        self.sun = sun
        self.m1_obj = m1_obj
        self.m2_obj = m2_obj
        self.id1 = id1
        self.id2 = id2
        self.ts = ts
        self.elevation = elevation

    def __call__(self, t):
        # Returns: 0: None, 1: m1 occults m2, 2: m2 occults m1,
        # 3: m1 eclipses m2, 4: m2 eclipses m1
        is_array = hasattr(t, "shape") and t.shape != ()
        res = np.zeros(len(t) if is_array else 1, dtype=int)

        # 1. Earth perspective (Occultations)
        m1_e = self.observer.at(t).observe(self.m1_obj).apparent(deflectors=(10, 599))
        m2_e = self.observer.at(t).observe(self.m2_obj).apparent(deflectors=(10, 599))
        sep_e = m1_e.separation_from(m2_e).degrees

        r1 = _get_moon_angular_radius(self.id1, m1_e.distance().km)
        r2 = _get_moon_angular_radius(self.id2, m2_e.distance().km)

        occ = sep_e < (r1 + r2)
        m1_front = m1_e.distance().km < m2_e.distance().km

        # 2. Sun perspective (Eclipses)
        j_obs = self.observer.at(t).observe(self.jupiter).apparent(deflectors=(10, 599))
        t_emitted = self.ts.tt_jd(t.tt - j_obs.light_time)

        m1_s = self.sun.at(t_emitted).observe(self.m1_obj).apparent(deflectors=(10, 599))
        m2_s = self.sun.at(t_emitted).observe(self.m2_obj).apparent(deflectors=(10, 599))
        sep_s = m1_s.separation_from(m2_s).degrees

        r1_s = _get_moon_angular_radius(self.id1, m1_s.distance().km)
        r2_s = _get_moon_angular_radius(self.id2, m2_s.distance().km)

        ecl = sep_s < (r1_s + r2_s)
        m1_caster = m1_s.distance().km < m2_s.distance().km

        visible = _is_jovian_event_visible(
            self.observer, t, j_obs, self.sun, self.elevation, is_array
        )

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
    elevation = _get_observer_elevation(observer)

    # Check all pairs of moons
    moon_ids = list(moon_map.keys())

    for i, id1 in enumerate(moon_ids):
        for id2 in moon_ids[i + 1 :]:
            m1_name = moon_map[id1]
            m2_name = moon_map[id2]
            m1_obj = moon_objs[id1]
            m2_obj = moon_objs[id2]

            mutual_state = JovianMutualState(
                observer, jupiter, sun, m1_obj, m2_obj, id1, id2, ts, elevation
            )

            # Step of 5 minutes is safe for fast-moving Jovian moons
            setattr(mutual_state, "step_days", 0.0035)
            t_events, y_events = almanac.find_discrete(t0, t1, mutual_state)

            if len(t_events) == 0:
                continue

            y_start = mutual_state(t0)
            y_prev = y_start[0] if hasattr(y_start, "shape") else y_start

            for te, ye in zip(t_events, y_events):
                _append_jovian_mutual_event(events, te, y_prev, m1_name, m2_name, False)
                _append_jovian_mutual_event(events, te, ye, m1_name, m2_name, True)
                y_prev = ye

    return events
