from typing import cast

import numpy
import pandas as pd
from matplotlib.patches import Ellipse
from skyfield.api import Star

from apts.constants.plot import CoordinateSystem
from apts.utils.coordinates import parse_ra_to_hours, parse_dec_to_degrees


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
    return parse_ra_to_hours(ra_str)


def _parse_dec(dec_str):
    return parse_dec_to_degrees(dec_str)


def _filter_by_proximity(
    df: pd.DataFrame,
    observer,
    target_object,
    zoom_deg: float,
) -> pd.DataFrame:
    """Filters a DataFrame of celestial objects with 'ra_hours' and 'dec_degrees' columns
    to those within zoom_deg of the target_object."""
    if df.empty:
        return df

    # Pre-filter to a bounding box before expensive separation calculation
    if hasattr(target_object, "ra"):
        ra_center_hours = target_object.ra.hours
        dec_center_degrees = target_object.dec.degrees
    else:
        # It's a planet or other solar system body
        ra, dec, _ = observer.observe(target_object).radec()
        ra_center_hours = ra.hours
        dec_center_degrees = dec.degrees

    # Create a generous bounding box around the target
    deg_margin = zoom_deg * 2
    ra_margin_hours = deg_margin / 15.0

    ra_min = ra_center_hours - ra_margin_hours
    ra_max = ra_center_hours + ra_margin_hours
    dec_min = dec_center_degrees - deg_margin
    dec_max = dec_center_degrees + deg_margin

    # Simple bounding box filter
    df_in_box = df[
        (df["ra_hours"] >= ra_min)
        & (df["ra_hours"] <= ra_max)
        & (df["dec_degrees"] >= dec_min)
        & (df["dec_degrees"] <= dec_max)
    ]

    if df_in_box.empty:
        return cast(pd.DataFrame, df_in_box)

    # Precise separation calculation
    if hasattr(target_object, "ra"):
        center = Star(ra=target_object.ra, dec=target_object.dec)
    else:
        ra, dec, _ = observer.observe(target_object).radec()
        center = Star(ra_hours=ra.hours, dec_degrees=dec.degrees)
    observed_center = observer.observe(center)

    df_in_box_copy = df_in_box.copy()
    df_in_box_copy["epoch_year"] = 2000.0
    all_stars_vectors = Star.from_dataframe(df_in_box_copy)
    observed_all_stars = observer.observe(all_stars_vectors)

    vec_center_np = observed_center.position.au
    vec_all_stars_np = observed_all_stars.position.au

    dot_product = numpy.dot(vec_center_np, vec_all_stars_np)
    # Handle single or multiple items norm dimension safely
    len_center = numpy.linalg.norm(vec_center_np, axis=0)
    len_all_stars = numpy.linalg.norm(vec_all_stars_np, axis=0)

    cosine_angle = dot_product / (len_center * len_all_stars)
    cosine_angle = numpy.clip(cosine_angle, -1.0, 1.0)

    separation = numpy.degrees(numpy.arccos(cosine_angle))
    nearby_mask = numpy.atleast_1d(separation < zoom_deg)
    return cast(pd.DataFrame, df_in_box.iloc[numpy.where(nearby_mask)[0]].copy())
