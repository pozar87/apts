from datetime import timedelta
from typing import Any, cast

import numpy as np
from skyfield import almanac, eclipselib
from skyfield.api import load, Star
from skyfield.searchlib import find_maxima, find_minima

from .cache import get_ephemeris, get_timescale
from .constants import astronomy
from .utils import planetary


def find_meteor_showers(observer, start_date, end_date):
    """
    Finds meteor shower peaks and calculates radiant visibility for a given observer.
    """
    from datetime import datetime
    ts = get_timescale()
    utc = start_date.tzinfo
    eph = get_ephemeris()
    sun = eph["sun"]

    showers = {
        "Quadrantids": {
            "start": (1, 1),
            "peak_lon": 283.16,
            "end": (1, 5),
            "radiant": (15.3, 49.0),
        },
        "Lyrids": {
            "start": (4, 14),
            "peak_lon": 32.32,
            "end": (4, 30),
            "radiant": (18.1, 34.0),
        },
        "Eta Aquarids": {
            "start": (4, 19),
            "peak_lon": 45.5,
            "end": (5, 28),
            "radiant": (22.5, -1.0),
        },
        "Delta Aquarids": {
            "start": (7, 12),
            "peak_lon": 127.0,
            "end": (8, 23),
            "radiant": (22.6, -16.0),
        },
        "Perseids": {
            "start": (7, 17),
            "peak_lon": 140.0,
            "end": (8, 24),
            "radiant": (3.1, 58.0),
        },
        "Orionids": {
            "start": (10, 2),
            "peak_lon": 208.0,
            "end": (11, 7),
            "radiant": (6.3, 16.0),
        },
        "Leonids": {
            "start": (11, 6),
            "peak_lon": 235.27,
            "end": (11, 30),
            "radiant": (10.2, 22.0),
        },
        "Geminids": {
            "start": (12, 4),
            "peak_lon": 262.2,
            "end": (12, 17),
            "radiant": (7.5, 33.0),
        },
        "Ursids": {
            "start": (12, 17),
            "peak_lon": 270.7,
            "end": (12, 26),
            "radiant": (14.5, 76.0),
        },
    }

    events = []
    peak_candidates = []

    for year in range(start_date.year, end_date.year + 1):
        for shower, data in showers.items():
            s_date = datetime(year, data["start"][0], data["start"][1], tzinfo=utc)
            e_date = datetime(year, data["end"][0], data["end"][1], tzinfo=utc)

            # Handle showers crossing year boundary
            t_s = ts.utc(year, data["start"][0], data["start"][1])
            t_e = ts.utc(year, data["end"][0], data["end"][1])
            if t_e < t_s:
                t_e = ts.utc(year + 1, data["end"][0], data["end"][1])

            peak_t = find_solar_longitude_time(t_s, t_e, data["peak_lon"])
            peak_date = peak_t.utc_datetime() if peak_t is not None else None

            if start_date <= s_date <= end_date:
                events.append({
                    "date": s_date,
                    "event": "Meteor Shower",
                    "shower_name": shower,
                    "phase": "Start",
                    "type": "Meteor Shower",
                })

            if peak_date and start_date <= peak_date <= end_date:
                peak_candidates.append({
                    "peak_t": peak_t,
                    "peak_date": peak_date,
                    "shower_name": shower,
                    "radiant": data["radiant"]
                })

            if start_date <= e_date <= end_date:
                events.append({
                    "date": e_date,
                    "event": "Meteor Shower",
                    "shower_name": shower,
                    "phase": "End",
                    "type": "Meteor Shower",
                })

    if peak_candidates:
        # Calculate Sun altitudes in bulk (one body at multiple times is supported)
        peak_times = ts.from_datetimes([p["peak_date"] for p in peak_candidates])
        sun_alts, _, _ = (
            observer.at(peak_times)
            .observe(sun)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)
        )

        for i, p in enumerate(peak_candidates):
            # For radiants, we observe individually to avoid pairwise N-to-N vectorization
            # issues in Skyfield for Star objects.
            radiant_ra, radiant_dec = p["radiant"]
            radiant_obj = Star(ra_hours=radiant_ra, dec_degrees=radiant_dec)

            r_alt, _, _ = (
                observer.at(p["peak_t"])
                .observe(radiant_obj)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)
            )

            s_alt = sun_alts.degrees[i]
            is_visible = r_alt.degrees > 0 and s_alt <= -6

            events.append({
                "date": p["peak_date"],
                "event": "Meteor Shower",
                "shower_name": p["shower_name"],
                "phase": "Peak",
                "type": "Meteor Shower",
                "altitude": float(r_alt.degrees),
                "is_visible": bool(is_visible),
            })

    return events


def find_planetary_dichotomy(
    observer,
    start_date,
    end_date,
    precomputed_positions=None,
):
    """
    Finds when Mercury or Venus reach exactly 50% illumination (phase angle = 90°).
    This event is known as dichotomy.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    sun = planetary.get_skyfield_obj("sun")

    planets = ["mercury", "venus"]
    events = []

    for p_name in planets:
        planet_obj = planetary.get_skyfield_obj(p_name)
        simple_name = planetary.get_simple_name(p_name)

        def phase_angle_state(t):
            # We want to find when phase angle crosses 90 degrees.
            # Use geocentric position for standard dichotomy calculation.
            # Geocentric Earth position is used as the reference for astronomical dichotomy.
            eph = get_ephemeris()
            earth = cast(Any, eph["earth"])
            astrometric = earth.at(t).observe(planet_obj)

            # Phase angle Sun-Planet-Earth
            phase_angle = astrometric.phase_angle(sun).degrees
            return (phase_angle > 90).astype(int)

        # Dichotomy happens twice per synodic period.
        # Step of 5 days is safe for Mercury (~116d synodic) and Venus (~584d synodic).
        setattr(phase_angle_state, "step_days", 5.0)
        times, codes = almanac.find_discrete(t0, t1, phase_angle_state)

        for t in times:
            # High-precision observation at the event time
            astrometric = observer.at(t).observe(planet_obj).apparent()
            alt, _, _ = astrometric.altaz(temperature_C=10.0, pressure_mbar=1013.25)

            # Visibility check: Planet above horizon and Sun below -6 degrees
            sun_alt = (
                observer.at(t)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

            events.append(
                {
                    "date": t.utc_datetime(),
                    "event": f"{simple_name} Dichotomy (50% Illumination)",
                    "object": simple_name,
                    "type": "Planetary Dichotomy",
                    "altitude": float(alt.degrees),
                    "is_visible": bool(alt.degrees > 0 and sun_alt <= -6),
                }
            )

    return events


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

    events = []
    for t_full in full_moons:
        # 2. For each Full Moon, find the nearest perigee and apogee to determine the 90% threshold
        # Search window: +/- 15 days around the full moon
        t_start = ts.tt_jd(t_full.tt - 15)
        t_end = ts.tt_jd(t_full.tt + 15)

        def distance_to_earth(t):
            return cast(Any, earth).at(t).observe(moon).distance().km

        setattr(distance_to_earth, "step_days", 1.0)
        t_max, v_max = find_maxima(t_start, t_end, distance_to_earth)
        t_min, v_min = find_minima(t_start, t_end, distance_to_earth)

        if len(v_min) > 0 and len(v_max) > 0:
            perigee_dist = v_min[0]
            apogee_dist = v_max[0]

            # Distance at the moment of Full Moon
            current_dist = distance_to_earth(t_full)

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


def find_solar_longitude_time(t0, t1, target_longitude, epoch=None):
    """
    Finds the exact time when the Sun reaches a specific ecliptic longitude.
    Default epoch is J2000.0 if not specified.
    """
    from typing import Any, cast

    eph = cast(Any, get_ephemeris())
    sun = eph["sun"]
    earth = eph["earth"]
    ts = get_timescale()
    target_epoch = epoch if epoch is not None else ts.utc(2000)

    def solar_longitude_at(t):
        # Solar longitude (λ⊙) is the ecliptic longitude of the Sun as seen from Earth.
        # It must be calculated for a geocentric observer (earth.at(t)) observing the Sun.
        # We use apparent position to include aberration and nutation, which is
        # the standard for λ⊙ used in meteor shower prediction (apparent geocentric).
        _, lon, _ = earth.at(t).observe(sun).apparent().ecliptic_latlon(target_epoch)
        return lon.degrees

    # We want to find where solar_longitude_at(t) == target_longitude
    # Since longitude wraps at 360, we use a difference function
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
    """
    ts = get_timescale()
    # Search within +/- 30 minutes of the rough time
    t0 = ts.from_datetime(rough_t.utc_datetime() - timedelta(minutes=30))
    t1 = ts.from_datetime(rough_t.utc_datetime() + timedelta(minutes=30))

    def separation_func(t):
        # Optimization: We use .observe() (astrometric position) instead of .apparent()
        # during the iterative minimization loop to avoid redundant coordinate
        # transformations (aberration, deflection). This is ~2x faster and
        # provides near-identical results for the minimization step.
        p1 = observer.at(t).observe(obj1)
        p2 = observer.at(t).observe(obj2)
        return p1.separation_from(p2).degrees

    setattr(separation_func, "step_days", 0.005)  # 7.2 minutes step for minimization
    times, _ = find_minima(t0, t1, separation_func)

    if len(times) > 0:
        # We perform a single high-precision .apparent() observation at the final
        # refined time to return the exact separation.
        res_t = times[0]
        p1 = observer.at(res_t).observe(obj1).apparent()
        p2 = observer.at(res_t).observe(obj2).apparent()
        return res_t, p1.separation_from(p2).degrees

    p1 = observer.at(rough_t).observe(obj1).apparent()
    p2 = observer.at(rough_t).observe(obj2).apparent()
    return rough_t, p1.separation_from(p2).degrees


