from typing import Any, cast
import numpy as np
from skyfield import almanac
from ...cache import get_timescale
from ...constants import astronomy
from .utils import (
    is_inside_ellipsoid_projection,
    JovianSearchContext,
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

    def state_func(t):
        """
        Computes geometric states for all 4 Galilean moons at time(s) t.
        Returns a 16-bit combined mask (4 bits per moon).
        Bits: 1: transit, 2: occultation, 4: shadow, 8: eclipse.
        """
        is_array = hasattr(t, "shape") and t.shape != ()
        visible = ctx.get_visibility(t)

        if not is_array:
            if not visible:
                return 0
            t_eval = t
        else:
            if not np.any(visible):
                return np.zeros(len(t), dtype=int)
            t_eval = t[visible]

        data = ctx.get_basic_data(t_eval)
        j_obs = data["j_obs"]
        z_pole = data["z_pole"]
        sun_from_j = data["sun_from_j"]

        re = astronomy.JUPITER_RADIUS_KM
        rp = astronomy.JUPITER_POLAR_RADIUS_KM

        p_j_e = -j_obs.position.km
        d_j_e = j_obs.distance().km
        u_e = p_j_e / d_j_e[None, :] if is_array else p_j_e / d_j_e

        p_j_s = sun_from_j.position.km
        d_j_s = sun_from_j.distance().km
        u_s = p_j_s / d_j_s[None, :] if is_array else p_j_s / d_j_s

        if not is_array:
            res = 0
            for i, moon_id in enumerate(ctx.moon_map.keys()):
                m_obs = ctx.get_moon_obs(t_eval, moon_id)
                p_m = m_obs.position.km - j_obs.position.km
                p_m_u_e = np.dot(p_m, u_e)
                p_m_u_s = np.dot(p_m, u_s)
                in_projection_e = is_inside_ellipsoid_projection(
                    p_m, u_e, z_pole, re, rp
                )
                in_projection_s = is_inside_ellipsoid_projection(
                    p_m, u_s, z_pole, re, rp
                )
                moon_mask = (
                    (in_projection_e & (p_m_u_e > 0)).astype(int)
                    | ((in_projection_e & (p_m_u_e <= 0)).astype(int) << 1)
                    | ((in_projection_s & (p_m_u_s > 0)).astype(int) << 2)
                    | ((in_projection_s & (p_m_u_s <= 0)).astype(int) << 3)
                )
                res |= moon_mask << (4 * i)
            return res
        else:
            final_res = np.zeros(len(t), dtype=int)
            mask_acc = np.zeros(len(t_eval), dtype=int)
            for i, moon_id in enumerate(ctx.moon_map.keys()):
                m_obs = ctx.get_moon_obs(t_eval, moon_id)
                p_m = m_obs.position.km - j_obs.position.km
                p_m_u_e = np.einsum("ij,ij->j", p_m, u_e)
                p_m_u_s = np.einsum("ij,ij->j", p_m, u_s)
                in_projection_e = is_inside_ellipsoid_projection(
                    p_m, u_e, z_pole, re, rp
                )
                in_projection_s = is_inside_ellipsoid_projection(
                    p_m, u_s, z_pole, re, rp
                )
                moon_mask = (
                    (in_projection_e & (p_m_u_e > 0)).astype(int)
                    | ((in_projection_e & (p_m_u_e <= 0)).astype(int) << 1)
                    | ((in_projection_s & (p_m_u_s > 0)).astype(int) << 2)
                    | ((in_projection_s & (p_m_u_s <= 0)).astype(int) << 3)
                )
                mask_acc |= moon_mask << (4 * i)
            final_res[visible] = mask_acc
            return final_res

    setattr(state_func, "step_days", 0.005)  # ~7.2 minutes
    t_events, y_events = almanac.find_discrete(t0, t1, state_func)

    y_start = state_func(t0)
    y_prev = int(np.atleast_1d(y_start)[0])

    event_types = [
        (1, "Transit"),
        (2, "Occultation"),
        (4, "Shadow Transit"),
        (8, "Eclipse"),
    ]
    moons = list(ctx.moon_map.items())

    for te, ye in zip(t_events, y_events):
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
        y_prev = ye

    events.sort(key=lambda x: x["date"])
    return events
