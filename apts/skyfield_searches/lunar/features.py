from typing import Any, Iterable, cast
import numpy as np
from skyfield.searchlib import find_maxima, find_minima
from ...cache import get_timescale
from ...utils import planetary

def find_moon_libration_maxima(observer, start_date, end_date):
    """
    Finds local maxima in lunar libration (longitude and latitude).
    These are the best times to observe features near the Moon's limb.
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

    def libration_lon(t):
        lon, _ = planetary.get_moon_libration(t, observer=lib_observer)
        return lon

    def libration_lat(t):
        _, lat = planetary.get_moon_libration(t, observer=lib_observer)
        return lat

    # Step of 2 days is safe for libration cycles (~27.3 days)
    setattr(libration_lon, "step_days", 2.0)
    setattr(libration_lat, "step_days", 2.0)

    # We want both extreme positive and negative values (East/West, North/South)
    lon_max_times, lon_max_vals = find_maxima(t0, t1, libration_lon)
    lon_min_times, lon_min_vals = find_minima(t0, t1, libration_lon)
    lat_max_times, lat_max_vals = find_maxima(t0, t1, libration_lat)
    lat_min_times, lat_min_vals = find_minima(t0, t1, libration_lat)

    events = []

    # Helper to calculate visibility and build event dict
    def add_lib_event(t, val, axis, extreme):
        # Oracle: use refracted positions for visibility check
        m_obs = observer.at(t).observe(moon_sf).apparent()
        m_alt, _, _ = m_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

        s_alt = (
            observer.at(t)
            .observe(sun)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )

        is_visible = (m_alt.degrees > 0 and s_alt <= -6) or observer_elevation == -9999

        side = {
            ("longitude", "max"): "East",
            ("longitude", "min"): "West",
            ("latitude", "max"): "North",
            ("latitude", "min"): "South",
        }[(axis, extreme)]

        events.append(
            {
                "date": t.utc_datetime(),
                "event": f"Maximum Lunar Libration ({side})",
                "object": "Moon",
                "type": "Moon Libration Maximum",
                "libration_value": float(val),
                "axis": axis,
                "side": side,
                "altitude": float(m_alt.degrees),
                "is_visible": bool(is_visible),
            }
        )

    for t, v in zip(cast(Iterable[Any], lon_max_times), lon_max_vals):
        add_lib_event(t, v, "longitude", "max")
    for t, v in zip(cast(Iterable[Any], lon_min_times), lon_min_vals):
        add_lib_event(t, v, "longitude", "min")
    for t, v in zip(cast(Iterable[Any], lat_max_times), lat_max_vals):
        add_lib_event(t, v, "latitude", "max")
    for t, v in zip(cast(Iterable[Any], lat_min_times), lat_min_vals):
        add_lib_event(t, v, "latitude", "min")

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
    if num_steps < 2:
        num_steps = 2

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
            # Oracle: use refracted positions for topocentric visibility
            m_obs = observer.at(t_refined).observe(moon_sf).apparent()
            m_alt, _, _ = m_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

            # Lazy check for darkness only if Moon is visible
            def check_dark():
                s_alt = (
                    observer.at(t_refined)
                    .observe(sun)
                    .apparent()
                    .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                    .degrees
                )
                return s_alt <= -6

            # Special elevation -9999 bypasses topocentric checks for global indexing
            if observer_elevation == -9999 or (m_alt.degrees > 0 and check_dark()):
                events.append(
                    {
                        "date": t_refined.utc_datetime(),
                        "event": name,
                        "object": "Moon",
                        "type": "Lunar Feature",
                        "altitude": float(m_alt.degrees),
                        "colongitude": float(planetary.get_moon_colongitude(t_refined)),
                    }
                )

    return events
