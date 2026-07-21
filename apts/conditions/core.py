from datetime import datetime
from typing import Optional, Union

from apts.constants.twilight import Twilight
from .defaults import DefaultConditions


class Conditions:
    """
    Class containing acceptable thresholds for observation quality.
    """

    def __init__(
        self,
        max_clouds: float = DefaultConditions.MAX_CLOUDS,
        max_precipitation_probability: float = DefaultConditions.MAX_PRECIPITATION_PROBABILITY,
        max_precipitation_intensity: float = DefaultConditions.MAX_PRECIPITATION_INTENSITY,
        max_wind: float = DefaultConditions.MAX_WIND,
        min_temperature: float = DefaultConditions.MIN_TEMPERATURE,
        max_temperature: float = DefaultConditions.MAX_TEMPERATURE,
        min_weather_goodness: float = DefaultConditions.MIN_WEATHER_GOODNESS,
        min_visibility: float = DefaultConditions.MIN_VISIBILITY,
        max_fog: float = DefaultConditions.MAX_FOG,
        min_sqm: float = DefaultConditions.MIN_SQM,
        max_seeing: float = DefaultConditions.MAX_SEEING,
        max_return: Optional[str] = DefaultConditions.MAX_RETURN,
        start_time: Optional[Union[str, datetime]] = DefaultConditions.START_TIME,
        min_object_altitude: float = DefaultConditions.MIN_OBJECT_ALTITUDE,
        max_object_magnitude: float = DefaultConditions.MAX_OBJECT_MAGNITUDE,
        min_object_azimuth: float = DefaultConditions.MIN_OBJECT_AZIMUTH,
        max_object_azimuth: float = DefaultConditions.MAX_OBJECT_AZIMUTH,
        max_moon_illumination: float = DefaultConditions.MAX_MOON_ILLUMINATION,
        twilight: Twilight = DefaultConditions.TWILIGHT,
        min_aurora: float = DefaultConditions.MIN_AURORA,
        horizon_file: Optional[str] = DefaultConditions.HORIZON_FILE,
        horizon_content: Optional[str] = DefaultConditions.HORIZON_CONTENT,
    ):
        self.max_clouds = max_clouds
        self.max_precipitation_probability = max_precipitation_probability
        self.max_precipitation_intensity = max_precipitation_intensity
        self.max_wind = max_wind
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature
        self.min_weather_goodness = min_weather_goodness
        self.min_visibility = min_visibility
        self.max_fog = max_fog
        self.min_sqm = min_sqm
        self.max_seeing = max_seeing
        self.max_return = max_return
        self.start_time = start_time
        self.min_object_altitude = min_object_altitude
        self.max_object_magnitude = max_object_magnitude
        self.min_object_azimuth = min_object_azimuth
        self.max_object_azimuth = max_object_azimuth
        self.max_moon_illumination = max_moon_illumination
        self.twilight = twilight
        self.min_aurora = min_aurora
        self.horizon_file = horizon_file
        self.horizon_content = horizon_content
        self._horizon = None

    @property
    def horizon(self):
        if self._horizon is None:
            from apts.horizon import Horizon

            self._horizon = Horizon(self.horizon_file, self.min_object_altitude, content=self.horizon_content)
        return self._horizon

    def is_visible(self, azimuth, altitude):
        """
        Check if an object at a given azimuth and altitude is visible.
        If a horizon file is provided, it is used for the check.
        Otherwise, simple min_object_altitude and min/max_object_azimuth are used.
        """
        if self.horizon_content or self.horizon_file:
            return self.horizon.is_visible(azimuth, altitude)

        # Fallback to simple min/max
        min_alt = getattr(self.min_object_altitude, "magnitude", self.min_object_altitude)
        min_az = getattr(self.min_object_azimuth, "magnitude", self.min_object_azimuth)
        max_az = getattr(self.max_object_azimuth, "magnitude", self.max_object_azimuth)

        alt_ok = altitude > min_alt

        if min_az > max_az:
            az_ok = (azimuth >= min_az) | (azimuth <= max_az)
        else:
            az_ok = (azimuth >= min_az) & (azimuth <= max_az)

        return alt_ok & az_ok
