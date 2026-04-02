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
    peak_altitude_threshold=40,
    rise_altitude_threshold=10,
    sun_altitude_threshold=-18.0,
):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    try:
        stations_url = "https://celestrak.org/NORAD/elements/stations.txt"
        # Load TLE file - no ephemeris needed for satellite data
        # Skyfield will cache this file by default
        satellites = load.tle_file(stations_url)
        satellite = next(s for s in satellites if s.name == satellite_name)
    except Exception as e:
        # Could be network error, or satellite not in file
        print(f"Could not load TLEs for {satellite_name}: {e}")
        return []

    # Find rise/culmination/set events above `rise_altitude_threshold`
    times, events = satellite.find_events(
        topos_observer, t0, t1, altitude_degrees=rise_altitude_threshold
    )

    events_list = []
    sun = planetary.get_skyfield_obj("sun")

    for i, event_code in enumerate(events):
        if event_code != 1:  # only look at culmination
            continue

        culmination_time = times[i]

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

        # Check if satellite is sunlit
        if not sat.is_sunlit(get_ephemeris()):
            continue

        # Calculate apparent magnitude
        mag = calculate_satellite_magnitude(
            satellite_name,
            sat.position.km,
            cast(Any, sun).at(culmination_time).position.km,
            obs.position.km,
            distance.km,
        )

        if magnitude_threshold is not None and mag > magnitude_threshold:
            continue

        event_data = {
            "date": culmination_time.utc_datetime(),
            "event": event_name,
            "type": event_type,
            "rise_time": None,
            "culmination_time": culmination_time.utc_datetime(),
            "set_time": None,
            "peak_altitude": alt.degrees,
            "peak_magnitude": float(mag),
        }

        # Find rise and set times for this pass
        # If they are not in the 'times' list (because they fell outside the search window),
        # we try to find them by searching a small window around the culmination.
        if i > 0 and events[i - 1] == 0:
            event_data["rise_time"] = times[i - 1].utc_datetime()
        else:
            # Rise happened before start_date? Search up to 30 mins before culmination.
            t_search_start = ts.utc(
                culmination_time.utc_datetime() - timedelta(minutes=30)
            )
            t_search_end = culmination_time
            r_times, r_events = satellite.find_events(
                topos_observer,
                t_search_start,
                t_search_end,
                altitude_degrees=rise_altitude_threshold,
            )
            r_indices = [idx for idx, code in enumerate(r_events) if code == 0]
            if r_indices:
                event_data["rise_time"] = r_times[r_indices[-1]].utc_datetime()
            else:
                event_data["rise_time"] = None

        if i < len(events) - 1 and events[i + 1] == 2:
            event_data["set_time"] = times[i + 1].utc_datetime()
        else:
            # Set will happen after end_date? Search up to 30 mins after culmination.
            t_search_start = culmination_time
            t_search_end = ts.utc(
                culmination_time.utc_datetime() + timedelta(minutes=30)
            )
            s_times, s_events = satellite.find_events(
                topos_observer,
                t_search_start,
                t_search_end,
                altitude_degrees=rise_altitude_threshold,
            )
            s_indices = [idx for idx, code in enumerate(s_events) if code == 2]
            if s_indices:
                event_data["set_time"] = s_times[s_indices[0]].utc_datetime()
            else:
                event_data["set_time"] = None

        events_list.append(event_data)

    return events_list

def find_iss_flybys(
    topos_observer,
    vector_observer,
    start_date,
    end_date,
    magnitude_threshold=-1.5,
    peak_altitude_threshold=40,
    rise_altitude_threshold=10,
    sun_altitude_threshold=-6.0,
):
    # Oracle: Relaxed default sun altitude to -6 (civil twilight) as bright ISS is visible.
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
    peak_altitude_threshold=40,
    rise_altitude_threshold=10,
    sun_altitude_threshold=-6.0,
):
    # Oracle: Relaxed default sun altitude to -6 (civil twilight) as Tiangong is visible.
    return _find_satellite_flybys(
        topos_observer,
        vector_observer,
        start_date,
        end_date,
        "CSS (TIANHE)",
        "Bright Tiangong Flyby",
        "Tiangong Flyby",
        None,  # No magnitude threshold for Tiangong
        peak_altitude_threshold,
        rise_altitude_threshold,
        sun_altitude_threshold,
    )
