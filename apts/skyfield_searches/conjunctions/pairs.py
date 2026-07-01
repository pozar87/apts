import numpy as np

from ...cache import get_timescale
from ...utils import planetary
from ..utils import _refine_conjunction


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
