from datetime import timedelta
from typing import Any, cast

import numpy as np
from skyfield.api import load

from ...cache import STATIONS_URL, get_ephemeris, get_timescale
from ...utils import planetary
from ..utils import fast_altaz
from .magnitude import calculate_satellite_magnitude


def _load_satellite(satellite_name: str):
    """Loads a satellite by name from the TLE data."""
    try:
        stations_url = STATIONS_URL
        # Load TLE file - no ephemeris needed for satellite data
        # Skyfield will cache this file by default
        satellites = load.tle_file(stations_url)
        return cast(Any, next(s for s in satellites if s.name == satellite_name))
    except Exception as e:
        # Could be network error, or satellite not in file
        print(f"Could not load TLEs for {satellite_name}: {e}")
        return None


def _get_pass_times(i, events, times):
    """Extracts rise and set times for a given culmination event index."""
    rise_time = None
    set_time = None
    if i > 0 and events[i - 1] == 0:
        rise_time = times[i - 1]
    if i < len(events) - 1 and events[i + 1] == 2:
        set_time = times[i + 1]
    return rise_time, set_time


def _check_sunlight(satellite, culmination_time, topos_observer, ts, eph):
    """Determines if the satellite is sunlit during its pass."""
    sat_at_t = cast(Any, satellite).at(culmination_time)
    if sat_at_t.is_sunlit(eph):
        return True

    # Check for sunlight at the 2.0-degree altitude points.
    t_s_start = ts.utc(culmination_time.utc_datetime() - timedelta(minutes=15))
    t_s_end = ts.utc(culmination_time.utc_datetime() + timedelta(minutes=15))
    v_times, v_events = satellite.find_events(
        topos_observer, t_s_start, t_s_end, altitude_degrees=2.0
    )
    for v_t, v_e in zip(v_times, v_events):
        if v_e in (0, 1, 2) and cast(Any, satellite).at(v_t).is_sunlit(eph):
            return True
    return False


