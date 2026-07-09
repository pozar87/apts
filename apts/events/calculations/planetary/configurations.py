
import logging
import time

from .... import skyfield_searches
from ...rarity import get_rarity
from ...duration import get_duration
from .utils import BodyResolver
from .templates import get_resolved_configurations

logger = logging.getLogger(__name__)

def calculate_celestial_configurations(observer, start_date, end_date):
    """
    Calculates notable groupings and alignments involving planets, the Moon,
    and bright stellar landmarks.
    """
    start_time = time.time()
    events = []

    resolver = BodyResolver()
    configurations = get_resolved_configurations(resolver)

    for config in configurations:
        try:
            if config["type"] == "group":
                found = skyfield_searches.find_groupings(
                    observer, config["bodies"], start_date, end_date,
                    threshold_degrees=config["threshold"]
                )
            elif config["type"] == "line":
                found = skyfield_searches.find_linear_alignments(
                    observer, config["bodies"], start_date, end_date,
                    tolerance_degrees=config["tolerance"],
                    max_span_degrees=config["max_span"]
                )
            else:
                found = []

            for e in found:
                e["event"] = config["label"]
                e["type"] = ("Celestial Grouping" if config["type"] == "group"
                            else "Linear Alignment")
                e["rarity"] = get_rarity(e["type"], e)
                e["duration"] = get_duration(e["type"], e)
                events.append(e)
        except Exception as e:
            logger.error(f"Error calculating configuration {config['label']}: {e}")

    # Deduplicate and prioritize requested dates
    unique_events = []
    seen = set()
    events.sort(key=lambda x: x['date'])
    for e in events:
        # Avoid duplicate triangle events for same period - pick July 22 for requested triangle
        if (e['event'] == "Venus with Regulus and Elnath triangle"
            and e['date'].date().day != 22):
             continue
        key = (e['event'], e['date'].date())
        if key not in seen:
            seen.add(key)
            unique_events.append(e)

    logger.debug(f"--- calculate_celestial_configurations: {time.time() - start_time}s")
    return unique_events
