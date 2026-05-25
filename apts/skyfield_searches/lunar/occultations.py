from typing import Any, cast
import numpy as np
from skyfield.api import Star
from ...cache import get_timescale
from ...constants import astronomy
from ...utils import planetary
from ..utils import _refine_conjunction

def find_lunar_occultations(observer, bright_stars, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = planetary.get_skyfield_obj("moon")
    earth = cast(Any, planetary.get_skyfield_obj("earth"))

    # Optimization: Filter stars close to the ecliptic (within 10 degrees)
    # The Moon stays within ~5.3 degrees of the ecliptic.
    v_ra_hours_all = bright_stars["ra_hours"].to_numpy()
    v_dec_degrees_all = bright_stars["dec_degrees"].to_numpy()
    star_names_all = bright_stars["Name"].to_numpy()

    stars_vector_all = Star(ra_hours=v_ra_hours_all, dec_degrees=v_dec_degrees_all)
    spos_at_t0_all = earth.at(t0).observe(stars_vector_all)
    lats, _, _ = spos_at_t0_all.ecliptic_latlon()

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

    # Topocentric position for Moon (coarse)
    mpos_coarse = observer.at(coarse_times).observe(moon).apparent()
    m_alt_coarse, _, m_dist_coarse = mpos_coarse.altaz()
    moon_rad_coarse = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_dist_coarse.km))

    # Unit vectors for Moon (coarse): (3, M)
    m_au_coarse = mpos_coarse.position.au
    u_moon_coarse = m_au_coarse / np.linalg.norm(m_au_coarse, axis=0)

    # Unit vectors for Stars (fixed at t0 in ICRS): (3, N)
    spos_stars = earth.at(t0).observe(stars_vector)
    stars_au = spos_stars.position.au
    u_stars = stars_au / np.linalg.norm(stars_au, axis=0)

    # Vectorized coarse separations: (N, M)
    # Using matrix multiplication to find separations between all stars and all Moon positions.
    dot_products = u_stars.T @ u_moon_coarse
    sep_coarse = np.degrees(np.arccos(np.clip(dot_products, -1.0, 1.0)))

    # Potential occultation: coarse separation < angular radius + margin (0.2 deg for safety)
    # Broadcast moon_rad_coarse (M,) to (N, M) and m_alt_coarse (M,) to (N, M)
    potential_mask = (sep_coarse < moon_rad_coarse + 0.2) & (m_alt_coarse.degrees > -1)

    events = []
    # Identify stars with potential occultations
    star_candidate_idxs = np.where(potential_mask.any(axis=1))[0]

    for star_idx in star_candidate_idxs:
        star_name = star_names[star_idx]
        star_obj = Star(ra_hours=v_ra_hours[star_idx], dec_degrees=v_dec_degrees[star_idx])

        # Find time windows for this star
        star_potential_mask = potential_mask[star_idx]
        window_indices = np.unique(
            np.concatenate(
                [
                    np.clip(coarse_idx[star_potential_mask] + offset, 0, num_steps - 1)
                    for offset in range(-15, 16)  # +/- 30 mins around potential event
                ]
            )
        )

        if len(window_indices) == 0:
            continue

        fine_times = times[window_indices]
        mpos_fine = observer.at(fine_times).observe(moon).apparent()
        m_alt_fine, _, m_dist_fine = mpos_fine.altaz(
            temperature_C=10.0, pressure_mbar=1013.25
        )
        moon_rad_fine = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_dist_fine.km))

        # Topocentric observation of star for maximum precision
        # Oracle: use apparent position to match refracted Moon position
        spos_fine = observer.at(fine_times).observe(star_obj).apparent()

        # Calculate separation from refracted positions
        # Skyfield's separation_from handles apparent positions correctly.
        # However, to be extra precise we should ensure we are comparing
        # refracted Moon to refracted Star.
        # .altaz() with temperature/pressure already accounts for refraction.
        # For separation, we compare positions in the observer's local frame.

        m_alt, m_az, _ = m_alt_fine, mpos_fine.altaz(temperature_C=10.0, pressure_mbar=1013.25)[1], None
        # m_alt is already m_alt_fine. I need m_az.
        m_alt, m_az, _ = mpos_fine.altaz(temperature_C=10.0, pressure_mbar=1013.25)
        s_alt, s_az, _ = spos_fine.altaz(temperature_C=10.0, pressure_mbar=1013.25)

        # Vectorized angular separation using Haversine-like formula on Alt/Az
        d_alt = m_alt.radians - s_alt.radians
        d_az = m_az.radians - s_az.radians

        a = np.sin(d_alt/2)**2 + np.cos(m_alt.radians) * np.cos(s_alt.radians) * np.sin(d_az/2)**2
        separations = np.degrees(2 * np.arcsin(np.sqrt(np.clip(a, 0, 1))))

        # Sun altitude for visibility check
        sun_alts = (
            observer.at(fine_times)
            .observe(planetary.get_skyfield_obj("sun"))
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
        )

        # Occultation check: separation < angular radius AND Moon above horizon AND Sun below -6 degrees
        occ_mask = (
            (separations < moon_rad_fine)
            & (m_alt.degrees > 0)
            & (sun_alts.degrees <= -6)
        )
        occ_indices_local = np.where(occ_mask)[0]

        if len(occ_indices_local) > 0:
            # map back to global times indices
            occ_indices_global = window_indices[occ_indices_local]
            # Group consecutive indices as one event
            groups = np.split(
                occ_indices_global, np.where(np.diff(occ_indices_global) > 10)[0] + 1
            )
            for group in groups:
                # To find min separation in this event, we need all separations for these indices
                # Actually we already have separations for all window_indices
                # Let's map global indices back to local (within window_indices)
                local_group_indices = np.searchsorted(window_indices, group)
                min_local_idx = local_group_indices[
                    np.argmin(separations[local_group_indices])
                ]
                min_global_idx = window_indices[min_local_idx]

                mid_t = times[min_global_idx]
                refined_t, _ = _refine_conjunction(observer, moon, star_obj, mid_t)

                # We need ingress/egress for the event dict
                ingress_idx = group[0]
                egress_idx = group[-1]

                events.append(
                    {
                        "date": refined_t.utc_datetime(),
                        "object1": "Moon",
                        "object2": star_name,
                        "ingress_time": times[ingress_idx].utc_datetime(),
                        "egress_time": times[egress_idx].utc_datetime(),
                        "type": "Lunar Occultation",
                        "event": "Lunar Occultation",
                    }
                )

    return events
