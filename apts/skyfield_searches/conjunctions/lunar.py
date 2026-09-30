from typing import cast

import numpy as np
from skyfield import almanac

from ...cache import get_ephemeris, get_timescale
from ...constants import astronomy
from ...utils import planetary
from ..utils import _refine_conjunction, fast_altaz


def _is_occulted(t, observer, moon, sun, planet):
    """
    Check if planet is occulted by the Moon at time t for observer.
    """
    # Optimization: Use fast_altaz for Sun and Moon altitude checks to bypass
    # atmospheric refraction & frame transformation overhead during discrete search steps.
    obs_at_t = observer.at(t)
    m = obs_at_t.observe(moon).apparent()
    p = obs_at_t.observe(planet).apparent()
    sep = m.separation_from(p).degrees
    rad = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m.distance().km))
    alt = fast_altaz(obs_at_t, moon, temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
    sun_alt = fast_altaz(obs_at_t, sun, temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
    return (sep < rad) & (alt > 0) & (sun_alt <= -6)


def _process_occultation_window(observer, moon, sun, planet, simple_name, times, group, coarse_idx, ts):
    """
    Process a single contiguous window of potential occultation coarse points.
    """
    num_steps = len(times)
    w_start_idx = max(0, coarse_idx[group[0]] - 30)
    w_end_idx = min(num_steps - 1, coarse_idx[group[-1]] + 30)
    w_start_t = times[w_start_idx]
    w_end_t = times[w_end_idx]

    def check_fn(t):
        return _is_occulted(t, observer, moon, sun, planet)

    check_fn.step_days = 0.005
    t_occ, _ = almanac.find_discrete(w_start_t, w_end_t, check_fn)

    t_list = list(t_occ)
    if check_fn(w_start_t):
        t_list.insert(0, w_start_t)
    if len(t_list) % 2 != 0:
        t_list.append(w_end_t)

    events = []
    for i in range(0, len(t_list), 2):
        if i + 1 < len(t_list):
            ingress_t = t_list[i]
            egress_t = t_list[i + 1]
            mid_t = ts.from_datetime(
                ingress_t.utc_datetime()
                + (egress_t.utc_datetime() - ingress_t.utc_datetime()) / 2
            )
            refined_t, _ = _refine_conjunction(observer, moon, planet, mid_t)

            events.append(
                {
                    "date": refined_t.utc_datetime(),
                    "object1": "Moon",
                    "object2": simple_name,
                    "ingress_time": ingress_t.utc_datetime(),
                    "egress_time": egress_t.utc_datetime(),
                    "type": "Lunar Planetary Occultation",
                    "event": "Lunar Planetary Occultation",
                }
            )
    return events


def find_lunar_planetary_occultations(observer, start_date, end_date):
    """
    Finds occultations of planets by the Moon for a specific observer.
    Provides precise ingress and egress times.
    Optimized via a two-stage geocentric/topocentric coarse check followed
    by windowed refinement.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = planetary.get_skyfield_obj("moon")
    sun = planetary.get_skyfield_obj("sun")
    eph = get_ephemeris()
    earth = eph["earth"]

    planet_names = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]
    planet_objs = [planetary.get_skyfield_obj(p) for p in planet_names]
    simple_names = [planetary.get_simple_name(p) for p in planet_names]

    duration_days = t1 - t0
    num_steps = int(duration_days * 24 * 30)
    if num_steps < 2:
        return []
    times = ts.linspace(t0, t1, num_steps)

    # Optimization: Use 1-minute coarse steps (step=30) for Stage 1 & Stage 2 coarse checks.
    coarse_step = 30
    coarse_idx = np.arange(0, num_steps, coarse_step)
    coarse_times = times[coarse_idx]

    # Optimization: Stage 1 Geocentric Coarse Filter.
    # Evaluating topocentric observer state over all coarse_times requires
    # expensive ITRS frame rotations, GAST, and iau2000a nutation calculations.
    # Since topocentric lunar parallax is bounded by < 1.05°, checking geocentric
    # unit vector separation with a 1.3° safety margin filters out ~99% of empty
    # coarse steps instantly, preserving full accuracy while avoiding redundant
    # topocentric observer setups.
    mpos_geo = earth.at(coarse_times).observe(moon)
    m_dist_geo = mpos_geo.distance()
    moon_rad_geo = np.degrees(
        np.arcsin(astronomy.MOON_RADIUS_KM / cast(float, m_dist_geo.km))
    )
    cos_threshold_geo = np.cos(np.radians(moon_rad_geo + 1.3))
    m_au_geo = mpos_geo.position.au
    u_moon_geo = m_au_geo / np.linalg.norm(m_au_geo, axis=0)

    events = []

    for p_idx, planet in enumerate(planet_objs):
        simple_name = simple_names[p_idx]

        ppos_geo = earth.at(coarse_times).observe(planet)
        p_au_geo = ppos_geo.position.au
        u_planet_geo = p_au_geo / np.linalg.norm(p_au_geo, axis=0)

        dot_geo = np.sum(u_moon_geo * u_planet_geo, axis=0)
        cand_mask = dot_geo > cos_threshold_geo

        if not np.any(cand_mask):
            continue

        # Stage 2: Evaluate topocentric positions ONLY for candidate coarse steps
        cand_coarse_idx = coarse_idx[cand_mask]
        cand_coarse_times = times[cand_coarse_idx]
        obs_at_cand = observer.at(cand_coarse_times)

        mpos_cand = obs_at_cand.observe(moon)
        m_alt_cand, _, m_dist_cand = fast_altaz(
            obs_at_cand, moon, temperature_C=10.0, pressure_mbar=1013.25
        )
        moon_rad_cand = np.degrees(
            np.arcsin(astronomy.MOON_RADIUS_KM / cast(float, m_dist_cand.km))
        )

        sun_alts_cand, _, _ = fast_altaz(
            obs_at_cand, sun, temperature_C=10.0, pressure_mbar=1013.25
        )

        ppos_cand = obs_at_cand.observe(planet)
        sep_cand = mpos_cand.separation_from(ppos_cand).degrees

        potential_mask = (
            (sep_cand < moon_rad_cand + 0.2)
            & (cast(float, m_alt_cand.degrees) > -1)
            & (cast(float, sun_alts_cand.degrees) <= -5)
        )

        if not np.any(potential_mask):
            continue

        cand_indices_in_group = np.where(potential_mask)[0]
        actual_coarse_indices = cand_coarse_idx[cand_indices_in_group]

        potential_groups = np.split(
            actual_coarse_indices,
            np.where(np.diff(actual_coarse_indices) > coarse_step)[0] + 1,
        )

        for group in potential_groups:
            coarse_group = [np.where(coarse_idx == idx)[0][0] for idx in group]
            group_events = _process_occultation_window(
                observer, moon, sun, planet, simple_name, times, coarse_group, coarse_idx, ts
            )
            events.extend(group_events)

    return events
