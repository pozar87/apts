import logging
from datetime import timedelta
from typing import TYPE_CHECKING, Optional

import numpy
import pandas as pd
from matplotlib import pyplot
from skyfield.units import Angle

from apts.constants.plot import CoordinateSystem
from ..constants import ObjectTableLabels

if TYPE_CHECKING:
    from apts.observations import Observation

logger = logging.getLogger(__name__)


def calculate_parallactic_angle(
    latitude_deg: float, declination: "Angle", azimuth: "Angle"
) -> float:
    """Calculates the parallactic angle in degrees."""
    if abs(declination.degrees) > 89.99:  # type: ignore
        return 0.0

    lat_rad = numpy.deg2rad(latitude_deg)
    dec_rad = declination.radians  # type: ignore
    az_rad = azimuth.radians  # type: ignore

    sin_q = numpy.sin(az_rad) * numpy.cos(lat_rad) / numpy.cos(dec_rad)  # type: ignore
    sin_q = numpy.clip(sin_q, -1.0, 1.0)
    q_rad = numpy.arcsin(sin_q)
    return numpy.rad2deg(q_rad)


def calculate_ellipse_angle(
    pos_angle: float,
    parallactic_angle: float,
    coordinate_system: CoordinateSystem,
    flipped_horizontally: bool,
    flipped_vertically: bool,
) -> float:
    """Calculates the final rotation angle for a celestial object's ellipse."""
    if coordinate_system == CoordinateSystem.HORIZONTAL:
        if hasattr(parallactic_angle, "degrees"):
            angle = pos_angle - parallactic_angle.degrees
        else:
            angle = pos_angle - parallactic_angle
    else:  # EQUATORIAL
        angle = pos_angle

    if flipped_horizontally:
        angle = -angle
    if flipped_vertically:
        angle = 180 - angle

    return angle


def get_object_angular_size_deg(observation: "Observation", object_name: str) -> float:
    """Gets the angular size of a solar system object in degrees."""
    visible_planets = observation.get_visible_planets()
    object_data = visible_planets[visible_planets["Name"] == object_name]
    if not object_data.empty:
        size_arcsec = object_data.iloc[0].get(ObjectTableLabels.SIZE)
        if pd.notna(size_arcsec):
            if hasattr(size_arcsec, "magnitude"):
                size_arcsec = size_arcsec.magnitude
            return float(size_arcsec) / 3600.0
    # Default size if not found or NaN
    if object_name in ["Sun", "Moon"]:
        return 0.5
    return 0.0


def get_brightness_color(magnitude: Optional[float]) -> str:
    """
    Calculates a grayscale color based on the magnitude of a celestial object.
    Dimmer objects get a color closer to the background.
    """
    if hasattr(magnitude, "magnitude"):
        magnitude = getattr(magnitude, "magnitude")  # type: ignore
    if magnitude is None or pd.isna(magnitude):
        return "none"

    # Normalize magnitude to a 0-1 range for color mapping
    # Typical naked-eye limit is 6. Faintest in catalogs can be ~15-20.
    # Let's cap the range for better visual differentiation.
    min_mag = 2.0  # Brightest objects
    max_mag = 12.0  # Faintest objects for fill variation

    norm_mag = (magnitude - min_mag) / (max_mag - min_mag)
    norm_mag = numpy.clip(norm_mag, 0, 1)

    # Invert the value, so brighter objects (lower mag) are lighter
    brightness = 1 - norm_mag

    # Blend the color with the background color to avoid pure white/black
    bg_color = pyplot.colormaps.get_cmap("gray")(0)
    fg_color = pyplot.colormaps.get_cmap("gray")(brightness)

    # Simple alpha blending: final_color = fg * alpha + bg * (1 - alpha)
    # We use brightness as a proxy for alpha here.
    final_color_val = fg_color[0] * brightness + bg_color[0] * (1 - brightness)
    final_color_val = numpy.clip(final_color_val, 0, 1)

    return str(final_color_val)


def normalize_dates(start, stop):
    if start is None or stop is None:
        return (None, None)
    if stop < start:
        stop += timedelta(days=1)
    return (start, stop)


def create_ra_zoom_mask(ra_hours, xlim):
    """
    Create a mask for RA values that fall within the zoom window,
    handling the case where the window crosses the RA = 0/24 boundary.

    Args:
        ra_hours: array of RA values in hours
        xlim: tuple of (xmin, xmax) RA values in hours

    Returns:
        boolean array mask indicating which RA values are in the zoom window
    """
    ra_min, ra_max = xlim

    if ra_min <= ra_max:
        # Normal case: no wrapping
        return (ra_hours >= ra_min) & (ra_hours <= ra_max)
    else:
        # Wrapping case: window crosses RA = 0/24 boundary
        return (ra_hours >= ra_min) | (ra_hours <= ra_max)


def mark_observation(
    observation: "Observation", plot, dark_mode_enabled: bool, style: dict
):
    if plot is None:
        return
    plot.axvspan(
        observation.start,
        observation.stop,
        color=style.get(
            "SPAN_BACKGROUND_COLOR",
            "#DDDDDD" if not dark_mode_enabled else "#FFFFFF",
        ),
        alpha=0.07 if dark_mode_enabled else 0.2,
    )
    moon_start, moon_stop = normalize_dates(
        observation.place.moonrise_time(), observation.place.moonset_time()
    )
    plot.axvspan(
        moon_start,
        moon_stop,
        color=style.get(
            "MOON_SPAN_COLOR", "#FFFFE0" if not dark_mode_enabled else "#5A1A75"
        ),
        alpha=0.07 if dark_mode_enabled else 0.1,
    )

    plot.axvline(observation.start, color=style["GRID_COLOR"], linestyle="--")
    plot.axvline(observation.time_limit, color=style["GRID_COLOR"], linestyle="--")


def mark_good_conditions(
    observation: "Observation",
    plot,
    minimal,
    maximal,
    dark_mode_enabled: bool,
    style: dict,
):
    if plot is None:
        return
    plot.axhspan(
        minimal,
        maximal,
        color=style.get(
            "GOOD_CONDITION_HL_COLOR",
            "#90EE90" if not dark_mode_enabled else "#007447",
        ),
        alpha=0.1,
    )
