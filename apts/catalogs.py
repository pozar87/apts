import logging
from importlib import resources
import pandas as pd
from skyfield.api import Star

from .units import get_unit_registry
from .constants.constellations import constellation_map


_messier_df = None
_bright_stars_df = None
_ngc_df = None

logger = logging.getLogger(__name__)


def _load_messier_with_units():
    # Load Messier catalogue data
    messier_df = pd.read_csv(str(resources.files("apts").joinpath("data/messier.csv")))

    # Set proper dtypes for string columns
    string_columns = ["Messier", "NGC", "Name", "Type", "Constellation"]
    for column in string_columns:
        messier_df[column] = messier_df[column].astype("string")

    # Convert columns to quantities with units
    ureg = get_unit_registry()
    messier_df["Distance"] = messier_df["Distance"].apply(lambda x: x * ureg.light_year)
    messier_df["RA"] = messier_df["RA"].apply(lambda x: x * ureg.hour)
    messier_df["Dec"] = messier_df["Dec"].apply(lambda x: x * ureg.degree)
    messier_df["Width"] = messier_df["Width"].apply(lambda x: x * ureg.arcminute)
    messier_df["Height"] = messier_df["Height"].apply(lambda x: x * ureg.arcminute)
    messier_df["Magnitude"] = messier_df["Magnitude"].apply(lambda x: x * ureg.mag)

    # Pre-calculate Skyfield objects
    messier_df["skyfield_object"] = messier_df.apply(
        lambda row: Star(ra_hours=row.RA.to('hour').magnitude, dec_degrees=row.Dec.to('degree').magnitude), axis=1
    )

    return messier_df


def _parse_ra(ra_str):
    if isinstance(ra_str, str) and ra_str.count(':') == 2:
        parts = ra_str.split(':')
        return float(parts[0]) + float(parts[1])/60 + float(parts[2])/3600
    return None

def _parse_dec(dec_str):
    if isinstance(dec_str, str) and dec_str.count(':') == 2:
        sign = -1 if dec_str.startswith('-') else 1
        parts = dec_str.lstrip('+-').split(':')
        return sign * (float(parts[0]) + float(parts[1])/60 + float(parts[2])/3600)
    return None

def _create_ngc_star(obj):
    ra = _parse_ra(obj.RA)
    dec = _parse_dec(obj.Dec)
    if ra is None or dec is None:
        return None
    return Star(ra_hours=ra, dec_degrees=dec)


def _load_ngc_with_units():
    # Load NGC catalogue data
    ngc_df = pd.read_csv(
        str(resources.files("apts").joinpath("data/ngc.csv")),
        sep=';',
        na_values=['']
    )

    # Rename columns for consistency
    ngc_df.rename(columns={
        'Const': 'Constellation',
        'V-Mag': 'Magnitude',
        'MajAx': 'Size'
    }, inplace=True)

    # Map constellation abbreviations to full names
    ngc_df['Constellation'] = ngc_df['Constellation'].map(constellation_map)  # type: ignore

    # Set proper dtypes for string columns
    string_columns = ["Name", "Type", "Constellation", "NGC"]
    for column in string_columns:
        if column in ngc_df.columns:
            ngc_df[column] = ngc_df[column].astype("string")

    # Convert columns to quantities with units
    ureg = get_unit_registry()
    ngc_df["Magnitude"] = pd.to_numeric(ngc_df["Magnitude"], errors='coerce').fillna(99).apply(lambda x: x * ureg.mag) # type: ignore
    ngc_df["Size"] = ngc_df["Size"].apply(lambda x: x * ureg.arcminute if pd.notna(x) else None)

    # Pre-calculate Skyfield objects
    ngc_df["skyfield_object"] = ngc_df.apply(_create_ngc_star, axis=1)

    return ngc_df


def _load_bright_stars_with_units():
    # Load bright stars catalogue data
    bright_stars_df = pd.read_csv(
        str(resources.files("apts").joinpath("data/bright_stars.csv"))
    )

    # Set proper dtypes for string columns
    string_columns = ["Name"]
    for column in string_columns:
        bright_stars_df[column] = bright_stars_df[column].astype("string")

    # Convert columns to quantities with units
    ureg = get_unit_registry()
    bright_stars_df["RA"] = bright_stars_df["RA"].apply(lambda x: x * ureg.hour)
    bright_stars_df["Dec"] = bright_stars_df["Dec"].apply(lambda x: x * ureg.degree)
    bright_stars_df["Magnitude"] = bright_stars_df["Magnitude"].apply(
        lambda x: x * ureg.mag
    )

    # Pre-calculate Skyfield objects
    bright_stars_df["skyfield_object"] = bright_stars_df.apply(
        lambda row: Star(ra_hours=row.RA.to('hour').magnitude, dec_degrees=row.Dec.to('degree').magnitude), axis=1
    )

    return bright_stars_df


class Catalogs:
    def __init__(self):
        global _messier_df, _ngc_df, _bright_stars_df
        if _messier_df is None:
            logger.info("Loading Messier catalog...")
            _messier_df = _load_messier_with_units()
        if _ngc_df is None:
            logger.info("Loading NGC catalog...")
            _ngc_df = _load_ngc_with_units()
        if _bright_stars_df is None:
            logger.info("Loading Bright Stars catalog...")
            _bright_stars_df = _load_bright_stars_with_units()

    @property
    def MESSIER(self):
        return _messier_df

    @property
    def NGC(self):
        return _ngc_df

    @property
    def BRIGHT_STARS(self):
        return _bright_stars_df


def initialize_catalogs():
    logger.info("Initializing catalogs...")
    Catalogs()