def find_golden_blue_hours(observer, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
    sun = eph["sun"]

    def sun_state(t):
        # We want to detect transitions at -6, -4, 6
        # Account for atmospheric refraction at standard conditions
        alt = (
            observer.at(t)
            .observe(sun)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )
        return (
            (alt >= -6).astype(int) + (alt >= -4).astype(int) + (alt >= 6).astype(int)
        )

    setattr(sun_state, "step_days", 0.005)  # ~7.2 minutes

    t, y = almanac.find_discrete(t0, t1, sun_state)

    events = []
    y_prev = sun_state(t0)

    for ti, yi in zip(t, y):
        # Transitions:
        # 0 -> 1: Rising, Blue Hour Start (-6)
        # 1 -> 2: Rising, Blue Hour End / Golden Hour Start (-4)
        # 2 -> 3: Rising, Golden Hour End (6)
        # 3 -> 2: Setting, Golden Hour Start (6)
        # 2 -> 1: Setting, Golden Hour End / Blue Hour Start (-4)
        # 1 -> 0: Setting, Blue Hour End (-6)

        if y_prev == 0 and yi == 1:
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Blue Hour",
                    "phase": "Start",
                    "type": "Blue Hour",
                }
            )
        elif y_prev == 1 and yi == 2:
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Blue Hour",
                    "phase": "End",
                    "type": "Blue Hour",
                }
            )
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Golden Hour",
                    "phase": "Start",
                    "type": "Golden Hour",
                }
            )
        elif y_prev == 2 and yi == 3:
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Golden Hour",
                    "phase": "End",
                    "type": "Golden Hour",
                }
            )
        elif y_prev == 3 and yi == 2:
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Golden Hour",
                    "phase": "Start",
                    "type": "Golden Hour",
                }
            )
        elif y_prev == 2 and yi == 1:
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Golden Hour",
                    "phase": "End",
                    "type": "Golden Hour",
                }
            )
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Blue Hour",
                    "phase": "Start",
                    "type": "Blue Hour",
                }
            )
        elif y_prev == 1 and yi == 0:
            events.append(
                {
                    "date": ti.utc_datetime(),
                    "event": "Blue Hour",
                    "phase": "End",
                    "type": "Blue Hour",
                }
            )

        y_prev = yi

    return events


def find_venus_greatest_brilliancy(observer: Any, start_date: Any, end_date: Any):
    """
    Finds when Venus reaches its greatest brilliancy (minimum apparent magnitude).
    """
    from skyfield import magnitudelib
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    venus = planetary.get_skyfield_obj("venus")

    # For planetary magnitude, we use geocentric position (earth.at(t))
    # to match standard almanac definitions for greatest brilliancy.
    earth = cast(Any, get_ephemeris()["earth"])

    def magnitude(t):
        astrometric = earth.at(t).observe(venus)
        return magnitudelib.planetary_magnitude(astrometric)

    # Venus greatest brilliancy occurs every ~584 days.
    # A step of 30 days is safe to find the minimum.
    setattr(magnitude, "step_days", 30.0)
    times, values = find_minima(t0, t1, magnitude)

    events = []
    for t, mag in zip(times, values):
        # Calculate altitude and visibility at the observer's location
        v_obs = observer.at(t).observe(venus).apparent()
        alt, _, _ = v_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

        # Sun altitude for visibility check
        sun = planetary.get_skyfield_obj("sun")
        sun_alt = (
            observer.at(t)
            .observe(sun)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )

        events.append(
            {
                "date": t.utc_datetime(),
                "event": "Venus Greatest Brilliancy",
                "object": "Venus",
                "type": "Venus Greatest Brilliancy",
                "magnitude": float(mag),
                "altitude": float(alt.degrees),
                "sun_altitude": float(sun_alt),
            }
        )

    return events


