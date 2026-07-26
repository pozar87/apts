from typing import TYPE_CHECKING, Any, Optional, cast

import numpy
import pandas as pd
from matplotlib import axes

from apts.constants.plot import CoordinateSystem
from apts.i18n import gettext_
from apts.plotting.utils import calculate_ellipse_angle, calculate_parallactic_angle

from ...constants import ObjectTableLabels

if TYPE_CHECKING:
    from ...observations import Observation


def setup_polar_ax(
    observation: "Observation",
    ax: axes.Axes,
    style: dict,
    coordinate_system: CoordinateSystem,
):
    """Sets up the axes for a polar skymap."""
    polar_ax = cast(Any, ax)
    is_sh = observation.place.lat_decimal < 0
    if coordinate_system == CoordinateSystem.HORIZONTAL:
        polar_ax.set_rlim(0, 90)
        polar_ax.set_theta_zero_location("S" if is_sh else "N")
        polar_ax.set_theta_direction(1)
        polar_ax.set_yticks([0, 30, 60, 90])
        polar_ax.set_yticklabels(["90°", "60°", "30°", "0°"], color=style["TEXT_COLOR"])
        polar_ax.set_rlabel_position(22.5)
        cardinal_directions = {
            "N": 0,
            "E": numpy.pi / 2,
            "S": numpy.pi,
            "W": 3 * numpy.pi / 2,
        }
        for direction, angle in cardinal_directions.items():
            polar_ax.text(
                angle,
                95,
                direction,
                ha="center",
                va="center",
                color=style["TEXT_COLOR"],
                fontsize=12,
            )
    else:  # Equatorial
        polar_ax.set_rlim(0, 90)
        polar_ax.set_theta_zero_location("S" if is_sh else "N")
        polar_ax.set_theta_direction(1)  # RA increases eastward
        polar_ax.set_yticks([0, 30, 60, 90])
        if is_sh:
            polar_ax.set_yticklabels(
                ["-90°", "-60°", "-30°", "0°"], color=style["TEXT_COLOR"]
            )
        else:
            polar_ax.set_yticklabels(
                ["90°", "60°", "30°", "0°"], color=style["TEXT_COLOR"]
            )
        polar_ax.set_rlabel_position(22.5)
        ra_labels = [f"{h}h" for h in range(0, 24, 3)]
        polar_ax.set_xticklabels(ra_labels, color=style["TEXT_COLOR"])

    ax.grid(True, color=style["GRID_COLOR"], linestyle="--", linewidth=0.5)


def setup_zoom_ax(
    observation: "Observation",
    ax: axes.Axes,
    style: dict,
    coordinate_system: CoordinateSystem,
    zoom_deg: float,
    target_alt: Any,
    target_az: Any,
    target_ra: Any,
    target_dec: Any,
):
    """Sets up the axes for a zoomed-in skymap."""
    if coordinate_system == CoordinateSystem.HORIZONTAL:
        ax.set_xlabel(gettext_("Azimuth (°)"), color=style["TEXT_COLOR"])
        ax.set_ylabel(gettext_("Altitude (°)"), color=style["TEXT_COLOR"])
        half_zoom = zoom_deg / 2
        ax.set_xlim(target_az.degrees - half_zoom, target_az.degrees + half_zoom)
        ax.set_ylim(target_alt.degrees - half_zoom, target_alt.degrees + half_zoom)
        ax.set_aspect("equal", adjustable="box")
    else:  # Equatorial
        ax.set_xlabel(gettext_("Right Ascension (hours)"), color=style["TEXT_COLOR"])
        ax.set_ylabel(gettext_("Declination (°)"), color=style["TEXT_COLOR"])
        dec_rad = numpy.deg2rad(target_dec.degrees)
        half_zoom_dec = zoom_deg / 2.0
        half_zoom_ra_hours = half_zoom_dec / (15.0 * numpy.cos(dec_rad))
        is_sh = observation.place.lat_decimal < 0
        if is_sh:
            # For Southern Hemisphere, North should be on the bottom.
            # Facing North in SH, Dec decreases as you go UP towards Zenith.
            # RA increases eastward, which is to the RIGHT when facing North.
            ax.set_xlim(
                target_ra.hours - half_zoom_ra_hours,
                target_ra.hours + half_zoom_ra_hours,
            )
            ax.set_ylim(
                target_dec.degrees + half_zoom_dec,
                target_dec.degrees - half_zoom_dec,
            )
        else:
            ax.set_xlim(
                target_ra.hours + half_zoom_ra_hours,
                target_ra.hours - half_zoom_ra_hours,
            )
            ax.set_ylim(
                target_dec.degrees - half_zoom_dec,
                target_dec.degrees + half_zoom_dec,
            )
        ax.set_aspect(1.0 / (15.0 * numpy.cos(dec_rad)))

    ax.tick_params(axis="x", colors=style["TEXT_COLOR"])
    ax.tick_params(axis="y", colors=style["TEXT_COLOR"])
    ax.spines["left"].set_color(style["AXIS_COLOR"])
    ax.spines["bottom"].set_color(style["AXIS_COLOR"])
    ax.spines["top"].set_color(style["AXIS_COLOR"])
    ax.spines["right"].set_color(style["AXIS_COLOR"])
    ax.grid(True, color=style["GRID_COLOR"], linestyle="--", linewidth=0.5)


