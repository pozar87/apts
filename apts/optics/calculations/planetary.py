import math
from typing import Any, Optional, Union, cast

import numpy


def calculate_planetary_size_in_pixels(
    angular_diameter: Any,
    pixel_scale_magnitude: float,
) -> Optional[Union[float, numpy.ndarray]]:
    """
    Calculates the projected size of a planet on the sensor in pixels.
    Uses the planet's angular diameter and the setup's pixel scale.
    """
    if pixel_scale_magnitude == 0:
        return None

    res = angular_diameter / pixel_scale_magnitude
    if numpy.isscalar(res):
        return float(cast(Any, res))
    return numpy.asarray(res)


def calculate_saturn_ring_size_in_pixels(
    major_axis_arcsec: Any,
    minor_axis_arcsec: Any,
    pixel_scale_magnitude: float,
) -> Optional[tuple[Union[float, numpy.ndarray], Union[float, numpy.ndarray]]]:
    """
    Calculates the projected size of Saturn's rings on the sensor in pixels.
    Returns a tuple (major_axis_pixels, minor_axis_pixels).
    """
    if pixel_scale_magnitude == 0:
        return None

    major = major_axis_arcsec / pixel_scale_magnitude
    minor = minor_axis_arcsec / pixel_scale_magnitude

    def _maybe_cast(val):
        if numpy.isscalar(val):
            return float(cast(Any, val))
        return numpy.asarray(val)

    return _maybe_cast(major), _maybe_cast(minor)


def calculate_max_planetary_rotation_duration(
    pixel_scale_magnitude: float,
    r_eq: float,
    period: float,
    cos_de: float,
    tolerance_pixels: float = 1.0,
) -> Optional[float]:
    """
    Calculates the maximum recording duration (in seconds) before planetary rotation
    causes a blur exceeding the given pixel tolerance.
    """
    if r_eq <= 0 or period <= 0:
        return None

    # Angular velocity of a point at the center of the disk as seen from Earth (arcsec/s)
    # v_arcsec = (2 * pi * r_eq_arcsec * cos(De)) / T
    omega = (2.0 * math.pi * r_eq * cos_de) / period

    if omega <= 1e-12:
        return 3600.0  # Cap at 1 hour for very slow rotators

    t_max = (tolerance_pixels * pixel_scale_magnitude) / omega
    return t_max