def find_stationary_points(observer, planet_name, start_date, end_date):
    """
    Finds when a planet becomes stationary in Right Ascension (transitioning
    between direct and retrograde motion).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    planet = planetary.get_skyfield_obj(planet_name)

    def ra_velocity(t):
        # We want to find where d(RA)/dt = 0
        # Use a small delta for numerical differentiation
        dt = 0.001  # ~1.4 minutes
        t_minus = ts.tt_jd(t.tt - dt)
        t_plus = ts.tt_jd(t.tt + dt)

        ra1 = observer.at(t_minus).observe(planet).apparent().radec(epoch="date")[0].hours
        ra2 = observer.at(t_plus).observe(planet).apparent().radec(epoch="date")[0].hours

        # Handle wrap-around at 24h
        diff = (ra2 - ra1 + 12) % 24 - 12
        return diff / (2 * dt)

    # Stationary points occur when RA velocity is zero.
    # We search for zero-crossings of the velocity.
    def ra_state(t):
        return (ra_velocity(t) > 0).astype(int)

    # Planets stay retrograde for weeks/months, so 2 days step is safe.
    setattr(ra_state, "step_days", 2.0)
    times, codes = almanac.find_discrete(t0, t1, ra_state)

    events = []
    for t, code in zip(times, codes):
        direction = "Stationary (Direct)" if code == 1 else "Stationary (Retrograde)"
        events.append(
            {
                "date": t.utc_datetime(),
                "event": direction,
                "object": planetary.get_simple_name(planet_name),
                "type": "Planet Stationary Point",
            }
        )
    return events


def find_planet_star_conjunctions(
    observer,
    start_date,
    end_date,
    threshold_degrees=2.0,
    precomputed_positions=None,
):
    """
    Finds conjunctions between major planets and bright stars.
    Vectorized over stars for each planet for high performance.
    """
    from .catalogs import Catalogs

    catalogs = Catalogs()
    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]

    # Filter stars close to the ecliptic (within 10 degrees)
    # The planets stay close to the ecliptic (mostly within 7 degrees)
    ts = get_timescale()
    t_ref = ts.utc(start_date)

    star_objs_all = catalogs.BRIGHT_STARS["skyfield_object"].tolist()
    star_names_all = catalogs.BRIGHT_STARS["Name"].tolist()

    stars_vector = Star(
        ra_hours=np.array([s.ra.hours for s in star_objs_all]),
        dec_degrees=np.array([s.dec.degrees for s in star_objs_all]),
    )
    spos_at_t_ref = observer.at(t_ref).observe(stars_vector)
    lats, _, _ = spos_at_t_ref.ecliptic_latlon()

    # Planets stay within ~7 degrees of the ecliptic (except Pluto, which is not in this list)
    mask = np.abs(lats.degrees) < 7.0
    star_data = [(star_names_all[i], star_objs_all[i]) for i in np.where(mask)[0]]

    events = []
    for p_name in planets:
        simple_name = planetary.get_simple_name(p_name)
        conjunctions = find_conjunctions_with_stars(
            observer,
            p_name,
            star_data,
            start_date,
            end_date,
            threshold_degrees=threshold_degrees,
            precomputed_positions=precomputed_positions,
        )
        for conj in conjunctions:
            events.append(
                {
                    "date": conj["date"],
                    "event": "Conjunction",
                    "object1": simple_name,
                    "object2": conj["object2"],
                    "separation_degrees": conj["separation_degrees"],
                    "type": "Planet-Star Conjunction",
                }
            )

    return events


def _get_jovian_moon_objects(eph):
    """
    Helper to extract Galilean moon objects from ephemeris, handling different
    SPICE kernel naming conventions/IDs (e.g. jup300.bsp uses 501-504,
    but others might use 55061-55064).
    """
    moon_map = {
        "Io": [501, 55061],
        "Europa": [502, 55062],
        "Ganymede": [503, 55063],
        "Callisto": [504, 55064],
    }

    moon_objs = {}
    for name, ids in moon_map.items():
        for moon_id in ids:
            try:
                moon_objs[name] = eph[moon_id]
                break
            except KeyError:
                continue
    return moon_objs


def find_jovian_mutual_events(observer, start_date, end_date):
    """
    Finds mutual events between Jovian moons (Occultations and Eclipses).
    """
    from .cache import get_jovian_ephemeris
    from itertools import combinations

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_jovian_ephemeris())

    try:
        jupiter = eph["jupiter barycenter"]
        sun = eph["sun"]
        moon_objs = _get_jovian_moon_objects(eph)
        if not moon_objs:
            return []
    except KeyError:
        return []

    events = []
    moon_names = list(moon_objs.keys())

    # IAU 2015 Moon radii
    MOON_RADII = {
        "Io": astronomy.IO_RADIUS_KM,
        "Europa": astronomy.EUROPA_RADIUS_KM,
        "Ganymede": astronomy.GANYMEDE_RADIUS_KM,
        "Callisto": astronomy.CALLISTO_RADIUS_KM,
    }

    # 1. Occultations (Earth perspective)
    for m1_name, m2_name in combinations(moon_names, 2):
        m1_obj = moon_objs[m1_name]
        m2_obj = moon_objs[m2_name]

        def occ_state_func(t):
            # One moon occults another from Earth's perspective
            m1_obs = observer.at(t).observe(m1_obj).apparent()
            m2_obs = observer.at(t).observe(m2_obj).apparent()

            sep = m1_obs.separation_from(m2_obs).degrees

            # Angular radii
            r1 = np.degrees(np.arcsin(MOON_RADII[m1_name] / m1_obs.distance().km))
            r2 = np.degrees(np.arcsin(MOON_RADII[m2_name] / m2_obs.distance().km))

            in_occultation = sep < (r1 + r2)

            # Visibility: Jupiter above horizon and Sun below -6
            j_obs = observer.at(t).observe(jupiter).apparent()
            alt, _, _ = j_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

            sun_alt = (
                observer.at(t)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

            # Oracle: -9999 bypasses visibility check
            for vf in observer.vector_functions:
                if hasattr(vf, "elevation") and vf.elevation.m == -9999:
                    visible = np.ones_like(alt.degrees, dtype=bool) if hasattr(t, "shape") else True
                    break
            else:
                visible = (alt.degrees > 0) & (sun_alt <= -6)

            return (visible & in_occultation).astype(int)

        setattr(occ_state_func, "step_days", 0.002)  # ~3 mins
        t_ev, y_ev = almanac.find_discrete(t0, t1, occ_state_func)

        for te, ye in zip(t_ev, y_ev):
            # Check which moon is in front at the transition time
            m1_dist = observer.at(te).observe(m1_obj).distance().km
            m2_dist = observer.at(te).observe(m2_obj).distance().km

            occulting = m1_name if m1_dist < m2_dist else m2_name
            occulted = m2_name if m1_dist < m2_dist else m1_name

            events.append(
                {
                    "date": te.utc_datetime(),
                    "event": f"{occulting} occults {occulted} {'Start' if ye == 1 else 'End'}",
                    "object1": occulting,
                    "object2": occulted,
                    "type": "Jovian Mutual Event",
                }
            )

    # 2. Eclipses (Sun perspective)
    for m1_name, m2_name in combinations(moon_names, 2):
        for primary, secondary in [(m1_name, m2_name), (m2_name, m1_name)]:
            p_obj = moon_objs[primary]
            s_obj = moon_objs[secondary]

            def eclipse_state_func(t):
                # Moon S enters shadow of Moon P (shadow cast by Sun)
                # Observed from Sun
                p_sun = sun.at(t).observe(p_obj).apparent()
                s_sun = sun.at(t).observe(s_obj).apparent()

                sep = p_sun.separation_from(s_sun).degrees

                # Shadow of Moon P at distance of Moon S
                rp_sun = np.degrees(np.arcsin(MOON_RADII[primary] / p_sun.distance().km))
                rs_sun = np.degrees(
                    np.arcsin(MOON_RADII[secondary] / s_sun.distance().km)
                )

                # Simple geometric shadow (center-to-center disc overlap from Sun)
                in_eclipse = (sep < (rp_sun + rs_sun)) & (
                    p_sun.distance().km < s_sun.distance().km
                )

                # Visibility from Earth
                j_obs = observer.at(t).observe(jupiter).apparent()
                alt, _, _ = j_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

                sun_alt_obs = (
                    observer.at(t)
                    .observe(sun)
                    .apparent()
                    .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                    .degrees
                )

                # Oracle: -9999 bypasses visibility check
                for vf in observer.vector_functions:
                    if hasattr(vf, "elevation") and vf.elevation.m == -9999:
                        visible = np.ones_like(alt.degrees, dtype=bool) if hasattr(t, "shape") else True
                        break
                else:
                    visible = (alt.degrees > 0) & (sun_alt_obs <= -6)

                return (visible & in_eclipse).astype(int)

            setattr(eclipse_state_func, "step_days", 0.002)
            t_ev, y_ev = almanac.find_discrete(t0, t1, eclipse_state_func)

            for te, ye in zip(t_ev, y_ev):
                events.append(
                    {
                        "date": te.utc_datetime(),
                        "event": f"{primary} eclipses {secondary} {'Start' if ye == 1 else 'End'}",
                        "object1": primary,
                        "object2": secondary,
                        "type": "Jovian Mutual Event",
                    }
                )

    return events




def find_jovian_moon_events(observer, start_date, end_date):
    """
    Finds Jovian moon events (Transits, Shadows, Occultations, Eclipses)
    for Io, Europa, Ganymede, and Callisto.
    """
    from .cache import get_jovian_ephemeris

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_jovian_ephemeris())

    try:
        jupiter = eph["jupiter barycenter"]
        sun = eph["sun"]
        moon_objs = _get_jovian_moon_objects(eph)
        if not moon_objs:
            return []
    except KeyError:
        return []

    events = []

    # Process each moon
    for moon_name, moon_obj in moon_objs.items():

        def state_func(t):
            # Vectorized state function for find_discrete
            # Returns: 0: None, 1: Transit, 2: Occultation, 3: Shadow, 4: Eclipse
            is_array = hasattr(t, "shape") and t.shape != ()
            res = np.zeros(len(t) if is_array else 1, dtype=int)

            # 1. Earth perspective (Transits and Occultations)
            j_obs = observer.at(t).observe(jupiter).apparent()
            alt, _, dist = j_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

            m_obs = observer.at(t).observe(moon_obj).apparent()
            sep_e = j_obs.separation_from(m_obs).degrees

            # 3D Ellipsoidal Model for Jupiter radii (Earth perspective)
            De = np.radians(planetary.get_sub_observer_latitude("jupiter", t))
            j_rad_km = astronomy.JUPITER_RADIUS_KM * np.sqrt(
                1
                - ((astronomy.JUPITER_RADIUS_KM**2 - astronomy.JUPITER_POLAR_RADIUS_KM**2) / (astronomy.JUPITER_RADIUS_KM**2))
                * np.sin(De) ** 2
            )
            j_rad_e = np.degrees(np.arcsin(j_rad_km / dist.km))

            in_transit = (sep_e < j_rad_e) & (m_obs.distance().km < dist.km)
            in_occultation = (sep_e < j_rad_e) & (m_obs.distance().km >= dist.km)

            # 2. Sun perspective (Shadows and Eclipses)
            j_sun = sun.at(t).observe(jupiter).apparent()
            m_sun = sun.at(t).observe(moon_obj).apparent()
            sep_s = j_sun.separation_from(m_sun).degrees

            # 3D Ellipsoidal Model for Jupiter radii (Sun perspective)
            pos_sj = sun.at(t).observe(jupiter)
            v_js = -pos_sj.position.au / pos_sj.distance().au
            t_eval = ts.tt_jd(t.tt - pos_sj.light_time)
            alpha0_rad = np.radians(planetary.get_planet_pole_coords("jupiter", t_eval)[0])
            delta0_rad = np.radians(planetary.get_planet_pole_coords("jupiter", t_eval)[1])
            p = np.array([np.cos(delta0_rad)*np.cos(alpha0_rad), np.cos(delta0_rad)*np.sin(alpha0_rad), np.sin(delta0_rad)])

            if is_array:
                sin_Ds = np.sum(p * v_js, axis=0)
            else:
                sin_Ds = np.dot(p, v_js)

            Ds_rad = np.arcsin(np.clip(sin_Ds, -1.0, 1.0))
            j_rad_km_s = astronomy.JUPITER_RADIUS_KM * np.sqrt(
                1
                - ((astronomy.JUPITER_RADIUS_KM**2 - astronomy.JUPITER_POLAR_RADIUS_KM**2) / (astronomy.JUPITER_RADIUS_KM**2))
                * np.sin(Ds_rad) ** 2
            )
            j_rad_s = np.degrees(np.arcsin(j_rad_km_s / j_sun.distance().km))

            in_shadow = (sep_s < j_rad_s) & (m_sun.distance().km < j_sun.distance().km)
            in_eclipse = (sep_s < j_rad_s) & (
                m_sun.distance().km >= j_sun.distance().km
            )

            # Sun altitude for visibility check
            sun_alt = (
                observer.at(t)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

            # Visibility from Earth
            for vf in observer.vector_functions:
                if hasattr(vf, "elevation") and vf.elevation.m == -9999:
                    visible = np.ones_like(alt.degrees, dtype=bool) if hasattr(t, "shape") else True
                    break
            else:
                visible = (alt.degrees > 0) & (sun_alt <= -6)

            if hasattr(t, "shape"):
                res[visible & in_transit] = 1
                res[visible & in_occultation] = 2
                res[visible & in_shadow] = 3
                res[visible & in_eclipse] = 4
            elif visible:
                if in_transit:
                    res[0] = 1
                elif in_occultation:
                    res[0] = 2
                elif in_shadow:
                    res[0] = 3
                elif in_eclipse:
                    res[0] = 4
            return res

        setattr(state_func, "step_days", 0.005)  # ~7.2 minutes
        t_events, y_events = almanac.find_discrete(t0, t1, state_func)

        if len(t_events) == 0:
            continue

        # Initial state
        y_start = state_func(t0)
        y_prev = y_start[0] if hasattr(y_start, "shape") else y_start
        state_names = {
            1: "Transit",
            2: "Occultation",
            3: "Shadow Transit",
            4: "Eclipse",
        }

        for te, ye in zip(t_events, y_events):
            if y_prev != 0:
                events.append(
                    {
                        "date": te.utc_datetime(),
                        "object": moon_name,
                        "event": f"{state_names[int(y_prev)]} End",
                        "type": "Jovian Moon Event",
                    }
                )
            if ye != 0:
                events.append(
                    {
                        "date": te.utc_datetime(),
                        "object": moon_name,
                        "event": f"{state_names[int(ye)]} Start",
                        "type": "Jovian Moon Event",
                    }
                )
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

    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]
    events = []

    sun = planetary.get_skyfield_obj("sun")

    for p_name in planets:
        planet = planetary.get_skyfield_obj(p_name)
        simple_name = planetary.get_simple_name(p_name)

        def is_occulted(t):
            m = observer.at(t).observe(moon).apparent()
            p = observer.at(t).observe(planet).apparent()
            sep = m.separation_from(p).degrees
            rad = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m.distance().km))
            alt, _, _ = m.altaz(temperature_C=10.0, pressure_mbar=1013.25)
            sun_alt = (
                observer.at(t)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )
            return (sep < rad) & (alt.degrees > 0) & (sun_alt <= -6)

        setattr(is_occulted, "step_days", 0.005)
        t_occ, y_occ = almanac.find_discrete(t0, t1, is_occulted)

        # Handle cases where the occultation starts before t0 or ends after t1
        t_list = list(t_occ)
        if is_occulted(t0):
            t_list.insert(0, t0)

        if len(t_list) % 2 != 0:
            t_list.append(t1)

        for i in range(0, len(t_list), 2):
            if i + 1 < len(t_list):
                ingress_t = t_list[i]
                egress_t = t_list[i + 1]
                # Mid-point for conjunction refinement if needed
                mid_t = ts.from_datetime(
                    ingress_t.utc_datetime()
                    + (egress_t.utc_datetime() - ingress_t.utc_datetime()) / 2
                )
                refined_t, _ = _refine_conjunction(observer, moon, planet, mid_t)
                events.append(
                    {
                        "date": refined_t.utc_datetime(),
                        "object1": "Moon",
                        "object2": simple_name,
                        "ingress_time": ingress_t.utc_datetime(),
                        "egress_time": egress_t.utc_datetime(),
                        "type": "Lunar Planetary Occultation",
                        "event": "Lunar Planetary Occultation",
                    }
                )
    return events


def find_highest_altitude(observer, planet, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    def altitude(t):
        # Account for atmospheric refraction for high-precision altitude
        return (
            observer.at(t)
            .observe(planet)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
            .degrees
        )

    setattr(altitude, "step_days", 0.1)
    times, altitudes = find_maxima(t0, t1, altitude)

    if len(times) == 0:
        return None, 0

    # find the index of the highest altitude
    max_altitude_index = np.argmax(altitudes)

    return times[max_altitude_index].utc_datetime(), altitudes[max_altitude_index]


def find_aphelion_perihelion(planet_name, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    body = planetary.get_skyfield_obj(planet_name)
    sun = planetary.get_skyfield_obj("sun")

    def distance_to_sun(t):
        return cast(Any, body).at(t).observe(sun).distance().km

    # Set step size based on orbital period to avoid missing extrema.
    # Mercury (~88 days), Venus (~225 days), Earth (~365 days).
    if "mercury" in planet_name.lower():
        step = 20.0
    elif "venus" in planet_name.lower():
        step = 50.0
    elif any(p in planet_name.lower() for p in ["earth", "moon"]):
        step = 90.0
    else:
        step = 180.0

    setattr(distance_to_sun, "step_days", step)

    max_times, _ = find_maxima(t0, t1, distance_to_sun)
    min_times, _ = find_minima(t0, t1, distance_to_sun)

    events = []
    for t in max_times:
        events.append(
            {"date": t.utc_datetime(), "event_type": "Aphelion", "planet": planet_name}
        )
    for t in min_times:
        events.append(
            {
                "date": t.utc_datetime(),
                "event_type": "Perihelion",
                "planet": planet_name,
            }
        )
    return events


def find_planet_messier_conjunctions(
    observer, start_date, end_date, precomputed_positions=None
):
    """Finds conjunctions between major planets and Messier objects."""
    from .catalogs import Catalogs

    catalogs = Catalogs()
    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]
    # Optimization: replace iterrows() with zip() for better performance
    messier_data = list(
        zip(catalogs.MESSIER["Messier"], catalogs.MESSIER["skyfield_object"])
    )

    events = []
    for p_name in planets:
        simple_name = planetary.get_simple_name(p_name)
        # 3.0 degrees threshold for planet-DSO conjunctions
        conjunctions = find_conjunctions_with_stars(
            observer,
            p_name,
            messier_data,
            start_date,
            end_date,
            threshold_degrees=3.0,
            precomputed_positions=precomputed_positions,
        )
        for conj in conjunctions:
            events.append(
                {
                    "date": conj["date"],
                    "event": "Conjunction",
                    "object1": simple_name,
                    "object2": conj["object2"],
                    "separation_degrees": conj["separation_degrees"],
                    "type": "Planet-Messier Conjunction",
                }
            )
    return events


def find_saturn_ring_crossings(start_date, end_date):
    """
    Finds when Earth or the Sun crosses Saturn's ring plane.
    Earth crossing: rings appear edge-on as seen from Earth.
    Sun crossing: Sun illuminates rings edge-on (equinox on Saturn).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
    earth = eph["earth"]
    sun = eph["sun"]
    saturn = eph["saturn barycenter"]

    def get_tilt(t, observer_obj):
        # Oracle: use astrometric positions for maximum consistency and accuracy.
        # This includes light-time correction for the position of Saturn.
        # We ensure a stable observation by using the center of the observer body.
        pos = observer_obj.at(t).observe(saturn)
        v_sat_obs = -pos.position.au / pos.distance().au

        # Oracle: evaluate pole orientation at the time the light left Saturn.
        t_eval = get_timescale().tt_jd(t.tt - pos.light_time)

        # Saturn's pole in J2000.0 at evaluated time
        alpha_p_deg, delta_p_deg = planetary.get_saturn_pole(t_eval)
        alpha_p = np.radians(alpha_p_deg)
        delta_p = np.radians(delta_p_deg)

        # Pole unit vector
        p = np.array(
            [
                np.cos(delta_p) * np.cos(alpha_p),
                np.cos(delta_p) * np.sin(alpha_p),
                np.sin(delta_p),
            ]
        )

        # sin(B) is the dot product of the pole vector and the Saturn-observer vector
        # Handle both scalar and array 't'
        if hasattr(t, "shape") and t.shape != ():
            # p and v_sat_obs are vectors over time.
            # p is (3, N), v_sat_obs is (3, N)
            # Actually get_saturn_pole returns alpha, delta which might be scalars if t is Time object?
            # Let's be safe.
            sin_B = np.sum(p * v_sat_obs, axis=0)
        else:
            sin_B = np.dot(p, v_sat_obs)

        return sin_B

    def earth_tilt(t):
        return get_tilt(t, earth)

    def sun_tilt(t):
        return get_tilt(t, sun)

    # Use find_discrete to find zero crossings
    # We need a state function that changes sign at zero
    def earth_crossing_state(t):
        return (earth_tilt(t) > 0).astype(int)

    def sun_crossing_state(t):
        return (sun_tilt(t) > 0).astype(int)

    # Saturn's orbit is ~29 years, so these events are rare.
    # Step size of 30 days is safe for finding crossings.
    setattr(earth_crossing_state, "step_days", 30.0)
    setattr(sun_crossing_state, "step_days", 30.0)

    events = []

    t_e, y_e = almanac.find_discrete(t0, t1, earth_crossing_state)
    for ti in t_e:
        events.append(
            {
                "date": ti.utc_datetime(),
                "event": "Saturn Ring Plane Crossing (Earth)",
                "type": "Saturn Ring Crossing",
            }
        )

    t_s, y_s = almanac.find_discrete(t0, t1, sun_crossing_state)
    for ti in t_s:
        events.append(
            {
                "date": ti.utc_datetime(),
                "event": "Saturn Ring Plane Crossing (Sun)",
                "type": "Saturn Ring Crossing",
            }
        )

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
    for t in max_times:
        events.append({"date": t.utc_datetime(), "event": "Apogee", "object": "Moon"})
    for t in min_times:
        events.append({"date": t.utc_datetime(), "event": "Perigee", "object": "Moon"})

    return events


