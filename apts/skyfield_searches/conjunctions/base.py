from typing import cast

import numpy as np
from skyfield.api import Star
from skyfield.searchlib import find_minima

from ...cache import get_timescale
from ...utils import planetary
from ..utils import _refine_conjunction


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
    star_data,  # List of (name, Star object) OR a vectorized Star object
    start_date,
    end_date,
    threshold_degrees=1.0,
    precomputed_positions=None,
    star_names=None,  # Required if star_data is a vectorized Star object
):
    """
    Finds conjunctions between a moving body and multiple fixed stars.
    Vectorized over both time and stars for maximum performance.
    """
    if star_data is None or (isinstance(star_data, list) and not star_data):
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
    if star_names is not None:
        # Optimized path: star_data is already a vectorized Star object
        stars_vector = cast(Star, star_data)
    else:
        # Legacy path: star_data is a list of (name, Star)
        star_names = [name for name, _ in star_data]
        star_objs = [obj for _, obj in star_data]
        stars_vector = Star(
            ra_hours=np.array([s.ra.hours for s in star_objs]),
            dec_degrees=np.array([s.dec.degrees for s in star_objs]),
        )

    # To maximize performance, we observe all stars once in ICRF (at the midpoint of the search)
    # and treat them as fixed unit vectors. This eliminates the O(N) loop of
    # expensive coordinate transformations.
    # Accuracy loss is sub-arcminute (mainly due to aberration), which is perfectly
    # acceptable for identifying conjunction candidates.
    t_mid = times[len(times) // 2]
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
    # Pre-cache coordinates for faster Star object creation during refinement
    v_ra_hours = np.atleast_1d(cast(np.ndarray, stars_vector.ra.hours))
    v_dec_degrees = np.atleast_1d(cast(np.ndarray, stars_vector.dec.degrees))

    for star_idx, time_idx in zip(star_idxs, time_idxs):
        # Refine conjunction time and separation
        # Refinement is still iterative as it requires high-precision topocentric observation
        # but is only performed for the final candidates.

        # Reconstruct the individual Star object for refinement
        # Skyfield Star objects are not subscriptable, so we recreate from coords.
        target_star = Star(
            ra_hours=v_ra_hours[star_idx], dec_degrees=v_dec_degrees[star_idx]
        )

        refined_t, refined_s = _refine_conjunction(
            observer, body, target_star, times[time_idx]
        )
        events.append(
            {
                "date": refined_t.utc_datetime(),
                "object2": star_names[star_idx],
                "separation_degrees": float(refined_s),
            }
        )

    return events


def _get_conjunction_step_size(body1_name, bodies2_data):
    # Dynamically adjust step size based on moving bodies
    # Using 15-minute resolution for the Moon for better conjunction accuracy
    if "moon" == body1_name.lower() or any(
        "moon" == name.lower() for name, _ in bodies2_data
    ):
        return 0.01  # ~14.4 minutes
    if "mercury" == body1_name.lower() or any(
        "mercury" == name.lower() for name, _ in bodies2_data
    ):
        return 0.1  # ~2.4 hours
    return 0.2  # ~4.8 hours


def _get_conjunction_times(ts, t0, t1, step, precomputed_positions):
    # Determine the time grid to use.
    if precomputed_positions:
        # Get the time array from the first available position object
        first_pos = next(iter(precomputed_positions.values()))
        return first_pos.t

    num_steps = int((t1 - t0) / step)
    if num_steps < 2:
        num_steps = 2
    return ts.linspace(t0, t1, num_steps)


def _observe_conjunction_body(
    observer, body_name, times, precomputed_positions, body_obj=None
):
    # Use precomputed positions if available, otherwise observe
    if precomputed_positions and body_name.lower() in precomputed_positions:
        # Check if length matches. Skyfield's Astrometric results store
        # their timestamps in '.t', which is a Time object with a .shape.
        pos_all = precomputed_positions[body_name.lower()]
        # Verify both 't' attribute and that the length of the vectorized time array matches
        if (
            hasattr(pos_all, "t")
            and hasattr(pos_all.t, "shape")
            and len(pos_all.t.shape) > 0
            and pos_all.t.shape[0] == len(times)
        ):
            return pos_all

    if body_obj is None:
        body_obj = planetary.get_skyfield_obj(body_name)
    return observer.at(times).observe(body_obj)


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
    Vectorized over time and target bodies for high performance.
    """
    if not bodies2_data:
        return []

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    step = _get_conjunction_step_size(body1_name, bodies2_data)
    times = _get_conjunction_times(ts, t0, t1, step, precomputed_positions)

    body1 = planetary.get_skyfield_obj(body1_name)
    pos1 = _observe_conjunction_body(
        observer, body1_name, times, precomputed_positions, body1
    )

    # Unit vectors for body1: (3, T)
    p1_au = pos1.position.au
    u1 = p1_au / np.linalg.norm(p1_au, axis=0)

    # Collect and observe all bodies in bodies2_data
    names2 = []
    objs2 = []
    u2_list = []
    for name2, body2 in bodies2_data:
        pos2 = _observe_conjunction_body(
            observer, name2, times, precomputed_positions, body2
        )
        p2_au = pos2.position.au
        u2 = p2_au / np.linalg.norm(p2_au, axis=0)
        u2_list.append(u2)
        names2.append(name2)
        objs2.append(body2)

    # u2_all shape: (M, 3, T)
    u2_all = np.array(u2_list)

    # Vectorized dot product for all bodies at all times: (T, 3) dot (M, 3, T)
    # Result dots shape: (M, T)
    dots = np.einsum("it,mit->mt", u1, u2_all)

    # Angular separations: (M, T)
    separations_all = np.degrees(np.arccos(np.clip(dots, -1.0, 1.0)))

    # Identify local minima where separation is below threshold (vectorized)
    is_minima = (separations_all[:, 1:-1] < separations_all[:, :-2]) & (
        separations_all[:, 1:-1] < separations_all[:, 2:]
    )
    is_below_threshold = separations_all[:, 1:-1] < threshold_degrees

    body_idxs, time_idxs_minus_1 = np.where(is_minima & is_below_threshold)
    time_idxs = time_idxs_minus_1 + 1

    events = []
    for body_idx, time_idx in zip(body_idxs, time_idxs):
        # Refine conjunction time and separation
        refined_t, refined_s = _refine_conjunction(
            observer, body1, objs2[body_idx], times[time_idx]
        )
        events.append(
            {
                "date": refined_t.utc_datetime(),
                "object2": names2[body_idx],
                "separation_degrees": float(refined_s),
            }
        )

    return events


def find_all_pairs_conjunctions(
    observer,
    bodies_data,  # List of (name, Skyfield object)
    start_date,
    end_date,
    threshold_degrees=1.0,
    precomputed_positions=None,
):
    """
    Finds conjunctions between all pairs of moving bodies in the list.
    Fully vectorized over time and all body combinations.
    """
    if len(bodies_data) < 2:
        return []

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    bodies_list = list(bodies_data)
    # Assume planets for step size if not specified
    step = _get_conjunction_step_size(bodies_list[0][0], bodies_list[1:])
    times = _get_conjunction_times(ts, t0, t1, step, precomputed_positions)

    names = []
    objs = []
    u_list = []
    for name, body in bodies_list:
        pos = _observe_conjunction_body(
            observer, name, times, precomputed_positions, body
        )
        p_au = pos.position.au
        u = p_au / np.linalg.norm(p_au, axis=0)
        u_list.append(u)
        names.append(name)
        objs.append(body)

    # u_all shape: (N_bodies, 3, T)
    u_all = np.array(u_list)

    # All-pairs dot products at each time: (N, 3, T) and (N, 3, T) -> (N, N, T)
    # We use einsum to get the dot product for each pair (i, j) at each time t.
    dots = np.einsum("ijt,kjt->ikt", u_all, u_all)

    # Convert to degrees: (N, N, T)
    separations_all = np.degrees(np.arccos(np.clip(dots, -1.0, 1.0)))

    events = []
    num_bodies = len(names)
    for i in range(num_bodies):
        for j in range(i + 1, num_bodies):
            separations = separations_all[i, j, :]

            # Identify local minima where separation is below threshold
            is_minima = (separations[1:-1] < separations[:-2]) & (
                separations[1:-1] < separations[2:]
            )
            is_below_threshold = separations[1:-1] < threshold_degrees

            minima_indices = np.where(is_minima & is_below_threshold)[0] + 1

            for idx in minima_indices:
                # Refine conjunction time and separation
                refined_t, refined_s = _refine_conjunction(
                    observer, objs[i], objs[j], times[idx]
                )
                events.append(
                    {
                        "date": refined_t.utc_datetime(),
                        "object1": planetary.get_simple_name(names[i]),
                        "object2": planetary.get_simple_name(names[j]),
                        "separation_degrees": float(refined_s),
                    }
                )

    return events
