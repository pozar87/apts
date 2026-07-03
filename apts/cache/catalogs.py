import functools
import logging
import os
import re
import zlib
import io
from typing import Any, cast, TYPE_CHECKING
from skyfield.api import Loader, load

if TYPE_CHECKING:
    import pandas as pd

from .. import data_loader
from ..config import get_minor_planet_settings

logger = logging.getLogger(__name__)

@functools.lru_cache(maxsize=None)
def get_hipparcos_data() -> "pd.DataFrame":
    """
    Returns a cached Hipparcos catalog as a pandas DataFrame.
    """
    import pandas as pd
    from skyfield.data import hipparcos

    # Ensure the 'data' directory exists
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Use the skyfield loader to cache the file to disk
    loader = Loader(data_dir)
    try:
        # Check if file exists locally first to avoid unnecessary downloads
        # and potential connection issues with the Strasbourg Data Center.
        filename = hipparcos.URL.split("/")[-1]
        path = os.path.join(data_dir, filename)
        if os.path.exists(path):
            with loader.open(hipparcos.URL) as f:
                df = hipparcos.load_dataframe(f)
        else:
            # Attempt download with a shorter timeout if possible via Loader (actually Loader doesn't expose timeout)
            # We wrap in a try-except to provide better error messages and handle Refused connections.
            with loader.open(hipparcos.URL) as f:
                df = hipparcos.load_dataframe(f)
    except Exception as e:
        logger.error(
            f"Failed to load Hipparcos catalog from {hipparcos.URL}: {e}. "
            "If this is a network issue, try running 'python scripts/download_catalogs.py' "
            "to manually fetch the required files."
        )
        # Fallback to an empty DataFrame if loading fails, to allow other parts of the system to function
        df = pd.DataFrame(
            columns=cast(
                Any,
                [
                    "magnitude",
                    "ra_degrees",
                    "dec_degrees",
                    "parallax_mas",
                    "ra_hours",
                    "epoch_year",
                ],
            )
        )

    # Ensure necessary columns exist for plotting consistency
    if not df.empty:
        if "ra_hours" not in df.columns and "ra_degrees" in df.columns:
            df["ra_hours"] = df["ra_degrees"] / 15.0
        if "epoch_year" not in df.columns:
            df["epoch_year"] = 1991.25

    return df


@functools.lru_cache(maxsize=None)
def get_mpcorb_data() -> "pd.DataFrame":
    """
    Returns a cached Minor Planet Center orbit catalog as a pandas DataFrame.
    If 'load_only' is specified in the [minor_planets] config, only those
    planets will be loaded.
    """
    import pandas as pd
    from skyfield.data import mpc

    planets_to_load = get_minor_planet_settings()
    path = data_loader.get_mpcorb_path()

    with load.open(path, reload=False) as f:
        data = zlib.decompress(f.read(), wbits=zlib.MAX_WBITS | 16)

        if planets_to_load:
            # Build a regex pattern to match the packed designations at the start of the line
            # This is much faster than reading line by line
            escaped_designations = [
                re.escape(d.encode("ascii")) for d in planets_to_load
            ]
            pattern = rb"^(?:" + rb"|".join(escaped_designations) + rb").*"
            regex = re.compile(pattern, re.MULTILINE)

            # Find all matching lines and join them
            lines = regex.findall(data)
            data = b"\n".join(lines)

        df = mpc.load_mpcorb_dataframe(io.BytesIO(data))

    # Post-processing to ensure data types are correct and index is set
    if df.empty:
        df = pd.DataFrame(
            data=None,
            columns=[
                "designation_packed",
                "magnitude_H",
                "magnitude_G",
                "epoch_packed",
                "mean_anomaly_degrees",
                "argument_of_perihelion_degrees",
                "longitude_of_ascending_node_degrees",
                "inclination_degrees",
                "eccentricity",
                "mean_daily_motion_degrees",
                "semimajor_axis_au",
                "uncertainty",
                "reference",
                "observations",
                "oppositions",
                "observation_period_years",
                "rms_residual_arcseconds",
                "coarse_perturbers",
                "precise_perturbers",
                "computer_name",
                "hex_flags",
                "designation",
                "last_observation_date",
            ],  # type: ignore
        )
        return df.set_index("designation")

    numeric_cols = [
        "semimajor_axis_au",
        "eccentricity",
        "inclination_degrees",
        "longitude_of_ascending_node_degrees",
        "argument_of_perihelion_degrees",
        "mean_anomaly_degrees",
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    if "designation" in df.columns:
        df["designation"] = df["designation"].str.strip()
        df = df.set_index("designation")

    return df
