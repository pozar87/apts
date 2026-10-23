import logging
import math
from datetime import timedelta
from typing import TYPE_CHECKING, Any

import numpy as np

from .resolvers import _get_observer_for_event, _resolve_skyfield_object
from .utils import is_long_event

if TYPE_CHECKING:
    from apts.events.event import Event

logger = logging.getLogger(__name__)


def _compute_sky_brightness_at_time(
    event_obj: "Event", observer: Any, ts_chart: Any
) -> str:
    """Computes topocentric sky brightness classification at a specific chart observation time."""
    from apts.cache import get_ephemeris
    from apts.events.calculations import get_sky_brightness

    try:
        eph = get_ephemeris()
        obs_at_c = observer.at(ts_chart)
        sun_alt = float(obs_at_c.observe(eph["sun"]).apparent().altaz()[0].degrees)
        moon_alt = float(obs_at_c.observe(eph["moon"]).apparent().altaz()[0].degrees)
        phase = (
            float(event_obj.extra_data.get("phase", 0.0))
            if isinstance(event_obj.extra_data.get("phase"), (int, float))
            else 0.0
        )
        return get_sky_brightness(sun_alt, moon_alt, phase)
    except (ValueError, KeyError, AttributeError, TypeError, RuntimeError):
        return getattr(event_obj, "sky_brightness", "NIGHT_DARK")


def _find_optimal_chart_time(
    event_obj: "Event",
    observer: Any,
    ts_time: Any,
    sf_obj1: Any | None,
) -> tuple[Any, float, str | None, str | None]:
    """
    Evaluates target altitude at peak time and searches for an optimal observation time
    when the target is at good altitude for long-lasting events.
    Returns (ts_chart, target_alt_chart, chart_datetime_utc, chart_time_note).
    """
    from apts.i18n import gettext_
    from apts.skyfield_searches.utils import fast_altaz

    dt_utc = event_obj.dt_utc

    alt_peak = 25.0
    if sf_obj1 is not None:
        try:
            app_peak = observer.at(ts_time).observe(sf_obj1).apparent()
            alt_o, _, _ = app_peak.altaz()
            alt_peak = float(alt_o.degrees)
        except (ValueError, KeyError, AttributeError, TypeError, RuntimeError):
            alt_peak = (
                float(event_obj.altitude_deg)
                if event_obj.altitude_deg is not None
                else 25.0
            )
    elif event_obj.altitude_deg is not None:
        alt_peak = float(event_obj.altitude_deg)

    if alt_peak < 0.0:
        event_obj.is_below_horizon = True

    if alt_peak >= 5.0:
        event_obj.target_altitude_deg = float(alt_peak)
        return ts_time, alt_peak, None, None

    # Target is below or near horizon (< 5.0 deg).
    if is_long_event(event_obj.category, event_obj.title) and sf_obj1 is not None:
        try:
            from apts.cache import get_ephemeris, get_timescale

            eph = get_ephemeris()
            sun = eph["sun"]

            ts_factory = (
                getattr(ts_time, "ts", None)
                or getattr(getattr(event_obj, "place", None), "ts", None)
                or get_timescale()
            )

            # Vectorized evaluation over +/- 12 hours grid (97 points)
            offsets_hours = np.linspace(-12.0, 12.0, 97)
            t_jd_vec = ts_time.tt + offsets_hours / 24.0
            ts_vec = ts_factory.tt_jd(t_jd_vec)
            obs_vec = observer.at(ts_vec)

            # Optimization: Fast AltAz evaluation over vectorized Time array
            alt_c_vec = fast_altaz(obs_vec, sf_obj1)[0].degrees
            sun_alt_c_vec = fast_altaz(obs_vec, sun)[0].degrees

            # Vectorized scoring logic
            scores = np.where(
                alt_c_vec < 0.0,
                -1000.0 + alt_c_vec,
                alt_c_vec
                + np.where(sun_alt_c_vec < -0.833, 100.0, 0.0)
                - np.abs(offsets_hours) * 0.5,
            )

            best_idx = int(np.argmax(scores))
            best_alt = float(alt_c_vec[best_idx])

            if best_alt >= 5.0 or (alt_peak < 0.0 and best_alt > 0.0):
                best_dh = float(offsets_hours[best_idx])
                best_dt = dt_utc + timedelta(hours=best_dh)
                best_ts = ts_factory.utc(
                    best_dt.year,
                    best_dt.month,
                    best_dt.day,
                    best_dt.hour,
                    best_dt.minute,
                    best_dt.second,
                )

                chart_datetime_str = best_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
                time_peak_str = dt_utc.strftime("%H:%M")
                time_chart_str = best_dt.strftime("%H:%M")
                alt_peak_fmt = f"{round(alt_peak, 1)}°"
                alt_chart_fmt = f"{round(best_alt, 1)}°"

                note = gettext_(
                    "Peak at {time_peak} UTC ({alt_peak}) is below horizon. Chart shown for {time_chart} UTC (Alt: {alt_chart})."
                ).format(
                    time_peak=time_peak_str,
                    alt_peak=alt_peak_fmt,
                    time_chart=time_chart_str,
                    alt_chart=alt_chart_fmt,
                )
                return best_ts, best_alt, chart_datetime_str, note
        except (ValueError, KeyError, AttributeError, TypeError, RuntimeError) as e:
            logger.debug(f"Failed to find optimal chart time: {e}")

    alt_peak_fmt = f"{round(alt_peak, 1)}°"
    warn_note = None
    if alt_peak < 0.0:
        warn_note = gettext_(
            "Warning: Target is below horizon ({alt_peak}) at event peak time."
        ).format(alt_peak=alt_peak_fmt)

    return ts_time, alt_peak, None, warn_note


