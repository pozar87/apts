from typing import Any, cast
import numpy as np
from skyfield.api import Star
from skyfield.searchlib import find_maxima
from ...cache import get_timescale, get_ephemeris
from ...utils import planetary

def find_culminations(observer, start_date, end_date, sun_alt_threshold=-6):
    """
    Finds culminations for major planets using a vectorized analytical approach (LST == RA).
    """
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

    lat_deg, lon_hours = _get_observer_coords(observer)

    # Generate reference points for each day in the interval.
    num_days = int(t1 - t0) + 1
    day_offsets = np.arange(-1, num_days + 1)
    t0_dt = cast(Any, t0.utc_datetime())
    t_refs = ts.utc(t0_dt.year, t0_dt.month, t0_dt.day + day_offsets, 12)

    events = []

    for name, obj in planet_objs:
        simple_name = planetary.get_simple_name(name)

        # Pass 1: Initial estimation of culmination times (LST == RA)
        pos_ref = observer.at(t_refs).observe(obj).apparent()
        ra_hours = pos_ref.radec(epoch="date")[0].hours

        # At culmination: LST == RA => GAST + Lon == RA => GAST == RA - Lon
        target_gast = (ra_hours - lon_hours) % 24
        diff_gast = (target_gast - t_refs.gast) % 24

        # Convert sidereal interval to UT (approx. factor 1.002737909)
        t_est_tt = t_refs.tt + (diff_gast / 1.002737909) / 24.0
        t_est = ts.tt_jd(t_est_tt)

        # Pass 2: Refinement to account for planetary motion during the day
        pos_refine = observer.at(t_est).observe(obj).apparent()
        ra_hours_refine = pos_refine.radec(epoch="date")[0].hours

        target_gast_refine = (ra_hours_refine - lon_hours) % 24
        # We handle wrap-around to find the smallest adjustment
        diff_gast_refine = (target_gast_refine - t_est.gast + 12) % 24 - 12

        t_est2_tt = t_est.tt + (diff_gast_refine / 1.002737909) / 24.0
        t_est2 = ts.tt_jd(t_est2_tt)

        # Pass 3: Final refinement (crucial for the fast-moving Moon)
        pos_refine2 = observer.at(t_est2).observe(obj).apparent()
        ra_hours_refine2 = pos_refine2.radec(epoch="date")[0].hours

        target_gast_refine2 = (ra_hours_refine2 - lon_hours) % 24
        diff_gast_refine2 = (target_gast_refine2 - t_est2.gast + 12) % 24 - 12

        t_transit_tt = t_est2_tt + (diff_gast_refine2 / 1.002737909) / 24.0

        # Pass 4: Parabolic refinement to find true maximum altitude (Culmination)
        # Meridian transit (LST=RA) != Max altitude for fast-moving bodies like the Moon.
        # We sample 3 points around transit and find the vertex of the parabola.
        dt_days = 0.001 # ~1.4 minutes
        t_samples_tt = np.stack([t_transit_tt - dt_days, t_transit_tt, t_transit_tt + dt_days])

        # Flatten for vectorized observation: (3, N) -> (3*N,)
        t_samples_flat = ts.tt_jd(t_samples_tt.flatten())
        alts_flat = observer.at(t_samples_flat).observe(obj).apparent().altaz(
            temperature_C=10.0, pressure_mbar=1013.25)[0].degrees

        # Reshape back: (3, N)
        alts_samples = alts_flat.reshape(3, -1)
        y1, y2, y3 = alts_samples[0], alts_samples[1], alts_samples[2]

        # Parabola vertex: x = -d * (y3 - y1) / (2 * (y3 + y1 - 2*y2))
        denominator = 2 * (y3 + y1 - 2 * y2)
        # Avoid division by zero for objects with no curvature (shouldn't happen near peak)
        denom_mask = np.abs(denominator) > 1e-12

        shift = np.zeros_like(y1)
        shift[denom_mask] = -dt_days * (y3[denom_mask] - y1[denom_mask]) / denominator[denom_mask]

        # Limit shift to 10 minutes to stay within the peak region
        shift = np.clip(shift, -0.007, 0.007)

        t_final_tt = t_transit_tt + shift
        t_final = ts.tt_jd(t_final_tt)

        # Filter culminations that fall within the requested window
        mask_window = (t_final_tt >= t0.tt) & (t_final_tt <= t1.tt)
        t_final = t_final[mask_window]

        if len(t_final) > 0:
            # Final high-precision altitude at the refined maximum
            obs_final = observer.at(t_final).observe(obj).apparent()
            alts_final_deg = (
                obs_final.altaz(temperature_C=10.0, pressure_mbar=1013.25)[0].degrees
            )

            # Sun altitude for visibility check (vectorized)
            sun_alts_deg = (
                observer.at(t_final)
                .observe(sun)
                .apparent()
                .altaz(temperature_C=10.0, pressure_mbar=1013.25)[0]
                .degrees
            )

            # Visibility threshold: Altitude > 0
            visible_mask = alts_final_deg > 0

            # For non-solar objects, Sun must be below threshold
            if simple_name != "Sun":
                visible_mask &= sun_alts_deg <= sun_alt_threshold

            final_times = t_final[visible_mask]
            final_alts = alts_final_deg[visible_mask]

            for t, alt in zip(cast(Any, final_times), final_alts):
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
