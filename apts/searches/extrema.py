from .. import skyfield_searches


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
