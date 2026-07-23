import logging
import time
from datetime import timezone
import numpy as np
from skyfield import almanac
from skyfield.api import Star

from ... import skyfield_searches
from ..rarity import get_rarity
from ..duration import get_duration

logger = logging.getLogger(__name__)
utc = timezone.utc

def calculate_moon_phases(ts, start_date, end_date, eph):
    start_time = time.time()
    events = []
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)
    which_phase = almanac.moon_phases(eph)
    t, y = almanac.find_discrete(t0, t1, which_phase)
    for ti, yi in zip(t, y):
        event_data = {
            "date": ti.utc_datetime().astimezone(utc),
            "event": almanac.MOON_PHASES[yi],
            "type": "Moon Phase",
        }
        event_data["rarity"] = get_rarity("Moon Phase", event_data)
        event_data["duration"] = get_duration("Moon Phase", event_data)
        events.append(event_data)
    logger.debug(f"--- calculate_moon_phases: {time.time() - start_time}s")
    return events

def calculate_lunar_occultations(observer, start_date, end_date, bright_stars):
    start_time = time.time()
    events = skyfield_searches.find_lunar_occultations(
        observer,
        bright_stars,
        start_date,
        end_date,
    )
    for event in events:
        event["type"] = "Lunar Occultation"
        event["event"] = "Lunar Occultation"
        event["rarity"] = get_rarity("Lunar Occultation", event)
        event["duration"] = get_duration("Lunar Occultation", event)
    logger.debug(f"--- calculate_lunar_occultations: {time.time() - start_time}s")
    return events

