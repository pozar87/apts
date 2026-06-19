from typing import Any, cast, List, Dict
import numpy as np
from skyfield import almanac
from ...cache import get_timescale
from ...constants import astronomy
from .utils import (
    JovianSearchContext,
)


class JovianMoonState:
    """
    Computes geometric states for all 4 Galilean moons.
    Returns a 16-bit combined mask (4 bits per moon).
    Bits: 1: transit, 2: occultation, 4: shadow, 8: eclipse.
    """

    def __init__(self, ctx: JovianSearchContext):
        self.ctx = ctx
        self.step_days = 0.005  # ~7.2 minutes

    def __call__(self, t):
        is_array = hasattr(t, "shape") and t.shape != ()
        visible = self.ctx.get_visibility(t)

        if not is_array:
            if not visible:
                return 0
            return self._compute_scalar(t)
        else:
            final_res = np.zeros(len(t), dtype=int)
            if not np.any(visible):
                return final_res
            final_res[visible] = self._compute_vector(t[visible])
            return final_res

    def _compute_scalar(self, t):
        from .utils import is_inside_ellipsoid_projection_fast

        data = self.ctx.get_basic_data(t)
        j_obs = data["j_obs"]
        z_pole = data["z_pole"]
        sun_from_j = data["sun_from_j"]

        re = astronomy.JUPITER_RADIUS_KM
        rp = astronomy.JUPITER_POLAR_RADIUS_KM

        p_j_e = -j_obs.position.km
        d_j_e = j_obs.distance().km
        u_e = p_j_e / d_j_e

        p_j_s = sun_from_j.position.km
        d_j_s = sun_from_j.distance().km
        u_s = p_j_s / d_j_s

        u_z_e = np.dot(u_e, z_pole)
        u_z_s = np.dot(u_s, z_pole)

        u_prime_sq_e = (1.0 - u_z_e**2) / re**2 + u_z_e**2 / rp**2
        u_prime_sq_s = (1.0 - u_z_s**2) / re**2 + u_z_s**2 / rp**2

        res = 0
        for i, moon_id in enumerate(self.ctx.moon_map.keys()):
            if moon_id not in self.ctx.moon_objs:
                continue
            m_obs = self.ctx.get_moon_obs(t, moon_id)
            p_m = m_obs.position.km - j_obs.position.km

            p_z = np.dot(p_m, z_pole)
            p_sq = np.dot(p_m, p_m)
            p_m_u_e = np.dot(p_m, u_e)
            p_m_u_s = np.dot(p_m, u_s)

            in_projection_e = is_inside_ellipsoid_projection_fast(
                p_z, p_m_u_e, p_sq, u_z_e, re, rp, u_prime_sq_e
            )
            in_projection_s = is_inside_ellipsoid_projection_fast(
                p_z, p_m_u_s, p_sq, u_z_s, re, rp, u_prime_sq_s
            )
            moon_mask = (
                (in_projection_e & (p_m_u_e > 0)).astype(int)
                | ((in_projection_e & (p_m_u_e <= 0)).astype(int) << 1)
                | ((in_projection_s & (p_m_u_s > 0)).astype(int) << 2)
                | ((in_projection_s & (p_m_u_s <= 0)).astype(int) << 3)
            )
            res |= moon_mask << (4 * i)
        return res

    def _compute_vector(self, t_eval):
        from .utils import is_inside_ellipsoid_projection_fast

        data = self.ctx.get_basic_data(t_eval)
        j_obs = data["j_obs"]
        z_pole = data["z_pole"]
        sun_from_j = data["sun_from_j"]

        re = astronomy.JUPITER_RADIUS_KM
        rp = astronomy.JUPITER_POLAR_RADIUS_KM

        p_j_e = -j_obs.position.km
        d_j_e = j_obs.distance().km
        u_e = p_j_e / d_j_e[None, :]

        p_j_s = sun_from_j.position.km
        d_j_s = sun_from_j.distance().km
        u_s = p_j_s / d_j_s[None, :]

        u_z_e = np.einsum("ij,ij->j", u_e, z_pole)
        u_z_s = np.einsum("ij,ij->j", u_s, z_pole)

        u_prime_sq_e = (1.0 - u_z_e**2) / re**2 + u_z_e**2 / rp**2
        u_prime_sq_s = (1.0 - u_z_s**2) / re**2 + u_z_s**2 / rp**2

        mask_acc = np.zeros(len(t_eval), dtype=int)
        for i, moon_id in enumerate(self.ctx.moon_map.keys()):
            if moon_id not in self.ctx.moon_objs:
                continue
            m_obs = self.ctx.get_moon_obs(t_eval, moon_id)
            p_m = m_obs.position.km - j_obs.position.km

            p_z = np.einsum("ij,ij->j", p_m, z_pole)
            p_sq = np.einsum("ij,ij->j", p_m, p_m)
            p_m_u_e = np.einsum("ij,ij->j", p_m, u_e)
            p_m_u_s = np.einsum("ij,ij->j", p_m, u_s)

            in_projection_e = is_inside_ellipsoid_projection_fast(
                p_z, p_m_u_e, p_sq, u_z_e, re, rp, u_prime_sq_e
            )
            in_projection_s = is_inside_ellipsoid_projection_fast(
                p_z, p_m_u_s, p_sq, u_z_s, re, rp, u_prime_sq_s
            )
            moon_mask = (
                (in_projection_e & (p_m_u_e > 0)).astype(int)
                | ((in_projection_e & (p_m_u_e <= 0)).astype(int) << 1)
                | ((in_projection_s & (p_m_u_s > 0)).astype(int) << 2)
                | ((in_projection_s & (p_m_u_s <= 0)).astype(int) << 3)
            )
            mask_acc |= moon_mask << (4 * i)
        return mask_acc


def _append_moon_events(events: List[Dict], te, ye, y_prev, moons: List):
    """Parses state bitmask transitions and appends events."""
    event_types = [
        (1, "Transit"),
        (2, "Occultation"),
        (4, "Shadow Transit"),
        (8, "Eclipse"),
    ]

    for i, (_, moon_name) in enumerate(moons):
        m_prev = (y_prev >> (4 * i)) & 0xF
        m_curr = (ye >> (4 * i)) & 0xF
        for mask, type_name in event_types:
            # Transition out of state
            if (m_prev & mask) and not (m_curr & mask):
                events.append(
                    {
                        "date": te.utc_datetime(),
                        "object": moon_name,
                        "event": f"{moon_name} {type_name} End",
                        "type": "Jovian Moon Event",
                    }
                )
            # Transition into state
            if not (m_prev & mask) and (m_curr & mask):
                events.append(
                    {
                        "date": te.utc_datetime(),
                        "object": moon_name,
                        "event": f"{moon_name} {type_name} Start",
                        "type": "Jovian Moon Event",
                    }
                )


def find_jovian_moon_events(observer, start_date, end_date):
    """
    Finds Jovian moon events (Transits, Shadows, Occultations, Eclipses)
    for Io, Europa, Ganymede, and Callisto.
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
    state_func = JovianMoonState(ctx)
    t_events, y_events = almanac.find_discrete(t0, t1, state_func)

    y_start = state_func(t0)
    y_prev = int(np.atleast_1d(y_start)[0])
    moons = list(ctx.moon_map.items())

    for te, ye in zip(t_events, y_events):
        _append_moon_events(events, te, ye, y_prev, moons)
        y_prev = ye

    events.sort(key=lambda x: x["date"])
    return events
