from datetime import datetime, timedelta
from typing import Any, cast, List, Tuple, Optional, Dict

import numpy as np
from skyfield import almanac, eclipselib
from skyfield.api import load, Star
from skyfield.searchlib import find_maxima, find_minima

from .cache import get_ephemeris, get_timescale
from .constants import astronomy
from .utils import planetary


def find_solar_longitude_time(t0, t1, target_longitude, epoch=None):
    """
    Finds the exact time when the Sun reaches a specific ecliptic longitude.
    Default epoch is J2000.0 if not specified.
    Used for high-precision meteor shower peak prediction.
    """
    eph = cast(Any, get_ephemeris())
    sun = eph["sun"]
    earth = eph["earth"]
    ts = get_timescale()
    target_epoch = epoch if epoch is not None else ts.utc(2000)

    def solar_longitude_at(t):
        # Solar longitude (λ⊙) is the ecliptic longitude of the Sun as seen from Earth.
        # We use apparent position to include aberration and nutation.
        _, lon, _ = earth.at(t).observe(sun).apparent().ecliptic_latlon(target_epoch)
        return lon.degrees

    def longitude_difference(t):
        diff = solar_longitude_at(t) - target_longitude
        return (diff + 180) % 360 - 180

    def abs_diff(t):
        return abs(longitude_difference(t))

    setattr(abs_diff, "step_days", 1.0)
    times, _ = find_minima(t0, t1, abs_diff)

    return times[0] if len(times) > 0 else None


def _refine_conjunction(observer, obj1, obj2, rough_t):
    """
    Refines the time of a conjunction using iterative minimization.
    Achieves sub-second timing precision.
    """
    ts = get_timescale()
    # Search within +/- 30 minutes of the rough time
    t0 = ts.from_datetime(rough_t.utc_datetime() - timedelta(minutes=30))
    t1 = ts.from_datetime(rough_t.utc_datetime() + timedelta(minutes=30))

    def separation_func(t):
        # We use .apparent() for maximum precision during refinement
        p1 = observer.at(t).observe(obj1).apparent()
        p2 = observer.at(t).observe(obj2).apparent()
        return p1.separation_from(p2).degrees

    setattr(separation_func, "step_days", 0.005)  # 7.2 minutes step for minimization
    times, separations = find_minima(t0, t1, separation_func)

    if len(times) > 0:
        return times[0], separations[0]
    return rough_t, separation_func(rough_t)


