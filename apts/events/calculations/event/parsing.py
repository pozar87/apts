import math
from datetime import datetime, timezone
from typing import Any

from .categories import get_event_category
from .direction import DirectionData, get_direction_data, get_sky_brightness

utc = timezone.utc


def _parse_event_datetime(data: dict[str, Any]) -> datetime:
    """Parses event UTC datetime from data dictionary."""
    raw_date = data.get("date") or data.get("datetime_utc") or datetime.now(utc)
    if isinstance(raw_date, str):
        try:
            clean_ts = raw_date.replace("Z", "+00:00")
            dt = datetime.fromisoformat(clean_ts)
        except ValueError:
            dt = datetime.now(utc)
    elif isinstance(raw_date, datetime):
        dt = raw_date
    elif hasattr(raw_date, "to_pydatetime"):
        dt = raw_date.to_pydatetime()
    else:
        dt = datetime.now(utc)

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=utc)

    return dt.astimezone(utc)


def _fallback_extract_sun_moon_objects(data: dict[str, Any]) -> list[str]:
    """Infers fallback Moon or Sun celestial target objects based on category and event keywords."""
    event_name = str(data.get("event") or data.get("title") or "").lower()
    event_type = str(data.get("type") or "").lower()
    category = str(data.get("category") or get_event_category(event_name, event_type)).upper()

    moon_kws = ["moon", "quarter", "crescent", "gibbous", "full moon", "new moon", "księżyc", "mond", "luna", "libration", "supermoon", "lunar"]
    sun_kws = ["sun", "solstice", "equinox", "słońce", "sonne", "sol", "autumnal", "vernal", "equinoccio", "solsticio", "tagundnachtgleiche", "równonoc", "przesilenie"]

    if category in ("MOON_PHASE", "SUPERMOON", "MOON_LIBRATION", "LUNAR_FEATURE", "LUNAR_ECLIPSE") or any(kw in event_name or kw in event_type for kw in moon_kws):
        return ["Moon"]
    if category in ("EQUINOX_SOLSTICE", "SOLAR_ECLIPSE") or any(kw in event_name or kw in event_type for kw in sun_kws):
        return ["Sun"]

    return []


def _extract_event_objects(data: dict[str, Any]) -> list[str]:
    """Extracts involved celestial object names from event record dictionary."""
    objs = []
    if data.get("object1"):
        objs.append(str(data["object1"]))
    if data.get("object2"):
        objs.append(str(data["object2"]))
    if not objs and "object" in data and data["object"]:
        objs.append(str(data["object"]))
    if not objs and "shower_name" in data and data["shower_name"]:
        objs.append(str(data["shower_name"]))
    if not objs and "planets" in data and data["planets"]:
        p_val = data["planets"]
        if isinstance(p_val, list):
            objs.extend([str(p) for p in p_val])
        elif isinstance(p_val, str):
            objs.append(p_val)

    if not objs:
        objs = _fallback_extract_sun_moon_objects(data)

    return objs


def _build_event_title(data: dict[str, Any], objs: list[str], category: str, event_name: str) -> str:
    """Constructs display title for the event if explicit title is absent."""
    title = data.get("title")
    if title:
        return title

    if len(objs) >= 2 and category == "OCCULTATION":
        return f"{objs[0].title()} occultation of {objs[1].title()}"
    if len(objs) >= 2 and category == "CONJUNCTION":
        return f"Conjunction of {objs[0].title()} and {objs[1].title()}"
    if objs and category == "METEOR_SHOWER":
        return f"{objs[0]} Meteor Shower Peak"

    return str(event_name)


def _format_angular_separation(data: dict[str, Any]) -> str | None:
    """Formats angular separation string from event dictionary."""
    angular_sep = data.get("angular_separation")
    if not angular_sep and "separation_degrees" in data and data["separation_degrees"] is not None:
        sep_val = float(data["separation_degrees"])
        if sep_val < 1.0:
            return f"{round(sep_val * 60.0, 1)}'"
        return f"{round(sep_val, 1)}°"
    return angular_sep