def _resolve_fallback_positions(
    event_obj: "Event",
    all_positions: list[tuple[float, float]],
    main_objs: list[Any],
    sep_deg: float,
) -> tuple[tuple[float, float], tuple[float, float] | None]:
    """Resolves primary and secondary target positions when topocentric positions are incomplete."""
    if all_positions:
        p1_pos = all_positions[0]
    elif event_obj.azimuth_deg is not None and event_obj.altitude_deg is not None:
        p1_pos = (float(event_obj.azimuth_deg), float(event_obj.altitude_deg))
    elif event_obj.azimuth_deg is not None:
        p1_pos = (float(event_obj.azimuth_deg), 25.0)
    else:
        p1_pos = (90.0, 25.0)

    p1_pos_draw = (p1_pos[0], max(1.0, p1_pos[1]))

    if len(all_positions) >= 2:
        p2_pos = all_positions[1]
        p2_pos_draw = (p2_pos[0], max(1.0, p2_pos[1]))
    elif len(main_objs) >= 2 or event_obj.angular_separation:
        p2_pos = (p1_pos[0] + sep_deg * 0.8, p1_pos[1] + sep_deg * 0.6)
        p2_pos_draw = (p2_pos[0], max(1.0, p2_pos[1]))
    else:
        p2_pos_draw = None

    return p1_pos_draw, p2_pos_draw


def _resolve_target_coordinates(
    event_obj: "Event",
    sep_deg: float,
) -> tuple[
    tuple[float, float],
    tuple[float, float] | None,
    list[tuple[float, float]],
    str,
]:
    """
    Calculates topocentric Az/Alt for target objects and evaluates optimal chart timing.
    Returns (p1_pos, p2_pos, all_object_positions, sky_brightness).
    """
    main_objs = event_obj.objects or []
    all_positions: list[tuple[float, float]] = []

    try:
        observer, ts_time = _get_observer_for_event(event_obj)
        sf_obj1 = _resolve_skyfield_object(str(main_objs[0])) if main_objs else None

        ts_chart, alt_chart, chart_dt_str, chart_note = _find_optimal_chart_time(
            event_obj, observer, ts_time, sf_obj1
        )

        event_obj.target_altitude_deg = float(alt_chart)
        if chart_dt_str:
            event_obj.chart_datetime_utc = chart_dt_str
        if chart_note:
            event_obj.chart_time_note = chart_note

        sky_brightness = _compute_sky_brightness_at_time(
            event_obj, observer, ts_chart
        )
        obs_at_chart = observer.at(ts_chart)

        for obj_name in main_objs:
            sf_obj = _resolve_skyfield_object(str(obj_name))
            if sf_obj is not None:
                app = obs_at_chart.observe(sf_obj).apparent()
                alt_o, az_o, _ = app.altaz()
                alt_v, az_v = float(alt_o.degrees), float(az_o.degrees)
                if not math.isnan(alt_v) and not math.isnan(az_v):
                    all_positions.append((az_v, alt_v))
    except (ValueError, KeyError, AttributeError, TypeError, RuntimeError) as e:
        logger.debug(f"Could not compute topocentric positions for target objects: {e}")
        sky_brightness = getattr(event_obj, "sky_brightness", "NIGHT_DARK")

    p1_pos_draw, p2_pos_draw = _resolve_fallback_positions(
        event_obj, all_positions, main_objs, sep_deg
    )
    all_positions_draw = [(az, max(1.0, alt)) for az, alt in all_positions]

    return p1_pos_draw, p2_pos_draw, all_positions_draw, sky_brightness
