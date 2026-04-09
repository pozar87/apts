import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from typing import List, Optional

import pandas as pd
from skyfield.api import Topos

from ..cache import get_ephemeris, get_timescale
from ..catalogs import Catalogs
from ..config import get_event_settings
from ..constants.event_types import EventType
from ..utils import planetary
from .rarity import get_rarity
from .translator import translate_events
from .calculations import lunar, planetary as planetary_calc, space, sky

logger = logging.getLogger(__name__)

utc = timezone.utc

class AstronomicalEvents:
    # Optimization: Only pre-compute positions if any conjunction-related events are enabled
    # to avoid significant overhead when only basic events (like Moon phases) are requested.
    CONJUNCTION_EVENTS = [
        "moon_messier_conjunctions",
        "moon_star_conjunctions",
        "planet_messier_conjunctions",
        "planet_star_conjunctions",
        "planetary_dichotomy",
    ]

    def __init__(
        self,
        place,
        start_date,
        end_date,
        events_to_calculate: Optional[List[EventType]] = None,
    ):
        # Oracle Persona Boundary: restrict predictions to +/- 100 years.
        current_year = datetime.now(timezone.utc).year
        if (
            abs(start_date.year - current_year) > 100
            or abs(end_date.year - current_year) > 100
        ):
            raise ValueError(
                f"Oracle: Prediction range restricted to +/- 100 years from current date ({current_year})."
            )

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
        # Load global settings from config
        config_settings = get_event_settings()

        # Default settings: most are True, some expensive ones are False
        self.event_settings = {event.value: True for event in EventType}
        # Disable expensive events by default
        self.event_settings["golden_hour"] = False
        self.event_settings["blue_hour"] = False
        self.event_settings["culminations"] = False
        self.event_settings["jovian_moon_events"] = False

        # Override with config settings if present
        for key, value in config_settings.items():
            if key in self.event_settings:
                self.event_settings[key] = value

        logger.debug(
            f"AstronomicalEvents initialized. Config-based settings: {self.event_settings}"
        )

        if events_to_calculate is not None:
            # If a list of events is provided, it should explicitly enable those
            # but ONLY if they are not explicitly disabled in config.
            # This allows tests to force-enable events (as they have no config)
            # while respecting user settings in real environments.
            events_to_calculate_str = [str(e) for e in events_to_calculate]
            logger.debug(f"Limiting to events_to_calculate: {events_to_calculate_str}")
            new_settings = {event.value: False for event in EventType}
            for e_str in events_to_calculate_str:
                # Use config if present, otherwise default to True for the requested event
                new_settings[e_str] = config_settings.get(e_str, True)
            self.event_settings = new_settings
            logger.debug(f"Final event_settings after override: {self.event_settings}")

        self.executor = ThreadPoolExecutor()
        self.catalogs = Catalogs()

    def shutdown(self):
        self.executor.shutdown(wait=True)

    def translate_events(self, df: pd.DataFrame) -> pd.DataFrame:
        return translate_events(df)

    def calculate_venus_greatest_brilliancy(self):
        return planetary_calc.calculate_venus_greatest_brilliancy(self.observer, self.start_date, self.end_date)

    def calculate_space_launches(self):
        return space.calculate_space_launches(self.start_date, self.end_date)

    def calculate_space_events(self):
        return space.calculate_space_events(self.start_date, self.end_date)

    def calculate_iss_flybys(self):
        return space.calculate_iss_flybys(self.place, self.observer, self.start_date, self.end_date)

    def calculate_tiangong_flybys(self):
        return space.calculate_tiangong_flybys(self.place, self.observer, self.start_date, self.end_date)

    def calculate_solar_eclipses(self):
        return sky.calculate_solar_eclipses(self.observer, self.start_date, self.end_date)

    def calculate_lunar_eclipses(self):
        return lunar.calculate_lunar_eclipses(self.observer, self.start_date, self.end_date)

    def calculate_moon_phases(self):
        return lunar.calculate_moon_phases(self.ts, self.start_date, self.end_date, self.eph)

    def calculate_conjunctions(self):
        return planetary_calc.calculate_conjunctions(self.ts, self.observer, self.start_date, self.end_date, self.executor)

    def calculate_oppositions(self):
        return planetary_calc.calculate_oppositions(self.observer, self.start_date, self.end_date, self.executor)

    def calculate_meteor_showers(self):
        return sky.calculate_meteor_showers(self.observer, self.start_date, self.end_date)

    def calculate_highest_altitudes(self):
        return planetary_calc.calculate_highest_altitudes(self.observer, self.start_date, self.end_date, self.executor)

    def calculate_lunar_occultations(self):
        return lunar.calculate_lunar_occultations(self.observer, self.start_date, self.end_date, self.catalogs.BRIGHT_STARS)

    def calculate_lunar_planetary_occultations(self):
        return lunar.calculate_lunar_planetary_occultations(self.observer, self.start_date, self.end_date)

    def calculate_aphelion_perihelion(self):
        return planetary_calc.calculate_aphelion_perihelion(self.start_date, self.end_date, self.executor)

    def calculate_moon_apogee_perigee(self):
        return lunar.calculate_moon_apogee_perigee(self.start_date, self.end_date)

    def calculate_mercury_inferior_conjunctions(self):
        return planetary_calc.calculate_mercury_inferior_conjunctions(self.observer, self.start_date, self.end_date)

    def calculate_moon_messier_conjunctions(self, precomputed_positions=None):
        return lunar.calculate_moon_messier_conjunctions(self.observer, self.start_date, self.end_date, self.catalogs.MESSIER, precomputed_positions)

    def calculate_moon_star_conjunctions(self, precomputed_positions=None):
        return lunar.calculate_moon_star_conjunctions(self.ts, self.observer, self.start_date, self.end_date, self.catalogs.BRIGHT_STARS, precomputed_positions)

    def calculate_nasa_comets(self):
        return sky.calculate_nasa_comets(self.start_date, self.end_date)

    def calculate_planet_alignments(self):
        return planetary_calc.calculate_planet_alignments(self.observer, self.start_date, self.end_date)

    def calculate_golden_blue_hours(self):
        return sky.calculate_golden_blue_hours(self.observer, self.start_date, self.end_date, self.event_settings)

    def calculate_culminations(self):
        return sky.calculate_culminations(self.observer, self.start_date, self.end_date)

    def calculate_messier_culminations(self):
        return sky.calculate_messier_culminations(self.observer, self.start_date, self.end_date, self.catalogs.MESSIER)

    def calculate_jovian_moon_events(self):
        return planetary_calc.calculate_jovian_moon_events(self.observer, self.start_date, self.end_date)

    def calculate_saturn_ring_crossings(self):
        return planetary_calc.calculate_saturn_ring_crossings(self.start_date, self.end_date)

    def calculate_greatest_elongations(self):
        return planetary_calc.calculate_greatest_elongations(self.observer, self.start_date, self.end_date)

    def calculate_planetary_dichotomy(self, precomputed_positions=None):
        return planetary_calc.calculate_planetary_dichotomy(self.observer, self.start_date, self.end_date, precomputed_positions)

    def calculate_seasons(self):
        return sky.calculate_seasons(self.start_date, self.end_date)

    def calculate_planet_messier_conjunctions(self, precomputed_positions=None):
        return planetary_calc.calculate_planet_messier_conjunctions(self.observer, self.start_date, self.end_date, precomputed_positions)

    def calculate_jupiter_grs_transits(self, grs_longitude: Optional[float] = None):
        return planetary_calc.calculate_jupiter_grs_transits(self.observer, self.start_date, self.end_date, grs_longitude)

    def calculate_planet_star_conjunctions(self, precomputed_positions=None):
        return planetary_calc.calculate_planet_star_conjunctions(self.observer, self.start_date, self.end_date, precomputed_positions)

    def calculate_planet_stationary_points(self):
        return planetary_calc.calculate_planet_stationary_points(self.observer, self.start_date, self.end_date)

    def calculate_planet_solar_conjunctions(self):
        return planetary_calc.calculate_planet_solar_conjunctions(self.observer, self.start_date, self.end_date)

    def calculate_lunar_features(self):
        return lunar.calculate_lunar_features(self.observer, self.start_date, self.end_date)

    def calculate_moon_libration_maxima(self):
        return lunar.calculate_moon_libration_maxima(self.observer, self.start_date, self.end_date)

    def calculate_planet_planet_occultations(self):
        return planetary_calc.calculate_planet_planet_occultations(self.observer, self.start_date, self.end_date)

    def calculate_supermoons(self):
        return lunar.calculate_supermoons(self.start_date, self.end_date)

    def calculate_mars_closest_approach(self):
        return planetary_calc.calculate_mars_closest_approach(self.observer, self.start_date, self.end_date)

    def calculate_jovian_mutual_events(self):
        return planetary_calc.calculate_jovian_mutual_events(self.observer, self.start_date, self.end_date)

    def _get_rarity(self, event_type: str, data: dict) -> int:
        return get_rarity(event_type, data)

    def get_events(self):
        start_time = time.time()
        executor = self.executor
        futures = []

        # Pre-compute positions for moving bodies often used in multiple searches
        # to improve overall calculation efficiency.
        precomputed = {}
        if any(self.event_settings.get(e) for e in self.CONJUNCTION_EVENTS):
            num_hours = int((self.end_date - self.start_date).total_seconds() / 3600)
            if num_hours >= 2:
                times = self.ts.linspace(
                    self.ts.utc(self.start_date), self.ts.utc(self.end_date), num_hours
                )
                moon_obj = planetary.get_skyfield_obj("moon")
                # Using .apparent() to share high-precision positions
                # Optimization: Hoist observer.at(times) out of the loop
                obs_at_times = self.observer.at(times)
                precomputed["moon"] = obs_at_times.observe(moon_obj).apparent()

                # Pre-compute positions for major planets
                for p_name in planetary.CONJUNCTION_PLANETS:
                    p_obj = planetary.get_skyfield_obj(p_name)
                    precomputed[p_name.lower()] = obs_at_times.observe(p_obj).apparent()

        # Dispatch mapping for event calculations to reduce cyclomatic complexity
        event_dispatch = {
            "moon_phases": self.calculate_moon_phases,
            "conjunctions": self.calculate_conjunctions,
            "oppositions": self.calculate_oppositions,
            "meteor_showers": self.calculate_meteor_showers,
            "highest_altitudes": self.calculate_highest_altitudes,
            "lunar_occultations": self.calculate_lunar_occultations,
            "aphelion_perihelion": self.calculate_aphelion_perihelion,
            "moon_apogee_perigee": self.calculate_moon_apogee_perigee,
            "mercury_inferior_conjunctions": self.calculate_mercury_inferior_conjunctions,
            "moon_messier_conjunctions": lambda: self.calculate_moon_messier_conjunctions(precomputed),
            "moon_star_conjunctions": lambda: self.calculate_moon_star_conjunctions(precomputed),
            "space_launches": self.calculate_space_launches,
            "space_events": self.calculate_space_events,
            "iss_flybys": self.calculate_iss_flybys,
            "tiangong_flybys": self.calculate_tiangong_flybys,
            "solar_eclipses": self.calculate_solar_eclipses,
            "lunar_eclipses": self.calculate_lunar_eclipses,
            "nasa_comets": self.calculate_nasa_comets,
            "planet_alignments": self.calculate_planet_alignments,
            "lunar_planetary_occultations": self.calculate_lunar_planetary_occultations,
            "messier_culminations": self.calculate_messier_culminations,
            "jovian_moon_events": self.calculate_jovian_moon_events,
            "saturn_ring_crossings": self.calculate_saturn_ring_crossings,
            "jupiter_grs_transits": self.calculate_jupiter_grs_transits,
            "planet_messier_conjunctions": lambda: self.calculate_planet_messier_conjunctions(precomputed),
            "planet_star_conjunctions": lambda: self.calculate_planet_star_conjunctions(precomputed),
            "planet_stationary_points": self.calculate_planet_stationary_points,
            "planet_solar_conjunctions": self.calculate_planet_solar_conjunctions,
            "lunar_features": self.calculate_lunar_features,
            "moon_libration_maxima": self.calculate_moon_libration_maxima,
            "planet_planet_occultations": self.calculate_planet_planet_occultations,
            "venus_great_brilliancy": self.calculate_venus_greatest_brilliancy,
            "supermoons": self.calculate_supermoons,
            "mars_closest_approach": self.calculate_mars_closest_approach,
            "jovian_mutual_events": self.calculate_jovian_mutual_events,
            "greatest_elongations": self.calculate_greatest_elongations,
            "planetary_dichotomy": lambda: self.calculate_planetary_dichotomy(precomputed),
            "seasons": self.calculate_seasons,
            "culminations": self.calculate_culminations,
        }

        for event_key, func in event_dispatch.items():
            if self.event_settings.get(event_key):
                futures.append(executor.submit(func))

        # Handle special cases for golden_hour and blue_hour which share a function
        if self.event_settings.get("golden_hour") or self.event_settings.get("blue_hour"):
            futures.append(executor.submit(self.calculate_golden_blue_hours))

        for future in as_completed(futures):
            try:
                self.events.extend(future.result())
            except Exception as e:
                logger.error(f"Error calculating astronomical events: {e}")

        # Standard columns for the events DataFrame
        columns = [
            "date",
            "event",
            "type",
            "rarity",
            "object",
            "object1",
            "object2",
            "altitude",
            "planets",
            "separation_degrees",
            "phase",
            "shower_name",
            "distance_km",
            "magnitude",
            "distance_au",
            "angular_diameter_arcsec",
        ]

        if not self.events:
            return pd.DataFrame(columns=pd.Index(columns))

        df = pd.DataFrame(self.events)
        # Ensure all standard columns exist
        for col in columns:
            if col not in df.columns:
                df[col] = None

        df = df.sort_values(by="date")
        df = translate_events(df)
        logger.debug(f"--- get_events: {time.time() - start_time}s")
        return df
