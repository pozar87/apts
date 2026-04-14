import datetime
import pytz
from typing import Any, cast
import numpy as np
from skyfield import almanac
from skyfield.api import Star, Topos, Time
from skyfield.searchlib import find_maxima
from ..cache import get_timescale, get_ephemeris
from ..utils import planetary
from ..constants.twilight import Twilight

def get_twilight_time_utc(lat, lon, elevation, start_date, twilight, event):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))

    if isinstance(start_date, Time):
        t0 = start_date
        t1 = ts.tt_jd(t0.tt + 2.0)
    else:
        t0 = ts.utc(start_date)
        t1 = ts.utc(start_date + datetime.timedelta(days=2))

    f = almanac.dark_twilight_day(eph, location)
    times, events = almanac.find_discrete(t0, t1, f)

    # Define transitions for evening (set) and morning (rise)
    if event == "set":  # Evening: getting darker
        transitions = {
            Twilight.CIVIL: (3, 2),  # Civil -> Nautical
            Twilight.NAUTICAL: (2, 1),  # Nautical -> Astronomical
            Twilight.ASTRONOMICAL: (1, 0),  # Astronomical -> Night
        }
    else:  # Morning: getting lighter
        transitions = {
            Twilight.ASTRONOMICAL: (0, 1),  # Night -> Astronomical
            Twilight.NAUTICAL: (1, 2),  # Astronomical -> Nautical
            Twilight.CIVIL: (2, 3),  # Nautical -> Civil
        }

    trans = transitions.get(twilight)
    if trans is None:
        return None
    prev_event, next_event = trans

    # The first event is the state at t0
    previous_y = f(t0)
    if times is not None and events is not None:
        for t, y in zip(times, events):
            if previous_y == prev_event and y == next_event:
                return t.utc_datetime().replace(tzinfo=pytz.UTC)
            previous_y = y

    return None

def previous_setting_time_utc(lat, lon, elevation, obj_name, start, horizon_degrees=None):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))
    obj = eph[obj_name]

    if isinstance(start, Time):
        t1 = start
        t0 = ts.tt_jd(t1.tt - 2.0)
    else:
        t1 = ts.utc(start)
        t0 = ts.utc(start - datetime.timedelta(days=2))

    if horizon_degrees is not None:
        f = almanac.risings_and_settings(eph, obj, location, horizon_degrees=horizon_degrees)
    else:
        f = almanac.risings_and_settings(eph, obj, location)
    t, y = almanac.find_discrete(t0, t1, f)

    if t is None:
        return None

    settings = [ti for ti, yi in zip(t, y) if yi == 0]
    if settings:
        return settings[-1].utc_datetime().replace(tzinfo=pytz.UTC)
    return None

def next_rising_time_utc(lat, lon, elevation, obj_name, start, horizon_degrees=None):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))
    obj = eph[obj_name]

    if isinstance(start, Time):
        t0 = start
        t1 = ts.tt_jd(t0.tt + 2.0)
    else:
        t0 = ts.utc(start)
        t1 = ts.utc(start + datetime.timedelta(days=2))

    if horizon_degrees is not None:
        f = almanac.risings_and_settings(eph, obj, location, horizon_degrees=horizon_degrees)
    else:
        f = almanac.risings_and_settings(eph, obj, location)
    t, y = almanac.find_discrete(t0, t1, f)

    if t is not None:
        for ti, yi in zip(t, y):
            if yi == 1:  # Rising
                return ti.utc_datetime().replace(tzinfo=pytz.UTC)
    return None

def next_setting_time_utc(lat, lon, elevation, obj_name, start, horizon_degrees=None):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))
    obj = eph[obj_name]

    if isinstance(start, Time):
        t0 = start
        t1 = ts.tt_jd(t0.tt + 2.0)
    else:
        t0 = ts.utc(start)
        t1 = ts.utc(start + datetime.timedelta(days=2))

    if horizon_degrees is not None:
        f = almanac.risings_and_settings(eph, obj, location, horizon_degrees=horizon_degrees)
    else:
        f = almanac.risings_and_settings(eph, obj, location)
    t, y = almanac.find_discrete(t0, t1, f)

    if t is not None:
        for ti, yi in zip(t, y):
            if yi == 0:  # Setting
                return ti.utc_datetime().replace(tzinfo=pytz.UTC)
    return None

def previous_rising_time_utc(lat, lon, elevation, obj_name, start, horizon_degrees=None):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))
    obj = eph[obj_name]

    if isinstance(start, Time):
        t1 = start
        t0 = ts.tt_jd(t1.tt - 2.0)
    else:
        t1 = ts.utc(start)
        t0 = ts.utc(start - datetime.timedelta(days=2))

    if horizon_degrees is not None:
        f = almanac.risings_and_settings(eph, obj, location, horizon_degrees=horizon_degrees)
    else:
        f = almanac.risings_and_settings(eph, obj, location)
    t, y = almanac.find_discrete(t0, t1, f)

    if t is None:
        return None

    risings = [ti for ti, yi in zip(t, y) if yi == 1]
    if risings:
        return risings[-1].utc_datetime().replace(tzinfo=pytz.UTC)
    return None

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
        # Oracle: Handle potential state jumps (e.g., 0 -> 2) by iterating through
        # all intermediate transitions. This ensures accuracy at high latitudes
        # or when using coarser time steps.
        step = 1 if yi > y_prev else -1
        for current_y in range(y_prev + step, yi + step, step):
            prev_y = current_y - step
            # Transitions:
            # 0 -> 1: Rising, Blue Hour Start (-6)
            # 1 -> 2: Rising, Blue Hour End / Golden Hour Start (-4)
            # 2 -> 3: Rising, Golden Hour End (6)
            # 3 -> 2: Setting, Golden Hour Start (6)
            # 2 -> 1: Setting, Golden Hour End / Blue Hour Start (-4)
            # 1 -> 0: Setting, Blue Hour End (-6)

            if prev_y == 0 and current_y == 1:
                events.append(
                    {
                        "date": ti.utc_datetime(),
                        "event": "Blue Hour",
                        "phase": "Start",
                        "type": "Blue Hour",
                    }
                )
            elif prev_y == 1 and current_y == 2:
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
            elif prev_y == 2 and current_y == 3:
                events.append(
                    {
                        "date": ti.utc_datetime(),
                        "event": "Golden Hour",
                        "phase": "End",
                        "type": "Golden Hour",
                    }
                )
            elif prev_y == 3 and current_y == 2:
                events.append(
                    {
                        "date": ti.utc_datetime(),
                        "event": "Golden Hour",
                        "phase": "Start",
                        "type": "Golden Hour",
                    }
                )
            elif prev_y == 2 and current_y == 1:
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
            elif prev_y == 1 and current_y == 0:
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
                            "event": f"{simple_name} Culmination",
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
                        "event": f"{name} Culmination",
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
                            "event": f"{name} Culmination",
                            "object": name,
                            "type": "Messier Culmination",
                            "altitude": float(alt),
                        }
                    )

    return events
