import logging
from importlib import resources
import pandas as pd

from .units import get_unit_registry


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

    return messier_df


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

    # RA parsing from HH:MM:SS.SS string to hours
    ngc_df['RA'] = ngc_df['RA'].apply(
        lambda x: (
            (lambda parts: float(parts[0]) + float(parts[1])/60 + float(parts[2])/3600)(x.split(':'))
        ) if isinstance(x, str) and len(x.split(':')) == 3 else None
    )

    # Dec parsing from DD:MM:SS.S string to degrees
    ngc_df['Dec'] = ngc_df['Dec'].apply(
        lambda x: (
            (lambda sign, parts: sign * (float(parts[0]) + float(parts[1])/60 + float(parts[2])/3600))
            (-1 if x.startswith('-') else 1, x.lstrip('+-').split(':'))
        ) if isinstance(x, str) and len(x.split(':')) == 3 else None
    )

    # Set proper dtypes for string columns
    string_columns = ["Name", "Type", "Constellation", "NGC", "IC", "Common names"]
    for column in string_columns:
        if column in ngc_df.columns:
            ngc_df[column] = ngc_df[column].astype("string")

    # Convert columns to quantities with units
    ureg = get_unit_registry()
    ngc_df["RA"] = ngc_df["RA"].apply(lambda x: x * ureg.hour if pd.notna(x) else None)
    ngc_df["Dec"] = ngc_df["Dec"].apply(lambda x: x * ureg.degree if pd.notna(x) else None)
    ngc_df["Magnitude"] = ngc_df["Magnitude"].apply(lambda x: x * ureg.mag if pd.notna(x) else None)
    ngc_df["Size"] = ngc_df["Size"].apply(lambda x: x * ureg.arcminute if pd.notna(x) else None)

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

    return bright_stars_df


class Catalogs:
    @property
    def MESSIER(self):
        global _messier_df
        if _messier_df is None:
            _messier_df = _load_messier_with_units()
        return _messier_df

    @property
    def NGC(self):
        global _ngc_df
        if _ngc_df is None:
            _ngc_df = _load_ngc_with_units()
        return _ngc_df

    @property
    def BRIGHT_STARS(self):
        global _bright_stars_df
        if _bright_stars_df is None:
            _bright_stars_df = _load_bright_stars_with_units()
        return _bright_stars_df


def initialize_catalogs():
    logger.info("Initializing catalogs...")
    # This function will trigger the loading of data with units
    # when it's explicitly called.
    _ = Catalogs().MESSIER
    _ = Catalogs().BRIGHT_STARS
    _ = Catalogs().NGC
