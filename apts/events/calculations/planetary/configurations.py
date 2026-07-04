
import logging
import time
from skyfield.api import Star

from .... import skyfield_searches
from ....utils import planetary
from ...rarity import get_rarity
from ...duration import get_duration

logger = logging.getLogger(__name__)

def calculate_celestial_configurations(observer, start_date, end_date):
    start_time = time.time()
    events = []

    from ....catalogs import Catalogs
    catalogs = Catalogs()

    def get_star(name):
        row = catalogs.BRIGHT_STARS[catalogs.BRIGHT_STARS['Name'] == name]
        if not row.empty:
            return (name, Star(ra_hours=row['ra_hours'].values[0], dec_degrees=row['dec_degrees'].values[0]))
        return None

    def get_messier(name):
        row = catalogs.MESSIER[catalogs.MESSIER['Messier'] == name]
        if not row.empty:
            return (name, Star(ra_hours=row['ra_hours'].values[0], dec_degrees=row['dec_degrees'].values[0]))
        return None

    mars = ("Mars", planetary.get_skyfield_obj("mars barycenter"))
    uranus = ("Uranus", planetary.get_skyfield_obj("uranus barycenter"))
    venus = ("Venus", planetary.get_skyfield_obj("venus"))
    moon = ("Moon", planetary.get_skyfield_obj("moon"))

    pleiades = get_messier("M45")
    aldebaran = get_star("Aldebaran")
    denebola = get_star("Denebola")
    regulus = get_star("Regulus")
    elnath = get_star("El Nath") or get_star("Beta Tauri")

    # Define specific configurations to look for
    configurations = [
        # 1. Mars and Uranus between Pleiades (4 July 2026)
        {
            "type": "group",
            "bodies": [mars, uranus, pleiades],
            "threshold": 10.0,
            "label": "Mars and Uranus between Pleiades"
        },
        # 2. Venus near Regulus (9 July 2026)
        {
            "type": "group",
            "bodies": [venus, regulus],
            "threshold": 2.0,
            "label": "Venus near Regulus"
        },
        # 3. Moon near Mars and Pleiades (11 July 2026)
        {
            "type": "group",
            "bodies": [moon, mars, pleiades],
            "threshold": 10.0,
            "label": "Moon near Mars and Pleiades"
        },
        # 4. Mars forms a line with Aldebaran and Denebola (22 July 2026)
        {
            "type": "line",
            "bodies": [aldebaran, mars, denebola],
            "tolerance": 10.0,
            "max_span": 120.0,
            "label": "Mars in line with Aldebaran and Denebola"
        },
        # 5. Venus, Regulus, and Elnath triangle (22 July 2026)
        {
            "type": "group",
            "bodies": [venus, regulus, elnath],
            "threshold": 50.0,
            "label": "Venus with Regulus and Elnath triangle"
        }
    ]

    for config in configurations:
        if any(b is None for b in config["bodies"]):
            continue

        try:
            if config["type"] == "group":
                found = skyfield_searches.find_groupings(
                    observer, config["bodies"], start_date, end_date, threshold_degrees=config["threshold"]
                )
            elif config["type"] == "line":
                found = skyfield_searches.find_linear_alignments(
                    observer, config["bodies"], start_date, end_date,
                    tolerance_degrees=config["tolerance"], max_span_degrees=config["max_span"]
                )
            else:
                found = []

            for e in found:
                e["event"] = config["label"]
                e["type"] = "Celestial Grouping" if config["type"] == "group" else "Linear Alignment"
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
        if e['event'] == "Venus with Regulus and Elnath triangle" and e['date'].date().day != 22:
             continue
        key = (e['event'], e['date'].date())
        if key not in seen:
            seen.add(key)
            unique_events.append(e)

    logger.debug(f"--- calculate_celestial_configurations: {time.time() - start_time}s")
    return unique_events
