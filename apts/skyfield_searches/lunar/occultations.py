from typing import Any, cast
import numpy as np
from skyfield.api import Star
from ...cache import get_timescale
from ...constants import astronomy
from ...utils import planetary
from ..utils import _refine_conjunction, fast_altaz

def find_lunar_occultations(observer, bright_stars, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = planetary.get_skyfield_obj("moon")
    earth = cast(Any, planetary.get_skyfield_obj("earth"))
    sun = planetary.get_skyfield_obj("sun")

    # Optimization: Filter stars close to the ecliptic (within 10 degrees)
    # The Moon stays within ~5.3 degrees of the ecliptic.
    v_ra_hours_all = bright_stars["ra_hours"].to_numpy()
    v_dec_degrees_all = bright_stars["dec_degrees"].to_numpy()
    star_names_all = bright_stars["Name"].to_numpy()

    stars_vector_all = Star(ra_hours=v_ra_hours_all, dec_degrees=v_dec_degrees_all)
    # Use midpoint for ecliptic check to account for slight precession if the window is very long
    t_mid = ts.tt_jd((t0.tt + t1.tt) / 2)
    spos_at_t_mid_all = earth.at(t_mid).observe(stars_vector_all)
    lats, _, _ = spos_at_t_mid_all.ecliptic_latlon()

    mask_ecliptic = np.abs(lats.degrees) < 10
    v_ra_hours = v_ra_hours_all[mask_ecliptic]
    v_dec_degrees = v_dec_degrees_all[mask_ecliptic]
    star_names = star_names_all[mask_ecliptic]
    stars_vector = Star(ra_hours=v_ra_hours, dec_degrees=v_dec_degrees)

    # Check every 2 minutes for precision
    num_steps = int((t1 - t0) * 24 * 30)
    if num_steps < 2:
        return []
    times = ts.linspace(t0, t1, num_steps)

    # Coarse check every 20 minutes (1 in 10 points)
    coarse_idx = np.arange(0, num_steps, 10)
    coarse_times = times[coarse_idx]

    # Optimization: use fast_altaz for coarse check
    mpos_coarse_alt, _, m_dist_coarse = fast_altaz(observer.at(coarse_times), moon)
    moon_rad_coarse = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_dist_coarse.km))

    # Unit vectors for Moon (coarse): (3, M)
    # We observe stars once in ICRS for the coarse check (sufficiently accurate)
    mpos_coarse = observer.at(coarse_times).observe(moon)
    m_au_coarse = mpos_coarse.position.au
    u_moon_coarse = m_au_coarse / np.linalg.norm(m_au_coarse, axis=0)

    spos_stars = earth.at(t_mid).observe(stars_vector)
    stars_au = spos_stars.position.au
    u_stars = stars_au / np.linalg.norm(stars_au, axis=0)

    # Vectorized coarse separations: (N, M)
    dot_products = u_stars.T @ u_moon_coarse
    sep_coarse = np.degrees(np.arccos(np.clip(dot_products, -1.0, 1.0)))

    # Potential occultation: coarse separation < angular radius + margin (0.2 deg for safety)
    potential_mask = (sep_coarse < moon_rad_coarse + 0.2) & (mpos_coarse_alt.degrees > -1)

    if not np.any(potential_mask):
        return []

    # Identify all required time indices for the fine check
    # +/- 30 mins around potential event (15 steps at 2-min resolution)
    active_indices = np.unique(
        np.concatenate(
            [
                np.clip(coarse_idx[np.any(potential_mask, axis=0)] + offset, 0, num_steps - 1)
                for offset in range(-15, 16)
            ]
        )
    )

    if len(active_indices) == 0:
        return []

    # --- Optimized Fine Check ---
    fine_times = times[active_indices]
    obs_at_fine_times = observer.at(fine_times)

    # Hoist environment observations using fast_altaz
    m_alt, _, m_dist = fast_altaz(obs_at_fine_times, moon)
    moon_rad_fine = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_dist.km))

    sun_alt, _, _ = fast_altaz(obs_at_fine_times, sun)

    # Determine which stars are candidates for the fine check
    star_candidate_idxs = np.where(potential_mask.any(axis=1))[0]
    num_candidates = len(star_candidate_idxs)

    # Vectorized Star observation for all candidates
    stars_vector_candidates = Star(
        ra_hours=v_ra_hours[star_candidate_idxs],
        dec_degrees=v_dec_degrees[star_candidate_idxs]
    )

    # Unit vectors for Moon at active times
    m_pos_topo = obs_at_fine_times.observe(moon)
    u_moon_fine = m_pos_topo.position.au / np.linalg.norm(m_pos_topo.position.au, axis=0)

    # Observe stars once at t_mid for the fine check grid.
    # Diurnal parallax and aberration change star positions by < 30",
    # which is negligible for finding occultation candidates.
    s_pos_mid = observer.at(t_mid).observe(stars_vector_candidates)
    u_stars_fine = s_pos_mid.position.au / np.linalg.norm(s_pos_mid.position.au, axis=0)

    # Vectorized dot products: (N, 3) @ (3, T) -> (N, T)
    dots_fine = u_stars_fine.T @ u_moon_fine
    separations_fine = np.degrees(np.arccos(np.clip(dots_fine, -1.0, 1.0)))

    # Occultation check grid: (N, T)
    occ_mask = (
        (separations_fine < moon_rad_fine)
        & (m_alt.degrees > 0)
        & (sun_alt.degrees <= -6)
    )

    events = []
    for i, star_idx in enumerate(star_candidate_idxs):
        star_name = star_names[star_idx]
        star_occ_mask = occ_mask[i]

        if not np.any(star_occ_mask):
            continue

        # Reconstruct the individual Star object for refinement
        target_star = Star(
            ra_hours=v_ra_hours[star_idx], dec_degrees=v_dec_degrees[star_idx]
        )

        occ_indices_local = np.where(star_occ_mask)[0]
        occ_indices_global = active_indices[occ_indices_local]

        # Group consecutive indices as one event
        groups = np.split(
            occ_indices_global, np.where(np.diff(occ_indices_global) > 10)[0] + 1
        )

        for group in groups:
            # Map global indices back to local (within active_indices)
            local_group_indices = np.searchsorted(active_indices, group)
            min_local_idx = local_group_indices[
                np.argmin(separations_fine[i, local_group_indices])
            ]
            min_global_idx = active_indices[min_local_idx]

            mid_t = times[min_global_idx]
            refined_t, _ = _refine_conjunction(observer, moon, target_star, mid_t)

            events.append(
                {
                    "date": refined_t.utc_datetime(),
                    "object1": "Moon",
                    "object2": star_name,
                    "ingress_time": times[group[0]].utc_datetime(),
                    "egress_time": times[group[-1]].utc_datetime(),
                    "type": "Lunar Occultation",
                    "event": "Lunar Occultation",
                }
            )

    return events
