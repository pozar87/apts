import logging
import time
from datetime import timezone
from concurrent.futures import as_completed

from .... import skyfield_searches
from ....utils import planetary
from ...rarity import get_rarity
from ...duration import get_duration

logger = logging.getLogger(__name__)
utc = timezone.utc

def calculate_oppositions(observer, start_date, end_date, executor):
    start_time = time.time()
    events = []
    planets = planetary.OPPOSITION_PLANETS
    futures = [
        executor.submit(
            skyfield_searches.find_oppositions,
            observer,
            p,
            start_date,
            end_date,
        )
        for p in planets
    ]
    for future in as_completed(futures):
        found_events = future.result()
        for event in found_events:
            event["type"] = "Opposition"
            simple_name = planetary.get_simple_name(event["planet"])
            event["event"] = "Opposition"
            event["object"] = simple_name
            del event["planet"]
            event["rarity"] = get_rarity("Opposition", event)
            event["duration"] = get_duration("Opposition", event)
        events.extend(found_events)
    logger.debug(f"--- calculate_oppositions: {time.time() - start_time}s")
    return events

def calculate_aphelion_perihelion(start_date, end_date, executor):
    start_time = time.time()
    events = []
    planets = planetary.APHELION_PERIHELION_PLANETS
    futures = [
        executor.submit(
            skyfield_searches.find_aphelion_perihelion,
            planet_name,
            start_date,
            end_date,
        )
        for planet_name in planets
    ]
    for future in as_completed(futures):
        events_from_search = future.result()
        for event_dict in events_from_search:
            simple_name = planetary.get_simple_name(event_dict["planet"])
            event_dict["event"] = event_dict["event_type"]
            event_dict["object"] = simple_name
            del event_dict["planet"]
            del event_dict["event_type"]
            event_dict["date"] = event_dict["date"].astimezone(utc)  # type: ignore
            event_dict["type"] = "Aphelion/Perihelion"
            event_dict["rarity"] = get_rarity(
                "Aphelion/Perihelion", event_dict
            )
            event_dict["duration"] = get_duration("Aphelion/Perihelion", event_dict)
            events.append(event_dict)
    logger.debug(f"--- calculate_aphelion_perihelion: {time.time() - start_time}s")
    return events

def calculate_mars_closest_approach(observer, start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_mars_closest_approach(
        start_date, end_date, observer=observer
    )
    for event in events:
        event["rarity"] = get_rarity("Mars Closest Approach", event)
        event["duration"] = get_duration("Mars Closest Approach", event)
    logger.debug(f"--- calculate_mars_closest_approach: {time.time() - start_time}s")
    return events
