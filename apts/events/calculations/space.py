import logging
import time
from datetime import timezone
import requests
from dateutil.parser import parse as parse_date
from skyfield.api import Topos

from ... import skyfield_searches
from ...utils.network import get_session
from ..rarity import get_rarity
from ..duration import get_duration

logger = logging.getLogger(__name__)
utc = timezone.utc

def calculate_space_launches(start_date, end_date):
    start_time = time.time()
    events = []
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")
    url = f"https://ll.thespacedevs.com/2.2.0/launch/upcoming/?window_start__gte={start_date_str}&window_end__lte={end_date_str}"
    try:
        response = get_session().get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        for launch in data.get("results", []):
            event_data = {
                "date": parse_date(launch["window_start"]).astimezone(utc),
                "event": launch["name"],
                "type": "Space Launch",
            }
            event_data["rarity"] = get_rarity("Space Launch", event_data)
            event_data["duration"] = get_duration("Space Launch", event_data)
            events.append(event_data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching space launches: {e}")
    logger.debug(f"--- calculate_space_launches: {time.time() - start_time}s")
    return events

def calculate_space_events(start_date, end_date):
    start_time = time.time()
    events = []
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")
    url = f"https://ll.thespacedevs.com/2.2.0/event/upcoming/?date__gte={start_date_str}&date__lte={end_date_str}"
    try:
        response = get_session().get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        for event in data.get("results", []):
            event_data = {
                "date": parse_date(event["date"]).astimezone(utc),
                "event": event["name"],
                "type": "Space Event",
            }
            event_data["rarity"] = get_rarity("Space Event", event_data)
            event_data["duration"] = get_duration("Space Event", event_data)
            events.append(event_data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching space events: {e}")
    logger.debug(f"--- calculate_space_events: {time.time() - start_time}s")
    return events

def calculate_iss_flybys(place, observer, start_date, end_date):
    start_time = time.time()
    topos_observer = Topos(
        latitude_degrees=place.lat_decimal,
        longitude_degrees=place.lon_decimal,
        elevation_m=place.elevation,
    )
    events = skyfield_searches.find_iss_flybys(
        topos_observer, observer, start_date, end_date
    )
    for event in events:
        event["rarity"] = get_rarity("ISS Flyby", event)
        event["duration"] = get_duration("ISS Flyby", event)
    logger.debug(f"--- calculate_iss_flybys: {time.time() - start_time}s")
    return events

def calculate_tiangong_flybys(place, observer, start_date, end_date):
    start_time = time.time()
    topos_observer = Topos(
        latitude_degrees=place.lat_decimal,
        longitude_degrees=place.lon_decimal,
        elevation_m=place.elevation,
    )
    events = skyfield_searches.find_tiangong_flybys(
        topos_observer, observer, start_date, end_date
    )
    for event in events:
        event["rarity"] = get_rarity("Tiangong Flyby", event)
        event["duration"] = get_duration("Tiangong Flyby", event)
    logger.debug(f"--- calculate_tiangong_flybys: {time.time() - start_time}s")
    return events
