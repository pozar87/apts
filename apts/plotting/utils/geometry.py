from typing import TYPE_CHECKING, Union

import numpy
import pandas as pd
from skyfield.units import Angle

from apts.constants.plot import CoordinateSystem
from apts.i18n import get_language
from apts.utils import planetary

from ...constants import ObjectTableLabels

if TYPE_CHECKING:
    from apts.observations import Observation


def calculate_parallactic_angle(
    latitude_deg: float,
    declination: Union[float, numpy.ndarray, Angle],
    azimuth: Union[float, numpy.ndarray, Angle],
) -> Union[float, numpy.ndarray]:
    """
    Calculates the parallactic angle in degrees.
    Optimization: supports vectorized NumPy arrays for declination and azimuth.
    """
    dec_deg = (
        declination.degrees  # type: ignore[union-attr]
        if hasattr(declination, "degrees")
        else numpy.asarray(declination)
    )
    # Mask for objects too close to poles to avoid division by zero/instability
    mask = numpy.abs(dec_deg) <= 89.99  # type: ignore[call-overload]

    lat_rad = numpy.deg2rad(latitude_deg)
    dec_rad = (
        declination.radians  # type: ignore[union-attr]
        if hasattr(declination, "radians")
        else numpy.deg2rad(numpy.asarray(declination))
    )
    az_rad = (
        azimuth.radians  # type: ignore[union-attr]
        if hasattr(azimuth, "radians")
        else numpy.deg2rad(numpy.asarray(azimuth))
    )

    q_rad = numpy.zeros_like(dec_rad)

    # Calculate only for non-polar objects
    if numpy.any(mask):
        sin_q = numpy.sin(az_rad) * numpy.cos(lat_rad) / numpy.cos(dec_rad)  # type: ignore[call-overload]
        sin_q = numpy.clip(sin_q, -1.0, 1.0)
        q_rad = numpy.where(mask, numpy.arcsin(sin_q), 0.0)  # type: ignore[call-overload]

    res = numpy.rad2deg(q_rad)  # type: ignore[call-overload]
    return float(res) if numpy.isscalar(res) else res  # type: ignore[arg-type]


def calculate_ellipse_angle(
    pos_angle: Union[float, numpy.ndarray],
    parallactic_angle: Union[float, numpy.ndarray, Angle],
    coordinate_system: CoordinateSystem,
    flipped_horizontally: bool,
    flipped_vertically: bool,
) -> Union[float, numpy.ndarray]:
    """
    Calculates the final rotation angle for a celestial object's ellipse.
    Optimization: supports vectorized NumPy arrays for pos_angle and parallactic_angle.
    """
    pos_angle_arr = numpy.asarray(pos_angle)

    if coordinate_system == CoordinateSystem.HORIZONTAL:
        p_angle_deg = (
            parallactic_angle.degrees  # type: ignore[union-attr]
            if hasattr(parallactic_angle, "degrees")
            else numpy.asarray(parallactic_angle)
        )
        angle = -(pos_angle_arr - p_angle_deg)
    else:  # EQUATORIAL
        angle = -pos_angle_arr

    if flipped_horizontally:
        angle = -angle
    if flipped_vertically:
        angle = 180 - angle

    res = angle % 360
    return float(res) if numpy.isscalar(res) else res  # type: ignore[arg-type]


def get_object_angular_size_deg(observation: "Observation", object_name: str) -> float:
    """Gets the angular size of a solar system object in degrees."""
    # Handle translated names by reverse-translating if necessary
    current_lang = get_language()
    if current_lang != "en":
        reverse_map = planetary.get_reverse_translated_planet_names(current_lang)
        object_name = reverse_map.get(object_name, object_name)

    # Use the technical name for consistent matching regardless of language
    technical_name = planetary.get_technical_name(object_name)

    # Search in all computed planets (language-independent)
    planets_df = observation.local_planets.objects
    object_data = planets_df[
        (planets_df[ObjectTableLabels.NAME] == technical_name)
        | (planets_df[ObjectTableLabels.NAME] == object_name)
    ]

    if not object_data.empty:
        size_arcsec = object_data.iloc[0].get(ObjectTableLabels.SIZE)
        if pd.notna(size_arcsec):
            if hasattr(size_arcsec, "magnitude"):
                size_arcsec = size_arcsec.magnitude
            return float(size_arcsec) / 3600.0

    # Fallback to English-named visible planets
    visible_planets = observation.get_visible_planets(language="en")
    object_data = visible_planets[
        (visible_planets["TechnicalName"] == object_name)
        | (visible_planets["Name"] == object_name)
    ]
    if not object_data.empty:
        size_arcsec = object_data.iloc[0].get(ObjectTableLabels.SIZE)
        if pd.notna(size_arcsec):
            if hasattr(size_arcsec, "magnitude"):
                size_arcsec = size_arcsec.magnitude
            return float(size_arcsec) / 3600.0

    # Final fallback for Sun/Moon if not found above
    if technical_name in ["sun", "moon"]:
        return 0.5
    return 0.0