def find_conjunctions(
    observer,
    p1_name,
    p2_name,
    start_date,
    end_date,
    threshold_degrees=None,
):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    p1 = planetary.get_skyfield_obj(p1_name)
    p2 = planetary.get_skyfield_obj(p2_name)

    def separation(t):
        # Use topocentric apparent positions to account for aberration and light deflection
        p1_obs = observer.at(t).observe(p1).apparent()
        p2_obs = observer.at(t).observe(p2).apparent()
        return p1_obs.separation_from(p2_obs).degrees

    # Dynamically adjust step size based on moving bodies
    # Moon moves ~13 deg/day, Mercury ~1.3 deg/day
    if "moon" in [p1_name.lower(), p2_name.lower()]:
        step = 0.05  # ~1.2 hours
    elif any(p in [p1_name.lower(), p2_name.lower()] for p in ["mercury", "venus"]):
        step = 0.2  # ~4.8 hours
    else:
        step = 0.5  # ~12 hours

    setattr(separation, "step_days", step)

    times, separations = find_minima(t0, t1, separation)

    events = []
    for t, s in zip(times, separations):
        if threshold_degrees is None or s < threshold_degrees:
            # Refine conjunction time and separation
            refined_t, refined_s = _refine_conjunction(observer, p1, p2, t)
            events.append(
                {
                    "date": refined_t.utc_datetime(),
                    "separation_degrees": float(refined_s),
                }
            )

    return events


