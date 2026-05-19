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

def calculate_venus_greatest_brilliancy(observer, start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_venus_greatest_brilliancy(
        observer, start_date, end_date
    )
    for event in events:
        event["rarity"] = get_rarity("Venus Greatest Brilliancy", event)
        event["duration"] = get_duration("Venus Greatest Brilliancy", event)
    logger.debug(
        f"--- calculate_venus_greatest_brilliancy: {time.time() - start_time}s"
    )
    return events

def calculate_highest_altitudes(observer, start_date, end_date, executor):
    start_time = time.time()
    events = []
    futures = {
        executor.submit(
            skyfield_searches.find_highest_altitude,
            observer,
            planetary.get_skyfield_obj(planet_name),
            start_date,
            end_date,
        ): planet_name
        for planet_name in ["mercury", "venus"]
    }
    for future in as_completed(futures):
        planet_name = futures[future]
        t, alt = future.result()
        if t:
            simple_name = planetary.get_simple_name(planet_name)
            event_data = {
                "date": t.astimezone(utc),  # type: ignore
                "event": "Highest altitude",
                "object": simple_name,
                "type": "Planet Altitude",
                "altitude": alt,
            }
            event_data["rarity"] = get_rarity("Planet Altitude", event_data)
            event_data["duration"] = get_duration("Planet Altitude", event_data)
            events.append(event_data)
    logger.debug(f"--- calculate_highest_altitudes: {time.time() - start_time}s")
    return events

def calculate_greatest_elongations(observer, start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_greatest_elongations(
        observer, start_date, end_date
    )
    for event in events:
        event["rarity"] = get_rarity("Greatest Elongation", event)
        event["duration"] = get_duration("Greatest Elongation", event)
    logger.debug(f"--- calculate_greatest_elongations: {time.time() - start_time}s")
    return events

def calculate_planetary_dichotomy(observer, start_date, end_date, precomputed_positions=None):
    start_time = time.time()
    events = skyfield_searches.find_planetary_dichotomy(
        observer,
        start_date,
        end_date,
        precomputed_positions=precomputed_positions,
    )
    for event in events:
        event["rarity"] = get_rarity("Planetary Dichotomy", event)
        event["duration"] = get_duration("Planetary Dichotomy", event)
    logger.debug(f"--- calculate_planetary_dichotomy: {time.time() - start_time}s")
    return events

def calculate_planet_stationary_points(observer, start_date, end_date):
    start_time = time.time()
    events = []
    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
        "pluto barycenter",
    ]
    for p in planets:
        found_events = skyfield_searches.find_stationary_points(
            observer,
            p,
            start_date,
            end_date,
        )
        for event in found_events:
            event["rarity"] = get_rarity("Planet Stationary Point", event)
            event["duration"] = get_duration("Planet Stationary Point", event)
        events.extend(found_events)
    logger.debug(
        f"--- calculate_planet_stationary_points: {time.time() - start_time}s"
    )
    return events
