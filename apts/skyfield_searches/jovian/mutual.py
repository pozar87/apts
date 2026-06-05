from typing import Any, cast, List
import numpy as np
from skyfield import almanac
from ...cache import get_timescale
from ...constants import astronomy
from .utils import JovianSearchContext

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
    """
    Computes mutual states for all 6 moon pairs.
    Returns a combined mask (3 bits per pair, 18 bits total).
    Bits per pair: 0: None, 1: m1 occ m2, 2: m2 occ m1, 3: m1 ecl m2, 4: m2 ecl m1
    """

    def __init__(self, ctx: JovianSearchContext, pairs: List):
        self.ctx = ctx
        self.pairs = pairs
        self.moon_ids = list(ctx.moon_map.keys())
        self.step_days = 0.0035  # ~5 minutes

    def __call__(self, t):
        is_array = hasattr(t, "shape") and t.shape != ()
        visible = self.ctx.get_visibility(t)

        if not is_array:
            if not visible:
                return 0
            t_eval = t
        else:
            if not np.any(visible):
                return np.zeros(len(t), dtype=int)
            t_eval = t[visible]

        res_acc = self._compute_pair_states(t_eval, is_array)

        if not is_array:
            return int(np.atleast_1d(res_acc)[0])
        else:
            final_res = np.zeros(len(t), dtype=int)
            final_res[visible] = res_acc
            return final_res

    def _compute_pair_states(self, t_eval, is_array):
        # Use a helper to extract scalar values if needed to avoid ambiguous truth value errors
        def _get_val(v):
            return v if np.isscalar(v) else (v[0] if v.size > 0 else False)

        res_acc = np.zeros(len(t_eval) if is_array else 1, dtype=int)

        # Pre-fetch all moon observations to avoid redundant calls in the loop
        moons_e = {mid: self.ctx.get_moon_obs(t_eval, mid) for mid in self.moon_ids}
        moons_s = {mid: self.ctx.get_moon_sun_obs(t_eval, mid) for mid in self.moon_ids}

        for i, (id1, id2) in enumerate(self.pairs):
            # Earth perspective
            m1_e = moons_e[id1]
            m2_e = moons_e[id2]
            sep_e = m1_e.separation_from(m2_e).degrees
            r1 = _get_moon_angular_radius(id1, m1_e.distance().km)
            r2 = _get_moon_angular_radius(id2, m2_e.distance().km)

            occ = sep_e < (r1 + r2)
            m1_front = m1_e.distance().km < m2_e.distance().km

            # Sun perspective
            m1_s = moons_s[id1]
            m2_s = moons_s[id2]
            sep_s = m1_s.separation_from(m2_s).degrees
            r1_s = _get_moon_angular_radius(id1, m1_s.distance().km)
            r2_s = _get_moon_angular_radius(id2, m2_s.distance().km)

            ecl = sep_s < (r1_s + r2_s)
            m1_caster = m1_s.distance().km < m2_s.distance().km

            pair_state = np.zeros_like(res_acc)
            if is_array:
                pair_state[occ & m1_front] = 1
                pair_state[occ & ~m1_front] = 2
                pair_state[ecl & m1_caster] = 3
                pair_state[ecl & ~m1_caster] = 4
            else:
                if _get_val(occ):
                    pair_state[:] = 1 if _get_val(m1_front) else 2
                elif _get_val(ecl):
                    pair_state[:] = 3 if _get_val(m1_caster) else 4

            res_acc |= (pair_state.astype(int) << (3 * i))
        return res_acc


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

    moon_ids = list(ctx.moon_map.keys())
    pairs = []
    for i, id1 in enumerate(moon_ids):
        for id2 in moon_ids[i + 1 :]:
            pairs.append((id1, id2))

    events = []
    state_func = JovianMutualState(ctx, pairs)
    t_events, y_events = almanac.find_discrete(t0, t1, state_func)

    y_start = state_func(t0)
    y_prev = int(np.atleast_1d(y_start)[0])

    for te, ye in zip(t_events, y_events):
        for i, (id1, id2) in enumerate(pairs):
            p_prev = (y_prev >> (3 * i)) & 0x7
            p_curr = (ye >> (3 * i)) & 0x7
            if p_prev != p_curr:
                m1_name = ctx.moon_map[id1]
                m2_name = ctx.moon_map[id2]
                _append_jovian_mutual_event(events, te, p_prev, m1_name, m2_name, False)
                _append_jovian_mutual_event(events, te, p_curr, m1_name, m2_name, True)
        y_prev = ye

    return events