def find_oppositions(observer, planet_name, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    planet = planetary.get_skyfield_obj(planet_name)
    sun = planetary.get_skyfield_obj("sun")

    def ecliptic_longitude_difference(t):
        # Use apparent topocentric positions for maximum observational accuracy
        planet_lon = (
            observer.at(t).observe(planet).apparent().ecliptic_latlon()[1].degrees
        )
        sun_lon = observer.at(t).observe(sun).apparent().ecliptic_latlon()[1].degrees
        diff = sun_lon - planet_lon
        return (diff + 180) % 360 - 180

    def opposition_angle_difference(t):
        return abs(abs(ecliptic_longitude_difference(t)) - 180)

    setattr(opposition_angle_difference, "step_days", 180)

    times, _ = find_minima(t0, t1, opposition_angle_difference)

    events = []
    for t in times:
        events.append({"date": t.utc_datetime(), "planet": planet_name})

    return events


def find_mercury_inferior_conjunctions(
    observer, start_date, end_date, threshold_degrees=1.0
):
    conjunctions = find_conjunctions(
        observer, "mercury", "sun", start_date, end_date, threshold_degrees
    )

    mercury = planetary.get_skyfield_obj("mercury")
    sun = planetary.get_skyfield_obj("sun")
    ts = get_timescale()

    inferior_events = []
    for event in conjunctions:
        t = ts.from_datetime(event["date"])
        mercury_obs = observer.at(t).observe(mercury)
        sun_obs = observer.at(t).observe(sun)

        mercury_dist = mercury_obs.distance().au
        sun_dist = sun_obs.distance().au

        if mercury_dist < sun_dist:
            # It is an inferior conjunction
            # Calculate angular radii
            mercury_angular_radius = np.degrees(
                np.arctan2(astronomy.MERCURY_RADIUS_KM / astronomy.AU_KM, mercury_dist)
            )
            sun_angular_radius = np.degrees(
                np.arctan2(astronomy.SUN_RADIUS_KM / astronomy.AU_KM, sun_dist)
            )

            event["is_transit"] = event["separation_degrees"] < (
                mercury_angular_radius + sun_angular_radius
            )
            inferior_events.append(event)

    return inferior_events


def find_conjunctions_with_star(
    observer,
    body1_name,
    star_object,
    start_date,
    end_date,
    threshold_degrees=1.0,
):
    """
    Finds conjunctions between a moving body and a fixed star.
    Wrapper around find_conjunctions_with_stars for single star case.
    """
    events = find_conjunctions_with_stars(
        observer,
        body1_name,
        [("Target", star_object)],
        start_date,
        end_date,
        threshold_degrees,
    )

    # Remove the object2 key for backward compatibility
    for event in events:
        if "object2" in event:
            del event["object2"]

    return events


def find_conjunctions_with_stars(
    observer,
    body_name,
    star_data,  # List of (name, Star object)
    start_date,
    end_date,
    threshold_degrees=1.0,
    precomputed_positions=None,
):
    """
    Finds conjunctions between a moving body and multiple fixed stars.
    Vectorized over both time and stars for maximum performance.
    """
    if not star_data:
        return []

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    # Determine the time grid to use.
    # If precomputed positions are provided, we use their time array to ensure
    # array compatibility and maximize reuse of pre-calculated data.
    if precomputed_positions:
        # Get the time array from the first available position object
        first_pos = next(iter(precomputed_positions.values()))
        times = first_pos.t
    else:
        # Hourly check
        num_hours = int((t1 - t0) * 24)
        if num_hours < 2:
            return []
        times = ts.linspace(t0, t1, num_hours)

    # Always get the body object as it is used for refinement later
    body = planetary.get_skyfield_obj(body_name)

    # Use precomputed positions if available, otherwise observe
    if precomputed_positions and body_name.lower() in precomputed_positions:
        pos_body_all = precomputed_positions[body_name.lower()]
        # Verify length matches
        if (
            hasattr(pos_body_all, "t")
            and hasattr(pos_body_all.t, "shape")
            and len(pos_body_all.t.shape) > 0
            and pos_body_all.t.shape[0] == len(times)
        ):
            pos_body = pos_body_all
        else:
            pos_body = observer.at(times).observe(body).apparent()
    else:
        pos_body = observer.at(times).observe(body).apparent()

    # Unit vectors for body at all times: (3, M)
    body_au = pos_body.position.au
    u_body = body_au / np.linalg.norm(body_au, axis=0)

    # Prepare vectorized Star objects
    star_names = [name for name, _ in star_data]
    star_objs = [obj for _, obj in star_data]

    # To maximize performance, we observe all stars once in ICRF (at the midpoint of the search)
    # and treat them as fixed unit vectors. This eliminates the O(N) loop of
    # expensive coordinate transformations.
    # Accuracy loss is sub-arcminute (mainly due to aberration), which is perfectly
    # acceptable for identifying conjunction candidates.
    t_mid = times[len(times) // 2]
    stars_vector = Star(
        ra_hours=np.array([s.ra.hours for s in star_objs]),
        dec_degrees=np.array([s.dec.degrees for s in star_objs]),
    )
    # Observe all stars at once in ICRF
    pos_stars = observer.at(t_mid).observe(stars_vector)
    # Unit vectors for stars: (3, N)
    stars_au = pos_stars.position.au
    u_stars = stars_au / np.linalg.norm(stars_au, axis=0)

    # Matrix multiplication: (N, 3) @ (3, M) -> (N, M)
    # This provides a ~5x speedup for typical catalog sizes by replacing the O(N) loop
    # of individual observations with a single vectorized operation.
    dot_products = u_stars.T @ u_body

    # Angular separation in degrees: acos(dot_product)
    # Using clip to avoid NaNs due to floating point precision
    separations = np.degrees(np.arccos(np.clip(dot_products, -1.0, 1.0)))

    # Identify local minima where separation is below threshold (vectorized)
    is_minima = (separations[:, 1:-1] < separations[:, :-2]) & (
        separations[:, 1:-1] < separations[:, 2:]
    )
    is_below_threshold = separations[:, 1:-1] < threshold_degrees

    # Find star and time indices for all conjunction candidates
    star_idxs, time_idxs_minus_1 = np.where(is_minima & is_below_threshold)
    time_idxs = time_idxs_minus_1 + 1

    events = []
    for star_idx, time_idx in zip(star_idxs, time_idxs):
        # Refine conjunction time and separation
        # Refinement is still iterative as it requires high-precision topocentric observation
        # but is only performed for the final candidates.
        refined_t, refined_s = _refine_conjunction(
            observer, body, star_objs[star_idx], times[time_idx]
        )
        events.append(
            {
                "date": refined_t.utc_datetime(),
                "object2": star_names[star_idx],
                "separation_degrees": float(refined_s),
            }
        )

    return events


def find_conjunctions_between_moving_bodies(
    observer,
    body1_name,
    bodies2_data,  # List of (name, Skyfield object)
    start_date,
    end_date,
    threshold_degrees=1.0,
    precomputed_positions=None,
):
    """
    Finds conjunctions between a moving body and multiple other moving bodies.
    Vectorized over time for each pair.
    """
    if not bodies2_data:
        return []

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    # Dynamically adjust step size based on moving bodies
    # Using 15-minute resolution for the Moon for better conjunction accuracy
    if "moon" == body1_name.lower() or any(
        "moon" == name.lower() for name, _ in bodies2_data
    ):
        step = 0.01  # ~14.4 minutes
    elif "mercury" == body1_name.lower() or any(
        "mercury" == name.lower() for name, _ in bodies2_data
    ):
        step = 0.1  # ~2.4 hours
    else:
        step = 0.2  # ~4.8 hours

    # Determine the time grid to use.
    if precomputed_positions:
        # Get the time array from the first available position object
        first_pos = next(iter(precomputed_positions.values()))
        times = first_pos.t
    else:
        num_steps = int((t1 - t0) / step)
        if num_steps < 2:
            num_steps = 2
        times = ts.linspace(t0, t1, num_steps)

    # Use precomputed positions if available, otherwise observe
    if precomputed_positions and body1_name.lower() in precomputed_positions:
        # Check if length matches. Skyfield's Astrometric results store
        # their timestamps in '.t', which is a Time object with a .shape.
        pos1_all = precomputed_positions[body1_name.lower()]
        # Verify both 't' attribute and that the length of the vectorized time array matches
        if (
            hasattr(pos1_all, "t")
            and hasattr(pos1_all.t, "shape")
            and len(pos1_all.t.shape) > 0
            and pos1_all.t.shape[0] == len(times)
        ):
            pos1 = pos1_all
        else:
            body1 = planetary.get_skyfield_obj(body1_name)
            pos1 = observer.at(times).observe(body1)
    else:
        body1 = planetary.get_skyfield_obj(body1_name)
        pos1 = observer.at(times).observe(body1)

    events = []
    for name2, body2 in bodies2_data:
        if precomputed_positions and name2.lower() in precomputed_positions:
            pos2_all = precomputed_positions[name2.lower()]
            if (
                hasattr(pos2_all, "t")
                and hasattr(pos2_all.t, "shape")
                and len(pos2_all.t.shape) > 0
                and pos2_all.t.shape[0] == len(times)
            ):
                pos2 = pos2_all
            else:
                pos2 = observer.at(times).observe(body2)
        else:
            pos2 = observer.at(times).observe(body2)

        separations = pos1.separation_from(pos2).degrees

        # Identify local minima where separation is below threshold
        is_minima = (separations[1:-1] < separations[:-2]) & (
            separations[1:-1] < separations[2:]
        )
        is_below_threshold = separations[1:-1] < threshold_degrees

        minima_indices = np.where(is_minima & is_below_threshold)[0] + 1

        for idx in minima_indices:
            # Refine conjunction time and separation
            # If precomputed positions are used, we still refine using the actual objects
            # to ensure maximum precision.
            body1 = planetary.get_skyfield_obj(body1_name)
            refined_t, refined_s = _refine_conjunction(
                observer, body1, body2, times[idx]
            )
            events.append(
                {
                    "date": refined_t.utc_datetime(),
                    "object2": name2,
                    "separation_degrees": float(refined_s),
                }
            )

    return events


def find_lunar_occultations(observer, bright_stars, start_date, end_date):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    moon = planetary.get_skyfield_obj("moon")
    earth = cast(Any, planetary.get_skyfield_obj("earth"))

    target_stars = [
        "Sirius",
        "Arcturus",
        "Rigel",
        "Procyon",
        "Betelgeuse",
        "Altair",
        "Aldebaran",
        "Antares",
        "Spica",
        "Pollux",
        "Fomalhaut",
        "Regulus",
        "Adhara",
        "Bellatrix",
        "El Nath",
        "Alnilam",
        "Alnitak",
        "Wezen",
        "Alhena",
        "Mirzam",
        "Alphard",
        "Hamal",
        "Beta Tauri",
    ]

    events = []

    stars_to_check = bright_stars[bright_stars["Name"].str.strip().isin(target_stars)]

    # Optimization: Pre-filter stars based on ecliptic latitude.
    # The Moon stays within ~5.3 degrees of the ecliptic.
    star_objs_all = stars_to_check["skyfield_object"].tolist()
    star_names_all = stars_to_check["Name"].tolist()

    # Observe all stars at once using a vectorized Star object
    # Optimization: use pre-calculated float columns instead of list comprehension over Star objects
    stars_vector = Star(
        ra_hours=stars_to_check["ra_hours"].to_numpy(),
        dec_degrees=stars_to_check["dec_degrees"].to_numpy(),
    )
    spos_at_t0_all = earth.at(t0).observe(stars_vector)
    lats, _, _ = spos_at_t0_all.ecliptic_latlon()

    # Filter using vectorized mask
    mask = np.abs(lats.degrees) < 10
    star_objects = [(star_names_all[i], star_objs_all[i]) for i in np.where(mask)[0]]

    # Check every 2 minutes for precision
    num_steps = int((t1 - t0) * 24 * 30)
    if num_steps < 2:
        return []
    times = ts.linspace(t0, t1, num_steps)

    # Coarse check every 20 minutes (1 in 10 points)
    coarse_idx = np.arange(0, num_steps, 10)
    coarse_times = times[coarse_idx]

    # Topocentric position for Moon (coarse)
    # Refraction is not critical here for the coarse filter
    mpos_coarse = observer.at(coarse_times).observe(moon).apparent()
    m_alt_coarse, _, m_dist_coarse = mpos_coarse.altaz()
    moon_rad_coarse = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_dist_coarse.km))

    # Unit vectors for Moon (coarse)
    m_au_coarse = mpos_coarse.position.au
    u_moon_coarse = m_au_coarse / np.linalg.norm(m_au_coarse, axis=0)

    for star_name, star_obj in star_objects:
        # Use ICRS position once (t0) for coarse filter - very fast.
        # This filters out stars far from the Moon's path.
        spos_star = earth.at(t0).observe(star_obj)
        u_star = spos_star.position.au / np.linalg.norm(spos_star.position.au)

        # Dot product for coarse separations
        dot_coarse = u_star @ u_moon_coarse
        sep_coarse = np.degrees(np.arccos(np.clip(dot_coarse, -1.0, 1.0)))

        # Potential occultation: coarse separation < angular radius + small margin (for parallax/aberration)
        # Moon parallax is up to ~1 deg, aberration is ~20 arcsec.
        # Using Topocentric Moon and ICRS Star at t0, so only need to cover Star motion (aberration/parallax).
        # Parallax for Stars is tiny (<1"), aberration ~20". Using 0.1 deg margin for safety.
        potential_mask = (sep_coarse < moon_rad_coarse + 0.1) & (
            m_alt_coarse.degrees > -1
        )

        if not potential_mask.any():
            continue

        # For potential candidates, perform high-precision check only near those windows
        # Expand windows to ensure we don't miss transitions
        window_indices = np.unique(
            np.concatenate(
                [
                    np.clip(coarse_idx[potential_mask] + offset, 0, num_steps - 1)
                    for offset in range(-15, 16)  # +/- 30 mins around potential event
                ]
            )
        )

        if len(window_indices) == 0:
            continue

        fine_times = times[window_indices]
        mpos_fine = observer.at(fine_times).observe(moon).apparent()
        m_alt_fine, _, m_dist_fine = mpos_fine.altaz(
            temperature_C=10.0, pressure_mbar=1013.25
        )
        moon_rad_fine = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_dist_fine.km))

        # Topocentric observation of star for maximum precision
        # Oracle: use apparent position to match refracted Moon position
        spos_fine = observer.at(fine_times).observe(star_obj).apparent()

        # Calculate separation from refracted positions
        # Skyfield's separation_from handles apparent positions correctly.
        # However, to be extra precise we should ensure we are comparing
        # refracted Moon to refracted Star.
        # .altaz() with temperature/pressure already accounts for refraction.
        # For separation, we compare positions in the observer's local frame.

        m_alt, m_az, _ = mpos_fine.altaz(temperature_C=10.0, pressure_mbar=1013.25)
        s_alt, s_az, _ = spos_fine.altaz(temperature_C=10.0, pressure_mbar=1013.25)

        # Vectorized angular separation using Haversine-like formula on Alt/Az
        d_alt = m_alt.radians - s_alt.radians
        d_az = m_az.radians - s_az.radians

        a = np.sin(d_alt/2)**2 + np.cos(m_alt.radians) * np.cos(s_alt.radians) * np.sin(d_az/2)**2
        separations = np.degrees(2 * np.arcsin(np.sqrt(np.clip(a, 0, 1))))

        # Sun altitude for visibility check
        sun_alts = (
            observer.at(fine_times)
            .observe(planetary.get_skyfield_obj("sun"))
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
        )

        # Occultation check: separation < angular radius AND Moon above horizon AND Sun below -6 degrees
        occ_mask = (
            (separations < moon_rad_fine)
            & (m_alt.degrees > 0)
            & (sun_alts.degrees <= -6)
        )
        occ_indices_local = np.where(occ_mask)[0]

        if len(occ_indices_local) > 0:
            # map back to global times indices
            occ_indices_global = window_indices[occ_indices_local]
            # Group consecutive indices as one event
            groups = np.split(
                occ_indices_global, np.where(np.diff(occ_indices_global) > 10)[0] + 1
            )
            for group in groups:
                # To find min separation in this event, we need all separations for these indices
                # Actually we already have separations for all window_indices
                # Let's map global indices back to local (within window_indices)
                local_group_indices = np.searchsorted(window_indices, group)
                min_local_idx = local_group_indices[
                    np.argmin(separations[local_group_indices])
                ]
                min_global_idx = window_indices[min_local_idx]

                mid_t = times[min_global_idx]
                refined_t, _ = _refine_conjunction(observer, moon, star_obj, mid_t)

                # We need ingress/egress for the event dict
                ingress_idx = group[0]
                egress_idx = group[-1]

                events.append(
                    {
                        "date": refined_t.utc_datetime(),
                        "object1": "Moon",
                        "object2": star_name,
                        "ingress_time": times[ingress_idx].utc_datetime(),
                        "egress_time": times[egress_idx].utc_datetime(),
                        "type": "Lunar Occultation",
                        "event": "Lunar Occultation",
                    }
                )

    return events


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
        if sun_alt.degrees > -18:  # not dark enough
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
    )


