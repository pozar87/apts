from typing import Any


def check_simple_visibility(
    azimuth: Any,
    altitude: Any,
    min_altitude: Any,
    min_azimuth: Any,
    max_azimuth: Any,
) -> Any:
    """
    Check if an object at a given azimuth and altitude is visible based on simple altitude and azimuth range bounds.
    """
    min_alt = getattr(min_altitude, "magnitude", min_altitude)
    min_az = getattr(min_azimuth, "magnitude", min_azimuth)
    max_az = getattr(max_azimuth, "magnitude", max_azimuth)

    alt_ok = altitude > min_alt

    if min_az > max_az:
        az_ok = (azimuth >= min_az) | (azimuth <= max_az)
    else:
        az_ok = (azimuth >= min_az) & (azimuth <= max_az)

    return alt_ok & az_ok


def check_visibility(
    azimuth: Any,
    altitude: Any,
    min_altitude: Any,
    min_azimuth: Any,
    max_azimuth: Any,
    horizon: Any | None = None,
) -> Any:
    """
    Check if an object at a given azimuth and altitude is visible.
    If a custom horizon object is provided, delegates to the horizon's visibility check.
    Otherwise, uses simple altitude and azimuth bounds.
    """
    if horizon is not None:
        return horizon.is_visible(azimuth, altitude)

    return check_simple_visibility(azimuth, altitude, min_altitude, min_azimuth, max_azimuth)
