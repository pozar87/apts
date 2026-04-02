import logging
import time
from datetime import timezone
from dateutil.parser import parse as parse_date

from ... import skyfield_searches, cache
from ..rarity import get_rarity

logger = logging.getLogger(__name__)
utc = timezone.utc

def calculate_meteor_showers(observer, start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_meteor_showers(
        observer, start_date, end_date
    )
    for event in events:
        event["date"] = event["date"].astimezone(utc)
        event["rarity"] = get_rarity("Meteor Shower", event)
    logger.debug(f"--- calculate_meteor_showers: {time.time() - start_time}s")
    return events

def calculate_solar_eclipses(observer, start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_solar_eclipses(
        observer, start_date, end_date
    )
    for event in events:
        kind = event.get("eclipse_type", "")
        event["event"] = f"{kind} Solar Eclipse"
        event["type"] = "Solar Eclipse"
        event["rarity"] = get_rarity("Solar Eclipse", event)
    logger.debug(f"--- calculate_solar_eclipses: {time.time() - start_time}s")
    return events

def calculate_golden_blue_hours(observer, start_date, end_date, event_settings):
    start_time = time.time()
    events = skyfield_searches.find_golden_blue_hours(
        observer, start_date, end_date
    )
    show_golden = event_settings.get("golden_hour")
    show_blue = event_settings.get("blue_hour")

    filtered_events = [
        e
        for e in events
        if (e["type"] == "Golden Hour" and show_golden)
        or (e["type"] == "Blue Hour" and show_blue)
    ]

    for event in filtered_events:
        event["rarity"] = 1

    logger.debug(f"--- calculate_golden_blue_hours: {time.time() - start_time}s")
    return filtered_events

def calculate_culminations(observer, start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_culminations(
        observer, start_date, end_date
    )
    for event in events:
        event["rarity"] = 2
    logger.debug(f"--- calculate_culminations: {time.time() - start_time}s")
    return events

def calculate_messier_culminations(observer, start_date, end_date, messier_catalog):
    start_time = time.time()
    messier_data = list(
        zip(
            messier_catalog["Messier"],
            messier_catalog["skyfield_object"],
        )
    )

    events = skyfield_searches.find_object_culminations(
        observer,
        messier_data,
        start_date,
        end_date,
    )

    for event in events:
        event["rarity"] = get_rarity("Messier Culmination", event)

    logger.debug(f"--- calculate_messier_culminations: {time.time() - start_time}s")
    return events

def calculate_seasons(start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_seasons(start_date, end_date)
    for event in events:
        event["rarity"] = get_rarity("Season", event)
    logger.debug(f"--- calculate_seasons: {time.time() - start_time}s")
    return events

def calculate_nasa_comets(start_date, end_date):
    start_time = time.time()
    events = []
    try:
        comets = cache.get_nasa_comets_data(start_date, end_date)
        for name, close_approach_data in zip(
            comets["name"], comets["close_approach_data"]
        ):
            event_data = {
                "date": parse_date(
                    close_approach_data[0]["close_approach_date_full"]  # type: ignore
                ).astimezone(utc),
                "event": name,
                "type": "Comet",
            }
            event_data["rarity"] = get_rarity("Comet", event_data)
            events.append(event_data)
    except Exception as e:
        logger.error(f"Error calculating NASA comets: {e}")
    logger.debug(f"--- calculate_nasa_comets: {time.time() - start_time}s")
    return events
