import functools
import logging
import copy
from typing import Any, cast
from skyfield.api import load

from .. import data_loader
from ..config import get_jovian_ephemeris_url

logger = logging.getLogger(__name__)

STATIONS_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"

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
    This ensures that the file is downloaded if not present.
    """
    path_or_url = data_loader.get_ephemeris_path()
    return load(path_or_url)


@functools.lru_cache(maxsize=None)
def get_jovian_ephemeris():
    """
    Returns a merged ephemeris containing both planetary and Jovian satellite data.
    """
    eph = get_ephemeris()
    # High-precision Galilean satellite orbits from SPICE kernel.
    # We default to jup310.bsp (1.1GB), but it can be overridden in config
    # to a smaller alternative (e.g. from skyfield-data).
    jovian_path = get_jovian_ephemeris_url()
    try:
        eph_jovian = cast(Any, load(jovian_path))
        # Create a new SpiceKernel object or merge segments.
        # In Skyfield, kernels can be merged by extending the .segments list.
        # We perform a shallow copy of the main ephemeris to avoid polluting it globally

        # For Jovian satellites, we prioritize the Jovian kernel
        # We perform a shallow copy of the Jovian ephemeris and add planetary segments
        merged_eph = cast(Any, copy.copy(eph_jovian))
        merged_eph.segments = list(eph_jovian.segments) + list(cast(Any, eph).segments)
        return merged_eph
    except Exception as e:
        logger.error(f"Failed to load Jovian ephemeris: {e}")
        return eph
