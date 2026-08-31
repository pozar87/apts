from .. import skyfield_searches
from .utils import _get_observer


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