def find_golden_blue_hours(observer, start_date, end_date):
    """
    Finds the start and end times for Golden and Blue hours.
    Golden Hour: Sun between -4° and 6° altitude.
    Blue Hour: Sun between -6° and -4° altitude.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
    sun = eph["sun"]

    def sun_state(t):
        # We want to detect transitions at -6, -4, 6
        # Account for atmospheric refraction at standard conditions (10C, 1013.25 mbar)
        alt = (
            observer.at(t)
            .observe(sun)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )
        return (alt >= -6).astype(int) + (alt >= -4).astype(int) + (alt >= 6).astype(int)

    setattr(sun_state, "step_days", 0.005)  # ~7.2 minutes

    t, y = almanac.find_discrete(t0, t1, sun_state)

    events = []
    y_prev = sun_state(t0)

    for ti, yi in zip(t, y):
        # Transitions mapping:
        # 0 -> 1: Rising Blue Start (-6)
        # 1 -> 2: Rising Blue End / Golden Start (-4)
        # 2 -> 3: Rising Golden End (6)
        if y_prev == 0 and yi == 1:
            events.append({"date": ti.utc_datetime(), "event": "Blue Hour", "phase": "Start", "type": "Blue Hour"})
        elif y_prev == 1 and yi == 2:
            events.append({"date": ti.utc_datetime(), "event": "Blue Hour", "phase": "End", "type": "Blue Hour"})
            events.append({"date": ti.utc_datetime(), "event": "Golden Hour", "phase": "Start", "type": "Golden Hour"})
        elif y_prev == 2 and yi == 3:
            events.append({"date": ti.utc_datetime(), "event": "Golden Hour", "phase": "End", "type": "Golden Hour"})
        elif y_prev == 3 and yi == 2:
            events.append({"date": ti.utc_datetime(), "event": "Golden Hour", "phase": "Start", "type": "Golden Hour"})
        elif y_prev == 2 and yi == 1:
            events.append({"date": ti.utc_datetime(), "event": "Golden Hour", "phase": "End", "type": "Golden Hour"})
            events.append({"date": ti.utc_datetime(), "event": "Blue Hour", "phase": "Start", "type": "Blue Hour"})
        elif y_prev == 1 and yi == 0:
            events.append({"date": ti.utc_datetime(), "event": "Blue Hour", "phase": "End", "type": "Blue Hour"})

        y_prev = yi

    return events


def find_jovian_moon_events(observer, start_date, end_date):
    """
    Finds Jovian moon events (Transits, Shadows, Occultations, Eclipses)
    for Io, Europa, Ganymede, and Callisto using high-precision jup310 ephemeris.
    """
    from .cache import get_jovian_ephemeris

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_jovian_ephemeris())

    try:
        jupiter = eph["jupiter barycenter"]
        sun = eph["sun"]
        moon_map = {501: "Io", 502: "Europa", 503: "Ganymede", 504: "Callisto"}
        moon_objs = {moon_id: eph[moon_id] for moon_id in moon_map}
    except KeyError:
        return []

    events = []

    for moon_id, moon_name in moon_map.items():
        moon_obj = moon_objs[moon_id]

        def state_func(t):
            # Vectorized state function for find_discrete
            # Returns: 0: None, 1: Transit, 2: Occultation, 3: Shadow, 4: Eclipse
            is_array = hasattr(t, "shape") and t.shape != ()
            res = np.zeros(len(t) if is_array else 1, dtype=int)

            # Jupiter observed from Earth
            j_obs = observer.at(t).observe(jupiter).apparent()
            alt, _, dist = j_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

            # Moon observed from Earth
            m_obs = observer.at(t).observe(moon_obj).apparent()
            sep_e = j_obs.separation_from(m_obs).degrees
            j_rad_e = np.degrees(np.arcsin(astronomy.JUPITER_RADIUS_KM / dist.km))

            # Perspective from Earth
            in_transit = (sep_e < j_rad_e) & (m_obs.distance().km < dist.km)
            in_occultation = (sep_e < j_rad_e) & (m_obs.distance().km >= dist.km)

            # Jupiter and Moon observed from Sun
            j_sun = sun.at(t).observe(jupiter).apparent()
            m_sun = sun.at(t).observe(moon_obj).apparent()
            sep_s = j_sun.separation_from(m_sun).degrees
            j_rad_s = np.degrees(np.arcsin(astronomy.JUPITER_RADIUS_KM / j_sun.distance().km))

            # Perspective from Sun (Shadows/Eclipses)
            in_shadow = (sep_s < j_rad_s) & (m_sun.distance().km < j_sun.distance().km)
            in_eclipse = (sep_s < j_rad_s) & (m_sun.distance().km >= j_sun.distance().km)

            visible = alt.degrees > 0

            if hasattr(t, "shape"):
                res[visible & in_transit] = 1
                res[visible & in_occultation] = 2
                res[visible & in_shadow] = 3
                res[visible & in_eclipse] = 4
            else:
                if visible:
                    if in_transit: res[0] = 1
                    elif in_occultation: res[0] = 2
                    elif in_shadow: res[0] = 3
                    elif in_eclipse: res[0] = 4
            return res

        setattr(state_func, "step_days", 0.005)
        t_events, y_events = almanac.find_discrete(t0, t1, state_func)

        if len(t_events) == 0:
            continue

        y_start = state_func(t0)
        y_prev = y_start[0] if hasattr(y_start, "shape") else y_start
        state_names = {1: "Transit", 2: "Occultation", 3: "Shadow Transit", 4: "Eclipse"}

        for te, ye in zip(t_events, y_events):
            if y_prev != 0:
                events.append({"date": te.utc_datetime(), "object": moon_name, "event": f"{state_names[int(y_prev)]} End", "type": "Jovian Moon Event"})
            if ye != 0:
                events.append({"date": te.utc_datetime(), "object": moon_name, "event": f"{state_names[int(ye)]} Start", "type": "Jovian Moon Event"})
            y_prev = ye

    return events


def find_lunar_planetary_occultations(observer, start_date, end_date):
    """
    Finds occultations of planets by the Moon for a specific observer.
    Provides precise ingress and egress times.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = planetary.get_skyfield_obj("moon")

    planets = ["mercury", "venus", "mars barycenter", "jupiter barycenter", "saturn barycenter", "uranus barycenter", "neptune barycenter"]
    events = []

    for p_name in planets:
        planet = planetary.get_skyfield_obj(p_name)
        simple_name = planetary.get_simple_name(p_name)

        def is_occulted(t):
            m = observer.at(t).observe(moon).apparent()
            p = observer.at(t).observe(planet).apparent()
            sep = m.separation_from(p).degrees
            rad = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m.distance().km))
            alt, _, _ = m.altaz(temperature_C=10.0, pressure_mbar=1013.25)
            return (sep < rad) & (alt.degrees > 0)

        setattr(is_occulted, "step_days", 0.05)
        t_occ, y_occ = almanac.find_discrete(t0, t1, is_occulted)

        for i in range(0, len(t_occ), 2):
            if i + 1 < len(t_occ):
                ingress_t = t_occ[i]
                egress_t = t_occ[i + 1]
                # Mid-point for conjunction refinement if needed
                mid_t = ts.from_datetime(ingress_t.utc_datetime() + (egress_t.utc_datetime() - ingress_t.utc_datetime()) / 2)
                refined_t, _ = _refine_conjunction(observer, moon, planet, mid_t)
                events.append({
                    "date": refined_t.utc_datetime(),
                    "object1": "Moon",
                    "object2": simple_name,
                    "ingress_time": ingress_t.utc_datetime(),
                    "egress_time": egress_t.utc_datetime(),
                    "type": "Lunar Planetary Occultation",
                    "event": "Lunar Planetary Occultation",
                })
    return events


