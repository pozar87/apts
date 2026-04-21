from typing import Any, cast
import numpy as np
from skyfield import almanac
from skyfield.searchlib import find_maxima, find_minima
from ...cache import get_timescale, get_ephemeris
from ...utils import planetary

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
        for i, t in enumerate(cast(Any, max_times)):
            events.append({
                "date": t.utc_datetime(),
                "event": "Apogee",
                "object": "Moon",
                "distance_km": float(max_dist[i])
            })
    if len(min_times) > 0:
        min_dist = cast(Any, earth).at(min_times).observe(moon).distance().km
        for i, t in enumerate(cast(Any, min_times)):
            events.append({
                "date": t.utc_datetime(),
                "event": "Perigee",
                "object": "Moon",
                "distance_km": float(min_dist[i])
            })

    return events
