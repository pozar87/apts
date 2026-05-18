from typing import Any, cast
import numpy as np
from skyfield.api import Star
from skyfield.searchlib import find_maxima
from ...cache import get_timescale, get_ephemeris
from ...utils import planetary

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

def _get_observer_coords(observer: Any) -> tuple[float, float]:
    """Extracts latitude (deg) and longitude (hours) from the observer object."""
    lon_hours = 0.0
    lat_deg = 0.0
    for vf in observer.vector_functions:
        if hasattr(vf, "latitude"):
            lat_deg = vf.latitude.degrees
            lon_hours = vf.longitude.hours
            break
    return lat_deg, lon_hours

def _apply_refraction(altitudes_deg: np.ndarray) -> np.ndarray:
    """Adds atmospheric refraction at culmination using Bennett's formula."""
    # R in arcminutes = 1 / tan(h + 7.31 / (h + 4.4))
    res = altitudes_deg.copy()
    r_mask = res > -1.0
    if np.any(r_mask):
        alts_m = res[r_mask]
        r_arcmin = 1.0 / np.tan(np.deg2rad(alts_m + 7.31 / (alts_m + 4.4)))
        res[r_mask] += r_arcmin / 60.0
    return res

def _find_fixed_object_culminations(
    observer: Any,
    fixed_objects: list[tuple[str, Any]],
    t0: Any,
    t1: Any,
    sun: Any,
    sun_alt_threshold: float,
) -> list[dict]:
    """Finds culminations for fixed objects using a vectorized analytical approach."""
    ts = get_timescale()
    lat_deg, lon_hours = _get_observer_coords(observer)
    events = []

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
        alts_final_deg = 90.0 - np.abs(lat_deg - dec_final_deg)
        alts_final_deg = _apply_refraction(alts_final_deg)

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
    return events

def _find_moving_object_culminations(
    observer: Any,
    moving_objects: list[tuple[str, Any]],
    t0: Any,
    t1: Any,
    sun: Any,
    sun_alt_threshold: float,
) -> list[dict]:
    """Finds culminations for moving objects with the traditional iterative solver."""
    events = []
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

    if not objects_data:
        return []

    # Separate fixed objects (e.g. Stars, DSOs) from moving objects (e.g. Planets)
    fixed_objects = []
    moving_objects = []
    for name, obj in objects_data:
        if hasattr(obj, "ra"):
            fixed_objects.append((name, obj))
        else:
            moving_objects.append((name, obj))

    events = []
    if fixed_objects:
        events.extend(
            _find_fixed_object_culminations(
                observer, fixed_objects, t0, t1, sun, sun_alt_threshold
            )
        )

    if moving_objects:
        events.extend(
            _find_moving_object_culminations(
                observer, moving_objects, t0, t1, sun, sun_alt_threshold
            )
        )

    return events
