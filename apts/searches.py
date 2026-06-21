from . import skyfield_searches
from .cache import get_ephemeris


def _get_observer(eph):
    """
    Returns a geocentric observer (Earth) from the ephemeris.
    Standard astronomical conjunctions and extrema are often defined geocentrically.
    """
    if eph is None:
        eph = get_ephemeris()
    # Check if eph is already an observer-like object (e.g. Earth + Topos)
    # or if it's the ephemeris dictionary.
    try:
        return eph["earth"]
    except (TypeError, KeyError):
        return eph


def find_highest_altitude(observer, planet, start_date, end_date):
    """
    Delegates to the optimized version in skyfield_searches.
    """
    return skyfield_searches.find_highest_altitude(observer, planet, start_date, end_date)


def find_aphelion_perihelion(eph, planet_name, start_date, end_date):
    """
    Delegates to the optimized version in skyfield_searches.
    The eph parameter is used to determine the geocentric reference.
    """
    new_events = skyfield_searches.find_aphelion_perihelion(
        planet_name, start_date, end_date
    )
    # Legacy format: {"date": ..., "event": "Mars Aphelion"}
    return [
        {
            "date": e["date"],
            "event": f"{e['planet'].capitalize()} {e['event_type']}",
        }
        for e in new_events
    ]


def find_moon_apogee_perigee(eph, start_date, end_date):
    """
    Delegates to the optimized version in skyfield_searches.
    """
    new_events = skyfield_searches.find_moon_apogee_perigee(start_date, end_date)
    # Legacy format: {"date": ..., "event": "Moon Apogee"}
    return [
        {
            "date": e["date"],
            "event": f"Moon {e['event']}",
        }
        for e in new_events
    ]


def find_conjunctions(
    eph, p1_name, p2_name, start_date, end_date, threshold_degrees=None
):
    """
    Delegates to the optimized version in skyfield_searches.
    """
    observer = _get_observer(eph)
    events = skyfield_searches.find_conjunctions(
        observer, p1_name, p2_name, start_date, end_date, threshold_degrees
    )
    # Add legacy 'event' key for backward compatibility
    for e in events:
        if "event" not in e:
            e["event"] = f"{p1_name.capitalize()} conjunct {p2_name.capitalize()}"
    return events


def find_mercury_inferior_conjunctions(eph, start_date, end_date, threshold_degrees=5.0):
    """
    Delegates to the optimized version in skyfield_searches.
    """
    observer = _get_observer(eph)
    return skyfield_searches.find_mercury_inferior_conjunctions(
        observer, start_date, end_date, threshold_degrees
    )


def find_lunar_occultations(observer, eph, bright_stars, start_date, end_date):
    """
    Delegates to the optimized version in skyfield_searches.
    """
    events = skyfield_searches.find_lunar_occultations(
        observer, bright_stars, start_date, end_date
    )
    # Adapt to legacy 'event' string if necessary
    for e in events:
        if "object2" in e:
            e["event"] = f"Moon occults {e['object2']}"
    return events
