import logging
import time

from .... import skyfield_searches
from ...rarity import get_rarity
from ...duration import get_duration

logger = logging.getLogger(__name__)

def calculate_planet_alignments(observer, start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_planet_alignments(
        observer, start_date, end_date
    )
    for event in events:
        event["type"] = "Planet Alignment"
        event["rarity"] = get_rarity("Planet Alignment", event)
        event["duration"] = get_duration("Planet Alignment", event)
    logger.debug(f"--- calculate_planet_alignments: {time.time() - start_time}s")
    return events

def calculate_planet_planet_occultations(observer, start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_planet_planet_occultations(
        observer, start_date, end_date
    )
    for event in events:
        event["rarity"] = get_rarity("Planet-Planet Occultation", event)
        event["duration"] = get_duration("Planet-Planet Occultation", event)
    logger.debug(
        f"--- calculate_planet_planet_occultations: {time.time() - start_time}s"
    )
    return events