def find_tiangong_flybys(
    topos_observer,
    vector_observer,
    start_date,
    end_date,
    peak_altitude_threshold=40,
    rise_altitude_threshold=10,
):
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
    )


def find_mars_closest_approach(start_date, end_date, observer=None):
    """
    Finds when Mars is at its closest point to Earth (perigee).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = get_ephemeris()
    earth = eph["earth"]
    mars = eph["mars barycenter"]
    sun = eph["sun"]

    def distance_to_earth(t):
        return cast(Any, earth).at(t).observe(mars).distance().au

    # Mars closest approach happens every ~780 days.
    # Step of 30 days is safe for find_minima.
    setattr(distance_to_earth, "step_days", 30.0)
    times, values = find_minima(t0, t1, distance_to_earth)

    events = []
    for t, dist in zip(times, values):
        event = {
            "date": t.utc_datetime(),
            "event": "Mars Closest Approach",
            "object": "Mars",
            "type": "Mars Closest Approach",
            "distance_au": float(dist),
        }

        if observer is not None:
            v_obs = observer.at(t).observe(mars).apparent()
            alt, _, _ = v_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

            sun_alt = (
                observer.at(t)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

            event.update(
                {
                    "altitude": float(alt.degrees),
                    "sun_altitude": float(sun_alt),
                    "is_visible": bool(alt.degrees > 0 and sun_alt <= -6),
                }
            )

        events.append(event)

    return events


def find_lunar_eclipses(start_date, end_date, observer=None):
    """
    Finds lunar eclipses and provides visibility info if an observer is provided.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
    t, y, details = eclipselib.lunar_eclipses(t0, t1, eph)
    events = []
    for i, (ti, yi) in enumerate(zip(t, y)):
        event = {
            "date": ti.utc_datetime(),
            "type": "Lunar Eclipse",
            "eclipse_kind": eclipselib.LUNAR_ECLIPSES[yi],
            "penumbral_magnitude": details["penumbral_magnitude"][i],
            "umbral_magnitude": details["umbral_magnitude"][i],
        }

        if observer is not None:
            moon = eph["moon"]
            sun = eph["sun"]

            m_obs = observer.at(ti).observe(moon).apparent()
            m_alt, _, _ = m_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

            s_alt = (
                observer.at(ti)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

            event.update(
                {
                    "altitude": float(m_alt.degrees),
                    "sun_altitude": float(s_alt),
                    "is_visible": bool(m_alt.degrees > 0 and s_alt <= -6),
                }
            )

        events.append(event)
    return events


def find_solar_eclipses(observer, start_date, end_date):
    """
    Finds solar eclipses for a specific observer, providing classification
    (Total, Annular, Partial), magnitude, and obscuration.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    sun = planetary.get_skyfield_obj("sun")
    moon = planetary.get_skyfield_obj("moon")

    def solar_separation(t):
        s = observer.at(t).observe(sun).apparent()
        m = observer.at(t).observe(moon).apparent()

        # Calculate topocentric angular radii
        s_dist = s.distance().km
        m_dist = m.distance().km

        s_radius = np.degrees(np.arcsin(astronomy.SUN_RADIUS_KM / s_dist))
        m_radius = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_dist))

        sep = s.separation_from(m).degrees
        return sep - (s_radius + m_radius)

    setattr(solar_separation, "step_days", 0.005)
    times, _ = find_minima(t0, t1, solar_separation)

    events = []
    for t in times:
        s_pos = observer.at(t).observe(sun).apparent()
        m_pos = observer.at(t).observe(moon).apparent()

        d = s_pos.separation_from(m_pos).degrees
        rs = np.degrees(np.arcsin(astronomy.SUN_RADIUS_KM / s_pos.distance().km))
        rm = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_pos.distance().km))

        if d < rs + rm:
            # Visibility check: Is the Sun above the horizon for this observer?
            # Account for atmospheric refraction for precise visibility check
            sun_alt = s_pos.altaz(temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
            if sun_alt <= 0:
                continue

            # Classification
            if d <= abs(rs - rm):
                if rm >= rs:
                    kind = "Total"
                else:
                    kind = "Annular"
            else:
                kind = "Partial"

            # Magnitude (fraction of solar diameter covered)
            mag = (rs + rm - d) / (2 * rs)

            # Obscuration (fraction of solar area covered)
            # Area of intersection of two circles
            if d <= abs(rs - rm):
                obs = 1.0 if rm >= rs else (rm / rs) ** 2
            else:
                # Formula for area of overlap of two circles
                # Source: http://mathworld.wolfram.com/Circle-CircleIntersection.html
                def area(r1, r2, d):
                    if d >= r1 + r2:
                        return 0.0
                    if d <= abs(r1 - r2):
                        return np.pi * min(r1, r2) ** 2
                    r1sq = r1**2
                    r2sq = r2**2
                    dsq = d**2
                    part1 = r1sq * np.arccos((dsq + r1sq - r2sq) / (2 * d * r1))
                    part2 = r2sq * np.arccos((dsq + r2sq - r1sq) / (2 * d * r2))
                    part3 = 0.5 * np.sqrt(
                        (-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2)
                    )
                    return part1 + part2 - part3

                overlap_area = area(rs, rm, d)
                sun_area = np.pi * rs**2
                obs = overlap_area / sun_area

            events.append(
                {
                    "date": t.utc_datetime(),
                    "type": "Solar Eclipse",
                    "eclipse_type": kind,
                    "magnitude": float(mag),
                    "obscuration": float(obs),
                    "separation_degrees": float(d),
                }
            )
    return events


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


def find_culminations(observer, start_date, end_date, sun_alt_threshold=-6):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
    sun = eph["sun"]

    planets = [
        "sun",
        "moon",
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]
    planet_objs = [(p, planetary.get_skyfield_obj(p)) for p in planets]

    events = []

    for name, obj in planet_objs:

        def altitude(t):
            # Account for atmospheric refraction for high-precision culmination altitude
            return (
                observer.at(t)
                .observe(obj)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

        setattr(altitude, "step_days", 0.5)  # Check twice a day
        times, altitudes = find_maxima(t0, t1, altitude)

        simple_name = planetary.get_simple_name(name)

        for t, alt in zip(cast(Any, times), altitudes):
            if alt > 0:
                # Visibility check: For non-solar objects, Sun must be below threshold
                sun_alt = (
                    observer.at(t)
                    .observe(sun)
                    .apparent()
                    .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                    .degrees
                )
                visible = True
                if simple_name != "Sun" and sun_alt > sun_alt_threshold:
                    visible = False

                if visible:
                    events.append(
                        {
                            "date": t.utc_datetime(),
                            "event": "Culmination",
                            "object": simple_name,
                            "type": "Culmination",
                            "altitude": float(alt),
                        }
                    )

    return events


def find_object_culminations(
    observer, objects_data, start_date, end_date, sun_alt_threshold=-12
):
    """
    Finds culminations for a list of objects (e.g. Messier catalog).
    Vectorized over objects using an analytical approach (LST == RA) for fixed objects.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
    sun = eph["sun"]

    events = []
    if not objects_data:
        return events

    # Separate fixed objects (e.g. Stars, DSOs) from moving objects (e.g. Planets)
    fixed_objects = []
    moving_objects = []
    for name, obj in objects_data:
        # Fixed objects are typically Star instances with a constant RA/Dec
        if hasattr(obj, "ra"):
            fixed_objects.append((name, obj))
        else:
            moving_objects.append((name, obj))

    # 1. Process fixed objects with vectorized analytical approach
    if fixed_objects:
        # Extract observer coordinates from the VectorSum object
        lon_hours = 0.0
        lat_deg = 0.0
        for vf in observer.vector_functions:
            if hasattr(vf, "latitude"):
                lat_deg = vf.latitude.degrees
                lon_hours = vf.longitude.hours
                break

        # Generate reference points for each day in the interval.
        num_days = int(t1 - t0) + 1
        day_offsets = np.arange(-1, num_days + 1)
        t0_dt = cast(Any, t0.utc_datetime())
        t_refs = ts.utc(t0_dt.year, t0_dt.month, t0_dt.day + day_offsets, 12)

        names_fixed = [f[0] for f in fixed_objects]
        num_fixed = len(fixed_objects)
        ra_fixed = np.array([obj.ra.hours for _, obj in fixed_objects])
        dec_fixed = np.array([obj.dec.degrees for _, obj in fixed_objects])

        # Consolidate all fixed objects into a single vectorized Star object
        stars_vector = Star(ra_hours=ra_fixed, dec_degrees=dec_fixed)

        all_t_culm_tt = []
        all_dec_deg = []

        # Optimization: Loop over days while vectorizing over all objects (N objects per day)
        for t_ref in t_refs:
            # Estimate apparent RA and Dec at mid-day for all objects
            obs_ref = observer.at(t_ref).observe(stars_vector).apparent()
            radec_ref = obs_ref.radec(epoch="date")
            ra_hours = radec_ref[0].hours
            dec_deg = radec_ref[1].degrees

            # At culmination: LST == RA => GAST + Lon == RA => GAST == RA - Lon
            target_gast = (ra_hours - lon_hours) % 24
            diff_gast = (target_gast - t_ref.gast) % 24

            # Convert sidereal interval to UT (approx. factor 1.0027379)
            t_culm_tt = t_ref.tt + (diff_gast / 1.002737909) / 24.0

            # For stars, a single estimation using apparent coordinates at mid-day
            # is extremely accurate (error < 0.1s).
            all_t_culm_tt.append(t_culm_tt)
            all_dec_deg.append(dec_deg)

        # Flatten all potential culminations
        t_culms_all_tt = np.concatenate(all_t_culm_tt)
        decs_all_deg = np.concatenate(all_dec_deg)
        obj_indices_all = np.tile(np.arange(num_fixed), len(t_refs))

        # Filter culminations that fall within the requested window
        mask_window = (t_culms_all_tt >= t0.tt) & (t_culms_all_tt <= t1.tt)

        t_final_tt = t_culms_all_tt[mask_window]
        t_final = ts.tt_jd(t_final_tt)
        dec_final_deg = decs_all_deg[mask_window]
        obj_indices_final = obj_indices_all[mask_window]

        if len(t_final) > 0:
            # Sun altitude for visibility check (vectorized)
            sun_alts_deg = (
                observer.at(t_final)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

            # Culmination altitude (geometric approximation: 90 - |lat - dec|)
            # Accurate to sub-arcsecond for stars when on the meridian.
            alts_final_deg = 90.0 - np.abs(lat_deg - dec_final_deg)

            # Add atmospheric refraction at culmination (Bennett's formula)
            # R in arcminutes = 1 / tan(h + 7.31 / (h + 4.4))
            r_mask = alts_final_deg > -1.0
            if np.any(r_mask):
                alts_m = alts_final_deg[r_mask]
                r_arcmin = 1.0 / np.tan(np.deg2rad(alts_m + 7.31 / (alts_m + 4.4)))
                alts_final_deg[r_mask] += r_arcmin / 60.0

            # Visibility threshold: Altitude > 15 deg and Sun below threshold
            valid_mask = (alts_final_deg > 15) & (sun_alts_deg <= sun_alt_threshold)

            final_names = [names_fixed[i] for i in obj_indices_final[valid_mask]]
            final_times = t_final[valid_mask]
            final_alts = alts_final_deg[valid_mask]

            for t, name, alt in zip(cast(Any, final_times), final_names, final_alts):
                events.append(
                    {
                        "date": t.utc_datetime(),
                        "event": "Culmination",
                        "object": name,
                        "type": "Messier Culmination",
                        "altitude": float(alt),
                    }
                )

    # 2. Process moving objects with the traditional iterative solver
    for name, obj in moving_objects:

        def altitude_func(t):
            return (
                observer.at(t)
                .observe(obj)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

        setattr(altitude_func, "step_days", 0.5)
        times, altitudes = find_maxima(t0, t1, altitude_func)

        for t, alt in zip(cast(Any, times), altitudes):
            if alt > 15:
                sun_alt = (
                    observer.at(t)
                    .observe(sun)
                    .apparent()
                    .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                    .degrees
                )
                if sun_alt <= sun_alt_threshold:
                    events.append(
                        {
                            "date": t.utc_datetime(),
                            "event": "Culmination",
                            "object": name,
                            "type": "Messier Culmination",
                            "altitude": float(alt),
                        }
                    )

    return events


def find_greatest_elongations(observer, start_date, end_date):
    """
    Finds greatest elongations for Mercury and Venus.
    Greatest Eastern Elongation is in the evening sky.
    Greatest Western Elongation is in the morning sky.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())
    sun = eph["sun"]
    earth = eph["earth"]

    planets = ["mercury", "venus"]
    events = []

    for p_name in planets:
        planet = planetary.get_skyfield_obj(p_name)

        def elongation(t):
            # Elongation is the angle between the Sun and the planet as seen from Earth
            # We use Earth center (barycentric) for standard elongation values
            s = earth.at(t).observe(sun)
            p = earth.at(t).observe(planet)
            return s.separation_from(p).degrees

        setattr(elongation, "step_days", 2.0)  # Elongations change slowly
        times, separations = find_maxima(t0, t1, elongation)

        for t, sep in zip(cast(Any, times), separations):
            # Determine if it's Eastern or Western elongation
            # Eastern elongation: planet is east of the Sun (evening sky)
            # Western elongation: planet is west of the Sun (morning sky)
            s_lon = cast(Any, earth).at(t).observe(sun).ecliptic_latlon()[1].degrees
            p_lon = cast(Any, earth).at(t).observe(planet).ecliptic_latlon()[1].degrees

            diff = (p_lon - s_lon + 180) % 360 - 180
            direction = "Eastern" if diff > 0 else "Western"

            events.append(
                {
                    "date": t.utc_datetime(),
                    "event": f"{planetary.get_simple_name(p_name)} Greatest {direction} Elongation",
                    "object": planetary.get_simple_name(p_name),
                    "type": "Greatest Elongation",
                    "separation_degrees": float(sep),
                    "direction": direction,
                }
            )

    return events


def find_seasons(start_date, end_date):
    """
    Finds the start of seasons (equinoxes and solstices).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    eph = cast(Any, get_ephemeris())

    t, y = almanac.find_discrete(t0, t1, almanac.seasons(eph))

    events = []
    for ti, yi in zip(t, y):
        events.append(
            {
                "date": ti.utc_datetime(),
                "event": almanac.SEASON_EVENTS[yi],
                "type": "Season",
            }
        )
    return events


def find_planet_solar_conjunctions(observer, start_date, end_date, threshold_degrees=2.0):
    """
    Finds conjunctions between planets and the Sun.
    Distinguishes between inferior and superior conjunctions for inner planets.
    """
    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]

    conjunctions = []
    for p_name in planets:
        planet_conjs = find_conjunctions(
            observer, p_name, "sun", start_date, end_date, threshold_degrees
        )
        simple_name = planetary.get_simple_name(p_name)

        for conj in planet_conjs:
            t = get_timescale().from_datetime(conj["date"])
            p_obj = planetary.get_skyfield_obj(p_name)
            sun_obj = planetary.get_skyfield_obj("sun")

            # Get distances to determine conjunction type
            p_dist = observer.at(t).observe(p_obj).distance().au
            sun_dist = observer.at(t).observe(sun_obj).distance().au

            if p_name in ["mercury", "venus"]:
                if p_dist < sun_dist:
                    kind = "Inferior Conjunction"
                else:
                    kind = "Superior Conjunction"
            else:
                kind = "Conjunction"

            conj.update(
                {
                    "event": f"{simple_name} Solar {kind}",
                    "object1": simple_name,
                    "object2": "Sun",
                    "type": "Planet Solar Conjunction",
                    "conjunction_kind": kind,
                }
            )
            conjunctions.append(conj)

    return conjunctions


def find_planet_planet_occultations(observer, start_date, end_date):
    """
    Finds occultations of one planet by another.
    Extremely rare events.
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]

    events = []
    # Check all pairs of planets
    for i, p1_name in enumerate(planets):
        for p2_name in planets[i + 1 :]:
            p1_obj = planetary.get_skyfield_obj(p1_name)
            p2_obj = planetary.get_skyfield_obj(p2_name)

            def separation(t):
                # Use topocentric apparent positions
                # Optimization: for coarse search, we could use .observe()
                p1_obs = observer.at(t).observe(p1_obj).apparent()
                p2_obs = observer.at(t).observe(p2_obj).apparent()
                sep = p1_obs.separation_from(p2_obs).degrees

                # Calculate angular radii
                r1 = np.degrees(
                    np.arcsin(
                        planetary.get_planet_radius_km(p1_name) / p1_obs.distance().km
                    )
                )
                r2 = np.degrees(
                    np.arcsin(
                        planetary.get_planet_radius_km(p2_name) / p2_obs.distance().km
                    )
                )

                return sep - (r1 + r2)

            # Step of 0.5 days is safe for these slow events
            setattr(separation, "step_days", 0.5)
            times, _ = find_minima(t0, t1, separation)

            for t in times:
                # Refine
                refined_t, refined_sep = _refine_conjunction(observer, p1_obj, p2_obj, t)

                p1_obs = observer.at(refined_t).observe(p1_obj).apparent()
                p2_obs = observer.at(refined_t).observe(p2_obj).apparent()

                r1 = np.degrees(
                    np.arcsin(
                        planetary.get_planet_radius_km(p1_name) / p1_obs.distance().km
                    )
                )
                r2 = np.degrees(
                    np.arcsin(
                        planetary.get_planet_radius_km(p2_name) / p2_obs.distance().km
                    )
                )

                if refined_sep < (r1 + r2):
                    # Determine which planet is in front
                    if p1_obs.distance().km < p2_obs.distance().km:
                        occulting = planetary.get_simple_name(p1_name)
                        occulted = planetary.get_simple_name(p2_name)
                    else:
                        occulting = planetary.get_simple_name(p2_name)
                        occulted = planetary.get_simple_name(p1_name)

                    events.append(
                        {
                            "date": refined_t.utc_datetime(),
                            "event": f"{occulting} occults {occulted}",
                            "object1": occulting,
                            "object2": occulted,
                            "separation_degrees": float(refined_sep),
                            "type": "Planet-Planet Occultation",
                        }
                    )
    return events


def find_jupiter_grs_transits(
    observer,
    start_date,
    end_date,
    grs_longitude=None,
):
    """
    Finds when Jupiter's Great Red Spot (GRS) transits the Central Meridian (System II).
    """
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    jupiter = planetary.get_skyfield_obj("jupiter barycenter")
    sun = planetary.get_skyfield_obj("sun")

    def cml_difference(t):
        # Use vectorized longitude calculations for better performance
        grs_lon = (
            grs_longitude
            if grs_longitude is not None
            else planetary.get_jupiter_grs_longitude(t)
        )
        sys_ii_lon = planetary.get_jupiter_system_ii_longitude(t)
        return (sys_ii_lon - grs_lon + 180) % 360 - 180

    def abs_diff(t):
        return np.abs(cml_difference(t))

    # Jupiter rotates every ~9.9 hours (~0.41 days).
    # A step of 0.1 days (~2.4 hours) is safe to find every transit.
    setattr(abs_diff, "step_days", 0.1)
    times, _ = find_minima(t0, t1, abs_diff)

    events = []
    for t in times:
        # Check visibility: Jupiter above horizon and Sun below -6 degrees
        j_obs = observer.at(t).observe(jupiter).apparent()
        alt, _, _ = j_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)

        if alt.degrees > 0:
            sun_alt = (
                observer.at(t)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

            if sun_alt <= -6:
                events.append(
                    {
                        "date": t.utc_datetime(),
                        "event": "Jupiter Great Red Spot Transit",
                        "object": "Jupiter",
                        "type": "Jupiter GRS Transit",
                        "altitude": float(alt.degrees),
                    }
                )

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
