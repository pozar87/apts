import os
from typing import Optional, Union
import numpy as np
from scipy.interpolate import interp1d

from .parser import parse_horizon_content, parse_horizon_file, process_horizon_data


class Horizon:
    def __init__(
        self,
        file_path: Optional[str] = None,
        min_altitude: float = 0.0,
        content: Optional[str] = None,
    ):
        self.file_path = file_path
        self.min_altitude = float(min_altitude)

        # Default fallback data
        raw_az = [0.0, 360.0]
        raw_alt = [self.min_altitude, self.min_altitude]

        if content:
            raw_az, raw_alt = parse_horizon_content(content)
        elif file_path and os.path.exists(file_path):
            raw_az, raw_alt = parse_horizon_file(file_path)

        az, alt = process_horizon_data(raw_az, raw_alt)

        if not az:
            az = [0.0, 360.0]
            alt = [self.min_altitude, self.min_altitude]

        self.azimuths = np.array(az)
        self.altitudes = np.array(alt)

        # Using any to avoid pyright issue with "extrapolate" literal
        self._interp = interp1d(
            self.azimuths,
            self.altitudes,
            kind="linear",
            fill_value="extrapolate",  # type: ignore
        )

    def get_min_altitude(self) -> float:
        """
        Get the minimum altitude of the entire horizon.
        """
        return float(np.min(self.altitudes))

    def get_altitude(self, azimuth: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        """
        Get the horizon altitude for a given azimuth (or array of azimuths).
        """
        # Ensure azimuth is in [0, 360]
        az_mod = np.mod(azimuth, 360.0)
        return self._interp(az_mod)

    def is_visible(
        self, azimuth: Union[float, np.ndarray], altitude: Union[float, np.ndarray]
    ) -> Union[bool, np.ndarray]:
        """
        Check if an object at a given azimuth and altitude is visible (above the horizon).
        """
        return altitude >= self.get_altitude(azimuth)
