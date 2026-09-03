import numpy as np
from skyfield.searchlib import find_minima

from ...cache import get_timescale
from ...utils import planetary
from ..utils import fast_altaz


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

    # Optimization: Pre-compute System II CML on a 1-hour grid over [t0, t1]
    # to avoid thousands of repetitive PyEphem evaluations during find_minima steps.
    hours_total = float((t1 - t0) * 24.0)
    n_grid = max(2, int(np.ceil(hours_total)) + 1)
    t_grid_rel = np.linspace(0, hours_total, n_grid)
    t_grid = ts.tt_jd(t0.tt + t_grid_rel / 24.0)

    cml2_grid = planetary.get_jupiter_system_ii_longitude(t_grid)
    cml2_unwrapped = np.unwrap(np.radians(cml2_grid))

    def cml_difference(t):
        grs_lon = (
            grs_longitude
            if grs_longitude is not None
            else planetary.get_jupiter_grs_longitude(t)
        )
        if hasattr(t, "tt"):
            rel_hours = (t.tt - t0.tt) * 24.0
            sys_ii_lon = (
                np.degrees(np.interp(rel_hours, t_grid_rel, cml2_unwrapped)) % 360
            )
        else:
            sys_ii_lon = planetary.get_jupiter_system_ii_longitude(t)
        return (sys_ii_lon - grs_lon + 180) % 360 - 180

    def abs_diff(t):
        return np.abs(cml_difference(t))

    # Jupiter rotates every ~9.9 hours (~0.41 days).
    # A step of 0.1 days (~2.4 hours) is safe to find every transit.
    abs_diff.step_days = 0.1
    times, _ = find_minima(t0, t1, abs_diff)

    if not len(times):
        return []

    # Vectorized visibility check
    # Optimization: Hoist observer.at(times) to avoid repeated coordinate setup.
    obs_at_times = observer.at(times)
    j_obs = obs_at_times.observe(jupiter).apparent()
    alt, _, _ = j_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)
    # Optimization: Use fast_altaz for Sun visibility check.
    sun_alt = fast_altaz(obs_at_times, sun)[0].degrees
    s_obs = obs_at_times.observe(sun)
    elongation = j_obs.separation_from(s_obs).degrees

    visible_mask = (alt.degrees > 0) & (sun_alt <= -6) & (elongation > 10)  # type: ignore[operator]

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
