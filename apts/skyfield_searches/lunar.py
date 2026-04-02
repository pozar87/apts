from typing import Any, cast
import numpy as np
from skyfield import almanac
from skyfield.api import Star
from skyfield.searchlib import find_maxima, find_minima
from ..cache import get_timescale, get_ephemeris
from ..constants import astronomy
from ..utils import planetary
from .utils import _refine_conjunction

def find_supermoons(start_date, end_date):
    """
    Finds Supermoons (Perigee-Syzygy events).
    A Supermoon is defined here as a Full Moon occurring when the Moon is within
    90% of its closest approach (perigee) for a given orbit.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = get_ephemeris()
    moon = planetary.get_skyfield_obj("moon")
    earth = planetary.get_skyfield_obj("earth")

    # 1. Find all Full Moons in the range
    f = almanac.moon_phases(eph)
    t_phases, y_phases = almanac.find_discrete(t0, t1, f)
    full_moons = [t for t, y in zip(t_phases, y_phases) if y == 2]

    events = []
    for t_full in full_moons:
        # 2. For each Full Moon, find the nearest perigee and apogee to determine the 90% threshold
        # Search window: +/- 15 days around the full moon
        t_start = ts.tt_jd(t_full.tt - 15)
        t_end = ts.tt_jd(t_full.tt + 15)

        def distance_to_earth(t):
            return cast(Any, earth).at(t).observe(moon).distance().km

        setattr(distance_to_earth, "step_days", 1.0)
        t_max, v_max = find_maxima(t_start, t_end, distance_to_earth)
        t_min, v_min = find_minima(t_start, t_end, distance_to_earth)

        if len(v_min) > 0 and len(v_max) > 0:
            perigee_dist = v_min[0]
            apogee_dist = v_max[0]

            # Distance at the moment of Full Moon
            current_dist = distance_to_earth(t_full)

            # Supermoon threshold (90% between apogee and perigee)
            # Threshold = Perigee + 0.1 * (Apogee - Perigee)
            threshold = perigee_dist + 0.1 * (apogee_dist - perigee_dist)

            if current_dist <= threshold:
                events.append({
                    "date": t_full.utc_datetime(),
                    "event": "Supermoon",
                    "object": "Moon",
                    "type": "Supermoon",
                    "distance_km": float(current_dist),
                    "perigee_distance_km": float(perigee_dist)
                })

    return events

def find_moon_apogee_perigee(start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    moon = planetary.get_skyfield_obj("moon")
    earth = planetary.get_skyfield_obj("earth")

    def distance_to_earth(t):
        return cast(Any, earth).at(t).observe(moon).distance().km

    setattr(distance_to_earth, "step_days", 13)

    max_times, _ = find_maxima(t0, t1, distance_to_earth)
    min_times, _ = find_minima(t0, t1, distance_to_earth)

    events = []
    for t in max_times:
        events.append({"date": t.utc_datetime(), "event": "Apogee", "object": "Moon"})
    for t in min_times:
        events.append({"date": t.utc_datetime(), "event": "Perigee", "object": "Moon"})

    return events

def find_lunar_occultations(observer, bright_stars, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = planetary.get_skyfield_obj("moon")
    earth = cast(Any, planetary.get_skyfield_obj("earth"))

    target_stars = [
        "Sirius",
        "Arcturus",
        "Rigel",
        "Procyon",
        "Betelgeuse",
        "Altair",
        "Aldebaran",
        "Antares",
        "Spica",
        "Pollux",
        "Fomalhaut",
        "Regulus",
        "Adhara",
        "Bellatrix",
        "El Nath",
        "Alnilam",
        "Alnitak",
        "Wezen",
        "Alhena",
        "Mirzam",
        "Alphard",
        "Hamal",
        "Beta Tauri",
    ]

    events = []

    stars_to_check = bright_stars[bright_stars["Name"].str.strip().isin(target_stars)]

    # Optimization: Pre-filter stars based on ecliptic latitude.
    # The Moon stays within ~5.3 degrees of the ecliptic.
    star_objs_all = stars_to_check["skyfield_object"].tolist()
    star_names_all = stars_to_check["Name"].tolist()

    # Observe all stars at once using a vectorized Star object
    # Optimization: use pre-calculated float columns instead of list comprehension over Star objects
    stars_vector = Star(
        ra_hours=stars_to_check["ra_hours"].to_numpy(),
        dec_degrees=stars_to_check["dec_degrees"].to_numpy(),
    )
    spos_at_t0_all = earth.at(t0).observe(stars_vector)
    lats, _, _ = spos_at_t0_all.ecliptic_latlon()

    # Filter using vectorized mask
    mask = np.abs(lats.degrees) < 10
    star_objects = [(star_names_all[i], star_objs_all[i]) for i in np.where(mask)[0]]

    # Check every 2 minutes for precision
    num_steps = int((t1 - t0) * 24 * 30)
    if num_steps < 2:
        return []
    times = ts.linspace(t0, t1, num_steps)

    # Coarse check every 20 minutes (1 in 10 points)
    coarse_idx = np.arange(0, num_steps, 10)
    coarse_times = times[coarse_idx]

    # Topocentric position for Moon (coarse)
    # Refraction is not critical here for the coarse filter
    mpos_coarse = observer.at(coarse_times).observe(moon).apparent()
    m_alt_coarse, _, m_dist_coarse = mpos_coarse.altaz()
    moon_rad_coarse = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_dist_coarse.km))

    # Unit vectors for Moon (coarse)
    m_au_coarse = mpos_coarse.position.au
    u_moon_coarse = m_au_coarse / np.linalg.norm(m_au_coarse, axis=0)

    for star_name, star_obj in star_objects:
        # Use ICRS position once (t0) for coarse filter - very fast.
        # This filters out stars far from the Moon's path.
        spos_star = earth.at(t0).observe(star_obj)
        u_star = spos_star.position.au / np.linalg.norm(spos_star.position.au)

        # Dot product for coarse separations
        dot_coarse = u_star @ u_moon_coarse
        sep_coarse = np.degrees(np.arccos(np.clip(dot_coarse, -1.0, 1.0)))

        # Potential occultation: coarse separation < angular radius + small margin (for parallax/aberration)
        # Moon parallax is up to ~1 deg, aberration is ~20 arcsec.
        # Using Topocentric Moon and ICRS Star at t0, so only need to cover Star motion (aberration/parallax).
        # Parallax for Stars is tiny (<1"), aberration ~20". Using 0.1 deg margin for safety.
        potential_mask = (sep_coarse < moon_rad_coarse + 0.1) & (
            m_alt_coarse.degrees > -1
        )

        if not potential_mask.any():
            continue

        # For potential candidates, perform high-precision check only near those windows
        # Expand windows to ensure we don't miss transitions
        window_indices = np.unique(
            np.concatenate(
                [
                    np.clip(coarse_idx[potential_mask] + offset, 0, num_steps - 1)
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

def find_lunar_features(observer, start_date, end_date):
    """
    Finds transient lunar features based on selenographic colongitude.
    - Lunar X and Lunar V: approx 358.0° (First Quarter).
    - Golden Handle: approx 15.0° (2 days after First Quarter).
    - Straight Wall (Sunrise): approx 11.0° (1 day after First Quarter).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    sun = planetary.get_skyfield_obj("sun")
    moon_sf = planetary.get_skyfield_obj("moon")

    # Features to track: (Name, Target Colongitude)
    # Target values represent the moment the feature becomes prominently visible
    # due to sunlight hitting its high points while the base is in shadow.
    features = [
        ("Lunar X", 358.0),
        ("Lunar V", 358.0),
        ("Golden Handle (Mountains of Jura)", 15.0),
        ("Straight Wall (Rupes Recta)", 11.0),
        ("Hesiodus Ray", 18.0),
    ]

    events = []

    # Check every 2.4 hours (10 steps per day) for coarse search
    num_steps = int((t1 - t0) * 10)
    if num_steps < 2:
        num_steps = 2

    times = ts.linspace(t0, t1, num_steps)

    # Precompute colongitudes for efficiency using the vectorized IAU 2015 model
    colongs = cast(np.ndarray, planetary.get_moon_colongitude(times))

    # Extract elevation from observer once
    observer_elevation = 0
    for vf in observer.vector_functions:
        if hasattr(vf, "latitude"):
            # latitude is usually not what I want here if I am looking for elevation
            pass
        if hasattr(vf, "elevation"):
            observer_elevation = vf.elevation.m
            break

    for name, target_colong in features:
        # Handle wrap-around
        diffs = cast(np.ndarray, (colongs - target_colong + 180) % 360 - 180)

        # Find zero crossings (rising edge corresponds to sunrise at that colongitude)
        crossings = np.where((diffs[:-1] < 0) & (diffs[1:] > 0))[0]

        for idx in crossings:
            # Refine crossing time using linear interpolation
            t_low = times[idx]
            t_high = times[idx + 1]
            d_low = diffs[idx]
            d_high = diffs[idx + 1]

            t_mid_jd = t_low.tt + (t_high.tt - t_low.tt) * (-d_low / (d_high - d_low))
            t_refined = ts.tt_jd(t_mid_jd)

            # Visibility check at refined time
            # Oracle: use refracted positions for topocentric visibility
            m_obs = observer.at(t_refined).observe(moon_sf).apparent()
            m_alt, _, _ = m_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

            # Lazy check for darkness only if Moon is visible
            def check_dark():
                s_alt = (
                    observer.at(t_refined)
                    .observe(sun)
                    .apparent()
                    .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                    .degrees
                )
                return s_alt <= -6

            # Special elevation -9999 bypasses topocentric checks for global indexing
            if observer_elevation == -9999 or (m_alt.degrees > 0 and check_dark()):
                events.append(
                    {
                        "date": t_refined.utc_datetime(),
                        "event": name,
                        "object": "Moon",
                        "type": "Lunar Feature",
                        "altitude": float(m_alt.degrees),
                        "colongitude": float(planetary.get_moon_colongitude(t_refined)),
                    }
                )

    return events
