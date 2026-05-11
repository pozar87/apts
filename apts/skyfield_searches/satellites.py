from datetime import timedelta
from typing import Any, cast
import numpy as np
from skyfield.api import load
from ..cache import get_timescale, get_ephemeris
from ..utils import planetary

def calculate_satellite_magnitude(
    satellite_name, sat_pos_km, sun_pos_km, observer_pos_km, distance_km
):
    """Calculates the apparent magnitude of a satellite."""
    # Vector from satellite to sun
    vec_sat_sun = sun_pos_km - sat_pos_km

    # Vector from satellite to observer
    vec_sat_obs = observer_pos_km - sat_pos_km

    # Calculate phase angle beta
    norm_sun = np.linalg.norm(vec_sat_sun)
    norm_obs = np.linalg.norm(vec_sat_obs)

    if norm_sun > 0 and norm_obs > 0:
        cos_beta = np.dot(vec_sat_sun, vec_sat_obs) / (norm_sun * norm_obs)
        beta = np.arccos(np.clip(cos_beta, -1.0, 1.0))

        # Phase function for diffuse sphere
        phi = (np.sin(beta) + (np.pi - beta) * np.cos(beta)) / np.pi

        # Standard magnitude (at 1000km, 0 phase)
        # ISS is approx -1.8, Tiangong is approx 0.0
        m_std = -1.8 if "ISS" in satellite_name else 0.0

        # Apparent magnitude
        return float(
            m_std + 5 * np.log10(distance_km / 1000.0) - 2.5 * np.log10(max(phi, 1e-9))
        )
    return 5.0

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

    try:
        stations_url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"
        # Load TLE file - no ephemeris needed for satellite data
        # Skyfield will cache this file by default
        satellites = load.tle_file(stations_url)
        satellite = next(s for s in satellites if s.name == satellite_name)
    except Exception as e:
        # Could be network error, or satellite not in file
        print(f"Could not load TLEs for {satellite_name}: {e}")
        return []

    # Find rise/culmination/set events above `rise_altitude_threshold`
    # Use a wider window for the initial search to avoid missing events near boundaries
    t_search_start = ts.utc(start_date - timedelta(minutes=30))
    t_search_end = ts.utc(end_date + timedelta(minutes=30))

    times, events = satellite.find_events(
        topos_observer, t_search_start, t_search_end, altitude_degrees=rise_altitude_threshold
    )

    events_list = []
    sun = planetary.get_skyfield_obj("sun")
    eph = get_ephemeris()

    for i, event_code in enumerate(events):
        if event_code != 1:  # only look at culmination
            continue

        culmination_time = times[i]

        # Only include flybys whose culmination is within the original start/end window
        if culmination_time.tt < t0.tt - 1e-9 or culmination_time.tt > t1.tt + 1e-9:
            continue

        # Sun altitude (dark-sky check)
        sun_alt, _, _ = (
            vector_observer.at(culmination_time)
            .observe(sun)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)
        )
        if sun_alt.degrees > sun_altitude_threshold:  # not dark enough
            continue

        # Topocentric satellite position
        sat = cast(Any, satellite).at(culmination_time)
        obs = cast(Any, topos_observer).at(culmination_time)
        topocentric = sat - obs

        # Altitude, azimuth, distance
        alt, az, distance = topocentric.altaz(temperature_C=10.0, pressure_mbar=1013.25)
        if alt.degrees < peak_altitude_threshold:
            continue

        # Find rise and set times for this pass at the rise_altitude_threshold
        rise_time = None
        set_time = None
        if i > 0 and events[i-1] == 0:
            rise_time = times[i-1]
        if i < len(events) - 1 and events[i+1] == 2:
            set_time = times[i+1]

        # Check if satellite is sunlit at any point during the pass
        # where it is at least 2.0 degrees above the horizon.
        is_sunlit = sat.is_sunlit(eph)

        if not is_sunlit:
            # Check for sunlight at the 2.0-degree altitude points.
            t_s_start = ts.utc(culmination_time.utc_datetime() - timedelta(minutes=15))
            t_s_end = ts.utc(culmination_time.utc_datetime() + timedelta(minutes=15))
            v_times, v_events = satellite.find_events(
                topos_observer, t_s_start, t_s_end, altitude_degrees=2.0
            )
            for v_t, v_e in zip(v_times, v_events):
                if v_e in (0, 1, 2) and satellite.at(v_t).is_sunlit(eph):
                    is_sunlit = True
                    break

        if not is_sunlit:
            continue

        # Calculate apparent magnitude
        # We need Sun position relative to Earth center for correct phase angle
        sun_pos_earth_center = (eph["sun"] - eph["earth"]).at(culmination_time).position.km
        mag = calculate_satellite_magnitude(
            satellite_name,
            sat.position.km,
            sun_pos_earth_center,
            obs.position.km,
            distance.km,
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
            "peak_altitude": alt.degrees,
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
