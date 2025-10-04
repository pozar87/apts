import functools
from skyfield.api import load, Loader
from skyfield.data import hipparcos, mpc
from .config import get_minor_planet_settings
from . import data_loader
import re
import pandas as pd
import zlib
import io
import os


@functools.lru_cache(maxsize=None)
def get_timescale():
    """
    Returns a cached timescale object.
    """
    return load.timescale()


@functools.lru_cache(maxsize=None)
def get_ephemeris():
    """
    Returns an ephemeris object, loading from a URL or local file.
    This ensures that the file is downloaded if not present in full mode.
    """
    path_or_url = data_loader.get_ephemeris_path()
    if '://' in path_or_url:
        # In 'full' mode, this is a URL, so we use the default `load`.
        return load(path_or_url)
    else:
        # In 'light' mode, this is an absolute path to a local file.
        # We need a Loader configured for the file's directory.
        directory, filename = os.path.split(path_or_url)
        local_loader = Loader(directory)
        return local_loader(filename)


@functools.lru_cache(maxsize=None)
def get_hipparcos_data() -> pd.DataFrame:
    """
    Returns a cached Hipparcos catalog as a pandas DataFrame.
    """
    with load.open(hipparcos.URL) as f:
        return hipparcos.load_dataframe(f)


@functools.lru_cache(maxsize=None)
def get_mpcorb_data() -> pd.DataFrame:
    """
    Returns a cached Minor Planet Center orbit catalog as a pandas DataFrame.
    If 'load_only' is specified in the [minor_planets] config, only those
    planets will be loaded.
    """
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
            ]
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