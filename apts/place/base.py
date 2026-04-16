import datetime
import logging
from math import radians as rad
from typing import Any, Optional, cast

from dateutil import tz
from skyfield import almanac
from skyfield.api import Topos

from apts.cache import get_ephemeris, get_timescale
from .utils import TFProxy, get_scalar_datetime
from .models import (
    PlaceConditionsMixIn,
    PlaceTimesMixIn,
    PlacePathsMixIn,
    PlaceImagingMixIn,
)
from ..utils.planetary import (
    get_moon_age,
    get_moon_distance,
    get_moon_illumination,
    get_moon_phase_name,
    get_skyfield_obj,
)

logger = logging.getLogger(__name__)


class Place(
    PlaceConditionsMixIn, PlaceTimesMixIn, PlacePathsMixIn, PlaceImagingMixIn
):
    TF = TFProxy()

    def __init__(
        self,
        lat,
        lon,
        name="",
        elevation=300,
        date=datetime.datetime.now(datetime.UTC),
    ):
        self.ts = get_timescale()
        self.eph = get_ephemeris()
        if isinstance(date, type(self.ts.now())):
            self.date = date
        else:
            self.date = self.ts.utc(date)
        self.lat = rad(lat)
        self.lon = rad(lon)
        self.lat_decimal = lat
        self.lon_decimal = lon
        self.name = name
        self.elevation = elevation
        self.location = Topos(
            latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation)
        )
        self.observer = self.eph["earth"] + self.location
        # Sun
        self.sun = self.eph["sun"]
        # Moon
        self.moon = self.eph["moon"]
        self.local_timezone = tz.gettz(
            Place.TF.timezone_at(lat=self.lat_decimal, lng=self.lon_decimal)
        )
        self.weather = None
        self.light_pollution = None
        logger.debug(f"Place {self.name} initialized, timezone: {self.local_timezone}")

    def _get_scalar_datetime(self, target_time: Any) -> datetime.datetime:
        """
        Legacy shim for tests mocking this method on Place instances.
        """
        return get_scalar_datetime(target_time)

    def get_altitude(self, object_or_name: Any, time: Optional[Any] = None) -> float:
        """
        Returns the topocentric apparent altitude of a celestial object in degrees.
        Supports both Skyfield objects and string names (e.g., 'Jupiter').
        Uses high-precision refraction settings (10°C, 1013.25 mbar).
        """
        target_time = time if time is not None else self.date
        obj = (
            get_skyfield_obj(object_or_name)
            if isinstance(object_or_name, str)
            else object_or_name
        )
        alt, _, _ = (
            self.observer.at(target_time)
            .observe(obj)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)
        )
        return float(alt.degrees)

    def get_azimuth(self, object_or_name: Any, time: Optional[Any] = None) -> float:
        """
        Returns the topocentric apparent azimuth of a celestial object in degrees.
        Supports both Skyfield objects and string names (e.g., 'Jupiter').
        Uses high-precision refraction settings (10°C, 1013.25 mbar).
        """
        target_time = time if time is not None else self.date
        obj = (
            get_skyfield_obj(object_or_name)
            if isinstance(object_or_name, str)
            else object_or_name
        )
        _, az, _ = (
            self.observer.at(target_time)
            .observe(obj)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)
        )
        return float(az.degrees)

    def _moon_phase_letter(self) -> str:
        phase_angle = almanac.moon_phase(self.eph, self.date)
        if hasattr(phase_angle, "degrees"):
            phase_angle_deg = phase_angle.degrees
        else:
            phase_angle_deg = float(phase_angle)  # type: ignore
        lunation = cast(float, phase_angle_deg) / 360.0
        letter = chr(ord("A") + int(round(lunation * 26)))
        return letter

    def moon_illumination(self):
        return get_moon_illumination(self.date)

    def moon_phase_name(self):
        """
        Returns the name of the moon phase.
        """
        return get_moon_phase_name(self.date)

    def moon_age(self):
        """
        Returns the Moon age in days.
        """
        return get_moon_age(self.date)

    def moon_distance(self):
        """
        Returns the Moon distance in km.
        """
        return get_moon_distance(self.date)

    def __getstate__(self):
        state = self.__dict__.copy()
        # Remove the unpicklable entries.
        del state["ts"]
        del state["eph"]
        del state["location"]
        del state["observer"]
        del state["sun"]
        del state["moon"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        # Re-create the unpicklable entries.
        self.ts = get_timescale()
        self.eph = get_ephemeris()
        self.location = Topos(
            latitude_degrees=self.lat_decimal,
            longitude_degrees=self.lon_decimal,
            elevation_m=self.elevation,
        )
        self.observer = self.eph["earth"] + self.location
        self.sun = self.eph["sun"]
        self.moon = self.eph["moon"]
