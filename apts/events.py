import pandas as pd
import numpy as np
from datetime import datetime, timedelta, timezone
from itertools import combinations
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import time
from typing import List, Optional
import requests
import requests_cache
from dateutil.parser import parse as parse_date
from .config import get_event_settings
from .constants.event_types import EventType
from .utils import planetary

logger = logging.getLogger(__name__)

requests_cache.install_cache("apts_cache", backend="memory", expire_after=300)

utc = timezone.utc
from . import skyfield_searches
from .catalogs import Catalogs
from skyfield.api import Topos, Star
from skyfield import almanac
from .cache import get_ephemeris, get_timescale


class AstronomicalEvents:
    def __init__(
        self,
        place,
        start_date,
        end_date,
        events_to_calculate: Optional[List[EventType]] = None,
    ):
        self.place = place
        self.start_date = start_date.astimezone(utc)  # Ensure start_date is UTC
        self.end_date = end_date.astimezone(utc)  # Ensure end_date is UTC
        self.ts = get_timescale()
        self.eph = get_ephemeris()
        self.observer = self.eph["earth"] + Topos(
            latitude_degrees=self.place.lat_decimal,
            longitude_degrees=self.place.lon_decimal,
            elevation_m=self.place.elevation,
        )
        self.events = []
        if events_to_calculate is not None:
            # If a list of events is provided, use it to build the settings
            events_to_calculate_str = [str(e) for e in events_to_calculate]
            self.event_settings = {
                event.value: (event.value in events_to_calculate_str)
                for event in EventType
            }
        else:
            # Otherwise, load from config as before
            self.event_settings = get_event_settings()
        self.executor = ThreadPoolExecutor()
        self.catalogs = Catalogs()

    def shutdown(self):
        self.executor.shutdown(wait=True)

    def get_events(self):
        start_time = time.time()
        executor = self.executor
        futures = []
        if self.event_settings.get("moon_phases", False):
            futures.append(executor.submit(self.calculate_moon_phases))
        if self.event_settings.get("conjunctions", False):
            futures.append(executor.submit(self.calculate_conjunctions))
        if self.event_settings.get("oppositions", False):
            futures.append(executor.submit(self.calculate_oppositions))
        if self.event_settings.get("meteor_showers", False):
            futures.append(executor.submit(self.calculate_meteor_showers))
        if self.event_settings.get("highest_altitudes", False):
            futures.append(executor.submit(self.calculate_highest_altitudes))
        if self.event_settings.get("lunar_occultations", False):
            futures.append(executor.submit(self.calculate_lunar_occultations))
        if self.event_settings.get("aphelion_perihelion", False):
            futures.append(executor.submit(self.calculate_aphelion_perihelion))
        if self.event_settings.get("moon_apogee_perigee", False):
            futures.append(executor.submit(self.calculate_moon_apogee_perigee))
        if self.event_settings.get("mercury_inferior_conjunctions", False):
            futures.append(
                executor.submit(self.calculate_mercury_inferior_conjunctions)
            )
        if self.event_settings.get("moon_messier_conjunctions", False):
            futures.append(executor.submit(self.calculate_moon_messier_conjunctions))
        if self.event_settings.get("space_launches", False):
            futures.append(executor.submit(self.calculate_space_launches))
        if self.event_settings.get("space_events", False):
            futures.append(executor.submit(self.calculate_space_events))
        if self.event_settings.get("iss_flybys", False):
            futures.append(executor.submit(self.calculate_iss_flybys))

        for future in as_completed(futures):
            self.events.extend(future.result())
        if not self.events:
            return pd.DataFrame(self.events)
        df = pd.DataFrame(self.events).sort_values(by="date")
        logger.debug(f"--- get_events: {time.time() - start_time}s")
        return df

    def calculate_space_launches(self):
        start_time = time.time()
        events = []
        start_date_str = self.start_date.strftime("%Y-%m-%d")
        end_date_str = self.end_date.strftime("%Y-%m-%d")
        url = f"https://ll.thespacedevs.com/2.2.0/launch/upcoming/?window_start__gte={start_date_str}&window_end__lte={end_date_str}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            for launch in data.get("results", []):
                events.append(
                    {
                        "date": parse_date(launch["window_start"]).astimezone(utc),
                        "event": launch["name"],
                        "type": "Space Launch",
                    }
                )
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching space launches: {e}")
        logger.debug(f"--- calculate_space_launches: {time.time() - start_time}s")
        return events

    def calculate_space_events(self):
        start_time = time.time()
        events = []
        start_date_str = self.start_date.strftime("%Y-%m-%d")
        end_date_str = self.end_date.strftime("%Y-%m-%d")
        url = f"https://ll.thespacedevs.com/2.2.0/event/upcoming/?date__gte={start_date_str}&date__lte={end_date_str}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            for event in data.get("results", []):
                events.append(
                    {
                        "date": parse_date(event["date"]).astimezone(utc),
                        "event": event["name"],
                        "type": "Space Event",
                    }
                )
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching space events: {e}")
        logger.debug(f"--- calculate_space_events: {time.time() - start_time}s")
        return events

    def calculate_iss_flybys(self):
        start_time = time.time()
        # Create the Topos object directly from place attributes
        topos_observer = Topos(
            latitude_degrees=self.place.lat_decimal,
            longitude_degrees=self.place.lon_decimal,
            elevation_m=self.place.elevation,
        )
        events = skyfield_searches.find_iss_flybys(
            topos_observer, self.observer, self.start_date, self.end_date
        )
        logger.debug(f"--- calculate_iss_flybys: {time.time() - start_time}s")
        return events

    def calculate_moon_phases(self):
        start_time = time.time()
        events = []
        t0 = self.ts.utc(self.start_date)
        t1 = self.ts.utc(self.end_date)
        which_phase = almanac.moon_phases(self.eph)
        t, y = almanac.find_discrete(t0, t1, which_phase)
        for ti, yi in zip(t, y):
            events.append(
                {
                    "date": ti.utc_datetime().astimezone(utc),
                    "event": almanac.MOON_PHASES[yi],
                    "type": "Moon Phase",
                }
            )
        logger.debug(f"--- calculate_moon_phases: {time.time() - start_time}s")
        return events

    def calculate_conjunctions(self):
        start_time = time.time()
        events = []
        planets = planetary.CONJUNCTION_PLANETS
        moon = "moon"
        moon_display_name = "Moon"

        executor = self.executor
        # Planet-Planet conjunctions
        futures = []
        for (p1, p1_name), (p2, p2_name) in combinations(planets.items(), 2):
            event_name = f"{p1_name} conjunct {p2_name}"
            futures.append(
                executor.submit(
                    skyfield_searches.find_conjunctions,
                    self.observer,
                    self.eph,
                    p1,
                    p2,
                    self.start_date,
                    self.end_date,
                    event_name=event_name,
                )
            )

        # Planet-Moon conjunctions
        for p, p_name in planets.items():
            event_name = f"{p_name} conjunct {moon_display_name}"
            futures.append(
                executor.submit(
                    skyfield_searches.find_conjunctions,
                    self.observer,
                    self.eph,
                    p,
                    moon,
                    self.start_date,
                    self.end_date,
                    event_name=event_name,
                )
            )

        for future in as_completed(futures):
            found_events = future.result()
            for event in found_events:
                event["type"] = "Conjunction"
            events.extend(found_events)
        logger.debug(f"--- calculate_conjunctions: {time.time() - start_time}s")
        return events

    def calculate_oppositions(self):
        start_time = time.time()
        events = []
        planets = planetary.OPPOSITION_PLANETS
        executor = self.executor
        futures = [
            executor.submit(
                skyfield_searches.find_oppositions,
                self.observer,
                self.eph,
                p,
                self.start_date,
                self.end_date,
            )
            for p in planets
        ]
        for future in as_completed(futures):
            found_events = future.result()
            for event in found_events:
                event["type"] = "Opposition"
                simple_name = planetary.get_simple_name(event["planet"])
                event["event"] = f"{simple_name} at opposition"
                del event["planet"]
            events.extend(found_events)
        logger.debug(f"--- calculate_oppositions: {time.time() - start_time}s")
        return events

    def calculate_meteor_showers(self):
        start_time = time.time()
        events = []
        showers = {
            "Quadrantids": {"start": (1, 1), "peak": (1, 4), "end": (1, 5)},
            "Lyrids": {"start": (4, 14), "peak": (4, 22), "end": (4, 30)},
            "Eta Aquarids": {"start": (4, 19), "peak": (5, 6), "end": (5, 28)},
            "Delta Aquarids": {"start": (7, 12), "peak": (7, 30), "end": (8, 23)},
            "Perseids": {"start": (7, 17), "peak": (8, 12), "end": (8, 24)},
            "Orionids": {"start": (10, 2), "peak": (10, 21), "end": (11, 7)},
            "Leonids": {"start": (11, 6), "peak": (11, 17), "end": (11, 30)},
            "Geminids": {"start": (12, 4), "peak": (12, 14), "end": (12, 17)},
            "Ursids": {"start": (12, 17), "peak": (12, 22), "end": (12, 26)},
        }
        for year in range(self.start_date.year, self.end_date.year + 1):
            for shower, dates in showers.items():
                start_date = datetime(
                    year, dates["start"][0], dates["start"][1], tzinfo=utc
                )
                peak_date = datetime(
                    year, dates["peak"][0], dates["peak"][1], tzinfo=utc
                )
                end_date = datetime(year, dates["end"][0], dates["end"][1], tzinfo=utc)

                if self.start_date <= start_date <= self.end_date:
                    events.append(
                        {
                            "date": start_date.astimezone(utc),
                            "event": f"{shower} Meteor Shower (Start)",
                            "type": "Meteor Shower",
                        }
                    )
                if self.start_date <= peak_date <= self.end_date:
                    events.append(
                        {
                            "date": peak_date.astimezone(utc),
                            "event": f"{shower} Meteor Shower (Peak)",
                            "type": "Meteor Shower",
                        }
                    )
                if self.start_date <= end_date <= self.end_date:
                    events.append(
                        {
                            "date": end_date.astimezone(utc),
                            "event": f"{shower} Meteor Shower (End)",
                            "type": "Meteor Shower",
                        }
                    )
        logger.debug(f"--- calculate_meteor_showers: {time.time() - start_time}s")
        return events

    def calculate_highest_altitudes(self):
        start_time = time.time()
        events = []
        executor = self.executor
        futures = {
            executor.submit(
                skyfield_searches.find_highest_altitude,
                self.observer,
                self.eph[planet_name],
                self.start_date,
                self.end_date,
            ): planet_name
            for planet_name in ["mercury", "venus"]
        }
        for future in as_completed(futures):
            planet_name = futures[future]
            t, alt = future.result()
            if t:
                simple_name = planetary.get_simple_name(planet_name)
                events.append(
                    {
                        "date": t.astimezone(utc),
                        "event": f"Highest altitude of {simple_name} ({alt:.2f}°)",
                        "type": "Planet Altitude",
                    }
                )
        logger.debug(f"--- calculate_highest_altitudes: {time.time() - start_time}s")
        return events

    def calculate_lunar_occultations(self):
        start_time = time.time()
        events = skyfield_searches.find_lunar_occultations(
            self.observer,
            self.eph,
            self.catalogs.BRIGHT_STARS,
            self.start_date,
            self.end_date,
        )
        for event in events:
            event["type"] = "Lunar Occultation"
        logger.debug(f"--- calculate_lunar_occultations: {time.time() - start_time}s")
        return events

    def calculate_aphelion_perihelion(self):
        start_time = time.time()
        events = []
        planets = planetary.APHELION_PERIHELION_PLANETS
        executor = self.executor
        futures = [
            executor.submit(
                skyfield_searches.find_aphelion_perihelion,
                self.eph,
                planet_name,
                self.start_date,
                self.end_date,
            )
            for planet_name in planets
        ]
        for future in as_completed(futures):
            events_from_search = future.result()
            for event_dict in events_from_search:
                simple_name = planetary.get_simple_name(event_dict["planet"])
                event_dict[
                    "event"
                ] = f"{simple_name} {event_dict['event_type']}"
                del event_dict["planet"]
                del event_dict["event_type"]
                event_dict["date"] = event_dict["date"].astimezone(utc)
                event_dict["type"] = "Aphelion/Perihelion"
                events.append(event_dict)
        logger.debug(f"--- calculate_aphelion_perihelion: {time.time() - start_time}s")
        return events

    def calculate_moon_apogee_perigee(self):
        start_time = time.time()
        events = skyfield_searches.find_moon_apogee_perigee(
            self.eph, self.start_date, self.end_date
        )
        for event in events:
            event["type"] = "Moon Apogee/Perigee"
        logger.debug(f"--- calculate_moon_apogee_perigee: {time.time() - start_time}s")
        return events

    def calculate_mercury_inferior_conjunctions(self):
        start_time = time.time()
        events = skyfield_searches.find_mercury_inferior_conjunctions(
            self.observer, self.eph, self.start_date, self.end_date
        )
        for event in events:
            event["type"] = "Inferior Conjunction"
        logger.debug(
            f"--- calculate_mercury_inferior_conjunctions: {time.time() - start_time}s"
        )
        return events

    def calculate_moon_messier_conjunctions(self):
        start_time = time.time()
        events = []
        messier_objects_to_check = [
            "M1",
            "M2",
            "M3",
            "M4",
            "M5",
            "M8",
            "M9",
            "M10",
            "M11",
            "M12",
            "M14",
            "M15",
            "M16",
            "M17",
            "M18",
            "M19",
            "M20",
            "M21",
            "M22",
            "M23",
            "M24",
            "M25",
            "M26",
            "M27",
            "M28",
            "M30",
            "M35",
            "M41",
            "M42",
            "M43",
            "M44",
            "M45",
            "M46",
            "M47",
            "M48",
            "M49",
            "M50",
            "M53",
            "M54",
            "M55",
            "M58",
            "M59",
            "M60",
            "M61",
            "M62",
            "M64",
            "M65",
            "M66",
            "M67",
            "M68",
            "M71",
            "M72",
            "M73",
            "M74",
            "M75",
            "M77",
            "M78",
            "M79",
            "M80",
            "M83",
            "M84",
            "M85",
            "M86",
            "M87",
            "M88",
            "M89",
            "M90",
            "M91",
            "M93",
            "M95",
            "M96",
            "M98",
            "M99",
            "M100",
            "M104",
            "M105",
            "M107",
        ]

        messier_df = self.catalogs.MESSIER[
            self.catalogs.MESSIER["Messier"].isin(messier_objects_to_check)
        ]

        # Pre-create Star objects outside the loop
        messier_stars = {}
        for _, row in messier_df.iterrows():
            messier_stars[row["Messier"]] = Star.from_dataframe(
                pd.DataFrame(
                    {
                        "ra_hours": [row["RA"].to("hour").magnitude],
                        "dec_degrees": [row["Dec"].to("degree").magnitude],
                        "ra_mas_per_year": [0],
                        "dec_mas_per_year": [0],
                        "parallax_mas": [0],
                        "radial_km_per_s": [0],
                        "epoch_year": [2000.0],
                    },
                    index=[0],
                )
            )

        def find_all_conjunctions(messier_stars_subset):
            all_events = []
            for messier_name, messier_star in messier_stars_subset.items():
                event_name = f"Moon conjunct {messier_name}"
                conjunctions = skyfield_searches.find_conjunctions_with_star(
                    self.observer,
                    self.eph,
                    "moon",
                    messier_star,
                    self.start_date,
                    self.end_date,
                    threshold_degrees=4.0,
                    event_name=event_name,
                )
                for conj in conjunctions:
                    all_events.append(
                        {
                            "date": conj["date"].astimezone(utc),
                            "event": f"{conj['event']} (Separation: {conj['separation_degrees']:.2f}°)",
                            "type": "Moon-Messier Conjunction",
                        }
                    )
            return all_events

        executor = self.executor
        # Split messier_stars into chunks for parallel processing
        chunk_size = 10
        messier_star_chunks = [
            dict(list(messier_stars.items())[i : i + chunk_size])
            for i in range(0, len(messier_stars), chunk_size)
        ]
        futures = [
            executor.submit(find_all_conjunctions, chunk)
            for chunk in messier_star_chunks
        ]

        for future in as_completed(futures):
            events.extend(future.result())

        logger.debug(
            f"--- calculate_moon_messier_conjunctions: {time.time() - start_time}s"
        )
        return events