def find_highest_altitude(observer, planet, start_date, end_date):
    """Finds the highest altitude of a planet in a given time range."""
    ts = get_timescale()
    t0, t1 = ts.utc(start_date), ts.utc(end_date)

    def altitude(t):
        return observer.at(t).observe(planet).apparent().altaz(temperature_C=10.0, pressure_mbar=1013.25)[0].degrees

    setattr(altitude, "step_days", 0.1)
    times, altitudes = find_maxima(t0, t1, altitude)

    if len(times) == 0:
        return None, 0

    max_idx = np.argmax(altitudes)
    return times[max_idx].utc_datetime(), altitudes[max_idx]


def find_aphelion_perihelion(planet_name, start_date, end_date):
    """Finds when a planet reaches aphelion or perihelion."""
    ts = get_timescale()
    t0, t1 = ts.utc(start_date), ts.utc(end_date)
    body = planetary.get_skyfield_obj(planet_name)
    sun = planetary.get_skyfield_obj("sun")

    def distance_to_sun(t):
        return cast(Any, body).at(t).observe(sun).distance().km

    setattr(distance_to_sun, "step_days", 180)
    max_times, _ = find_maxima(t0, t1, distance_to_sun)
    min_times, _ = find_minima(t0, t1, distance_to_sun)

    events = [{"date": t.utc_datetime(), "event_type": "Aphelion", "planet": planet_name} for t in max_times]
    events += [{"date": t.utc_datetime(), "event_type": "Perihelion", "planet": planet_name} for t in min_times]
    return events


def find_planet_messier_conjunctions(observer, start_date, end_date):
    """Finds conjunctions between major planets and Messier objects."""
    from .catalogs import Catalogs
    catalogs = Catalogs()
    planets = ["mercury", "venus", "mars barycenter", "jupiter barycenter", "saturn barycenter", "uranus barycenter", "neptune barycenter"]
    messier_data = [(row["Messier"], row["skyfield_object"]) for _, row in catalogs.MESSIER.iterrows()]

    events = []
    for p_name in planets:
        planet_obj = planetary.get_skyfield_obj(p_name)
        simple_name = planetary.get_simple_name(p_name)
        # 3.0 degrees threshold for planet-DSO conjunctions
        conjunctions = find_conjunctions_with_stars(observer, p_name, messier_data, start_date, end_date, threshold_degrees=3.0)
        for conj in conjunctions:
            events.append({
                "date": conj["date"],
                "event": "Conjunction",
                "object1": simple_name,
                "object2": conj["object2"],
                "separation_degrees": conj["separation_degrees"],
                "type": "Planet-Messier Conjunction",
            })
    return events


def find_lunar_eclipses(start_date, end_date):
    """Finds lunar eclipses using Skyfield's eclipselib."""
    ts = get_timescale()
    t0, t1 = ts.utc(start_date), ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
    t, y, details = eclipselib.lunar_eclipses(t0, t1, eph)
    events = []
    for i, (ti, yi) in enumerate(zip(t, y)):
        events.append({
            "date": ti.utc_datetime(),
            "type": "Lunar Eclipse",
            "eclipse_kind": eclipselib.LUNAR_ECLIPSES[yi],
            "penumbral_magnitude": details["penumbral_magnitude"][i],
            "umbral_magnitude": details["umbral_magnitude"][i],
        })
    return events


