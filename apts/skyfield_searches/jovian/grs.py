import numpy as np
from skyfield.searchlib import find_minima
from ...cache import get_timescale
from ...utils import planetary

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

    if not len(times):
        return []

    # Vectorized visibility check
    j_obs = observer.at(times).observe(jupiter).apparent()
    alt, _, _ = j_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)
    s_obs = observer.at(times).observe(sun).apparent()
    sun_alt = s_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
    elongation = j_obs.separation_from(s_obs).degrees

    visible_mask = (alt.degrees > 0) & (sun_alt <= -6) & (elongation > 10)

    events = []
    for i, t in enumerate(times):
        if visible_mask[i]:
            events.append(
                {
                    "date": t.utc_datetime(),
                    "event": "Jupiter Great Red Spot Transit",
                    "object": "Jupiter",
                    "type": "Jupiter GRS Transit",
                    "altitude": float(alt.degrees[i]),
                }
            )

    return events
