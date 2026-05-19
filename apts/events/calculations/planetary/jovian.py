import logging
import time
from datetime import timezone

from .... import skyfield_searches
from ...rarity import get_rarity
from ...duration import get_duration

logger = logging.getLogger(__name__)
utc = timezone.utc

def calculate_jovian_moon_events(observer, start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_jovian_moon_events(
        observer, start_date, end_date
    )
    for event in events:
        event["rarity"] = get_rarity("Jovian Moon Event", event)
        event["duration"] = get_duration("Jovian Moon Event", event)
    logger.debug(f"--- calculate_jovian_moon_events: {time.time() - start_time}s")
    return events

def calculate_saturn_ring_crossings(start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_saturn_ring_crossings(
        start_date, end_date
    )
    for event in events:
        event["date"] = event["date"].astimezone(utc)
        event["rarity"] = get_rarity("Saturn Ring Crossing", event)
        event["duration"] = get_duration("Saturn Ring Crossing", event)
    logger.debug(
        f"--- calculate_saturn_ring_crossings: {time.time() - start_time}s"
    )
    return events

def calculate_jupiter_grs_transits(observer, start_date, end_date, grs_longitude=None):
    start_time = time.time()
    events = skyfield_searches.find_jupiter_grs_transits(
        observer, start_date, end_date, grs_longitude=grs_longitude
    )
    for event in events:
        event["rarity"] = get_rarity("Jupiter GRS Transit", event)
        event["duration"] = get_duration("Jupiter GRS Transit", event)
    logger.debug(f"--- calculate_jupiter_grs_transits: {time.time() - start_time}s")
    return events

def calculate_jovian_mutual_events(observer, start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_jovian_mutual_events(
        observer, start_date, end_date
    )
    for event in events:
        event["rarity"] = get_rarity(event["type"], event)
        event["duration"] = get_duration(event["type"], event)
    logger.debug(f"--- calculate_jovian_mutual_events: {time.time() - start_time}s")
    return events
