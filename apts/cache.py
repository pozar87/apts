import functools
from skyfield.api import load
from skyfield.data import hipparcos, mpc
import pandas as pd
import zlib
import io

@functools.lru_cache(maxsize=None)
def get_timescale():
    """
    Returns a cached timescale object.
    """
    return load.timescale()

@functools.lru_cache(maxsize=None)
def get_ephemeris():
    """
    Returns an ephemeris object, loading from a URL.
    This ensures that the file is downloaded if not present.
    """
    # de440 is a comprehensive ephemeris that includes dwarf planets.
    url = "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de440.bsp"
    return load(url)

@functools.lru_cache(maxsize=None)
def get_hipparcos_data() -> pd.DataFrame:
    """
    Returns a cached Hipparcos catalog as a pandas DataFrame.
    """
    with load.open(hipparcos.URL) as f:
        return hipparcos.load_dataframe(f)

from .config import get_minor_planet_settings
import re

@functools.lru_cache(maxsize=None)
def get_mpcorb_data() -> pd.DataFrame:
    """
    Returns a cached Minor Planet Center orbit catalog as a pandas DataFrame.
    If 'load_only' is specified in the [minor_planets] config, only those
    planets will be loaded.
    """
    planets_to_load = get_minor_planet_settings()

    with load.open(mpc.MPCORB_URL, reload=False) as f:
        data = zlib.decompress(f.read(), wbits=zlib.MAX_WBITS | 16)

        if planets_to_load:
            # Build a regex pattern to match the packed designations at the start of the line
            # This is much faster than reading line by line
            escaped_designations = [re.escape(d.encode('ascii')) for d in planets_to_load]
            pattern = rb'^(?:' + rb'|'.join(escaped_designations) + rb')'
            regex = re.compile(pattern, re.MULTILINE)

            # Find all matching lines and join them
            lines = regex.findall(data)
            filtered_data = b'\n'.join(lines)

            # If no lines are found, return an empty dataframe with correct columns
            if not filtered_data:
                # Create an empty dataframe with the expected columns from mpc.mpcorb_dataframe
                # This avoids errors when no planets are found
                return pd.DataFrame(columns=[
                    'designation_packed', 'magnitude_H', 'magnitude_G', 'epoch_packed',
                    'mean_anomaly_degrees', 'argument_of_perihelion_degrees',
                    'longitude_of_ascending_node_degrees', 'inclination_degrees',
                    'eccentricity', 'mean_daily_motion_degrees', 'semimajor_axis_au',
                    'uncertainty', 'reference', 'observations', 'oppositions',
                    'observation_period_years', 'rms_residual_arcseconds',
                    'coarse_perturbers', 'precise_perturbers', 'computer_name',
                    'hex_flags', 'designation', 'last_observation_date'
                ])

            data = filtered_data

        return mpc.load_mpcorb_dataframe(io.BytesIO(data))