def _extract_coordinates(data: dict[str, Any]) -> tuple[float | None, float | None]:
    """Extracts float azimuth and altitude degrees from event dictionary."""
    azimuth_deg = data.get("azimuth") or data.get("azimuth_deg")
    altitude_deg = data.get("altitude") or data.get("altitude_deg")
    return (
        float(azimuth_deg) if azimuth_deg is not None else None,
        float(altitude_deg) if altitude_deg is not None else None,
    )


def parse_event_datetime(datetime_utc: datetime | str) -> tuple[datetime, str]:
    """Parses datetime input into a UTC datetime object and ISO string."""
    if isinstance(datetime_utc, datetime):
        if datetime_utc.tzinfo is None:
            datetime_utc = datetime_utc.replace(tzinfo=utc)
        dt_utc = datetime_utc.astimezone(utc)
        datetime_utc_str = dt_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    else:
        datetime_utc_str = str(datetime_utc)
        try:
            clean_ts = datetime_utc_str.replace("Z", "+00:00")
            dt_utc = datetime.fromisoformat(clean_ts).astimezone(utc)
        except ValueError:
            dt_utc = datetime.now(utc)
    return dt_utc, datetime_utc_str


def resolve_topocentric_state(
    place: Any,
    dt_utc: datetime,
    objects: list[str],
    azimuth_deg: float | None,
    altitude_deg: float | None,
    extra_data: dict[str, Any],
) -> tuple[float | None, float | None, str]:
    """Resolves topocentric object position and sky brightness classification."""
    import logging
    logger = logging.getLogger(__name__)

    sun_alt = extra_data.get("sun_altitude")
    moon_alt = extra_data.get("moon_altitude")
    phase = extra_data.get("phase", 0.0)
    phase_frac = float(phase) if isinstance(phase, (int, float)) else 0.0

    if place is not None and hasattr(place, "get_altitude"):
        try:
            t_sf = place.ts.utc(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour, dt_utc.minute, dt_utc.second)
            if sun_alt is None:
                sun_alt = place.get_altitude(place.sun, t_sf)
                moon_alt = place.get_altitude(place.moon, t_sf)
            if (azimuth_deg is None or altitude_deg is None) and objects:
                alt_primary = place.get_altitude(objects[0], t_sf)
                az_primary = place.get_azimuth(objects[0], t_sf)
                if not math.isnan(alt_primary) and not math.isnan(az_primary):
                    altitude_deg = float(alt_primary)
                    azimuth_deg = float(az_primary)
        except (ValueError, KeyError, AttributeError, TypeError) as e:
            logger.debug(f"Could not resolve topocentric position for primary object: {e}")

    sky_brightness = get_sky_brightness(sun_alt, moon_alt, phase_frac)
    return azimuth_deg, altitude_deg, sky_brightness


def resolve_horizon_and_chart_metadata(
    altitude_deg: float | None,
    extra_data: dict[str, Any],
) -> tuple[bool, str | None, str | None, float | None]:
    """Evaluates horizon status, chart datetime notes, and target altitude."""
    is_below_horizon = bool(extra_data.get("is_below_horizon", False))
    chart_datetime_utc = extra_data.get("chart_datetime_utc")
    chart_time_note = extra_data.get("chart_time_note")
    target_altitude_deg = (
        float(extra_data["target_altitude_deg"])
        if "target_altitude_deg" in extra_data and extra_data["target_altitude_deg"] is not None
        else altitude_deg
    )

    if altitude_deg is not None:
        if target_altitude_deg is None:
            target_altitude_deg = float(altitude_deg)
        if altitude_deg < 0.0:
            is_below_horizon = True

    return is_below_horizon, chart_datetime_utc, chart_time_note, target_altitude_deg


def resolve_direction_data(
    direction: DirectionData | dict[str, Any] | None,
    azimuth_deg: float | None,
) -> DirectionData:
    """Constructs DirectionData instance from raw direction or azimuth input."""
    if isinstance(direction, DirectionData):
        return direction
    if isinstance(direction, dict):
        return DirectionData(
            code=direction.get("code", "E"),
            name=direction.get("name", "Look East"),
            azimuth_deg=float(direction.get("azimuth_deg", azimuth_deg if azimuth_deg is not None else 90.0)),
        )
    return get_direction_data(azimuth_deg)
