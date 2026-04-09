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

    if not full_moons:
        return []

    # 2. Bulk search for all Apogees and Perigees in the padded range.
    # Padding by 16 days ensures we find the nearest events for every Full Moon.
    t_padded_start = ts.tt_jd(t0.tt - 16)
    t_padded_end = ts.tt_jd(t1.tt + 16)

    def distance_to_earth(t):
        return cast(Any, earth).at(t).observe(moon).distance().km

    # Optimization: perform global search once instead of iteratively per Full Moon.
    setattr(distance_to_earth, "step_days", 13.0)
    t_apogees, v_apogees = find_maxima(t_padded_start, t_padded_end, distance_to_earth)
    t_perigees, v_perigees = find_minima(t_padded_start, t_padded_end, distance_to_earth)

    if len(v_perigees) == 0 or len(v_apogees) == 0:
        return []

    # 3. Vectorized distance calculation for all Full Moons
    full_moons_t = ts.tt_jd(np.array([t.tt for t in full_moons]))
    current_distances = cast(Any, earth).at(full_moons_t).observe(moon).distance().km

    # 4. Use NumPy to find the nearest perigee and apogee for each Full Moon.
    events = []
    apogee_tt = np.array([t.tt for t in t_apogees])
    perigee_tt = np.array([t.tt for t in t_perigees])

    for i, t_full in enumerate(full_moons):
        idx_apogee = np.argmin(np.abs(apogee_tt - t_full.tt))
        idx_perigee = np.argmin(np.abs(perigee_tt - t_full.tt))

        perigee_dist = v_perigees[idx_perigee]
        apogee_dist = v_apogees[idx_apogee]
        current_dist = current_distances[i]

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
    # Optimization: pre-calculate distances for all extrema
    if len(max_times) > 0:
        max_dist = cast(Any, earth).at(max_times).observe(moon).distance().km
        for i, t in enumerate(max_times):
            events.append({
                "date": t.utc_datetime(),
                "event": "Apogee",
                "object": "Moon",
                "distance_km": float(max_dist[i])
            })
    if len(min_times) > 0:
        min_dist = cast(Any, earth).at(min_times).observe(moon).distance().km
        for i, t in enumerate(min_times):
            events.append({
                "date": t.utc_datetime(),
                "event": "Perigee",
                "object": "Moon",
                "distance_km": float(min_dist[i])
            })

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

def find_moon_libration_maxima(observer, start_date, end_date):
    """
    Finds local maxima in lunar libration (longitude and latitude).
    These are the best times to observe features near the Moon's limb.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    sun = planetary.get_skyfield_obj("sun")
    moon_sf = planetary.get_skyfield_obj("moon")

    def libration_lon(t):
        lon, _ = planetary.get_moon_libration(t)
        return lon

    def libration_lat(t):
        _, lat = planetary.get_moon_libration(t)
        return lat

    # Step of 2 days is safe for libration cycles (~27.3 days)
    setattr(libration_lon, "step_days", 2.0)
    setattr(libration_lat, "step_days", 2.0)

    # We want both extreme positive and negative values (East/West, North/South)
    lon_max_times, lon_max_vals = find_maxima(t0, t1, libration_lon)
    lon_min_times, lon_min_vals = find_minima(t0, t1, libration_lon)
    lat_max_times, lat_max_vals = find_maxima(t0, t1, libration_lat)
    lat_min_times, lat_min_vals = find_minima(t0, t1, libration_lat)

    events = []

    # Helper to calculate visibility and build event dict
    def add_lib_event(t, val, axis, extreme):
        # Oracle: use refracted positions for visibility check
        m_obs = observer.at(t).observe(moon_sf).apparent()
        m_alt, _, _ = m_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

        s_alt = (
            observer.at(t)
            .observe(sun)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )

        # Observer elevation for global indexing
        observer_elevation = 0
        for vf in observer.vector_functions:
            if hasattr(vf, "elevation"):
                observer_elevation = vf.elevation.m
                break

        is_visible = (m_alt.degrees > 0 and s_alt <= -6) or observer_elevation == -9999

        side = {
            ("longitude", "max"): "East",
            ("longitude", "min"): "West",
            ("latitude", "max"): "North",
            ("latitude", "min"): "South",
        }[(axis, extreme)]

        events.append(
            {
                "date": t.utc_datetime(),
                "event": f"Maximum Lunar Libration ({side})",
                "object": "Moon",
                "type": "Moon Libration Maximum",
                "libration_value": float(val),
                "axis": axis,
                "side": side,
                "altitude": float(m_alt.degrees),
                "is_visible": bool(is_visible),
            }
        )

    from typing import Any, Iterable, cast
    for t, v in zip(cast(Iterable[Any], lon_max_times), lon_max_vals):
        add_lib_event(t, v, "longitude", "max")
    for t, v in zip(cast(Iterable[Any], lon_min_times), lon_min_vals):
        add_lib_event(t, v, "longitude", "min")
    for t, v in zip(cast(Iterable[Any], lat_max_times), lat_max_vals):
        add_lib_event(t, v, "latitude", "max")
    for t, v in zip(cast(Iterable[Any], lat_min_times), lat_min_vals):
        add_lib_event(t, v, "latitude", "min")

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
        # Hesiodus Ray: sunrise ray in crater Hesiodus. Colongitude ~18.0.
        # Source: Sky & Telescope July 1996; ALPO Lunar Tool Kit.
        ("Hesiodus Ray", 18.0),
        # Curtiss Cross: "X" pattern near crater Fra Mauro. Colongitude ~193.8.
        # Source: Jim Mosher; Sky & Telescope (originally reported by Curtiss).
        ("Curtiss Cross", 193.8),
        ("Golden Handle (Mountains of Jura)", 15.0),
        ("Straight Wall (Rupes Recta)", 11.0),
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
