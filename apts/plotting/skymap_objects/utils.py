from typing import cast

import numpy
from matplotlib.patches import Ellipse

from apts.constants.plot import CoordinateSystem


def _plot_celestial_object(
    ax,
    name: str,
    alt_deg: float,
    az_deg: float,
    ra_hours: float,
    dec_deg: float,
    width_deg: float,
    height_deg: float,
    angle: float,
    face_color: str,
    edge_color: str,
    is_polar: bool,
    ra_rad: float,
    coordinate_system: CoordinateSystem = cast(
        CoordinateSystem, CoordinateSystem.HORIZONTAL
    ),
    is_sh: bool = False,
    plot_labels: bool = True,
):
    """Helper function to plot a celestial object on a skymap."""
    if is_polar:
        size = (width_deg + height_deg) / 2 * 100
        if coordinate_system == CoordinateSystem.HORIZONTAL:
            x, y = numpy.deg2rad(az_deg), 90 - alt_deg
        else:
            x, y = ra_rad, 90 + dec_deg if is_sh else 90 - dec_deg

        ax.scatter(x, y, s=size, color=edge_color, marker="+")
        if plot_labels:
            ax.annotate(
                name,
                (x, y),
                textcoords="offset points",
                xytext=(5, 5),
                color=edge_color,
            )
    else:  # Cartesian / Zoomed
        if coordinate_system == CoordinateSystem.HORIZONTAL:
            x_coord, y_coord = az_deg, alt_deg
            ellipse_width = width_deg
        else:  # Equatorial
            x_coord, y_coord = ra_hours, dec_deg
            ellipse_width = width_deg / (15 * numpy.cos(numpy.deg2rad(dec_deg)))

        ellipse = Ellipse(
            xy=(x_coord, y_coord),
            width=ellipse_width,
            height=height_deg,
            angle=angle,
            edgecolor=edge_color,
            facecolor=face_color,
            alpha=0.6,
        )
        ax.add_patch(ellipse)
        if plot_labels:
            ax.annotate(
                name,
                (x_coord, y_coord),
                textcoords="offset points",
                xytext=(5, 5),
                color=edge_color,
            )


def _parse_ra(ra_str):
    if isinstance(ra_str, str):
        parts = ra_str.split(":")
        if len(parts) > 0:
            try:
                h = float(parts[0])
                m = float(parts[1]) if len(parts) > 1 else 0
                s = float(parts[2]) if len(parts) > 2 else 0
                return h + m / 60 + s / 3600
            except ValueError:
                return None
    return None


def _parse_dec(dec_str):
    if isinstance(dec_str, str):
        sign = -1 if dec_str.startswith("-") else 1
        parts = dec_str.lstrip("+-").split(":")
        if len(parts) > 0:
            try:
                d = float(parts[0])
                m = float(parts[1]) if len(parts) > 1 else 0
                s = float(parts[2]) if len(parts) > 2 else 0
                return sign * (d + m / 60 + s / 3600)
            except ValueError:
                return None
    return None
