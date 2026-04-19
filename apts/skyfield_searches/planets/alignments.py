from typing import Any, cast
import numpy as np

from ...cache import get_timescale, get_ephemeris
from ...utils import planetary


def find_planet_alignments(observer, start_date, end_date):
    """
    Finds planetary alignments (multiple planets close together in ecliptic longitude).
    Takes into account visibility from the observer's location to highlight "planet parades".
    """
    from datetime import timedelta

    ts = get_timescale()
    t_start = ts.utc(start_date)
    t_end = ts.utc(end_date)

    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]
    planet_objs = [(p, planetary.get_skyfield_obj(p)) for p in planets]
    eph = get_ephemeris()
    earth = eph["earth"]
    sun = planetary.get_skyfield_obj("sun")

    # Thresholds for different numbers of planets
    thresholds = {
        3: 10,
        4: 25,
        5: 45,
        6: 90,
        7: 150,
    }

    # Use 1-hour steps to find best visibility and alignment
    duration_days = float(t_end - t_start)
    if duration_days <= 0:
        return []

    num_steps = int(duration_days * 24) + 1
    t_list = [t_start.utc_datetime() + timedelta(hours=i) for i in range(num_steps)]
    times = ts.from_datetimes(t_list)

    # Pre-calculate longitudes, altitudes and sun altitude vectorized
    longitudes = []
    altitudes = []
    for _, obj in planet_objs:
        # Longitudes are geocentric ecliptic
        lons = cast(Any, earth).at(times).observe(obj).ecliptic_latlon()[1].degrees
        longitudes.append(lons)

        # Altitudes are topocentric (from observer)
        alts = observer.at(times).observe(obj).apparent().altaz()[0].degrees
        altitudes.append(alts)

    longitudes = np.array(longitudes)  # (n_planets, n_times)
    altitudes = np.array(altitudes)  # (n_planets, n_times)

    sun_alts = observer.at(times).observe(sun).apparent().altaz()[0].degrees
    is_dark = sun_alts < -6

    def get_best_k_and_arc(lons_at_t):
        sorted_indices = np.argsort(lons_at_t)
        sorted_lons = lons_at_t[sorted_indices]
        n = len(sorted_lons)
        lons_extended = np.concatenate([sorted_lons, sorted_lons + 360])

        best_k = 0
        best_arc = 360
        best_indices = []

        for k in range(3, n + 1):
            min_arc_k = 360
            min_indices_k = []
            for i in range(n):
                arc = lons_extended[i + k - 1] - lons_extended[i]
                if arc < min_arc_k:
                    min_arc_k = arc
                    # Indices of planets in the arc
                    min_indices_k = [sorted_indices[j % n] for j in range(i, i + k)]

            if min_arc_k < thresholds.get(k, 360):
                best_k = k
                best_arc = min_arc_k
                best_indices = min_indices_k

        return best_k, best_arc, best_indices

    # Calculate stats for every hour
    step_results = []
    for i in range(len(times)):
        k, arc, indices = get_best_k_and_arc(longitudes[:, i])

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

    # Aggregate to daily results to maintain consistent grouping
    from collections import defaultdict

    by_day = defaultdict(list)
    for i, res in enumerate(step_results):
        day = times[i].utc_datetime().date()
        by_day[day].append((times[i], res))

    daily_results = []
    sorted_days = sorted(by_day.keys())
    for day in sorted_days:
        day_steps = by_day[day]
        # Best day means: max k, then max num_visible, then min arc
        best_step = max(
            day_steps, key=lambda x: (x[1]["k"], x[1]["num_visible"], -x[1]["arc"])
        )
        daily_results.append(best_step)

    events = []
    i = 0
    while i < len(daily_results):
        if daily_results[i][1]["k"] >= 3:
            # Start of an alignment period
            start_i = i
            while i < len(daily_results) and daily_results[i][1]["k"] >= 3:
                i += 1
            end_i = i

            # Find the best representative day in the window
            window = daily_results[start_i:end_i]
            best_day_tuple = max(
                window, key=lambda x: (x[1]["k"], x[1]["num_visible"], -x[1]["arc"])
            )

            t_best, res = best_day_tuple
            k = res["k"]
            arc = res["arc"]
            indices = res["indices"]
            num_visible = res["num_visible"]
            visible_indices = res["visible_indices"]

            aligned_planets = [planetary.get_simple_name(planets[idx]) for idx in indices]
            visible_names = [
                planetary.get_simple_name(planets[idx]) for idx in visible_indices
            ]

            event_label = f"Alignment of {k} planets"
            if num_visible >= 3:
                event_label += f" ({num_visible} visible)"

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
