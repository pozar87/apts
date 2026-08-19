import pandas as pd

from ..constants.objecttablelabels import TECHNICAL_COLUMNS
from ..utils.astronomy.refraction import calculate_refraction
from ..utils.astronomy.calculations import (
    vectorized_geometric_compute,
    vectorized_geometric_imaging_duration,
)


def filter_technical_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes internal technical calculation and caching columns from a DataFrame
    before returning or presenting it to the user.
    """
    cols_to_drop = [col for col in TECHNICAL_COLUMNS if col in df.columns]
    if cols_to_drop:
        return df.drop(columns=cols_to_drop, errors="ignore")
    return df


# Keep the original exports for backward compatibility
__all__ = [
    "calculate_refraction",
    "vectorized_geometric_compute",
    "vectorized_geometric_imaging_duration",
    "filter_technical_columns",
]
