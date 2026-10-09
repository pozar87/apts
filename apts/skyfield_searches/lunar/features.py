from collections.abc import Iterable
from typing import Any, cast

import numpy as np
from skyfield.searchlib import find_maxima, find_minima

from ...cache import get_timescale
from ...utils import planetary
from ..utils import fast_altaz


def find_moon_libration_maxima(observer, start_date, end_date):
    """
    Finds local maxima in lunar libration (longitude and latitude).
    These are the best times to observe features near the Moon's limb.
    Uses a two-stage search strategy:
    1. Candidate extrema timestamps are found using geocentric libration (observer=None).
       This bypasses topocentric frame rotations, GAST, and nutation calculations across time step grids
       while eliminating topocentric diurnal oscillation noise (~40x speedup for candidate searching).
    2. Vectorized topocentric refinement around candidate peaks with 3-point parabolic peak interpolation
       for exact topocentric extremum timing and altitude visibility.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    sun = planetary.get_skyfield_obj("sun")
    moon_sf = planetary.get_skyfield_obj("moon")

    # Observer elevation for global indexing
    observer_elevation = 0
    for vf in observer.vector_functions:
        if hasattr(vf, "elevation"):
            observer_elevation = vf.elevation.m
            break

    # Oracle: Use topocentric libration if not global indexing
    lib_observer = observer if observer_elevation != -9999 else None

    # Step 1: Geocentric libration candidate search
    def geo_lib_lon(t):
        lon, _ = planetary.get_moon_libration(t, observer=None)
        return lon

    def geo_lib_lat(t):
        _, lat = planetary.get_moon_libration(t, observer=None)
        return lat

    geo_lib_lon.step_days = 2.0
    geo_lib_lat.step_days = 2.0

    lon_max_times, lon_max_vals = find_maxima(t0, t1, geo_lib_lon)
    lon_min_times, lon_min_vals = find_minima(t0, t1, geo_lib_lon)
    lat_max_times, lat_max_vals = find_maxima(t0, t1, geo_lib_lat)
    lat_min_times, lat_min_vals = find_minima(t0, t1, geo_lib_lat)

    # Step 2: Vectorized topocentric peak refinement and visibility calculation
    def process_candidates(cand_times, cand_vals, axis, extreme):
        results = []
        for t_geo, val_geo in zip(cast(Iterable[Any], cand_times), cand_vals):
            if lib_observer is not None:
                # Sample 25 points over +/- 0.5 days around t_geo in a single vectorized pass
                tt_samples = np.linspace(t_geo.tt - 0.5, t_geo.tt + 0.5, 25)
                t_samples = ts.tt_jd(tt_samples)
                if axis == "longitude":
                    lons, _ = planetary.get_moon_libration(t_samples, observer=lib_observer)
                    vals = lons
                else:
                    _, lats = planetary.get_moon_libration(t_samples, observer=lib_observer)
                    vals = lats

                idx = int(np.argmax(vals)) if extreme == "max" else int(np.argmin(vals))

                # Parabolic 3-point peak interpolation
                if 0 < idx < len(vals) - 1:
                    y1, y2, y3 = vals[idx - 1], vals[idx], vals[idx + 1]
                    denom = y1 - 2 * y2 + y3
                    if abs(denom) > 1e-9:
                        delta = 0.5 * (y1 - y3) / denom
                        delta = float(np.clip(delta, -0.5, 0.5))
                        tt_ref = tt_samples[idx] + delta * (tt_samples[1] - tt_samples[0])
                        val_ref = y2 - 0.25 * (y1 - y3) * delta
                    else:
                        tt_ref = tt_samples[idx]
                        val_ref = y2
                else:
                    tt_ref = tt_samples[idx]
                    val_ref = vals[idx]
                t_ref = ts.tt_jd(tt_ref)
            else:
                t_ref = t_geo
                val_ref = val_geo

            obs_at_t = observer.at(t_ref)
            m_alt = fast_altaz(obs_at_t, moon_sf, temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
            s_alt = fast_altaz(obs_at_t, sun, temperature_C=10.0, pressure_mbar=1013.25)[0].degrees

            is_visible = (m_alt > 0 and s_alt <= -6) or observer_elevation == -9999

            side = {
                ("longitude", "max"): "East",
                ("longitude", "min"): "West",
                ("latitude", "max"): "North",
                ("latitude", "min"): "South",
            }[(axis, extreme)]

            results.append(
                {
                    "date": t_ref.utc_datetime(),
                    "event": f"Maximum Lunar Libration ({side})",
                    "object": "Moon",
                    "type": "Moon Libration Maximum",
                    "libration_value": float(val_ref),
                    "axis": axis,
                    "side": side,
                    "altitude": float(m_alt),
                    "is_visible": bool(is_visible),
                }
            )
        return results

    events = []
    events.extend(process_candidates(lon_max_times, lon_max_vals, "longitude", "max"))
    events.extend(process_candidates(lon_min_times, lon_min_vals, "longitude", "min"))
    events.extend(process_candidates(lat_max_times, lat_max_vals, "latitude", "max"))
    events.extend(process_candidates(lat_min_times, lat_min_vals, "latitude", "min"))

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
    num_steps = max(num_steps, 2)

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
            # Oracle: use fast_altaz for topocentric visibility
            obs_at_t = observer.at(t_refined)
            m_alt = fast_altaz(obs_at_t, moon_sf, temperature_C=10.0, pressure_mbar=1013.25)[0].degrees

            # Lazy check for darkness only if Moon is visible
            def check_dark(obs=obs_at_t):
                s_alt = fast_altaz(obs, sun, temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
                return s_alt <= -6

            # Special elevation -9999 bypasses topocentric checks for global indexing
            if observer_elevation == -9999 or (m_alt > 0 and check_dark()):
                events.append(
                    {
                        "date": t_refined.utc_datetime(),
                        "event": name,
                        "object": "Moon",
                        "type": "Lunar Feature",
                        "altitude": float(m_alt),
                        "colongitude": float(planetary.get_moon_colongitude(t_refined)),
                    }
                )

    return events