def _find_satellite_flybys(
    topos_observer,
    vector_observer,
    start_date,
    end_date,
    satellite_name,
    event_name,
    event_type,
    magnitude_threshold=None,
    peak_altitude_threshold=10,
    rise_altitude_threshold=5,
    sun_altitude_threshold=-18.0,
):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    satellite = _load_satellite(satellite_name)
    if satellite is None:
        return []

    # Find rise/culmination/set events above `rise_altitude_threshold`
    # Use a wider window for the initial search to avoid missing events near boundaries
    t_search_start = ts.utc(start_date - timedelta(minutes=30))
    t_search_end = ts.utc(end_date + timedelta(minutes=30))

    times, events = satellite.find_events(
        topos_observer,
        t_search_start,
        t_search_end,
        altitude_degrees=rise_altitude_threshold,
    )

    if len(events) == 0:
        return []

    sun = planetary.get_skyfield_obj("sun")
    eph = get_ephemeris()

    # Optimization: Extract all culmination event indices within search window upfront
    culm_indices = []
    for i, event_code in enumerate(events):
        if event_code == 1:
            culm_t = times[i]
            if t0.tt - 1e-9 <= culm_t.tt <= t1.tt + 1e-9:
                culm_indices.append(i)

    if not culm_indices:
        return []

    # Optimization: Calculate Sun altitudes for all culmination times in a single
    # vectorized pass using fast_altaz, bypassing expensive Standard Apparent calculations
    # (~3x overall speedup for satellite flyby searches)
    culm_times_vec = ts.tt_jd([times[i].tt for i in culm_indices])
    sun_alts_raw = fast_altaz(
        vector_observer.at(culm_times_vec),
        sun,
        temperature_C=10.0,
        pressure_mbar=1013.25,
    )[0].degrees
    sun_alts = np.broadcast_to(np.atleast_1d(sun_alts_raw), len(culm_indices))

    # Filter candidates by dark-sky threshold in bulk
    dark_mask = sun_alts <= sun_altitude_threshold
    dark_indices = [
        culm_indices[idx] for idx in range(len(culm_indices)) if dark_mask[idx]
    ]

    if not dark_indices:
        return []

    dark_times_vec = ts.tt_jd([times[i].tt for i in dark_indices])

    # Optimization: Vectorized topocentric satellite observation for dark candidates
    sat = cast(Any, satellite).at(dark_times_vec)
    obs = cast(Any, topos_observer).at(dark_times_vec)
    topocentric = sat - obs
    alts, _, distances = topocentric.altaz(temperature_C=10.0, pressure_mbar=1013.25)

    alts_deg = np.broadcast_to(np.atleast_1d(alts.degrees), len(dark_indices))
    distances_km = np.broadcast_to(np.atleast_1d(distances.km), len(dark_indices))

    sun_pos_earth_center_all = (
        cast(Any, eph["sun"] - eph["earth"]).at(dark_times_vec).position.km
    )

    events_list = []
    for idx, i in enumerate(dark_indices):
        culmination_time = times[i]
        alt_deg = alts_deg[idx]
        if alt_deg < peak_altitude_threshold:
            continue

        rise_time, set_time = _get_pass_times(i, events, times)

        if not _check_sunlight(satellite, culmination_time, topos_observer, ts, eph):
            continue

        dist_km = distances_km[idx]
        sat_pos_km = (
            sat.position.km[:, idx]
            if isinstance(sat.position.km, np.ndarray) and sat.position.km.ndim > 1
            else sat.position.km
        )
        sun_pos_km = (
            sun_pos_earth_center_all[:, idx]
            if isinstance(sun_pos_earth_center_all, np.ndarray)
            and sun_pos_earth_center_all.ndim > 1
            else sun_pos_earth_center_all
        )
        obs_pos_km = (
            obs.position.km[:, idx]
            if isinstance(obs.position.km, np.ndarray) and obs.position.km.ndim > 1
            else obs.position.km
        )

        mag = calculate_satellite_magnitude(
            satellite_name,
            sat_pos_km,
            sun_pos_km,
            obs_pos_km,
            dist_km,
        )

        if magnitude_threshold is not None and mag > magnitude_threshold:
            continue

        event_data = {
            "date": culmination_time.utc_datetime(),
            "event": event_name,
            "type": event_type,
            "rise_time": rise_time.utc_datetime() if rise_time is not None else None,
            "culmination_time": culmination_time.utc_datetime(),
            "set_time": set_time.utc_datetime() if set_time is not None else None,
            "peak_altitude": float(alt_deg),
            "peak_magnitude": float(mag),
        }

        events_list.append(event_data)

    return events_list


def find_iss_flybys(
    topos_observer,
    vector_observer,
    start_date,
    end_date,
    magnitude_threshold=2.0,
    peak_altitude_threshold=10,
    rise_altitude_threshold=5,
    sun_altitude_threshold=-4.0,
):
    return _find_satellite_flybys(
        topos_observer,
        vector_observer,
        start_date,
        end_date,
        "ISS (ZARYA)",
        "Bright ISS Flyby",
        "ISS Flyby",
        magnitude_threshold,
        peak_altitude_threshold,
        rise_altitude_threshold,
        sun_altitude_threshold,
    )


def find_tiangong_flybys(
    topos_observer,
    vector_observer,
    start_date,
    end_date,
    peak_altitude_threshold=10,
    rise_altitude_threshold=5,
    sun_altitude_threshold=-6.0,
):
    return _find_satellite_flybys(
        topos_observer,
        vector_observer,
        start_date,
        end_date,
        "CSS (TIANHE)",
        "Bright Tiangong Flyby",
        "Tiangong Flyby",
        None,
        peak_altitude_threshold,
        rise_altitude_threshold,
        sun_altitude_threshold,
    )