def parse_target_geometry(
    target_object: Any,
    target_object_data: Any,
    observer: Any,
) -> tuple[float, float, float, Optional[Any], Optional[float]]:
    """
    Parses size dimensions, position angle, declination, and magnitude from target data.
    Returns: (width_deg, height_deg, pos_angle, dec, magnitude)
    """
    width_arcmin = target_object_data.get(ObjectTableLabels.SIZE_MAJOR, 0)
    width_arcmin = getattr(width_arcmin, "magnitude", width_arcmin)
    width_deg = width_arcmin / 60.0

    height_arcmin = target_object_data.get(
        ObjectTableLabels.SIZE_MINOR, width_arcmin
    )
    height_arcmin = getattr(height_arcmin, "magnitude", height_arcmin)
    height_deg = height_arcmin / 60.0

    pos_angle = target_object_data.get("PosAng", 0.0)
    if pd.isna(pos_angle):
        pos_angle = 0.0
    pos_angle = getattr(pos_angle, "magnitude", pos_angle)
    pos_angle = float(pos_angle)

    dec = None
    if hasattr(target_object, "dec"):
        dec = getattr(target_object, "dec", None)
    else:
        try:
            _, dec, _ = observer.observe(target_object).apparent().radec()
        except Exception:
            dec = None

    magnitude = target_object_data.get("Magnitude")
    if pd.isna(magnitude) or magnitude is None:
        magnitude = target_object_data.get("Mag")
    if pd.isna(magnitude) or magnitude is None:
        magnitude = target_object_data.get("magnitude")

    return width_deg, height_deg, pos_angle, dec, magnitude


def calculate_target_ellipse_angle(
    pos_angle: float,
    dec: Optional[Any],
    target_az: Any,
    place_lat: Any,
    coordinate_system: CoordinateSystem,
    flipped_horizontally: bool,
    flipped_vertically: bool,
    calculate_parallactic_angle_func=calculate_parallactic_angle,
    calculate_ellipse_angle_func=calculate_ellipse_angle,
) -> float:
    """Calculates the target's rotated ellipse angle based on position, coordinate system, and flips."""
    if dec is not None:
        parallactic_angle = calculate_parallactic_angle_func(
            place_lat, dec, target_az
        )
        angle = calculate_ellipse_angle_func(
            pos_angle,
            parallactic_angle,
            coordinate_system,
            flipped_horizontally,
            flipped_vertically,
        )
    else:
        angle = pos_angle
    return float(angle)


def get_target_plot_coordinates(
    target_alt: Any,
    target_az: Any,
    target_ra: Any,
    target_dec: Any,
    coordinate_system: CoordinateSystem,
) -> tuple[float, float]:
    """Returns the plotting (x, y) coordinates for the target based on coordinate system."""
    if coordinate_system == CoordinateSystem.HORIZONTAL:
        return float(target_az.degrees), float(target_alt.degrees)
    else:
        return float(target_ra.hours), float(target_dec.degrees)