def find_solar_eclipses(observer, start_date, end_date):
    """Finds solar eclipses for a specific observer, providing classification and magnitude."""
    ts = get_timescale()
    t0, t1 = ts.utc(start_date), ts.utc(end_date)
    sun = planetary.get_skyfield_obj("sun")
    moon = planetary.get_skyfield_obj("moon")

    def solar_separation(t):
        s = observer.at(t).observe(sun).apparent()
        m = observer.at(t).observe(moon).apparent()
        s_radius = np.degrees(np.arcsin(astronomy.SUN_RADIUS_KM / s.distance().km))
        m_radius = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m.distance().km))
        return s.separation_from(m).degrees - (s_radius + m_radius)

    setattr(solar_separation, "step_days", 0.05)
    times, _ = find_minima(t0, t1, solar_separation)

    events = []
    for t in times:
        s_pos = observer.at(t).observe(sun).apparent()
        m_pos = observer.at(t).observe(moon).apparent()
        d = s_pos.separation_from(m_pos).degrees
        rs = np.degrees(np.arcsin(astronomy.SUN_RADIUS_KM / s_pos.distance().km))
        rm = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_pos.distance().km))

        if d < rs + rm:
            sun_alt = s_pos.altaz(temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
            if sun_alt <= 0: continue
            kind = "Total" if d <= abs(rs - rm) and rm >= rs else ("Annular" if d <= abs(rs - rm) else "Partial")
            mag = (rs + rm - d) / (2 * rs)

            def overlap_area(r1, r2, d):
                if d >= r1 + r2: return 0.0
                if d <= abs(r1 - r2): return np.pi * min(r1, r2)**2
                r1sq, r2sq, dsq = r1**2, r2**2, d**2
                p1 = r1sq * np.arccos((dsq + r1sq - r2sq) / (2 * d * r1))
                p2 = r2sq * np.arccos((dsq + r2sq - r1sq) / (2 * d * r2))
                p3 = 0.5 * np.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
                return p1 + p2 - p3

            obs = overlap_area(rs, rm, d) / (np.pi * rs**2)
            events.append({
                "date": t.utc_datetime(), "type": "Solar Eclipse", "eclipse_type": kind,
                "magnitude": float(mag), "obscuration": float(obs), "separation_degrees": float(d),
            })
    return events


def find_planet_alignments(observer, start_date, end_date):
    """Finds alignment of 3 or more planets in the ecliptic longitude."""
    ts = get_timescale()
    t_start, t_end = ts.utc(start_date), ts.utc(end_date)
    planets = ["mercury", "venus", "mars barycenter", "jupiter barycenter", "saturn barycenter", "uranus barycenter", "neptune barycenter"]
    planet_objs = [(p, planetary.get_skyfield_obj(p)) for p in planets]
    earth = get_ephemeris()["earth"]
    thresholds = {3: 10, 4: 25, 5: 45, 6: 90, 7: 150}

    num_days = int(t_end - t_start) + 1
    if num_days <= 0: return []
    times = ts.utc(t_start.utc_datetime().year, t_start.utc_datetime().month, t_start.utc_datetime().day + np.arange(num_days))

    longitudes = np.array([earth.at(times).observe(obj).apparent().ecliptic_latlon()[1].degrees for _, obj in planet_objs])

    def get_best_k_and_arc(lons_at_t):
        sorted_indices = np.argsort(lons_at_t)
        sorted_lons = lons_at_t[sorted_indices]
        n = len(sorted_lons)
        lons_extended = np.concatenate([sorted_lons, sorted_lons + 360])
        best_k, best_arc, best_indices = 0, 360, []
        for k in range(3, n + 1):
            min_arc_k, min_indices_k = 360, []
            for i in range(n):
                arc = lons_extended[i + k - 1] - lons_extended[i]
                if arc < min_arc_k:
                    min_arc_k, min_indices_k = arc, [sorted_indices[j % n] for j in range(i, i + k)]
            if min_arc_k < thresholds.get(k, 360):
                best_k, best_arc, best_indices = k, min_arc_k, min_indices_k
        return best_k, best_arc, best_indices

    daily_results = [get_best_k_and_arc(longitudes[:, i]) for i in range(len(times))]
    events, i = [], 0
    while i < len(daily_results):
        if daily_results[i][0] >= 3:
            start_i = i
            while i < len(daily_results) and daily_results[i][0] >= 3: i += 1
            window = daily_results[start_i:i]
            max_k = max(w[0] for w in window)
            best_idx = np.argmin([w[1] if w[0] == max_k else 360 for w in window])
            k, arc, indices = window[best_idx]
            events.append({
                "date": times[start_i + best_idx].utc_datetime(), "event": f"Alignment of {k} planets",
                "planets": [planetary.get_simple_name(planets[idx]) for idx in indices], "arc_degrees": arc,
            })
        else: i += 1
    return events


def find_culminations(observer, start_date, end_date, sun_alt_threshold=-6):
    """Finds culminations (meridian transits) for major solar system bodies."""
    ts, eph = get_timescale(), get_ephemeris()
    t0, t1 = ts.utc(start_date), ts.utc(end_date)
    sun = eph["sun"]
    planets = ["sun", "moon", "mercury", "venus", "mars barycenter", "jupiter barycenter", "saturn barycenter", "uranus barycenter", "neptune barycenter"]
    events = []
    for name in planets:
        obj = planetary.get_skyfield_obj(name)
        def altitude(t):
            return observer.at(t).observe(obj).apparent().altaz(temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
        setattr(altitude, "step_days", 0.5)
        times, altitudes = find_maxima(t0, t1, altitude)
        simple_name = planetary.get_simple_name(name)
        for t, alt in zip(cast(Any, times), altitudes):
            if alt > 0:
                s_alt = observer.at(t).observe(sun).apparent().altaz(temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
                if simple_name == "Sun" or s_alt <= sun_alt_threshold:
                    events.append({"date": t.utc_datetime(), "event": "Culmination", "object": simple_name, "type": "Culmination", "altitude": float(alt)})
    return events


def find_object_culminations(observer, objects_data, start_date, end_date, sun_alt_threshold=-12):
    """Finds culminations for a list of objects (e.g., Messier catalog)."""
    ts, eph = get_timescale(), get_ephemeris()
    sun = eph["sun"]
    t0, t1 = ts.utc(start_date), ts.utc(end_date)
    events = []
    for name, obj in objects_data:
        def altitude(t):
            return observer.at(t).observe(obj).apparent().altaz(temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
        setattr(altitude, "step_days", 0.5)
        times, altitudes = find_maxima(t0, t1, altitude)
        for t, alt in zip(cast(Any, times), altitudes):
            if alt > 15:
                s_alt = observer.at(t).observe(sun).apparent().altaz(temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
                if s_alt <= sun_alt_threshold:
                    events.append({"date": t.utc_datetime(), "event": "Culmination", "object": name, "type": "Messier Culmination", "altitude": float(alt)})
    return events


def _find_satellite_flybys(topos_observer, vector_observer, start_date, end_date, satellite_name, event_name, event_type, magnitude_threshold=None, peak_altitude_threshold=40, rise_altitude_threshold=10):
    """Internal helper to find satellite flybys from TLE data."""
    ts = get_timescale()
    t0, t1 = ts.utc(start_date), ts.utc(end_date)
    try:
        stations_url = "https://celestrak.org/NORAD/elements/stations.txt"
        satellites = load.tle_file(stations_url)
        satellite = next(s for s in satellites if s.name == satellite_name)
    except Exception as e:
        import logging
        logging.getLogger(__name__).warning(f"Could not load TLE for {satellite_name}: {e}")
        return []

    times, events = satellite.find_events(topos_observer, t0, t1, altitude_degrees=rise_altitude_threshold)
    events_list, sun = [], get_ephemeris()["sun"]
    for i, code in enumerate(events):
        if code != 1: continue
        culm_t = times[i]
        s_alt, _, _ = vector_observer.at(culm_t).observe(sun).apparent().altaz()
        if s_alt.degrees > -18: continue
        sat_pos = cast(Any, satellite).at(culm_t)
        obs_pos = cast(Any, topos_observer).at(culm_t)
        alt, _, dist = (sat_pos - obs_pos).altaz()
        if alt.degrees < peak_altitude_threshold or not sat_pos.is_sunlit(get_ephemeris()): continue
        mag = calculate_satellite_magnitude(satellite_name, sat_pos.position.km, cast(Any, sun).at(culm_t).position.km, obs_pos.position.km, dist.km)
        if magnitude_threshold is not None and mag > magnitude_threshold: continue

        event_data = {"date": culm_t.utc_datetime(), "event": event_name, "type": event_type, "culmination_time": culm_t.utc_datetime(), "peak_altitude": alt.degrees, "peak_magnitude": float(mag)}
        if i > 0 and events[i-1] == 0: event_data["rise_time"] = times[i-1].utc_datetime()
        else:
            rt, re = satellite.find_events(topos_observer, ts.utc(culm_t.utc_datetime()-timedelta(minutes=30)), culm_t, altitude_degrees=rise_altitude_threshold)
            event_data["rise_time"] = rt[re==0][-1].utc_datetime() if any(re==0) else None
        if i < len(events)-1 and events[i+1] == 2: event_data["set_time"] = times[i+1].utc_datetime()
        else:
            st, se = satellite.find_events(topos_observer, culm_t, ts.utc(culm_t.utc_datetime()+timedelta(minutes=30)), altitude_degrees=rise_altitude_threshold)
            event_data["set_time"] = st[se==2][0].utc_datetime() if any(se==2) else None
        events_list.append(event_data)
    return events_list


def find_iss_flybys(topos_observer, vector_observer, start_date, end_date, magnitude_threshold=-1.5, peak_altitude_threshold=40, rise_altitude_threshold=10):
    """Finds ISS flybys for a given observer."""
    return _find_satellite_flybys(topos_observer, vector_observer, start_date, end_date, "ISS (ZARYA)", "Bright ISS Flyby", "ISS Flyby", magnitude_threshold, peak_altitude_threshold, rise_altitude_threshold)


def find_tiangong_flybys(topos_observer, vector_observer, start_date, end_date, peak_altitude_threshold=40, rise_altitude_threshold=10):
    """Finds Tiangong flybys for a given observer."""
    return _find_satellite_flybys(topos_observer, vector_observer, start_date, end_date, "CSS (TIANHE)", "Bright Tiangong Flyby", "Tiangong Flyby", None, peak_altitude_threshold, rise_altitude_threshold)


def calculate_satellite_magnitude(satellite_name, sat_pos_km, sun_pos_km, observer_pos_km, distance_km):
    """Calculates the apparent magnitude of a satellite."""
    v_sun, v_obs = sun_pos_km - sat_pos_km, observer_pos_km - sat_pos_km
    n_sun, n_obs = np.linalg.norm(v_sun), np.linalg.norm(v_obs)
    if n_sun > 0 and n_obs > 0:
        beta = np.arccos(np.clip(np.dot(v_sun, v_obs) / (n_sun * n_obs), -1.0, 1.0))
        phi = (np.sin(beta) + (np.pi - beta) * np.cos(beta)) / np.pi
        m_std = -1.8 if "ISS" in satellite_name else 0.0
        return float(m_std + 5 * np.log10(distance_km / 1000.0) - 2.5 * np.log10(max(phi, 1e-9)))
    return 5.0


def find_greatest_elongations(observer, start_date, end_date):
    """Finds greatest elongations for Mercury and Venus."""
    ts, eph = get_timescale(), get_ephemeris()
    sun, earth = eph["sun"], eph["earth"]
    t0, t1 = ts.utc(start_date), ts.utc(end_date)
    events = []
    for p_name in ["mercury", "venus"]:
        planet = planetary.get_skyfield_obj(p_name)
        def elongation(t): return earth.at(t).observe(sun).separation_from(earth.at(t).observe(planet)).degrees
        setattr(elongation, "step_days", 2.0)
        times, separations = find_maxima(t0, t1, elongation)
        for t, sep in zip(cast(Any, times), separations):
            s_lon = cast(Any, earth).at(t).observe(sun).apparent().ecliptic_latlon()[1].degrees
            p_lon = cast(Any, earth).at(t).observe(planet).apparent().ecliptic_latlon()[1].degrees
            direction = "Eastern" if ((p_lon - s_lon + 180) % 360 - 180) > 0 else "Western"
            events.append({"date": t.utc_datetime(), "event": f"{planetary.get_simple_name(p_name)} Greatest {direction} Elongation", "object": planetary.get_simple_name(p_name), "type": "Greatest Elongation", "separation_degrees": float(sep), "direction": direction})
    return events


def find_saturn_ring_crossings(start_date, end_date):
    """Finds when Earth or the Sun crosses Saturn's ring plane."""
    ts, eph = get_timescale(), get_ephemeris()
    t0, t1 = ts.utc(start_date), ts.utc(end_date)
    earth, sun, saturn = eph["earth"], eph["sun"], eph["saturn barycenter"]
    def get_tilt(t, observer_obj):
        v_sat_obs = -observer_obj.at(t).observe(saturn).position.au / observer_obj.at(t).observe(saturn).distance().au
        a_p, d_p = planetary.get_saturn_pole(t)
        p = np.array([np.cos(np.radians(d_p))*np.cos(np.radians(a_p)), np.cos(np.radians(d_p))*np.sin(np.radians(a_p)), np.sin(np.radians(d_p))])
        return np.sum(p * v_sat_obs, axis=0) if hasattr(t, "shape") and t.shape != () else np.dot(p, v_sat_obs)
    events = []
    for obs, name in [(earth, "Earth"), (sun, "Sun")]:
        def state(t): return (get_tilt(t, obs) > 0).astype(int)
        setattr(state, "step_days", 30.0)
        t_c, _ = almanac.find_discrete(t0, t1, state)
        for ti in t_c: events.append({"date": ti.utc_datetime(), "event": f"Saturn Ring Plane Crossing ({name})", "type": "Saturn Ring Crossing"})
    return events


def find_moon_apogee_perigee(start_date, end_date):
    """Finds Moon apogee and perigee."""
    ts, eph = get_timescale(), get_ephemeris()
    t0, t1 = ts.utc(start_date), ts.utc(end_date)
    moon, earth = eph["moon"], eph["earth"]
    def dist(t): return earth.at(t).observe(moon).distance().km
    setattr(dist, "step_days", 13)
    ma, _ = find_maxima(t0, t1, dist)
    mi, _ = find_minima(t0, t1, dist)
    events = [{"date": t.utc_datetime(), "event": "Apogee", "object": "Moon"} for t in ma]
    events += [{"date": t.utc_datetime(), "event": "Perigee", "object": "Moon"} for t in mi]
    return events


def find_conjunctions(observer, p1_name, p2_name, start_date, end_date, threshold_degrees=None):
    """Finds conjunctions between two moving bodies."""
    ts = get_timescale()
    t0, t1 = ts.utc(start_date), ts.utc(end_date)
    p1, p2 = planetary.get_skyfield_obj(p1_name), planetary.get_skyfield_obj(p2_name)
    def separation(t): return observer.at(t).observe(p1).apparent().separation_from(observer.at(t).observe(p2).apparent()).degrees
    step = 0.05 if "moon" in [p1_name.lower(), p2_name.lower()] else (0.2 if any(p in [p1_name.lower(), p2_name.lower()] for p in ["mercury", "venus"]) else 0.5)
    setattr(separation, "step_days", step)
    times, separations = find_minima(t0, t1, separation)
    events = []
    for t, s in zip(times, separations):
        if threshold_degrees is None or s < threshold_degrees:
            rt, rs = _refine_conjunction(observer, p1, p2, t)
            events.append({"date": rt.utc_datetime(), "separation_degrees": float(rs)})
    return events


def find_oppositions(observer, planet_name, start_date, end_date):
    """Finds when a planet is in opposition."""
    ts, sun = get_timescale(), planetary.get_skyfield_obj("sun")
    t0, t1 = ts.utc(start_date), ts.utc(end_date)
    planet = planetary.get_skyfield_obj(planet_name)
    def diff(t):
        p_lon = observer.at(t).observe(planet).apparent().ecliptic_latlon()[1].degrees
        s_lon = observer.at(t).observe(sun).apparent().ecliptic_latlon()[1].degrees
        return abs(abs((s_lon - p_lon + 180) % 360 - 180) - 180)
    setattr(diff, "step_days", 180)
    times, _ = find_minima(t0, t1, diff)
    return [{"date": t.utc_datetime(), "planet": planet_name} for t in times]


def find_mercury_inferior_conjunctions(observer, start_date, end_date, threshold_degrees=1.0):
    """Finds Mercury's inferior conjunctions and transits."""
    conjs = find_conjunctions(observer, "mercury", "sun", start_date, end_date, threshold_degrees)
    mercury, sun, ts = planetary.get_skyfield_obj("mercury"), planetary.get_skyfield_obj("sun"), get_timescale()
    inf_events = []
    for e in conjs:
        t = ts.from_datetime(e["date"])
        m_obs, s_obs = observer.at(t).observe(mercury), observer.at(t).observe(sun)
        if m_obs.distance().au < s_obs.distance().au:
            m_rad = np.degrees(np.arctan2(astronomy.MERCURY_RADIUS_KM/astronomy.AU_KM, m_obs.distance().au))
            s_rad = np.degrees(np.arctan2(astronomy.SUN_RADIUS_KM/astronomy.AU_KM, s_obs.distance().au))
            e["is_transit"] = e["separation_degrees"] < (m_rad + s_rad)
            inf_events.append(e)
    return inf_events


def find_conjunctions_with_star(observer, body1_name, star_object, start_date, end_date, threshold_degrees=1.0):
    """Finds conjunctions between a moving body and a single star."""
    events = find_conjunctions_with_stars(observer, body1_name, [("Target", star_object)], start_date, end_date, threshold_degrees)
    for e in events: e.pop("object2", None)
    return events


def find_conjunctions_with_stars(observer, body_name, star_data, start_date, end_date, threshold_degrees=1.0):
    """Finds conjunctions between a moving body and multiple stars (vectorized)."""
    if not star_data: return []
    ts, body = get_timescale(), planetary.get_skyfield_obj(body_name)
    t0, t1 = ts.utc(start_date), ts.utc(end_date)
    num_steps = int((t1 - t0) * 24 * 4) # 15-minute resolution
    if num_steps < 2: return []
    times = ts.linspace(t0, t1, num_steps)
    u_body = observer.at(times).observe(body).apparent().position.au
    u_body /= np.linalg.norm(u_body, axis=0)
    events = []
    for name, star_obj in star_data:
        u_star = observer.at(times).observe(star_obj).apparent().position.au
        u_star /= np.linalg.norm(u_star, axis=0)
        seps = np.degrees(np.arccos(np.clip(np.einsum('kj,kj->j', u_star, u_body), -1.0, 1.0)))
        mins = np.where((seps[1:-1] < seps[:-2]) & (seps[1:-1] < seps[2:]) & (seps[1:-1] < threshold_degrees))[0] + 1
        for idx in mins:
            rt, rs = _refine_conjunction(observer, body, star_obj, times[idx])
            events.append({"date": rt.utc_datetime(), "object2": name, "separation_degrees": float(rs)})
    return events


def find_conjunctions_between_moving_bodies(observer, body1_name, bodies2_data, start_date, end_date, threshold_degrees=1.0, precomputed_positions=None):
    """Finds conjunctions between a moving body and multiple other moving bodies (vectorized)."""
    if not bodies2_data: return []
    ts = get_timescale()
    t0, t1 = ts.utc(start_date), ts.utc(end_date)
    step = 0.01 if "moon" in [body1_name.lower()] + [n.lower() for n, _ in bodies2_data] else (0.1 if "mercury" in [body1_name.lower()] + [n.lower() for n, _ in bodies2_data] else 0.2)
    num_steps = max(2, int((t1 - t0) / step))
    times = ts.linspace(t0, t1, num_steps)
    body1 = planetary.get_skyfield_obj(body1_name)
    pos1 = precomputed_positions.get(body1_name.lower()) if precomputed_positions and body1_name.lower() in precomputed_positions else observer.at(times).observe(body1).apparent()
    if not hasattr(pos1, 't') or (hasattr(pos1.t, 'shape') and (len(pos1.t.shape)==0 or pos1.t.shape[0] != len(times))): pos1 = observer.at(times).observe(body1).apparent()
    events = []
    for name2, body2 in bodies2_data:
        pos2 = precomputed_positions.get(name2.lower()) if precomputed_positions and name2.lower() in precomputed_positions else observer.at(times).observe(body2).apparent()
        if not hasattr(pos2, 't') or (hasattr(pos2.t, 'shape') and (len(pos2.t.shape)==0 or pos2.t.shape[0] != len(times))): pos2 = observer.at(times).observe(body2).apparent()
        seps = pos1.separation_from(pos2).degrees
        mins = np.where((seps[1:-1] < seps[:-2]) & (seps[1:-1] < seps[2:]) & (seps[1:-1] < threshold_degrees))[0] + 1
        for idx in mins:
            rt, rs = _refine_conjunction(observer, body1, body2, times[idx])
            events.append({"date": rt.utc_datetime(), "object2": name2, "separation_degrees": float(rs)})
    return events


def find_lunar_occultations(observer, bright_stars, start_date, end_date):
    """Finds occultations of bright stars by the Moon (optimized filtering)."""
    ts, eph = get_timescale(), get_ephemeris()
    moon, earth = eph["moon"], eph["earth"]
    t0, t1 = ts.utc(start_date), ts.utc(end_date)
    targets = ["Sirius", "Arcturus", "Rigel", "Procyon", "Betelgeuse", "Altair", "Aldebaran", "Antares", "Spica", "Pollux", "Fomalhaut", "Regulus", "Adhara", "Bellatrix", "El Nath", "Alnilam", "Alnitak", "Wezen", "Alhena", "Mirzam", "Alphard", "Hamal", "Beta Tauri"]

    stars = bright_stars[bright_stars["Name"].str.strip().isin(targets)]
    # Efficient pre-filtering using ecliptic latitude (Moon is within ~5.3 deg)
    stars_vector = Star(ra_hours=np.array([s.ra.hours for s in stars["skyfield_object"]]), dec_degrees=np.array([s.dec.degrees for s in stars["skyfield_object"]]))
    lats, _, _ = earth.at(t0).observe(stars_vector).apparent().ecliptic_latlon()
    mask = np.abs(lats.degrees) < 10.0
    filtered_stars = stars[mask]

    events = []
    for _, row in filtered_stars.iterrows():
        star_obj, name = row["skyfield_object"], row["Name"]
        def is_occ(t):
            m, s = observer.at(t).observe(moon).apparent(), observer.at(t).observe(star_obj).apparent()
            alt, _, _ = m.altaz(temperature_C=10.0, pressure_mbar=1013.25)
            rad = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m.distance().km))
            return (m.separation_from(s).degrees < rad) & (alt.degrees > 0)
        setattr(is_occ, "step_days", 0.05)
        t_occ, _ = almanac.find_discrete(t0, t1, is_occ)
        for i in range(0, len(t_occ), 2):
            if i + 1 < len(t_occ):
                in_t, eg_t = t_occ[i], t_occ[i+1]
                mid_t = ts.from_datetime(in_t.utc_datetime() + (eg_t.utc_datetime()-in_t.utc_datetime())/2)
                rt, _ = _refine_conjunction(observer, moon, star_obj, mid_t)
                events.append({"date": rt.utc_datetime(), "object1": "Moon", "object2": name, "ingress_time": in_t.utc_datetime(), "egress_time": eg_t.utc_datetime(), "type": "Lunar Occultation", "event": "Lunar Occultation"})
    return events


def find_seasons(start_date, end_date):
    """Finds the start of seasons (equinoxes and solstices)."""
    ts, eph = get_timescale(), get_ephemeris()
    t_s, y_s = almanac.find_discrete(ts.utc(start_date), ts.utc(end_date), almanac.seasons(eph))
    return [{"date": ti.utc_datetime(), "event": almanac.SEASON_EVENTS[yi], "type": "Season"} for ti, yi in zip(t_s, y_s)]
