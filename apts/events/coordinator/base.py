import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, datetime

import pandas as pd
from skyfield.api import Topos

from ...cache import get_ephemeris, get_timescale
from ...catalogs import Catalogs
from ...constants.event_types import EventType
from ..duration import get_duration
from ..rarity import get_rarity
from ..translator import translate_events
from .dispatch import build_event_dispatch_map
from .precomputation import PrecomputationEngine
from .settings import EventSettingsManager
from .wrappers import EventCalculationWrappers

logger = logging.getLogger(__name__)

utc = UTC


class AstronomicalEvents(EventCalculationWrappers):
    """
    Coordinates the calculation of various astronomical events.
    """

    def __init__(
        self,
        place,
        start_date,
        end_date,
        events_to_calculate: list[EventType] | None = None,
    ):
        # Oracle Persona Boundary: restrict predictions to +/- 100 years.
        current_year = datetime.now(UTC).year
        if (
            abs(start_date.year - current_year) > 100
            or abs(end_date.year - current_year) > 100
        ):
            raise ValueError(
                f"Oracle: Prediction range restricted to +/- 100 years from current date ({current_year})."
            )

        self.place = place
        self.start_date = start_date.astimezone(utc)
        self.end_date = end_date.astimezone(utc)
        self.ts = get_timescale()
        self.eph = get_ephemeris()
        self.observer = self.eph["earth"] + Topos(
            latitude_degrees=self.place.lat_decimal,
            longitude_degrees=self.place.lon_decimal,
            elevation_m=self.place.elevation,
        )
        self.events = []

        # Modularized configuration management
        self.settings_manager = EventSettingsManager(events_to_calculate)
        self.event_settings = self.settings_manager.get_all()

        self.executor = ThreadPoolExecutor()
        self.catalogs = Catalogs()

        # Modularized pre-computation
        self.precomputation_engine = PrecomputationEngine(
            self.ts, self.observer, self.start_date, self.end_date
        )

    @property
    def CONJUNCTION_EVENTS(self):
        return self.precomputation_engine.CONJUNCTION_EVENTS

    def shutdown(self):
        self.executor.shutdown(wait=True)

    def translate_events(self, df: pd.DataFrame) -> pd.DataFrame:
        return translate_events(df)

    def _get_rarity(self, event_type: str, data: dict) -> int:
        return get_rarity(event_type, data)

    def _get_duration(self, event_type: str, data: dict) -> int:
        return get_duration(event_type, data)

    def _precompute_positions(self):
        return self.precomputation_engine.precompute_positions(
            self.event_settings, self.executor
        )

    def get_events(self):
        start_time = time.time()
        executor = self.executor
        futures = []

        precomputed = self._precompute_positions()

        # Dispatch mapping for event calculations built by helper
        event_dispatch = build_event_dispatch_map(self, precomputed)

        for event_key, func in event_dispatch.items():
            if self.event_settings.get(event_key):
                futures.append(executor.submit(func))

        # Handle special cases for golden_hour and blue_hour which share a function
        if self.event_settings.get("golden_hour") or self.event_settings.get(
            "blue_hour"
        ):
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
            "duration",
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
            "libration_value",
            "side",
            "axis",
            "colongitude",
            "ingress_time",
            "egress_time",
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
