from .base import config

def get_data_settings() -> str:
    """
    Reads the data settings from the [data] section.

    Returns:
        str: The data mode ('light' or 'full').
    """
    return config.get("data", "mode", fallback="light")


def get_jovian_ephemeris_url() -> str:
    """
    Reads the Jovian ephemeris URL from the [data] section.

    Returns:
        str: The URL to download the Jovian ephemeris from.
    """
    # Default is jup365.bsp (~1.1GB, 1600-2600) which contains high-precision Galilean moon orbits.
    # A smaller alternative (138MB) is jup300.bsp, but it lacks Galilean satellites at standard IDs.
    # The high-precision jup310.bsp (~1.2GB) is also available from NASA NAIF:
    # https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/a_old_versions/jup310.bsp
    default_url = (
        "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/jup365.bsp"
    )
    return config.get("data", "jovian_ephemeris_url", fallback=default_url)
