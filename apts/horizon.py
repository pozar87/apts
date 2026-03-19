import os
from typing import Optional, Union
import numpy as np
from scipy.interpolate import interp1d


class Horizon:
    def __init__(self, file_path: Optional[str] = None, min_altitude: float = 0.0):
        self.file_path = file_path
        self.min_altitude = float(min_altitude)
        self.azimuths = np.array([0.0, 360.0])
        self.altitudes = np.array([self.min_altitude, self.min_altitude])
        if file_path and os.path.exists(file_path):
            self._load_from_file(file_path)
        # Using any to avoid pyright issue with "extrapolate" literal
        self._interp = interp1d(
            self.azimuths, self.altitudes, kind="linear", fill_value="extrapolate" # type: ignore
        )

    def _load_from_file(self, file_path: str):
        if file_path.lower().endswith(".ini"):
            import configparser

            config = configparser.ConfigParser()
            try:
                config.read(file_path)
                if config.has_section("landscape") and config.has_option(
                    "landscape", "polygonal_horizon_list"
                ):
                    hrz_filename = config.get("landscape", "polygonal_horizon_list")
                    # Assume .hrz is in the same directory as .ini
                    hrz_path = os.path.join(os.path.dirname(file_path), hrz_filename)
                    if os.path.exists(hrz_path):
                        file_path = hrz_path
                    else:
                        return
                else:
                    return
            except Exception:
                return

        az = []
        alt = []
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith(("#", ";")):
                    continue
                parts = line.split()
                if len(parts) >= 2:
                    try:
                        az.append(float(parts[0]))
                        alt.append(float(parts[1]))
                    except ValueError:
                        continue

        if not az:
            return

        # Ensure sorted
        data = sorted(zip(az, alt))
        az, alt = map(list, zip(*data))

        # Ensure 0 and 360 are covered for interpolation
        if az[0] > 0:
            if az[-1] == 360.0:
                az.insert(0, 0.0)
                alt.insert(0, alt[-1])
            else:
                az.insert(0, 0.0)
                alt.insert(0, alt[0])

        if az[-1] < 360:
            az.append(360.0)
            alt.append(alt[0])

        self.azimuths = np.array(az)
        self.altitudes = np.array(alt)

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
