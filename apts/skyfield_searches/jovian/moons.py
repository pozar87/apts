from typing import Any, cast
import numpy as np
from skyfield import almanac
from ...cache import get_timescale
from ...constants import astronomy
from ...utils import planetary
from .utils import _get_jovian_moon_objects, is_inside_ellipsoid_projection

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
        jupiter = eph["jupiter barycenter"]
        sun = eph["sun"]
        moon_map, moon_objs = _get_jovian_moon_objects(eph)
    except KeyError:
        return []

    events = []

    # Process each moon
    for moon_id, moon_name in moon_map.items():
        moon_obj = moon_objs[moon_id]

        def get_geometry(t):
            """
            Computes geometric states for a given moon at time(s) t.
            Returns visible, in_transit, in_occultation, in_shadow, in_eclipse.
            """
            is_array = hasattr(t, "shape") and t.shape != ()

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
            ])

            # Vector from Jupiter to Moon
            p_m = m_obs.position.km - j_obs.position.km

            # 3. Earth perspective (Transits and Occultations)
            # Vector from Jupiter to Earth
            p_j_e = -j_obs.position.km
            if is_array:
                u_e = p_j_e / np.linalg.norm(p_j_e, axis=0)
                p_m_u_e = np.sum(p_m * u_e, axis=0)
            else:
                u_e = p_j_e / np.linalg.norm(p_j_e)
                p_m_u_e = np.dot(p_m, u_e)

            in_projection_e = is_inside_ellipsoid_projection(p_m, u_e, z_pole, re, rp)
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
                p_m_u_s = np.dot(p_m, u_s)

            in_projection_s = is_inside_ellipsoid_projection(p_m, u_s, z_pole, re, rp)
            # Between Sun and Jupiter (Shadow on Jupiter) means p_m . u_s > 0
            in_shadow = in_projection_s & (p_m_u_s > 0)
            in_eclipse = in_projection_s & (p_m_u_s <= 0)

            return visible, in_transit, in_occultation, in_shadow, in_eclipse

        def find_events_for_type(type_name, type_idx):
            def state_func(t):
                geom = get_geometry(t)
                # visible is index 0, others follow: 1: transit, 2: occultation, 3: shadow, 4: eclipse
                return (geom[0] & geom[type_idx]).astype(int)

            setattr(state_func, "step_days", 0.005)  # ~7.2 minutes
            t_events, y_events = almanac.find_discrete(t0, t1, state_func)

            # Check initial state
            y_start = state_func(t0)
            y_prev = int(np.atleast_1d(y_start)[0])

            for te, ye in zip(t_events, y_events):
                if y_prev != 0:
                    events.append(
                        {
                            "date": te.utc_datetime(),
                            "object": moon_name,
                            "event": f"{moon_name} {type_name} End",
                            "type": "Jovian Moon Event",
                        }
                    )
                if ye != 0:
                    events.append(
                        {
                            "date": te.utc_datetime(),
                            "object": moon_name,
                            "event": f"{moon_name} {type_name} Start",
                            "type": "Jovian Moon Event",
                        }
                    )
                y_prev = ye

        find_events_for_type("Transit", 1)
        find_events_for_type("Occultation", 2)
        find_events_for_type("Shadow Transit", 3)
        find_events_for_type("Eclipse", 4)

    events.sort(key=lambda x: x["date"])
    return events
