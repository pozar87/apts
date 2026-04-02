from typing import Any, cast
import numpy as np
from skyfield.api import Star
from skyfield.searchlib import find_minima
from ..cache import get_timescale, get_ephemeris
from ..constants import astronomy
from ..utils import planetary
from .utils import _refine_conjunction

def find_planet_star_conjunctions(
    observer,
    start_date,
    end_date,
    threshold_degrees=2.0,
    precomputed_positions=None,
):
    """
    Finds conjunctions between major planets and bright stars.
    Vectorized over stars for each planet for high performance.
    """
    from ..catalogs import Catalogs

    catalogs = Catalogs()
    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]

    # Filter stars close to the ecliptic (within 10 degrees)
    # The planets stay close to the ecliptic (mostly within 7 degrees)
    ts = get_timescale()
    t_ref = ts.utc(start_date)

    star_objs_all = catalogs.BRIGHT_STARS["skyfield_object"].tolist()
    star_names_all = catalogs.BRIGHT_STARS["Name"].tolist()

    stars_vector = Star(
        ra_hours=np.array([s.ra.hours for s in star_objs_all]),
        dec_degrees=np.array([s.dec.degrees for s in star_objs_all]),
    )
    spos_at_t_ref = observer.at(t_ref).observe(stars_vector)
    lats, _, _ = spos_at_t_ref.ecliptic_latlon()

    # Planets stay within ~7 degrees of the ecliptic (except Pluto, which is not in this list)
    mask = np.abs(lats.degrees) < 7.0
    star_data = [(star_names_all[i], star_objs_all[i]) for i in np.where(mask)[0]]

    events = []
    for p_name in planets:
        simple_name = planetary.get_simple_name(p_name)
        conjunctions = find_conjunctions_with_stars(
            observer,
            p_name,
            star_data,
            start_date,
            end_date,
            threshold_degrees=threshold_degrees,
            precomputed_positions=precomputed_positions,
        )
        for conj in conjunctions:
            events.append(
                {
                    "date": conj["date"],
                    "event": "Conjunction",
                    "object1": simple_name,
                    "object2": conj["object2"],
                    "separation_degrees": conj["separation_degrees"],
                    "type": "Planet-Star Conjunction",
                }
            )

    return events

