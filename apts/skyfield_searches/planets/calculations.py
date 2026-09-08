from collections import defaultdict
from typing import Any, Optional

import numpy as np

from ...utils import planetary

# Thresholds for different numbers of planets (number: arc_degrees)
PLANET_ALIGNMENT_THRESHOLDS = {
    3: 15,
    4: 30,
    5: 60,
    6: 160,
    7: 150,
}


def get_best_alignment_at_time(
    lons_at_t: np.ndarray,
    thresholds: Optional[dict[int, float]] = None,
) -> tuple[int, float, list[int]]:
    """
    Identifies the largest and tightest planetary alignment for a given set of longitudes.
    """
    if thresholds is None:
        thresholds = PLANET_ALIGNMENT_THRESHOLDS

    sorted_indices = np.argsort(lons_at_t)
    sorted_lons = lons_at_t[sorted_indices]
    n = len(sorted_lons)
    lons_extended = np.concatenate([sorted_lons, sorted_lons + 360])

    best_k = 0
    best_arc = 360.0
    best_indices: list[int] = []

    for k in range(3, n + 1):
        min_arc_k = 360.0
        min_indices_k: list[int] = []
        for i in range(n):
            arc = float(lons_extended[i + k - 1] - lons_extended[i])
            if arc < min_arc_k:
                min_arc_k = arc
                # Indices of planets in the arc
                min_indices_k = [int(sorted_indices[j % n]) for j in range(i, i + k)]

        if min_arc_k < thresholds.get(k, 360.0):
            best_k = k
            best_arc = min_arc_k
            best_indices = min_indices_k

    return best_k, best_arc, best_indices


def calculate_alignment_step_results(
    times: Any,
    longitudes: np.ndarray,
    altitudes: np.ndarray,
    is_dark: np.ndarray,
    thresholds: Optional[dict[int, float]] = None,
) -> list[dict[str, Any]]:
    """
    Calculates alignment and visibility stats for each time step.
    """
    step_results = []
    for i in range(len(times)):
        k, arc, indices = get_best_alignment_at_time(
            longitudes[:, i], thresholds=thresholds
        )

        # Count visible planets among those in the alignment
        visible_in_alignment = 0
        visible_indices = []
        if k >= 3:
            for idx in indices:
                if altitudes[idx, i] > 0 and is_dark[i]:
                    visible_in_alignment += 1
                    visible_indices.append(idx)

        step_results.append(
            {
                "k": k,
                "arc": arc,
                "indices": indices,
                "num_visible": visible_in_alignment,
                "visible_indices": visible_indices,
            }
        )
    return step_results


def aggregate_alignment_daily_results(
    times: Any,
    step_results: list[dict[str, Any]],
) -> list[tuple[Any, dict[str, Any]]]:
    """
    Aggregates hourly results to find the best representative alignment for each day.
    Best means: max num_visible, then max k, then min arc.
    Visibility is prioritized to ensure we report events when they are best seen.
    """
    by_day = defaultdict(list)
    for i, res in enumerate(step_results):
        day = times[i].utc_datetime().date()
        by_day[day].append((times[i], res))

    daily_results = []
    sorted_days = sorted(by_day.keys())
    for day in sorted_days:
        day_steps = by_day[day]
        best_step = max(
            day_steps, key=lambda x: (x[1]["num_visible"], x[1]["k"], -x[1]["arc"])
        )
        daily_results.append(best_step)
    return daily_results


def format_alignment_events(
    daily_results: list[tuple[Any, dict[str, Any]]],
    planets: list[str],
) -> list[dict[str, Any]]:
    """
    Identifies alignment windows from daily results and formats them into events.
    """
    events = []
    i = 0
    while i < len(daily_results):
        # We consider a day "aligned" if it has k>=3 AND is observationally
        # significant (num_visible >= 3).
        res = daily_results[i][1]
        if res["k"] >= 3 and res["num_visible"] >= 3:
            # Start of an alignment period
            start_i = i
            while i < len(daily_results):
                r = daily_results[i][1]
                if not (r["k"] >= 3 and r["num_visible"] >= 3):
                    break
                i += 1
            end_i = i

            # Find the best representative day in the window
            window = daily_results[start_i:end_i]
            best_day_tuple = max(
                window, key=lambda x: (x[1]["num_visible"], x[1]["k"], -x[1]["arc"])
            )

            t_best, res_best = best_day_tuple
            k = res_best["k"]
            arc = res_best["arc"]
            indices = res_best["indices"]
            num_visible = res_best["num_visible"]
            visible_indices = res_best["visible_indices"]

            aligned_planets = [
                planetary.get_simple_name(planets[idx]) for idx in indices
            ]
            visible_names = [
                planetary.get_simple_name(planets[idx]) for idx in visible_indices
            ]

            event_label = f"Alignment of {k} planets ({num_visible} visible)"

            events.append(
                {
                    "date": t_best.utc_datetime(),
                    "event": event_label,
                    "planets": aligned_planets,
                    "visible_planets": visible_names,
                    "arc_degrees": arc,
                    "num_visible": num_visible,
                }
            )
        else:
            i += 1
    return events


# Aliases for backward compatibility
_PLANET_ALIGNMENT_THRESHOLDS = PLANET_ALIGNMENT_THRESHOLDS
_get_best_alignment_at_time = get_best_alignment_at_time
_calculate_step_results = calculate_alignment_step_results
_aggregate_to_daily_results = aggregate_alignment_daily_results
_format_alignment_events = format_alignment_events
