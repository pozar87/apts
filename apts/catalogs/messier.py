import logging
import urllib.parse
from importlib import resources
from typing import cast

import numpy as np
import pandas as pd
from skyfield.api import Star

from ..constants.objecttablelabels import ObjectTableLabels
from ..constants.strategies import DSOType
from ..units import get_unit_registry

logger = logging.getLogger(__name__)

_messier_df = None

def _load_messier_with_units():
    # Load Messier catalogue data
    messier_df = pd.read_csv(str(resources.files("apts").joinpath("data/messier.csv")))

    # Set proper dtypes for string columns
    string_columns = ["Messier", "NGC", "Name", "Type", "Constellation"]
    for column in string_columns:
        messier_df[column] = messier_df[column].astype("string")

    # Map Messier types to DSOType
    messier_type_map = {
        "Diffuse Nebula": DSOType.DN,
        "Double Star": DSOType.DS,
        "Elliptical Galaxy": DSOType.GX,
        "Globular Cluster": DSOType.GC,
        "Group/Asterism": DSOType.AST,
        "Irregular Galaxy": DSOType.GX,
        "Lenticular (S0) Galaxy": DSOType.GX,
        "Open Cluster": DSOType.OC,
        "Planetary Nebula": DSOType.PN,
        "Spiral Galaxy": DSOType.GX,
        "Star Cloud": DSOType.SC,
        "Supernova Remnant": DSOType.SNR,
        'Pleiades. Subaru."': DSOType.OC,  # Special case for M45 entry
    }
    messier_df[ObjectTableLabels.DSO_TYPE] = (
        messier_df["Type"]
        .map(messier_type_map.get)
        .fillna(cast(DSOType, DSOType.OTHER))
    )

    # Pre-calculate Skyfield objects using raw floats before wrapping in Quantities
    # Optimization: avoiding row-wise apply and costly Quantity.to().magnitude calls
    messier_df["skyfield_object"] = [  # type: ignore
        Star(ra_hours=ra, dec_degrees=dec)
        for ra, dec in zip(messier_df["RA"], messier_df["Dec"])
    ]

    # Store float versions for performance-critical filtering and calculations
    # to avoid Pint and Skyfield object overhead in high-frequency loops.
    messier_df["ra_hours"] = messier_df["RA"].values
    messier_df["dec_degrees"] = messier_df["Dec"].values
    messier_df["Magnitude_float"] = messier_df["Magnitude"].values

    # Pre-calculate trigonometric values for fixed stars to avoid redundant
    # transcendental function calls in hot paths (visibility, scoring).
    ra_rad = np.deg2rad(messier_df["ra_hours"].values * 15.0)
    dec_rad = np.deg2rad(messier_df["dec_degrees"].values)
    messier_df["sin_ra"] = np.sin(ra_rad)
    messier_df["cos_ra"] = np.cos(ra_rad)
    messier_df["sin_dec"] = np.sin(dec_rad)
    messier_df["cos_dec"] = np.cos(dec_rad)

    # Convert columns to quantities with units (vectorized)
    # Optimization: list(values * unit) is much faster than Series.apply()
    ureg = get_unit_registry()
    messier_df["Distance"] = list(messier_df["Distance"].values * ureg.light_year)
    messier_df["RA"] = list(messier_df["RA"].values * ureg.hour)
    messier_df["Dec"] = list(messier_df["Dec"].values * ureg.degree)
    messier_df[ObjectTableLabels.SIZE_MAJOR] = list(
        messier_df["Width"].values * ureg.arcminute
    )
    messier_df[ObjectTableLabels.SIZE_MINOR] = list(
        messier_df["Height"].values * ureg.arcminute
    )
    messier_df["Magnitude"] = list(messier_df["Magnitude"].values * ureg.mag)

    # Drop redundant columns
    messier_df.drop(columns=["Width", "Height"], inplace=True)

    # Add external links (vectorized list comprehension)
    quoted_messier = [urllib.parse.quote(str(x)) for x in messier_df["Messier"]]
    messier_df[ObjectTableLabels.SIMBAD] = [
        f"https://simbad.u-strasbg.fr/simbad/sim-basic?Ident={q}"
        for q in quoted_messier
    ]
    messier_df[ObjectTableLabels.ALADIN] = [
        f"https://aladin.cds.unistra.fr/AladinLite/?target={q}" for q in quoted_messier
    ]
    messier_df[ObjectTableLabels.ASTROBIN] = [
        f"https://www.astrobin.com/search/?q={q}" for q in quoted_messier
    ]

    return messier_df

def get_messier() -> pd.DataFrame:
    global _messier_df
    if _messier_df is None:
        logger.info("Loading Messier catalog...")
        _messier_df = _load_messier_with_units()
    return _messier_df  # type: ignore
