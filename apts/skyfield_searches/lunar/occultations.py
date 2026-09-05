from typing import Any, cast

import numpy as np
from skyfield.api import Star

from ...cache import get_timescale
from ...constants import astronomy
from ...utils import planetary
from ..utils import _refine_conjunction, fast_altaz


def _filter_ecliptic_stars(bright_stars, earth, t_mid):
    """
    Filter stars close to the ecliptic (within 10 degrees).
    The Moon stays within ~5.3 degrees of the ecliptic.
    """
    v_ra_hours_all = bright_stars["ra_hours"].to_numpy()
    v_dec_degrees_all = bright_stars["dec_degrees"].to_numpy()
    star_names_all = bright_stars["Name"].to_numpy()

    stars_vector_all = Star(ra_hours=v_ra_hours_all, dec_degrees=v_dec_degrees_all)
    spos_at_t_mid_all = earth.at(t_mid).observe(stars_vector_all)
    lats, _, _ = spos_at_t_mid_all.ecliptic_latlon()

    mask_ecliptic = np.abs(lats.degrees) < 10
    v_ra_hours = v_ra_hours_all[mask_ecliptic]
    v_dec_degrees = v_dec_degrees_all[mask_ecliptic]
    star_names = star_names_all[mask_ecliptic]

    stars_au = spos_at_t_mid_all.position.au[:, mask_ecliptic]
    u_stars = stars_au / np.linalg.norm(stars_au, axis=0)

    return v_ra_hours, v_dec_degrees, star_names, u_stars


def _perform_coarse_occultation_check(observer, moon, coarse_times, u_stars):
    """
    Perform coarse 20-minute grid separation and topocentric altitude checks.
    Returns potential_mask where occultations could occur.
    """
    mpos_coarse = observer.at(coarse_times).observe(moon)
    m_dist_coarse = mpos_coarse.distance()
    moon_rad_coarse = np.degrees(
        np.arcsin(astronomy.MOON_RADIUS_KM / m_dist_coarse.km)
    )

    m_au_coarse = mpos_coarse.position.au
    u_moon_coarse = m_au_coarse / np.linalg.norm(m_au_coarse, axis=0)

    dot_products = u_stars.T @ u_moon_coarse
    sep_coarse = np.degrees(np.arccos(np.clip(dot_products, -1.0, 1.0)))

    potential_mask_sep = sep_coarse < moon_rad_coarse + 0.2
    has_potential_star = np.any(potential_mask_sep, axis=0)

    mpos_coarse_alt_deg = np.full(len(coarse_times), -999.0)
    if np.any(has_potential_star):
        active_coarse_times = coarse_times[has_potential_star]
        alt, _, _ = fast_altaz(observer.at(active_coarse_times), moon)
        mpos_coarse_alt_deg[has_potential_star] = alt.degrees

    return potential_mask_sep & (mpos_coarse_alt_deg > -1)


def _perform_fine_occultation_check(
    observer,
    moon,
    sun,
    times,
    active_indices,
    potential_mask,
    u_stars,
    v_ra_hours,
    v_dec_degrees,
    star_names,
):
    """
    Perform fine 2-minute grid check and refine event conjunction timings.
    """
    fine_times = times[active_indices]
    obs_at_fine_times = observer.at(fine_times)

    m_alt, _, m_dist = fast_altaz(obs_at_fine_times, moon)
    moon_rad_fine = np.degrees(
        np.arcsin(astronomy.MOON_RADIUS_KM / cast(float, m_dist.km))
    )

    sun_alt, _, _ = fast_altaz(obs_at_fine_times, sun)

    star_candidate_idxs = np.where(potential_mask.any(axis=1))[0]

    m_pos_topo = obs_at_fine_times.observe(moon)
    u_moon_fine = m_pos_topo.position.au / np.linalg.norm(
        m_pos_topo.position.au, axis=0
    )

    u_stars_fine = u_stars[:, star_candidate_idxs]

    dots_fine = u_stars_fine.T @ u_moon_fine
    separations_fine = np.degrees(np.arccos(np.clip(dots_fine, -1.0, 1.0)))

    occ_mask = (
        (separations_fine < moon_rad_fine)
        & (cast(float, m_alt.degrees) > 0)
        & (cast(float, sun_alt.degrees) <= -6)
    )

    events = []
    for i, star_idx in enumerate(star_candidate_idxs):
        star_name = star_names[star_idx]
        star_occ_mask = occ_mask[i]

        if not np.any(star_occ_mask):
            continue

        target_star = Star(
            ra_hours=v_ra_hours[star_idx], dec_degrees=v_dec_degrees[star_idx]
        )

        occ_indices_local = np.where(star_occ_mask)[0]
        occ_indices_global = active_indices[occ_indices_local]

        groups = np.split(
            occ_indices_global, np.where(np.diff(occ_indices_global) > 10)[0] + 1
        )

        for group in groups:
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


def find_lunar_occultations(observer, bright_stars, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = planetary.get_skyfield_obj("moon")
    earth = cast(Any, planetary.get_skyfield_obj("earth"))
    sun = planetary.get_skyfield_obj("sun")

    t_mid = ts.tt_jd((t0.tt + t1.tt) / 2)
    (
        v_ra_hours,
        v_dec_degrees,
        star_names,
        u_stars,
    ) = _filter_ecliptic_stars(bright_stars, earth, t_mid)

    num_steps = int((t1 - t0) * 24 * 30)
    if num_steps < 2:
        return []
    times = ts.linspace(t0, t1, num_steps)

    coarse_idx = np.arange(0, num_steps, 10)
    coarse_times = times[coarse_idx]

    potential_mask = _perform_coarse_occultation_check(
        observer, moon, coarse_times, u_stars
    )

    if not np.any(potential_mask):
        return []

    active_indices = np.unique(
        np.concatenate(
            [
                np.clip(
                    coarse_idx[np.any(potential_mask, axis=0)] + offset,
                    0,
                    num_steps - 1,
                )
                for offset in range(-15, 16)
            ]
        )
    )

    if len(active_indices) == 0:
        return []

    return _perform_fine_occultation_check(
        observer,
        moon,
        sun,
        times,
        active_indices,
        potential_mask,
        u_stars,
        v_ra_hours,
        v_dec_degrees,
        star_names,
    )