def find_lunar_planetary_occultations(observer, start_date, end_date):
    """
    Finds occultations of planets by the Moon for a specific observer.
    Provides precise ingress and egress times.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = planetary.get_skyfield_obj("moon")

    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]
    events = []

    sun = planetary.get_skyfield_obj("sun")

    for p_name in planets:
        planet = planetary.get_skyfield_obj(p_name)
        simple_name = planetary.get_simple_name(p_name)

        def is_occulted(t):
            m = observer.at(t).observe(moon).apparent()
            p = observer.at(t).observe(planet).apparent()
            sep = m.separation_from(p).degrees
            rad = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m.distance().km))
            alt, _, _ = m.altaz(temperature_C=10.0, pressure_mbar=1013.25)
            sun_alt = (
                observer.at(t)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )
            return (sep < rad) & (alt.degrees > 0) & (sun_alt <= -6)

        from skyfield import almanac
        setattr(is_occulted, "step_days", 0.005)
        t_occ, y_occ = almanac.find_discrete(t0, t1, is_occulted)

        # Handle cases where the occultation starts before t0 or ends after t1
        t_list = list(t_occ)
        if is_occulted(t0):
            t_list.insert(0, t0)

        if len(t_list) % 2 != 0:
            t_list.append(t1)

        for i in range(0, len(t_list), 2):
            if i + 1 < len(t_list):
                ingress_t = t_list[i]
                egress_t = t_list[i + 1]
                # Mid-point for conjunction refinement if needed
                from datetime import timedelta
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

def find_planet_messier_conjunctions(
    observer, start_date, end_date, precomputed_positions=None
):
    """Finds conjunctions between major planets and Messier objects."""
    from ..catalogs import Catalogs

    catalogs = Catalogs()
    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]
    # Optimization: replace iterrows() with zip() for better performance
    messier_data = list(
        zip(catalogs.MESSIER["Messier"], catalogs.MESSIER["skyfield_object"])
    )

    events = []
    for p_name in planets:
        simple_name = planetary.get_simple_name(p_name)
        # 3.0 degrees threshold for planet-DSO conjunctions
        conjunctions = find_conjunctions_with_stars(
            observer,
            p_name,
            messier_data,
            start_date,
            end_date,
            threshold_degrees=3.0,
            precomputed_positions=precomputed_positions,
        )
        for conj in conjunctions:
            events.append(
                {
                    "date": conj["date"],
                    "event": "Conjunction",
                    "object1": simple_name,
                    "object2": conj["object2"],
                    "separation_degrees": conj["separation_degrees"],
                    "type": "Planet-Messier Conjunction",
                }
            )
    return events

def find_conjunctions(
    observer,
    p1_name,
    p2_name,
    start_date,
    end_date,
    threshold_degrees=None,
):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    p1 = planetary.get_skyfield_obj(p1_name)
    p2 = planetary.get_skyfield_obj(p2_name)

    def separation(t):
        # Use topocentric apparent positions to account for aberration and light deflection
        p1_obs = observer.at(t).observe(p1).apparent()
        p2_obs = observer.at(t).observe(p2).apparent()
        return p1_obs.separation_from(p2_obs).degrees

    # Dynamically adjust step size based on moving bodies
    # Moon moves ~13 deg/day, Mercury ~1.3 deg/day
    if "moon" in [p1_name.lower(), p2_name.lower()]:
        step = 0.05  # ~1.2 hours
    elif any(p in [p1_name.lower(), p2_name.lower()] for p in ["mercury", "venus"]):
        step = 0.2  # ~4.8 hours
    else:
        step = 0.5  # ~12 hours

    setattr(separation, "step_days", step)

    times, separations = find_minima(t0, t1, separation)

    events = []
    for t, s in zip(times, separations):
        if threshold_degrees is None or s < threshold_degrees:
            # Refine conjunction time and separation
            refined_t, refined_s = _refine_conjunction(observer, p1, p2, t)
            events.append(
                {
                    "date": refined_t.utc_datetime(),
                    "separation_degrees": float(refined_s),
                }
            )

    return events

def find_mercury_inferior_conjunctions(
    observer, start_date, end_date, threshold_degrees=1.0
):
    conjunctions = find_conjunctions(
        observer, "mercury", "sun", start_date, end_date, threshold_degrees
    )

    mercury = planetary.get_skyfield_obj("mercury")
    sun = planetary.get_skyfield_obj("sun")
    ts = get_timescale()

    inferior_events = []
    for event in conjunctions:
        t = ts.from_datetime(event["date"])
        mercury_obs = observer.at(t).observe(mercury)
        sun_obs = observer.at(t).observe(sun)

        mercury_dist = mercury_obs.distance().au
        sun_dist = sun_obs.distance().au

        if mercury_dist < sun_dist:
            # It is an inferior conjunction
            # Calculate angular radii
            mercury_angular_radius = np.degrees(
                np.arctan2(astronomy.MERCURY_RADIUS_KM / astronomy.AU_KM, mercury_dist)
            )
            sun_angular_radius = np.degrees(
                np.arctan2(astronomy.SUN_RADIUS_KM / astronomy.AU_KM, sun_dist)
            )

            event["is_transit"] = event["separation_degrees"] < (
                mercury_angular_radius + sun_angular_radius
            )
            inferior_events.append(event)

    return inferior_events

def find_conjunctions_with_star(
    observer,
    body1_name,
    star_object,
    start_date,
    end_date,
    threshold_degrees=1.0,
):
    """
    Finds conjunctions between a moving body and a fixed star.
    Wrapper around find_conjunctions_with_stars for single star case.
    """
    events = find_conjunctions_with_stars(
        observer,
        body1_name,
        [("Target", star_object)],
        start_date,
        end_date,
        threshold_degrees,
    )

    # Remove the object2 key for backward compatibility
    for event in events:
        if "object2" in event:
            del event["object2"]

    return events

def find_conjunctions_with_stars(
    observer,
    body_name,
    star_data,  # List of (name, Star object)
    start_date,
    end_date,
    threshold_degrees=1.0,
    precomputed_positions=None,
):
    """
    Finds conjunctions between a moving body and multiple fixed stars.
    Vectorized over both time and stars for maximum performance.
    """
    if not star_data:
        return []

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    # Determine the time grid to use.
    # If precomputed positions are provided, we use their time array to ensure
    # array compatibility and maximize reuse of pre-calculated data.
    if precomputed_positions:
        # Get the time array from the first available position object
        first_pos = next(iter(precomputed_positions.values()))
        times = first_pos.t
    else:
        # Hourly check
        num_hours = int((t1 - t0) * 24)
        if num_hours < 2:
            return []
        times = ts.linspace(t0, t1, num_hours)

    # Always get the body object as it is used for refinement later
    body = planetary.get_skyfield_obj(body_name)

    # Use precomputed positions if available, otherwise observe
    if precomputed_positions and body_name.lower() in precomputed_positions:
        pos_body_all = precomputed_positions[body_name.lower()]
        # Verify length matches
        if (
            hasattr(pos_body_all, "t")
            and hasattr(pos_body_all.t, "shape")
            and len(pos_body_all.t.shape) > 0
            and pos_body_all.t.shape[0] == len(times)
        ):
            pos_body = pos_body_all
        else:
            pos_body = observer.at(times).observe(body).apparent()
    else:
        pos_body = observer.at(times).observe(body).apparent()

    # Unit vectors for body at all times: (3, M)
    body_au = pos_body.position.au
    u_body = body_au / np.linalg.norm(body_au, axis=0)

    # Prepare vectorized Star objects
    star_names = [name for name, _ in star_data]
    star_objs = [obj for _, obj in star_data]

    # To maximize performance, we observe all stars once in ICRF (at the midpoint of the search)
    # and treat them as fixed unit vectors. This eliminates the O(N) loop of
    # expensive coordinate transformations.
    # Accuracy loss is sub-arcminute (mainly due to aberration), which is perfectly
    # acceptable for identifying conjunction candidates.
    t_mid = times[len(times) // 2]
    stars_vector = Star(
        ra_hours=np.array([s.ra.hours for s in star_objs]),
        dec_degrees=np.array([s.dec.degrees for s in star_objs]),
    )
    # Observe all stars at once in ICRF
    pos_stars = observer.at(t_mid).observe(stars_vector)
    # Unit vectors for stars: (3, N)
    stars_au = pos_stars.position.au
    u_stars = stars_au / np.linalg.norm(stars_au, axis=0)

    # Matrix multiplication: (N, 3) @ (3, M) -> (N, M)
    # This provides a ~5x speedup for typical catalog sizes by replacing the O(N) loop
    # of individual observations with a single vectorized operation.
    dot_products = u_stars.T @ u_body

    # Angular separation in degrees: acos(dot_product)
    # Using clip to avoid NaNs due to floating point precision
    separations = np.degrees(np.arccos(np.clip(dot_products, -1.0, 1.0)))

    # Identify local minima where separation is below threshold (vectorized)
    is_minima = (separations[:, 1:-1] < separations[:, :-2]) & (
        separations[:, 1:-1] < separations[:, 2:]
    )
    is_below_threshold = separations[:, 1:-1] < threshold_degrees

    # Find star and time indices for all conjunction candidates
    star_idxs, time_idxs_minus_1 = np.where(is_minima & is_below_threshold)
    time_idxs = time_idxs_minus_1 + 1

    events = []
    for star_idx, time_idx in zip(star_idxs, time_idxs):
        # Refine conjunction time and separation
        # Refinement is still iterative as it requires high-precision topocentric observation
        # but is only performed for the final candidates.
        refined_t, refined_s = _refine_conjunction(
            observer, body, star_objs[star_idx], times[time_idx]
        )
        events.append(
            {
                "date": refined_t.utc_datetime(),
                "object2": star_names[star_idx],
                "separation_degrees": float(refined_s),
            }
        )

    return events

def find_conjunctions_between_moving_bodies(
    observer,
    body1_name,
    bodies2_data,  # List of (name, Skyfield object)
    start_date,
    end_date,
    threshold_degrees=1.0,
    precomputed_positions=None,
):
    """
    Finds conjunctions between a moving body and multiple other moving bodies.
    Vectorized over time for each pair.
    """
    if not bodies2_data:
        return []

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    # Dynamically adjust step size based on moving bodies
    # Using 15-minute resolution for the Moon for better conjunction accuracy
    if "moon" == body1_name.lower() or any(
        "moon" == name.lower() for name, _ in bodies2_data
    ):
        step = 0.01  # ~14.4 minutes
    elif "mercury" == body1_name.lower() or any(
        "mercury" == name.lower() for name, _ in bodies2_data
    ):
        step = 0.1  # ~2.4 hours
    else:
        step = 0.2  # ~4.8 hours

    # Determine the time grid to use.
    if precomputed_positions:
        # Get the time array from the first available position object
        first_pos = next(iter(precomputed_positions.values()))
        times = first_pos.t
    else:
        num_steps = int((t1 - t0) / step)
        if num_steps < 2:
            num_steps = 2
        times = ts.linspace(t0, t1, num_steps)

    # Use precomputed positions if available, otherwise observe
    if precomputed_positions and body1_name.lower() in precomputed_positions:
        # Check if length matches. Skyfield's Astrometric results store
        # their timestamps in '.t', which is a Time object with a .shape.
        pos1_all = precomputed_positions[body1_name.lower()]
        # Verify both 't' attribute and that the length of the vectorized time array matches
        if (
            hasattr(pos1_all, "t")
            and hasattr(pos1_all.t, "shape")
            and len(pos1_all.t.shape) > 0
            and pos1_all.t.shape[0] == len(times)
        ):
            pos1 = pos1_all
        else:
            body1 = planetary.get_skyfield_obj(body1_name)
            pos1 = observer.at(times).observe(body1)
    else:
        body1 = planetary.get_skyfield_obj(body1_name)
        pos1 = observer.at(times).observe(body1)

    events = []
    for name2, body2 in bodies2_data:
        if precomputed_positions and name2.lower() in precomputed_positions:
            pos2_all = precomputed_positions[name2.lower()]
            if (
                hasattr(pos2_all, "t")
                and hasattr(pos2_all.t, "shape")
                and len(pos2_all.t.shape) > 0
                and pos2_all.t.shape[0] == len(times)
            ):
                pos2 = pos2_all
            else:
                pos2 = observer.at(times).observe(body2)
        else:
            pos2 = observer.at(times).observe(body2)

        separations = pos1.separation_from(pos2).degrees

        # Identify local minima where separation is below threshold
        is_minima = (separations[1:-1] < separations[:-2]) & (
            separations[1:-1] < separations[2:]
        )
        is_below_threshold = separations[1:-1] < threshold_degrees

        minima_indices = np.where(is_minima & is_below_threshold)[0] + 1

        for idx in minima_indices:
            # Refine conjunction time and separation
            # If precomputed positions are used, we still refine using the actual objects
            # to ensure maximum precision.
            body1 = planetary.get_skyfield_obj(body1_name)
            refined_t, refined_s = _refine_conjunction(
                observer, body1, body2, times[idx]
            )
            events.append(
                {
                    "date": refined_t.utc_datetime(),
                    "object2": name2,
                    "separation_degrees": float(refined_s),
                }
            )

    return events

def find_planet_solar_conjunctions(observer, start_date, end_date, threshold_degrees=2.0):
    """
    Finds conjunctions between planets and the Sun.
    Distinguishes between inferior and superior conjunctions for inner planets.
    """
    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]

    conjunctions = []
    for p_name in planets:
        planet_conjs = find_conjunctions(
            observer, p_name, "sun", start_date, end_date, threshold_degrees
        )
        simple_name = planetary.get_simple_name(p_name)

        for conj in planet_conjs:
            t = get_timescale().from_datetime(conj["date"])
            p_obj = planetary.get_skyfield_obj(p_name)
            sun_obj = planetary.get_skyfield_obj("sun")

            # Get distances to determine conjunction type
            p_dist = observer.at(t).observe(p_obj).distance().au
            sun_dist = observer.at(t).observe(sun_obj).distance().au

            if p_name in ["mercury", "venus"]:
                if p_dist < sun_dist:
                    kind = "Inferior Conjunction"
                else:
                    kind = "Superior Conjunction"
            else:
                kind = "Conjunction"

            conj.update(
                {
                    "event": f"{simple_name} Solar {kind}",
                    "object1": simple_name,
                    "object2": "Sun",
                    "type": "Planet Solar Conjunction",
                    "conjunction_kind": kind,
                }
            )
            conjunctions.append(conj)

    return conjunctions

def find_planet_planet_occultations(observer, start_date, end_date):
    """
    Finds occultations of one planet by another.
    Extremely rare events.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]

    events = []
    # Check all pairs of planets
    for i, p1_name in enumerate(planets):
        for p2_name in planets[i + 1 :]:
            p1_obj = planetary.get_skyfield_obj(p1_name)
            p2_obj = planetary.get_skyfield_obj(p2_name)

            def separation(t):
                # Use topocentric apparent positions
                # Optimization: for coarse search, we could use .observe()
                p1_obs = observer.at(t).observe(p1_obj).apparent()
                p2_obs = observer.at(t).observe(p2_obj).apparent()
                sep = p1_obs.separation_from(p2_obs).degrees

                # Calculate angular radii
                r1 = np.degrees(
                    np.arcsin(
                        planetary.get_planet_radius_km(p1_name) / p1_obs.distance().km
                    )
                )
                r2 = np.degrees(
                    np.arcsin(
                        planetary.get_planet_radius_km(p2_name) / p2_obs.distance().km
                    )
                )

                return sep - (r1 + r2)

            # Step of 0.5 days is safe for these slow events
            setattr(separation, "step_days", 0.5)
            times, _ = find_minima(t0, t1, separation)

            for t in times:
                # Refine
                refined_t, refined_sep = _refine_conjunction(observer, p1_obj, p2_obj, t)

                p1_obs = observer.at(refined_t).observe(p1_obj).apparent()
                p2_obs = observer.at(refined_t).observe(p2_obj).apparent()

                r1 = np.degrees(
                    np.arcsin(
                        planetary.get_planet_radius_km(p1_name) / p1_obs.distance().km
                    )
                )
                r2 = np.degrees(
                    np.arcsin(
                        planetary.get_planet_radius_km(p2_name) / p2_obs.distance().km
                    )
                )

                if refined_sep < (r1 + r2):
                    # Determine which planet is in front
                    if p1_obs.distance().km < p2_obs.distance().km:
                        occulting = planetary.get_simple_name(p1_name)
                        occulted = planetary.get_simple_name(p2_name)
                    else:
                        occulting = planetary.get_simple_name(p2_name)
                        occulted = planetary.get_simple_name(p1_name)

                    events.append(
                        {
                            "date": refined_t.utc_datetime(),
                            "event": f"{occulting} occults {occulted}",
                            "object1": occulting,
                            "object2": occulted,
                            "separation_degrees": float(refined_sep),
                            "type": "Planet-Planet Occultation",
                        }
                    )
    return events
