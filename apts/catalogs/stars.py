import logging
from importlib import resources

import numpy as np
import pandas as pd
from skyfield.api import Star

from ..units import get_unit_registry

logger = logging.getLogger(__name__)

_bright_stars_df = None

def _load_bright_stars_with_units():
    # Load bright stars catalogue data
    bright_stars_df = pd.read_csv(
        str(resources.files("apts").joinpath("data/bright_stars.csv"))
    )

    # Set proper dtypes for string columns
    string_columns = ["Name"]
    for column in string_columns:
        bright_stars_df[column] = bright_stars_df[column].astype("string")

    # Pre-calculate Skyfield objects using raw floats before wrapping in Quantities
    # Optimization: avoiding row-wise apply and costly Quantity.to().magnitude calls
    bright_stars_df["skyfield_object"] = [  # type: ignore
        Star(ra_hours=ra, dec_degrees=dec)
        for ra, dec in zip(bright_stars_df["RA"], bright_stars_df["Dec"])
    ]

    # Store float versions for performance-critical filtering and calculations
    # to avoid Pint and Skyfield object overhead in high-frequency loops.
    bright_stars_df["ra_hours"] = bright_stars_df["RA"].values
    bright_stars_df["dec_degrees"] = bright_stars_df["Dec"].values
    bright_stars_df["Magnitude_float"] = bright_stars_df["Magnitude"].values

    # Pre-calculate trigonometric values for fixed stars to avoid redundant
    # transcendental function calls in hot paths (visibility, scoring).
    ra_rad = np.deg2rad(bright_stars_df["ra_hours"].values * 15.0)
    dec_rad = np.deg2rad(bright_stars_df["dec_degrees"].values)
    bright_stars_df["sin_ra"] = np.sin(ra_rad)
    bright_stars_df["cos_ra"] = np.cos(ra_rad)
    bright_stars_df["sin_dec"] = np.sin(dec_rad)
    bright_stars_df["cos_dec"] = np.cos(dec_rad)

    # Convert columns to quantities with units (vectorized)
    # Optimization: list(values * unit) is much faster than Series.apply()
    ureg = get_unit_registry()
    bright_stars_df["RA"] = list(bright_stars_df["RA"].values * ureg.hour)
    bright_stars_df["Dec"] = list(bright_stars_df["Dec"].values * ureg.degree)
    bright_stars_df["Magnitude"] = list(bright_stars_df["Magnitude"].values * ureg.mag)

    return bright_stars_df

def get_bright_stars() -> pd.DataFrame:
    global _bright_stars_df
    if _bright_stars_df is None:
        logger.info("Loading Bright Stars catalog...")
        _bright_stars_df = _load_bright_stars_with_units()
    return _bright_stars_df  # type: ignore
