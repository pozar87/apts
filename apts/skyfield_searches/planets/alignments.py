from typing import Any, cast
import numpy as np

from ...cache import get_timescale, get_ephemeris
from ...utils import planetary


def find_planet_alignments(observer, start_date, end_date):
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
    earth = get_ephemeris()["earth"]

    # Thresholds for different numbers of planets
    thresholds = {
        3: 10,
        4: 25,
        5: 45,
        6: 90,
        7: 150,
    }

    # We'll check every day.
    num_days = int(t_end - t_start) + 1
    if num_days <= 0:
        return []

    t_utc = cast(Any, t_start.utc_datetime())
    times = ts.utc(
        t_utc.year,
        t_utc.month,
        t_utc.day + np.arange(num_days),
    )

    # Pre-calculate longitudes for all planets at all times
    longitudes = []
    for _, obj in planet_objs:
        lons = cast(Any, earth).at(times).observe(obj).ecliptic_latlon()[1].degrees
        longitudes.append(lons)

    longitudes = np.array(longitudes)  # (n_planets, n_times)

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

    daily_results = []
    for i in range(len(times)):
        k, arc, indices = get_best_k_and_arc(longitudes[:, i])
        daily_results.append((k, arc, indices))

    events = []
    i = 0
    while i < len(daily_results):
        if daily_results[i][0] >= 3:
            # Start of an alignment period
            start_i = i
            while i < len(daily_results) and daily_results[i][0] >= 3:
                i += 1
            end_i = i

            # Find the best day in [start_i, end_i)
            # "Best" means max k, then min arc
            window = daily_results[start_i:end_i]
            max_k_in_window = max(w[0] for w in window)

            best_j = -1
            min_arc = 360
            for j, (k, arc, _) in enumerate(window):
                if k == max_k_in_window:
                    if arc < min_arc:
                        min_arc = arc
                        best_j = j

            best_i = start_i + best_j
            k, arc, indices = daily_results[best_i]
            aligned_planets = [
                planetary.get_simple_name(planets[idx]) for idx in indices
            ]

            events.append(
                {
                    "date": times[best_i].utc_datetime(),
                    "event": f"Alignment of {k} planets",
                    "planets": aligned_planets,
                    "arc_degrees": arc,
                }
            )
        else:
            i += 1

    return events
