import numpy
import pandas as pd
from typing import TYPE_CHECKING, Any, cast
from skyfield.units import Angle

from apts.constants.plot import CoordinateSystem
from apts.i18n import get_language
from apts.utils import planetary
from ...constants import ObjectTableLabels

if TYPE_CHECKING:
    from apts.observations import Observation


def calculate_parallactic_angle(
    latitude_deg: float, declination: Any, azimuth: Any
) -> float:
    """Calculates the parallactic angle in degrees."""
    dec_deg = (
        declination.degrees if hasattr(declination, "degrees") else float(declination)
    )
    if abs(dec_deg) > 89.99:
        return 0.0

    lat_rad = numpy.deg2rad(latitude_deg)
    dec_rad = (
        declination.radians if hasattr(declination, "radians") else numpy.deg2rad(dec_deg)
    )
    az_rad = (
        azimuth.radians
        if hasattr(azimuth, "radians")
        else numpy.deg2rad(azimuth)
    )

    sin_q = numpy.sin(az_rad) * numpy.cos(lat_rad) / numpy.cos(dec_rad)
    sin_q = numpy.clip(sin_q, -1.0, 1.0)
    q_rad = numpy.arcsin(sin_q)
    return numpy.rad2deg(q_rad)


def calculate_ellipse_angle(
    pos_angle: float,
    parallactic_angle: float | Angle,
    coordinate_system: CoordinateSystem,
    flipped_horizontally: bool,
    flipped_vertically: bool,
) -> float:
    """Calculates the final rotation angle for a celestial object's ellipse."""
    if coordinate_system == CoordinateSystem.HORIZONTAL:
        if hasattr(parallactic_angle, "degrees"):
            angle = pos_angle - cast(Any, parallactic_angle).degrees
        else:
            angle = pos_angle - cast(float, parallactic_angle)
        angle = -angle
    else:  # EQUATORIAL
        angle = -pos_angle

    if flipped_horizontally:
        angle = -angle
    if flipped_vertically:
        angle = 180 - angle

    return angle % 360


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
