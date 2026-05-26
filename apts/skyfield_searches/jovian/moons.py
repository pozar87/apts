from typing import Any, cast
import numpy as np
from skyfield import almanac
from ...cache import get_timescale
from ...constants import astronomy
from .utils import (
    _get_jovian_moon_objects,
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

    # Process each moon
    for moon_id, moon_name in ctx.moon_map.items():

        def state_func(t):
            """
            Computes geometric states for a given moon at time(s) t.
            Returns a bitmask: 1: transit, 2: occultation, 4: shadow, 8: eclipse.
            All gated by visibility.
            """
            is_array = hasattr(t, "shape") and t.shape != ()
            data = ctx.get_basic_data(t)
            j_obs = data["j_obs"]
            m_obs = ctx.get_moon_obs(t, moon_id)

            # Visibility check (cached in ctx)
            visible = ctx.get_visibility(t)

            # Vector from Jupiter to Moon
            p_m = m_obs.position.km - j_obs.position.km

            # Jupiter physical parameters
            re = astronomy.JUPITER_RADIUS_KM
            rp = astronomy.JUPITER_POLAR_RADIUS_KM
            z_pole = data["z_pole"]

            # Earth perspective (Transits and Occultations)
            p_j_e = -j_obs.position.km
            if is_array:
                u_e = p_j_e / np.linalg.norm(p_j_e, axis=0)
                # Optimization: einsum is ~2x faster than np.sum(A*B, axis=0)
                p_m_u_e = np.einsum("ij,ij->j", p_m, u_e)
            else:
                u_e = p_j_e / np.linalg.norm(p_j_e)
                p_m_u_e = np.dot(p_m, u_e)

            in_projection_e = is_inside_ellipsoid_projection(p_m, u_e, z_pole, re, rp)
            in_transit = visible & in_projection_e & (p_m_u_e > 0)
            in_occultation = visible & in_projection_e & (p_m_u_e <= 0)

            # Sun perspective (Shadows and Eclipses)
            p_j_s = data["sun_from_j"].position.km
            if is_array:
                u_s = p_j_s / np.linalg.norm(p_j_s, axis=0)
                # Optimization: einsum is ~2x faster than np.sum(A*B, axis=0)
                p_m_u_s = np.einsum("ij,ij->j", p_m, u_s)
            else:
                u_s = p_j_s / np.linalg.norm(p_j_s)
                p_m_u_s = np.dot(p_m, u_s)

            in_projection_s = is_inside_ellipsoid_projection(p_m, u_s, z_pole, re, rp)
            in_shadow = visible & in_projection_s & (p_m_u_s > 0)
            in_eclipse = visible & in_projection_s & (p_m_u_s <= 0)

            # Combine into bitmask
            res = (
                in_transit.astype(int)
                | (in_occultation.astype(int) << 1)
                | (in_shadow.astype(int) << 2)
                | (in_eclipse.astype(int) << 3)
            )
            return res

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

        for te, ye in zip(t_events, y_events):
            for mask, type_name in event_types:
                # Transition out of state
                if (y_prev & mask) and not (ye & mask):
                    events.append(
                        {
                            "date": te.utc_datetime(),
                            "object": moon_name,
                            "event": f"{moon_name} {type_name} End",
                            "type": "Jovian Moon Event",
                        }
                    )
                # Transition into state
                if not (y_prev & mask) and (ye & mask):
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
