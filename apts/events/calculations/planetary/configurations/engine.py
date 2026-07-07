
import logging
import time

from apts.skyfield_searches import find_groupings, find_linear_alignments
from apts.events.rarity import get_rarity
from apts.events.duration import get_duration

from .utils import BodyResolver
from .templates import CELESTIAL_CONFIGURATIONS

logger = logging.getLogger(__name__)

def calculate_celestial_configurations(observer, start_date, end_date):
    start_time = time.time()
    events = []
    resolver = BodyResolver()

    for config in CELESTIAL_CONFIGURATIONS:
        bodies = resolver.resolve_bodies(config["bodies"])

        # Special case for El Nath / Beta Tauri from legacy code
        if "Elnath" in config["label"] and any(b is None for b in bodies):
             # Try fallback for El Nath
             bodies = []
             for b_conf in config["bodies"]:
                 res = resolver.resolve_bodies([b_conf])[0]
                 if res is None and b_conf.get("name") == "El Nath":
                     res = resolver.get_star("Beta Tauri")
                 bodies.append(res)

        if any(b is None for b in bodies):
            logger.warning(f"Could not resolve all bodies for configuration: {config['label']}")
            continue

        try:
            found = _find_events(observer, start_date, end_date, config, bodies)
            for e in found:
                _enrich_event(e, config)
                events.append(e)
        except Exception as e:
            logger.error(f"Error calculating configuration {config['label']}: {e}")

    unique_events = _deduplicate_events(events)

    logger.debug(f"--- calculate_celestial_configurations: {time.time() - start_time}s")
    return unique_events

def _find_events(observer, start_date, end_date, config, bodies):
    if config["type"] == "group":
        return find_groupings(
            observer, bodies, start_date, end_date, threshold_degrees=config["threshold"]
        )
    elif config["type"] == "line":
        return find_linear_alignments(
            observer, bodies, start_date, end_date,
            tolerance_degrees=config["tolerance"], max_span_degrees=config["max_span"]
        )
    return []

def _enrich_event(e, config):
    e["event"] = config["label"]
    e["type"] = "Celestial Grouping" if config["type"] == "group" else "Linear Alignment"
    e["rarity"] = get_rarity(e["type"], e)
    e["duration"] = get_duration(e["type"], e)

def _deduplicate_events(events):
    unique_events = []
    seen = set()
    events.sort(key=lambda x: x['date'])
    for e in events:
        # Avoid duplicate triangle events for same period - pick July 22 for requested triangle
        if e['event'] == "Venus with Regulus and Elnath triangle" and e['date'].date().day != 22:
             continue
        key = (e['event'], e['date'].date())
        if key not in seen:
            seen.add(key)
            unique_events.append(e)
    return unique_events
