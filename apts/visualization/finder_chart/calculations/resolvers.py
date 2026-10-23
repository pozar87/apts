import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from apts.events.event import Event

logger = logging.getLogger(__name__)


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
        m_match = messier_df[messier_df["Messier"].str.lower() == clean_lower]
        if m_match.empty:
            m_match = messier_df[
                messier_df["Messier"].str.lower()
                == f"m{clean_lower.replace('messier', '').strip()}"
            ]
        if not m_match.empty:
            row = m_match.iloc[0]
            return Star(
                ra_hours=float(row["ra_hours"]), dec_degrees=float(row["dec_degrees"])
            )
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
            return Star(
                ra_hours=float(row["ra_hours"]), dec_degrees=float(row["dec_degrees"])
            )
    except (ValueError, KeyError, RuntimeError, AttributeError):
        pass

    return None


def _get_observer_for_event(event_obj: "Event") -> tuple[Any, Any]:
    """Returns Skyfield observer object and Skyfield time for the event moment."""
    place = getattr(event_obj, "place", None)
    if place is not None and hasattr(place, "observer") and hasattr(place, "ts"):
        dt_utc = event_obj.dt_utc
        ts_time = place.ts.utc(
            dt_utc.year,
            dt_utc.month,
            dt_utc.day,
            dt_utc.hour,
            dt_utc.minute,
            dt_utc.second,
        )
        return place.observer, ts_time

    # Default Topos observer if place is missing
    from skyfield.api import Topos

    from apts.cache import get_ephemeris, get_timescale

    ts = get_timescale()
    eph = get_ephemeris()
    dt_utc = event_obj.dt_utc
    ts_time = ts.utc(
        dt_utc.year,
        dt_utc.month,
        dt_utc.day,
        dt_utc.hour,
        dt_utc.minute,
        dt_utc.second,
    )
    lat = float(getattr(event_obj, "extra_data", {}).get("lat", 52.2))
    lon = float(getattr(event_obj, "extra_data", {}).get("lon", 21.0))
    observer = eph["earth"] + Topos(latitude_degrees=lat, longitude_degrees=lon)
    return observer, ts_time
