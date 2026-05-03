from typing import Any, cast

from skyfield import almanac
from ...cache import get_timescale, get_ephemeris


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
