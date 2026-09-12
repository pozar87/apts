import logging
import math
from typing import TYPE_CHECKING, Any

import numpy as np

from .constants import COMPASS_POINTS, LONG_EVENT_CATEGORIES

if TYPE_CHECKING:
    from apts.events.event import Event

logger = logging.getLogger(__name__)


def _get_compass_labels(az_min: float, az_max: float) -> list[tuple[float, str]]:
    """Returns compass direction labels that fall within the given azimuth window."""
    labels = []
    for deg, code in COMPASS_POINTS:
        d = deg
        if d < az_min and d + 360.0 <= az_max:
            d += 360.0
        elif d > az_max and d - 360.0 >= az_min:
            d -= 360.0

        if az_min <= d <= az_max:
            labels.append((d, code))

    return labels


def _hex_to_rgb(hex_str: str) -> np.ndarray:
    clean = hex_str.lstrip("#")
    return np.array([int(clean[i : i + 2], 16) / 255.0 for i in (0, 2, 4)])


def _parse_separation_deg(sep_str: str | None) -> float:
    """Parses angular separation degrees from string representation."""
    if not sep_str:
        return 1.2
    try:
        clean_sep = sep_str.replace("°", "").replace("'", "").strip()
        val = float(clean_sep)
        if "'" in sep_str:
            val = val / 60.0
        return max(0.2, min(5.0, val))
    except ValueError:
        return 1.2


def _get_satellite_name(event_obj: "Event") -> str:
    """Helper to derive clean satellite name (ISS, Tiangong, etc.) without generic fallback."""
    if event_obj.objects:
        obj_name = str(event_obj.objects[0])
        if obj_name and obj_name.lower() != "target":
            return obj_name

    title_lower = str(event_obj.title).lower()
    cat_lower = str(event_obj.category).lower()

    if "tiangong" in title_lower or "tiangong" in cat_lower or "css" in title_lower:
        return "Tiangong"
    if "iss" in title_lower or "iss" in cat_lower or "station" in title_lower:
        return "ISS"

    return "Satellite"


def _get_event_moon_phase_frac(event_obj: "Event") -> float:
    """Helper to determine float phase fraction (0.0-1.0) for Moon rendering."""
    p_val = getattr(event_obj, "extra_data", {}).get("phase")
    if isinstance(p_val, (int, float)):
        if float(p_val) > 1.0:
            return (float(p_val) % 360.0) / 360.0
        return float(p_val)

    title_lower = f"{event_obj.title} {event_obj.category} {p_val}".lower()
    if "first quarter" in title_lower or "pierwsza kwadra" in title_lower or "cuarto creciente" in title_lower or "erstes viertel" in title_lower or "primeiro quarto" in title_lower:
        return 0.25
    if "third quarter" in title_lower or "last quarter" in title_lower or "trzecia kwadra" in title_lower or "ostatnia kwadra" in title_lower or "cuarto menguante" in title_lower or "drittes viertel" in title_lower or "quarto minguante" in title_lower:
        return 0.75
    if "full moon" in title_lower or "pełnia" in title_lower or "luna llena" in title_lower or "vollmond" in title_lower or "lua cheia" in title_lower:
        return 0.5
    if "new moon" in title_lower or "nów" in title_lower or "luna nueva" in title_lower or "neumond" in title_lower or "lua nova" in title_lower:
        return 0.0

    return 0.25


def is_long_event(category: str, title: str = "") -> bool:
    """Checks if an event category or title represents a multi-hour / long-duration event."""
    cat = str(category).upper()
    title_lower = str(title).lower()
    if cat in LONG_EVENT_CATEGORIES:
        return True
    long_keywords = [
        "conjunction",
        "alignment",
        "opposition",
        "elongation",
        "phase",
        "shower",
        "solstice",
        "equinox",
    ]
    return any(kw in title_lower for kw in long_keywords)


def _compute_sky_brightness_at_time(
    event_obj: "Event", observer: Any, ts_chart: Any
) -> str:
    """Computes topocentric sky brightness classification at a specific chart observation time."""
    from apts.cache import get_ephemeris
    from apts.events.event import get_sky_brightness

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
    from datetime import timedelta

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

            ts_factory = getattr(ts_time, "ts", None) or getattr(
                getattr(event_obj, "place", None), "ts", None
            ) or get_timescale()

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
                alt_c_vec + np.where(sun_alt_c_vec < -0.833, 100.0, 0.0) - np.abs(offsets_hours) * 0.5,
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


