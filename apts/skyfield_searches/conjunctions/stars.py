from typing import cast

import numpy as np
from skyfield.api import Star

from ...cache import get_timescale
from ...utils import planetary
from ..utils import _refine_conjunction


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
