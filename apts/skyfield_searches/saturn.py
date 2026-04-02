from typing import Any, cast
import numpy as np
from skyfield import almanac
from ..cache import get_timescale, get_ephemeris
from ..utils import planetary

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
        # Oracle: use astrometric positions for maximum consistency and accuracy.
        # This includes light-time correction for the position of Saturn.
        # We ensure a stable observation by using the center of the observer body.
        pos = observer_obj.at(t).observe(saturn)
        v_sat_obs = -pos.position.au / pos.distance().au

        # Oracle: evaluate pole orientation at the time the light left Saturn.
        t_eval = get_timescale().tt_jd(t.tt - pos.light_time)

        # Saturn's pole in J2000.0 at evaluated time
        alpha_p_deg, delta_p_deg = planetary.get_saturn_pole(t_eval)
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