def _resolve_skyfield_object(name_str: str) -> Any | None:
    """Attempts to resolve any string object name to a Skyfield object."""
    from skyfield.api import Star

    from apts.catalogs.messier import get_messier_raw
    from apts.catalogs.stars import get_bright_stars_raw
    from apts.utils import planetary

    if not name_str or not isinstance(name_str, str):
        return None

    clean = name_str.strip()
    clean_lower = clean.lower()

    # Common synonym mapping across languages
    synonyms = {
        "księżyc": "moon",
        "mond": "moon",
        "luna": "moon",
        "słońce": "sun",
        "sonne": "sun",
        "sol": "sun",
        "jowisz": "jupiter",
        "wenus": "venus",
        "mars": "mars",
        "saturn": "saturn",
        "merkury": "mercury",
        "merkur": "mercurio",
        "uran": "uranus",
        "neptun": "neptune",
    }
    lookup_name = synonyms.get(clean_lower, clean)

    # 1. Ephemeris (major / minor planets, Sun, Moon)
    try:
        return planetary.get_skyfield_obj(lookup_name)
    except (ValueError, KeyError, RuntimeError, AttributeError):
        pass

    # 2. Messier catalog
    try:
        messier_df = get_messier_raw()
        m_match = messier_df[
            messier_df["Messier"].str.lower() == clean_lower
        ]
        if m_match.empty:
            m_match = messier_df[
                messier_df["Messier"].str.lower() == f"m{clean_lower.replace('messier', '').strip()}"
            ]
        if not m_match.empty:
            row = m_match.iloc[0]
            return Star(ra_hours=float(row["ra_hours"]), dec_degrees=float(row["dec_degrees"]))
    except (ValueError, KeyError, RuntimeError, AttributeError):
        pass

    # 3. Bright stars catalog
    try:
        stars_df = get_bright_stars_raw()
        s_match = stars_df[stars_df["Name"].str.lower() == clean_lower]
        if not s_match.empty:
            row = s_match.iloc[0]
            st_obj = row.get("skyfield_object")
            if st_obj is not None:
                return st_obj
            return Star(ra_hours=float(row["ra_hours"]), dec_degrees=float(row["dec_degrees"]))
    except (ValueError, KeyError, RuntimeError, AttributeError):
        pass

    return None


def _get_observer_for_event(event_obj: "Event") -> tuple[Any, Any]:
    """Returns Skyfield observer object and Skyfield time for the event moment."""
    place = getattr(event_obj, "place", None)
    if place is not None and hasattr(place, "observer") and hasattr(place, "ts"):
        dt_utc = event_obj.dt_utc
        ts_time = place.ts.utc(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour, dt_utc.minute, dt_utc.second)
        return place.observer, ts_time

    # Default Topos observer if place is missing
    from skyfield.api import Topos

    from apts.cache import get_ephemeris, get_timescale

    ts = get_timescale()
    eph = get_ephemeris()
    dt_utc = event_obj.dt_utc
    ts_time = ts.utc(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour, dt_utc.minute, dt_utc.second)
    lat = float(getattr(event_obj, "extra_data", {}).get("lat", 52.2))
    lon = float(getattr(event_obj, "extra_data", {}).get("lon", 21.0))
    observer = eph["earth"] + Topos(latitude_degrees=lat, longitude_degrees=lon)
    return observer, ts_time


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

        sky_brightness = _compute_sky_brightness_at_time(event_obj, observer, ts_chart)
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

    # Primary position priority:
    # 1. Computed topocentric position from primary object
    # 2. Event azimuth_deg / altitude_deg if explicitly provided
    # 3. Fallback default (90.0, 25.0)
    if all_positions:
        p1_pos = all_positions[0]
    elif event_obj.azimuth_deg is not None and event_obj.altitude_deg is not None:
        p1_pos = (float(event_obj.azimuth_deg), float(event_obj.altitude_deg))
    elif event_obj.azimuth_deg is not None:
        p1_pos = (float(event_obj.azimuth_deg), 25.0)
    else:
        p1_pos = (90.0, 25.0)

    # Clamp drawing altitude to >= 1.0 deg so no object is drawn below horizon
    p1_pos_draw = (p1_pos[0], max(1.0, p1_pos[1]))

    # Secondary position priority:
    if len(all_positions) >= 2:
        p2_pos = all_positions[1]
        p2_pos_draw = (p2_pos[0], max(1.0, p2_pos[1]))
    elif len(main_objs) >= 2 or event_obj.angular_separation:
        p2_pos = (p1_pos[0] + sep_deg * 0.8, p1_pos[1] + sep_deg * 0.6)
        p2_pos_draw = (p2_pos[0], max(1.0, p2_pos[1]))
    else:
        p2_pos_draw = None

    all_positions_draw = [(az, max(1.0, alt)) for az, alt in all_positions]

    return p1_pos_draw, p2_pos_draw, all_positions_draw, sky_brightness
