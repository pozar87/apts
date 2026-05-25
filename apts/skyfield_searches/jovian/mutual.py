from typing import Any, cast
import numpy as np
from skyfield import almanac
from ...cache import get_timescale
from ...constants import astronomy
from .utils import _get_jovian_moon_objects, JovianSearchContext

# Radii from constants (Galilean moons are spherical enough for this)
GALILEAN_MOON_RADII = {
    501: astronomy.IO_RADIUS_KM,
    502: astronomy.EUROPA_RADIUS_KM,
    503: astronomy.GANYMEDE_RADIUS_KM,
    504: astronomy.CALLISTO_RADIUS_KM,
}


def _get_moon_angular_radius(moon_id, distance_km):
    """Calculates the apparent angular radius of a moon in degrees."""
    return np.degrees(np.arcsin(GALILEAN_MOON_RADII[moon_id] / distance_km))


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

    def __init__(self, ctx, id1, id2, elevation):
        self.ctx = ctx
        self.id1 = id1
        self.id2 = id2
        self.elevation = elevation

    def __call__(self, t):
        # Returns: 0: None, 1: m1 occults m2, 2: m2 occults m1,
        # 3: m1 eclipses m2, 4: m2 eclipses m1
        is_array = hasattr(t, "shape") and t.shape != ()
        res = np.zeros(len(t) if is_array else 1, dtype=int)

        # 1. Earth perspective (Occultations)
        m1_e = self.ctx.get_moon_obs(t, self.id1)
        m2_e = self.ctx.get_moon_obs(t, self.id2)
        sep_e = m1_e.separation_from(m2_e).degrees

        r1 = _get_moon_angular_radius(self.id1, m1_e.distance().km)
        r2 = _get_moon_angular_radius(self.id2, m2_e.distance().km)

        occ = sep_e < (r1 + r2)
        m1_front = m1_e.distance().km < m2_e.distance().km

        # 2. Sun perspective (Eclipses)
        data = self.ctx.get_basic_data(t)
        m1_s = self.ctx.get_moon_sun_obs(t, self.id1)
        m2_s = self.ctx.get_moon_sun_obs(t, self.id2)
        sep_s = m1_s.separation_from(m2_s).degrees

        r1_s = _get_moon_angular_radius(self.id1, m1_s.distance().km)
        r2_s = _get_moon_angular_radius(self.id2, m2_s.distance().km)

        ecl = sep_s < (r1_s + r2_s)
        m1_caster = m1_s.distance().km < m2_s.distance().km

        visible = self.ctx.get_visibility(t)

        if is_array:
            res[visible & occ & m1_front] = 1
            res[visible & occ & ~m1_front] = 2
            res[visible & ecl & m1_caster] = 3
            res[visible & ecl & ~m1_caster] = 4
        else:
            v_val = visible if np.isscalar(visible) else (visible[0] if visible.size > 0 else False)
            if v_val:
                occ_val = occ if np.isscalar(occ) else (occ[0] if occ.size > 0 else False)
                if occ_val:
                    m1f_val = m1_front if np.isscalar(m1_front) else (m1_front[0] if m1_front.size > 0 else False)
                    res[0] = 1 if m1f_val else 2
                else:
                    ecl_val = ecl if np.isscalar(ecl) else (ecl[0] if ecl.size > 0 else False)
                    if ecl_val:
                        m1c_val = m1_caster if np.isscalar(m1_caster) else (m1_caster[0] if m1_caster.size > 0 else False)
                        res[0] = 3 if m1c_val else 4
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
        ctx = JovianSearchContext(observer, eph, ts)
    except KeyError:
        return []

    events = []

    # Check all pairs of moons
    moon_ids = list(ctx.moon_map.keys())

    for i, id1 in enumerate(moon_ids):
        for id2 in moon_ids[i + 1 :]:
            m1_name = ctx.moon_map[id1]
            m2_name = ctx.moon_map[id2]

            mutual_state = JovianMutualState(ctx, id1, id2, ctx.elevation)

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