def calculate_lunar_planetary_occultations(observer, start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_lunar_planetary_occultations(
        observer,
        start_date,
        end_date,
    )
    for event in events:
        event["type"] = "Lunar Planetary Occultation"
        event["event"] = "Lunar Planetary Occultation"
        event["rarity"] = get_rarity("Lunar Planetary Occultation", event)
        event["duration"] = get_duration("Lunar Planetary Occultation", event)
    logger.debug(
        f"--- calculate_lunar_planetary_occultations: {time.time() - start_time}s"
    )
    return events

def calculate_moon_apogee_perigee(start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_moon_apogee_perigee(
        start_date, end_date
    )
    for event in events:
        event["type"] = "Moon Apogee/Perigee"
        event["rarity"] = get_rarity("Moon Apogee/Perigee", event)
        event["duration"] = get_duration("Moon Apogee/Perigee", event)
    logger.debug(f"--- calculate_moon_apogee_perigee: {time.time() - start_time}s")
    return events

def calculate_moon_messier_conjunctions(observer, start_date, end_date, messier_catalog, precomputed_positions=None):
    start_time = time.time()
    messier_objects_to_check = [
        "M1", "M2", "M3", "M4", "M5", "M8", "M9", "M10", "M11", "M12", "M14", "M15", "M16", "M17", "M18", "M19", "M20", "M21", "M22", "M23", "M24", "M25", "M26", "M27", "M28", "M30", "M35", "M41", "M42", "M43", "M44", "M45", "M46", "M47", "M48", "M49", "M50", "M53", "M54", "M55", "M58", "M59", "M60", "M61", "M62", "M64", "M65", "M66", "M67", "M68", "M71", "M72", "M73", "M74", "M75", "M77", "M78", "M79", "M80", "M83", "M84", "M85", "M86", "M87", "M88", "M89", "M90", "M91", "M93", "M95", "M96", "M98", "M99", "M100", "M104", "M105", "M107",
    ]

    messier_df = messier_catalog[
        messier_catalog["Messier"].isin(messier_objects_to_check)
    ]

    messier_vector = Star(
        ra_hours=messier_df["ra_hours"].to_numpy(),
        dec_degrees=messier_df["dec_degrees"].to_numpy(),
    )
    messier_names = messier_df["Messier"].to_numpy()

    conjunctions = skyfield_searches.find_conjunctions_with_stars(
        observer,
        "moon",
        messier_vector,
        start_date,
        end_date,
        threshold_degrees=4.0,
        precomputed_positions=precomputed_positions,
        star_names=messier_names,
    )

    events = []
    for conj in conjunctions:
        event_data = {
            "date": conj["date"].astimezone(utc),
            "event": "Conjunction",
            "object1": "Moon",
            "object2": conj["object2"],
            "separation_degrees": conj["separation_degrees"],
            "type": "Moon-Messier Conjunction",
        }
        event_data["rarity"] = get_rarity(
            "Moon-Messier Conjunction", event_data
        )
        event_data["duration"] = get_duration("Moon-Messier Conjunction", event_data)
        events.append(event_data)

    logger.debug(
        f"--- calculate_moon_messier_conjunctions: {time.time() - start_time}s"
    )
    return events

def calculate_moon_star_conjunctions(ts, observer, start_date, end_date, bright_stars, precomputed_positions=None):
    start_time = time.time()

    # Filter stars close to the ecliptic (within 10 degrees)
    # The Moon stays within ~5.1 degrees of the ecliptic.
    t_ref = ts.utc(start_date)

    # Observe all stars at once using a vectorized Star object
    # Optimization: use pre-calculated float columns instead of list comprehension over Star objects
    stars_vector = Star(
        ra_hours=bright_stars["ra_hours"].to_numpy(),
        dec_degrees=bright_stars["dec_degrees"].to_numpy(),
    )
    spos_at_t_ref = observer.at(t_ref).observe(stars_vector)
    lats, _, _ = spos_at_t_ref.ecliptic_latlon()

    # Filter using vectorized mask
    mask = np.abs(lats.degrees) < 10.0
    filtered_stars_df = bright_stars[mask]

    star_vector_filtered = Star(
        ra_hours=filtered_stars_df["ra_hours"].to_numpy(),
        dec_degrees=filtered_stars_df["dec_degrees"].to_numpy(),
    )
    star_names_filtered = filtered_stars_df["Name"].to_numpy()

    conjunctions = skyfield_searches.find_conjunctions_with_stars(
        observer,
        "moon",
        star_vector_filtered,
        start_date,
        end_date,
        threshold_degrees=5.0,
        precomputed_positions=precomputed_positions,
        star_names=star_names_filtered,
    )

    events = []
    for conj in conjunctions:
        event_data = {
            "date": conj["date"].astimezone(utc),
            "event": "Conjunction",
            "object1": "Moon",
            "object2": conj["object2"],
            "separation_degrees": conj["separation_degrees"],
            "type": "Moon-Star Conjunction",
        }
        event_data["rarity"] = get_rarity("Moon-Star Conjunction", event_data)
        event_data["duration"] = get_duration("Moon-Star Conjunction", event_data)
        events.append(event_data)

    logger.debug(
        f"--- calculate_moon_star_conjunctions: {time.time() - start_time}s"
    )
    return events

def calculate_lunar_features(observer, start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_lunar_features(
        observer, start_date, end_date
    )
    for event in events:
        event["rarity"] = get_rarity("Lunar Feature", event)
        event["duration"] = get_duration("Lunar Feature", event)
    logger.debug(f"--- calculate_lunar_features: {time.time() - start_time}s")
    return events

def calculate_supermoons(start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_supermoons(start_date, end_date)
    for event in events:
        # Ensure date is timezone-aware UTC
        event["date"] = event["date"].astimezone(utc)
        event["rarity"] = get_rarity("Supermoon", event)
        event["duration"] = get_duration("Supermoon", event)
    logger.debug(f"--- calculate_supermoons: {time.time() - start_time}s")
    return events

def calculate_lunar_eclipses(observer, start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_lunar_eclipses(
        start_date, end_date, observer=observer
    )
    for event in events:
        event["event"] = "Lunar Eclipse"
        event["type"] = "Lunar Eclipse"
        event["rarity"] = get_rarity("Lunar Eclipse", event)
        event["duration"] = get_duration("Lunar Eclipse", event)
    logger.debug(f"--- calculate_lunar_eclipses: {time.time() - start_time}s")
    return events

def calculate_moon_libration_maxima(observer, start_date, end_date):
    start_time = time.time()
    events = skyfield_searches.find_moon_libration_maxima(
        observer, start_date, end_date
    )
    for event in events:
        event["rarity"] = get_rarity("Moon Libration Maximum", event)
        event["duration"] = get_duration("Moon Libration Maximum", event)
    logger.debug(f"--- calculate_moon_libration_maxima: {time.time() - start_time}s")
    return events
