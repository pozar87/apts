import ephem
import numpy as np
import pandas as pd

_MPC_CENTURY = {"I": 18, "J": 19, "K": 20}
_MPC_MONTH = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
}
_MPC_DAY = {str(d): d for d in range(1, 10)}
_MPC_DAY.update({chr(ord("A") + i): i + 10 for i in range(22)})


def parse_mpc_epoch(packed_epoch):
    """Parses MPC packed epoch format."""
    year = _MPC_CENTURY[packed_epoch[0]] * 100 + int(packed_epoch[1:3])
    month = _MPC_MONTH[packed_epoch[3]]
    day = _MPC_DAY[packed_epoch[4]]
    return ephem.Date(f"{year}/{month}/{day}")


def compute_minor_planet_ephem(object_name, minor_planets_df, ephem_observer):
    """Computes ephem data for a minor planet."""
    try:
        minor_planet_details = minor_planets_df.loc[object_name]
        dp = ephem.EllipticalBody()
        dp._inc = np.deg2rad(minor_planet_details["inclination_degrees"])
        dp._Om = np.deg2rad(minor_planet_details["longitude_of_ascending_node_degrees"])
        dp._om = np.deg2rad(minor_planet_details["argument_of_perihelion_degrees"])
        dp._a = minor_planet_details["semimajor_axis_au"]
        dp._e = minor_planet_details["eccentricity"]
        dp._M = np.deg2rad(minor_planet_details["mean_anomaly_degrees"])
        if pd.notna(minor_planet_details["magnitude_H"]):
            dp._H = minor_planet_details["magnitude_H"]
        if pd.notna(minor_planet_details["magnitude_G"]):
            dp._G = minor_planet_details["magnitude_G"]

        dp._epoch_M = parse_mpc_epoch(minor_planet_details["epoch_packed"])

        dp.compute(ephem_observer)
        return dp.mag, None, None
    except Exception:
        return np.nan, None, None
