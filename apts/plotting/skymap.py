import logging
from datetime import datetime
from typing import TYPE_CHECKING, Any, Optional, cast

import numpy
import pandas as pd
from matplotlib import pyplot
from matplotlib.patches import Ellipse
from skyfield.api import Star as SkyfieldStar
from skyfield.units import Angle

from apts.config import get_dark_mode
from apts.constants.graphconstants import get_planet_color, get_plot_style
from apts.constants.plot import CoordinateSystem
from apts.i18n import _thread_local, gettext_
from apts.plotting.utils import (
    calculate_ellipse_angle,
    calculate_parallactic_angle,
    create_ra_zoom_mask,
    get_brightness_color,
    get_object_angular_size_deg,
)
from apts.utils.planetary import get_reverse_translated_planet_names
from ..cache import get_hipparcos_data
from ..constants import ObjectTableLabels

if TYPE_CHECKING:
    from ..observations import Observation

logger = logging.getLogger(__name__)


def plot_sun_and_moon_path(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    if observation.sun_observation:
        return observation.place.plot_sun_path(dark_mode_override, **args)
    else:
        return observation.place.plot_moon_path(dark_mode_override, **args)


def _plot_bright_stars_on_skymap(
    observation: "Observation",
    ax,
    observer,
    is_polar,
    style: dict,
    zoom_deg: Optional[float] = None,
    coordinate_system: Optional[CoordinateSystem] = None,
):
    bright_stars_df = observation.local_stars.objects.copy()
    if bright_stars_df.empty:
        return

    if hasattr(bright_stars_df["RA"].iloc[0], "magnitude"):
        bright_stars_df["RA"] = bright_stars_df["RA"].apply(lambda x: x.magnitude)
    if hasattr(bright_stars_df["Dec"].iloc[0], "magnitude"):
        bright_stars_df["Dec"] = bright_stars_df["Dec"].apply(lambda x: x.magnitude)
    if hasattr(bright_stars_df["Magnitude"].iloc[0], "magnitude"):
        bright_stars_df["Magnitude"] = bright_stars_df["Magnitude"].apply(
            lambda x: x.magnitude
        )

    bright_stars_df["epoch_year"] = 2000.0
    bright_stars_df.rename(
        columns={"RA": "ra_hours", "Dec": "dec_degrees"}, inplace=True
    )

    star_positions = observer.observe(SkyfieldStar.from_dataframe(bright_stars_df))
    alt, az, _ = star_positions.apparent().altaz()
    ra, dec, _ = star_positions.apparent().radec()

    # For Equatorial plots, we don't filter by horizon. All stars in the catalog are candidates.
    # For Horizontal plots, we only want stars above the horizon.
    if coordinate_system == CoordinateSystem.HORIZONTAL:
        visible_mask = alt.degrees > 0
    else:
        visible_mask = numpy.ones(len(bright_stars_df), dtype=bool)

    df_visible = bright_stars_df[visible_mask]
    # We still need these for the Horizontal plotting paths
    alt_visible_deg = alt.degrees[visible_mask]
    az_visible_deg = az.degrees[visible_mask]
    az_visible_rad = az.radians[visible_mask]

    if df_visible.empty:
        return

    star_color = style.get("EMPHASIS_COLOR", "yellow")

    if (
        not is_polar
        and zoom_deg is not None
        and coordinate_system == CoordinateSystem.HORIZONTAL
    ):
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        zoom_mask = (
            (az_visible_deg >= xlim[0])
            & (az_visible_deg <= xlim[1])
            & (alt_visible_deg >= ylim[0])
            & (alt_visible_deg <= ylim[1])
        )

        df_zoomed = df_visible[zoom_mask]
        alt_zoomed_deg = alt_visible_deg[zoom_mask]
        az_zoomed_deg = az_visible_deg[zoom_mask]

        if df_zoomed.empty:  # type: ignore
            return

        ax.scatter(az_zoomed_deg, alt_zoomed_deg, s=40, color=star_color, marker="*")

        for i in range(len(df_zoomed)):
            star = df_zoomed.iloc[i]  # type: ignore
            ax.annotate(
                star["Name"],
                (az_zoomed_deg[i], alt_zoomed_deg[i]),
                textcoords="offset points",
                xytext=(5, 5),
                color=star_color,
                fontsize=8,
            )
    elif coordinate_system == CoordinateSystem.EQUATORIAL and zoom_deg is not None:
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        ra_hours_apparent = ra.hours
        dec_degrees_apparent = dec.degrees

        zoom_mask = create_ra_zoom_mask(ra_hours_apparent, xlim) & (
            (dec_degrees_apparent >= ylim[0]) & (dec_degrees_apparent <= ylim[1])
        )

        df_zoomed = df_visible[zoom_mask]
        if df_zoomed.empty:  # type: ignore
            return

        ra_zoomed = ra_hours_apparent[zoom_mask]
        dec_zoomed = dec_degrees_apparent[zoom_mask]

        ax.scatter(ra_zoomed, dec_zoomed, s=40, color=star_color, marker="*")

        for i in range(len(df_zoomed)):
            star = df_zoomed.iloc[i]  # type: ignore
            ax.annotate(
                star["Name"],
                (ra_zoomed[i], dec_zoomed[i]),
                textcoords="offset points",
                xytext=(5, 5),
                color=star_color,
                fontsize=8,
            )
    else:
        if is_polar:
            if coordinate_system == CoordinateSystem.HORIZONTAL:
                ax.scatter(
                    az_visible_rad,
                    90 - alt_visible_deg,
                    s=40,
                    color=star_color,
                    marker="*",
                )
                for i in range(len(df_visible)):
                    star = df_visible.iloc[i]
                    ax.annotate(
                        star["Name"],
                        (az_visible_rad[i], 90 - alt_visible_deg[i]),
                        textcoords="offset points",
                        xytext=(5, 5),
                        color=star_color,
                        fontsize=8,
                    )
            else:
                ax.scatter(
                    ra.radians[visible_mask],
                    90 - dec.degrees[visible_mask],
                    s=40,
                    color=star_color,
                    marker="*",
                )
                for i in range(len(df_visible)):
                    star = df_visible.iloc[i]
                    ax.annotate(
                        star["Name"],
                        (
                            ra.radians[visible_mask][i],
                            90 - dec.degrees[visible_mask][i],
                        ),
                        textcoords="offset points",
                        xytext=(5, 5),
                        color=star_color,
                        fontsize=8,
                    )
        else:
            ax.scatter(
                az_visible_deg,
                alt_visible_deg,
                s=40,
                color=star_color,
                marker="*",
            )
            for i in range(len(df_visible)):
                star = df_visible.iloc[i]
                ax.annotate(
                    star["Name"],
                    (az_visible_deg[i], alt_visible_deg[i]),
                    textcoords="offset points",
                    xytext=(5, 5),
                    color=star_color,
                    fontsize=8,
                )


def _plot_stars_on_skymap(
    observation: "Observation",
    ax,
    observer,
    mag_limit,
    is_polar,
    style: dict,
    zoom_deg: Optional[float] = None,
    target_object=None,
    coordinate_system: CoordinateSystem = cast(
        CoordinateSystem, CoordinateSystem.HORIZONTAL
    ),
):
    stars = get_hipparcos_data()

    if zoom_deg is not None and target_object is not None:
        # Optimization: pre-filter stars to a bounding box before expensive separation calculation
        if hasattr(target_object, "ra"):
            ra_center_hours = target_object.ra.hours
            dec_center_degrees = target_object.dec.degrees
        else:
            # It's a planet or other solar system body
            ra, dec, _ = observer.observe(target_object).radec()
            ra_center_hours = ra.hours
            dec_center_degrees = dec.degrees

        # Create a generous bounding box around the target
        # The conversion from degrees to RA hours depends on declination,
        # but for a rough filter, a fixed factor is acceptable.
        deg_margin = zoom_deg * 2  # A larger margin to be safe
        ra_margin_hours = deg_margin / 15.0

        ra_min = ra_center_hours - ra_margin_hours
        ra_max = ra_center_hours + ra_margin_hours
        dec_min = dec_center_degrees - deg_margin
        dec_max = dec_center_degrees + deg_margin

        # Simple bounding box filter
        stars_in_box = stars[
            (stars["ra_hours"] >= ra_min)
            & (stars["ra_hours"] <= ra_max)
            & (stars["dec_degrees"] >= dec_min)
            & (stars["dec_degrees"] <= dec_max)
        ]

        # Now perform the precise separation calculation on the much smaller subset
        if not stars_in_box.empty:
            if hasattr(target_object, "ra"):
                center = SkyfieldStar(ra=target_object.ra, dec=target_object.dec)
            else:
                ra, dec, _ = observer.observe(target_object).radec()
                center = SkyfieldStar(ra_hours=ra.hours, dec_degrees=dec.degrees)
            observed_center = observer.observe(center)

            all_stars_vectors = SkyfieldStar.from_dataframe(stars_in_box)
            observed_all_stars = observer.observe(all_stars_vectors)

            dist_center = observed_center.position.au
            dist_all_stars = observed_all_stars.position.au

            vec_center_np = dist_center
            vec_all_stars_np = dist_all_stars

            dot_product = numpy.dot(vec_center_np, vec_all_stars_np)

            len_center = numpy.linalg.norm(vec_center_np, axis=0)
            len_all_stars = numpy.linalg.norm(vec_all_stars_np, axis=0)

            cosine_angle = dot_product / (len_center * len_all_stars)
            cosine_angle = numpy.clip(cosine_angle, -1.0, 1.0)

            separation_radians = numpy.arccos(cosine_angle)
            separation = numpy.degrees(separation_radians)
            nearby_mask = separation < zoom_deg
            stars = stars_in_box[nearby_mask]
        else:
            stars = stars_in_box  # empty dataframe

    if mag_limit is not None:
        limit = mag_limit
    elif is_polar:
        limit = 4.5
    elif zoom_deg is not None:
        limit = 7.5
    else:
        limit = 6.0

    bright_stars = stars[stars["magnitude"] <= limit]

    if bright_stars.empty:  # type: ignore
        return

    star_positions = observer.observe(SkyfieldStar.from_dataframe(bright_stars))
    alt, az, _ = star_positions.apparent().altaz()
    ra, dec, _ = star_positions.apparent().radec()

    if coordinate_system == CoordinateSystem.HORIZONTAL:
        visible = alt.degrees > 0
    else:
        visible = numpy.ones(len(bright_stars), dtype=bool)

    if not any(visible):
        return

    if (
        not is_polar
        and zoom_deg is not None
        and coordinate_system == CoordinateSystem.HORIZONTAL
    ):
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        visible_mask = alt.degrees > 0

        az_visible = az.degrees[visible_mask]
        alt_visible = alt.degrees[visible_mask]

        zoom_mask = (
            (az_visible >= xlim[0])
            & (az_visible <= xlim[1])
            & (alt_visible >= ylim[0])
            & (alt_visible <= ylim[1])
        )

        az_plot = az_visible[zoom_mask]
        alt_plot = alt_visible[zoom_mask]

        mag_plot = bright_stars[visible_mask][zoom_mask]["magnitude"]

        sizes = (limit + 1 - numpy.array(mag_plot)) * 3
        ax.scatter(
            az_plot,
            alt_plot,
            s=sizes,
            color=style["TEXT_COLOR"],
            marker=".",
        )
    elif coordinate_system == CoordinateSystem.EQUATORIAL and zoom_deg is not None:
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        ra_hours_apparent = ra.hours[visible]
        dec_degrees_apparent = dec.degrees[visible]

        zoom_mask = create_ra_zoom_mask(ra_hours_apparent, xlim) & (
            (dec_degrees_apparent >= ylim[0]) & (dec_degrees_apparent <= ylim[1])
        )

        ra_plot = ra_hours_apparent[zoom_mask]
        dec_plot = dec_degrees_apparent[zoom_mask]
        mag_plot = bright_stars[visible][zoom_mask]["magnitude"]

        sizes = (limit + 1 - numpy.array(mag_plot)) * 3
        ax.scatter(
            ra_plot,
            dec_plot,
            s=sizes,
            color=style["TEXT_COLOR"],
            marker=".",
        )
    else:
        sizes = (limit + 1 - numpy.array(bright_stars["magnitude"][visible])) * (
            5 if is_polar else 3
        )
        if is_polar:
            if coordinate_system == CoordinateSystem.HORIZONTAL:
                ax.scatter(
                    az.radians[visible],
                    90 - alt.degrees[visible],
                    s=sizes,
                    color=ax.get_facecolor(),
                    marker=".",
                    edgecolors=style["TEXT_COLOR"],
                )
            else:
                ax.scatter(
                    ra.radians[visible],
                    90 - dec.degrees[visible],
                    s=sizes,
                    color=ax.get_facecolor(),
                    marker=".",
                    edgecolors=style["TEXT_COLOR"],
                )
        else:
            ax.scatter(
                az.degrees[visible],
                alt.degrees[visible],
                s=sizes,
                color=style["TEXT_COLOR"],
                marker=".",
            )


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
):
    """Helper function to plot a celestial object on a skymap."""
    angle = angle % 360
    if is_polar:
        size = (width_deg + height_deg) / 2 * 100
        if coordinate_system == CoordinateSystem.HORIZONTAL:
            x, y = numpy.deg2rad(az_deg), 90 - alt_deg
        else:
            x, y = ra_rad, 90 - dec_deg

        ax.scatter(x, y, s=size, color=edge_color, marker="+")
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
        ax.annotate(
            name,
            (x_coord, y_coord),
            textcoords="offset points",
            xytext=(5, 5),
            color=edge_color,
        )


def _plot_messier_on_skymap(
    observation: "Observation",
    ax,
    observer,
    is_polar,
    target_name: str,
    flipped_horizontally: bool = False,
    flipped_vertically: bool = False,
    coordinate_system: CoordinateSystem = cast(
        CoordinateSystem, CoordinateSystem.HORIZONTAL
    ),
):
    visible_messier = observation.get_visible_messier()
    if not visible_messier.empty:
        for _, m_obj in visible_messier.iterrows():
            messier_name = m_obj[ObjectTableLabels.MESSIER]
            if messier_name == target_name:
                continue
            messier_object = observation.local_messier.find_by_name(messier_name)
            if messier_object:
                alt, az, _ = observer.observe(messier_object).apparent().altaz()
                ra, dec, _ = observer.observe(messier_object).apparent().radec()
                if bool(numpy.any(alt.degrees > 0)):
                    width_arcmin = m_obj.get(ObjectTableLabels.WIDTH)
                    if bool(pd.isna(width_arcmin)):
                        width_arcmin = 1.0  # Default to 1 arcmin if missing
                    width_arcmin = getattr(width_arcmin, "magnitude", width_arcmin)
                    width_deg = float(width_arcmin or 1.0) / 60.0

                    height_arcmin = m_obj.get("Height")
                    if bool(pd.isna(height_arcmin)):
                        height_arcmin = width_arcmin
                    height_arcmin = getattr(height_arcmin, "magnitude", height_arcmin)
                    height_deg = float(height_arcmin or 1.0) / 60.0

                    pos_angle = m_obj.get("PosAng", 0.0)
                    if bool(pd.isna(pos_angle)):
                        pos_angle = 0.0
                    pos_angle = getattr(pos_angle, "magnitude", pos_angle)
                    pos_angle = float(pos_angle or 0.0)

                    dec = messier_object.dec
                    parallactic_angle = calculate_parallactic_angle(
                        observation.place.lat, dec, az
                    )
                    angle = calculate_ellipse_angle(
                        pos_angle,
                        parallactic_angle,
                        coordinate_system,
                        flipped_horizontally,
                        flipped_vertically,
                    )
                    magnitude = m_obj.get("Magnitude")
                    face_color = get_brightness_color(magnitude)

                    _plot_celestial_object(
                        ax,
                        name=cast(str, messier_name),
                        alt_deg=alt.degrees,
                        az_deg=az.degrees,
                        ra_hours=ra.hours,
                        dec_deg=dec.degrees,
                        width_deg=width_deg,
                        height_deg=height_deg,
                        angle=angle,
                        face_color=face_color,
                        edge_color="red",
                        is_polar=is_polar,
                        ra_rad=ra.radians,
                        coordinate_system=coordinate_system,
                    )


def _parse_ra(ra_str):
    if isinstance(ra_str, str) and ra_str.count(":") == 2:
        parts = ra_str.split(":")
        return float(parts[0]) + float(parts[1]) / 60 + float(parts[2]) / 3600
    return None


def _parse_dec(dec_str):
    if isinstance(dec_str, str) and dec_str.count(":") == 2:
        sign = -1 if dec_str.startswith("-") else 1
        parts = dec_str.lstrip("+-").split(":")
        return sign * (float(parts[0]) + float(parts[1]) / 60 + float(parts[2]) / 3600)
    return None


def _plot_ngc_on_skymap(
    observation: "Observation",
    ax,
    observer,
    is_polar,
    target_name: str,
    star_magnitude_limit: Optional[float] = None,
    zoom_deg: Optional[float] = None,
    target_object=None,
    flipped_horizontally: bool = False,
    flipped_vertically: bool = False,
    coordinate_system: CoordinateSystem = cast(
        CoordinateSystem, CoordinateSystem.HORIZONTAL
    ),
):
    if zoom_deg is not None and target_object is not None:
        visible_ngc = observation.local_ngc.objects.copy()
    else:
        visible_ngc = observation.get_visible_ngc(
            star_magnitude_limit=star_magnitude_limit
        )

    if not cast(pd.DataFrame, visible_ngc).empty:
        if zoom_deg is not None and target_object is not None:
            ra_center_hours = target_object.ra.hours
            dec_center_degrees = target_object.dec.degrees
            deg_margin = zoom_deg * 2
            ra_margin_hours = deg_margin / 15.0
            ra_min = ra_center_hours - ra_margin_hours
            ra_max = ra_center_hours + ra_margin_hours
            dec_min = dec_center_degrees - deg_margin
            dec_max = dec_center_degrees + deg_margin

            visible_ngc["RA_parsed"] = visible_ngc["RA"].apply(_parse_ra)
            visible_ngc["Dec_parsed"] = visible_ngc["Dec"].apply(_parse_dec)

            ngc_in_box = visible_ngc[
                (visible_ngc["RA_parsed"] >= ra_min)
                & (visible_ngc["RA_parsed"] <= ra_max)
                & (visible_ngc["Dec_parsed"] >= dec_min)
                & (visible_ngc["Dec_parsed"] <= dec_max)
            ]

            if not ngc_in_box.empty:
                center = SkyfieldStar(ra=target_object.ra, dec=target_object.dec)
                observed_center = observer.observe(center)

                all_ngc_vectors = observation.local_ngc.get_skyfield_object(ngc_in_box)
                observed_all_ngc = all_ngc_vectors.apply(observer.observe)

                dist_center = observed_center.position.au
                vec_all_ngc = observed_all_ngc.apply(lambda x: x.xyz.au)

                vec_center_np = dist_center
                vec_all_ngc_np = numpy.array(vec_all_ngc.tolist()).T

                dot_product = numpy.dot(vec_center_np, vec_all_ngc_np)

                len_center = numpy.linalg.norm(vec_center_np)
                len_all_ngc = numpy.linalg.norm(vec_all_ngc_np, axis=0)

                cosine_angle = dot_product / (len_center * len_all_ngc)
                cosine_angle = numpy.clip(cosine_angle, -1.0, 1.0)

                separation_radians = numpy.arccos(cosine_angle)
                separation = numpy.degrees(separation_radians)
                nearby_mask = separation < zoom_deg
                visible_ngc = ngc_in_box[nearby_mask]
            else:
                visible_ngc = ngc_in_box

    if not cast(pd.DataFrame, visible_ngc).empty:
        for _, n_obj in cast(pd.DataFrame, visible_ngc).iterrows():
            ngc_name = n_obj[ObjectTableLabels.NGC]
            if bool(pd.isna(ngc_name)):
                ngc_name = n_obj[ObjectTableLabels.NAME]
            if ngc_name == target_name:
                continue
            ngc_object = observation.local_ngc.get_skyfield_object(n_obj)
            if ngc_object:
                alt, az, _ = observer.observe(ngc_object).apparent().altaz()
                ra, dec, _ = observer.observe(ngc_object).apparent().radec()
                if bool(numpy.any(alt.degrees > 0)):
                    width_arcmin = n_obj.get("Size")
                    if bool(pd.isna(width_arcmin)):
                        width_arcmin = n_obj.get("MajAx", 1.0)
                    width_arcmin = getattr(width_arcmin, "magnitude", width_arcmin)
                    width_deg = float(width_arcmin or 1.0) / 60.0

                    height_arcmin = n_obj.get("MinAx")
                    if bool(pd.isna(height_arcmin)):
                        height_arcmin = width_arcmin
                    height_arcmin = getattr(height_arcmin, "magnitude", height_arcmin)
                    height_deg = float(height_arcmin or 1.0) / 60.0

                    pos_angle = n_obj.get("PosAng")
                    if bool(pd.isna(pos_angle)):
                        pos_angle = 0.0
                    pos_angle = getattr(pos_angle, "magnitude", pos_angle)
                    pos_angle = float(pos_angle or 0.0)

                    dec = ngc_object.dec
                    parallactic_angle = calculate_parallactic_angle(
                        observation.place.lat, dec, az
                    )
                    angle = calculate_ellipse_angle(
                        pos_angle,
                        parallactic_angle,
                        coordinate_system,
                        flipped_horizontally,
                        flipped_vertically,
                    )
                    magnitude = n_obj.get("Mag")
                    face_color = get_brightness_color(magnitude)
                    _plot_celestial_object(
                        ax,
                        name=cast(str, ngc_name),
                        alt_deg=alt.degrees,
                        az_deg=az.degrees,
                        ra_hours=ra.hours,
                        dec_deg=dec.degrees,
                        width_deg=width_deg,
                        height_deg=height_deg,
                        angle=angle,
                        face_color=face_color,
                        edge_color="green",
                        is_polar=is_polar,
                        ra_rad=ra.radians,
                        coordinate_system=coordinate_system,
                    )


def _plot_planets_on_skymap(
    observation: "Observation",
    ax,
    observer,
    is_polar,
    effective_dark_mode,
    style,
    target_name: str,
    coordinate_system: CoordinateSystem = cast(
        CoordinateSystem, CoordinateSystem.HORIZONTAL
    ),
):
    visible_planets = observation.get_visible_planets()
    if not visible_planets.empty:
        for _, p_obj in visible_planets.iterrows():
            planet_name = p_obj[ObjectTableLabels.NAME]
            if planet_name == target_name:
                continue  # Skip the target object, it will be plotted separately
            _plot_solar_system_object_on_skymap(
                observation,
                ax,
                observer,
                is_polar,
                style,
                cast(str, planet_name),
                coordinate_system=coordinate_system,
            )


def _plot_solar_system_object_on_skymap(
    observation: "Observation",
    ax,
    observer,
    is_polar,
    style,
    object_name: str,
    is_target: bool = False,
    coordinate_system: CoordinateSystem = cast(
        CoordinateSystem, CoordinateSystem.HORIZONTAL
    ),
):
    """Helper to plot a solar system object, handling regular and target styles."""
    obj = observation.local_planets.find_by_name(object_name)
    if not obj:
        return  # Object not found

    alt, az, _ = observer.observe(obj).apparent().altaz()
    ra, dec, _ = observer.observe(obj).apparent().radec()

    is_below_horizon = numpy.all(numpy.asarray(alt.degrees) <= 0)
    if is_below_horizon and coordinate_system == CoordinateSystem.HORIZONTAL:
        return

    size_deg = get_object_angular_size_deg(observation, object_name)

    # Determine colors and markers
    effective_dark_mode = get_dark_mode()
    default_color = style.get("EMPHASIS_COLOR", "yellow")
    edge_color = get_planet_color(object_name, effective_dark_mode, default_color)
    face_color = edge_color
    marker = "o"
    if object_name == "Sun":
        marker = "*"

    linestyle = "solid"
    linewidth = 1

    if is_target:
        edge_color = "yellow"
        linestyle = "--"
        linewidth = 2

    if is_polar:
        size = size_deg * 200
        if coordinate_system == CoordinateSystem.HORIZONTAL:
            x, y = az.radians, 90 - alt.degrees
        else:
            x, y = ra.radians, 90 - dec.degrees
        ax.scatter(x, y, s=size, color=edge_color, marker=marker)
        if not is_target:
            ax.annotate(
                object_name,
                (x, y),
                textcoords="offset points",
                xytext=(5, 5),
                color=edge_color,
            )
    else:  # Cartesian / Zoomed
        x_coord, y_coord = (
            (az.degrees, alt.degrees)
            if coordinate_system == CoordinateSystem.HORIZONTAL
            else (ra.hours, dec.degrees)
        )
        ellipse_width = (
            size_deg
            if coordinate_system == CoordinateSystem.HORIZONTAL
            else size_deg / (15 * numpy.cos(numpy.deg2rad(dec.degrees)))
        )

        ellipse = Ellipse(
            xy=(x_coord, y_coord),
            width=ellipse_width,
            height=size_deg,
            angle=0,
            edgecolor=edge_color,
            facecolor=face_color,
            linewidth=linewidth,
            linestyle=linestyle,
            alpha=0.6,
        )
        ax.add_patch(ellipse)
        if not is_target:
            ax.annotate(
                object_name,
                (x_coord, y_coord),
                textcoords="offset points",
                xytext=(5, 5),
                color=edge_color,
            )


def _generate_plot_skymap(
    observation: "Observation",
    target_name: str,
    dark_mode_override: Optional[bool] = None,
    zoom_deg: Optional[float] = None,
    star_magnitude_limit: Optional[float] = None,
    plot_stars: bool = True,
    plot_messier: bool = False,
    plot_ngc: bool = False,
    plot_planets: bool = False,
    plot_sun: bool = False,
    plot_moon: bool = False,
    plot_date: Optional[datetime] = None,
    flipped_horizontally: bool = False,
    flipped_vertically: bool = False,
    coordinate_system: CoordinateSystem = cast(
        CoordinateSystem, CoordinateSystem.HORIZONTAL
    ),
    **kwargs,
):
    """
    Generates a skymap for a given time and location, highlighting a target object.
    Can generate a full polar skymap or a zoomed-in Cartesian skymap.
    """
    current_language = getattr(_thread_local, "language", "en")
    if current_language != "en":
        reverse_map = get_reverse_translated_planet_names(current_language)
        target_name = reverse_map.get(target_name, target_name)

    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)

    if plot_date:
        # Use the specified plot_date
        t = observation.place.ts.utc(plot_date)
    elif observation.start and observation.stop:
        # Default to the middle of the observation window
        start_ts = observation.place.ts.utc(observation.start)
        stop_ts = observation.place.ts.utc(observation.stop)
        middle_julian_date = (start_ts.tt + stop_ts.tt) / 2
        t = observation.place.ts.tt_jd(middle_julian_date)
    elif observation.effective_date is not None:
        # Fallback to effective_date if start/stop are not available
        t = observation.effective_date
    else:
        # Final fallback to the current time
        t = observation.place.ts.now()

    observer = observation.place.observer.at(t)

    generation_time_str = t.astimezone(observation.place.local_timezone).strftime(
        "%Y-%m-%d %H:%M %Z"
    )

    target_object = None
    target_object_data = None

    # Search logic that mirrors find_by_name methods
    # Messier
    result_df = observation.local_messier.objects[
        observation.local_messier.objects["Messier"] == target_name
    ]
    if not result_df.empty:
        target_object_data = result_df.iloc[0]
        target_object = observation.local_messier.get_skyfield_object(
            target_object_data
        )
    else:
        # NGC
        result_df = observation.local_ngc.objects[
            (observation.local_ngc.objects["NGC"] == target_name)
            | (observation.local_ngc.objects["Name"] == target_name)
        ]
        if not result_df.empty:
            target_object_data = result_df.iloc[0]
            target_object = observation.local_ngc.get_skyfield_object(
                target_object_data
            )
        else:
            # Stars
            result_df = observation.local_stars.objects[
                observation.local_stars.objects["Name"] == target_name
            ]
            if not result_df.empty:
                target_object_data = result_df.iloc[0]
                target_object = observation.local_stars.get_skyfield_object(
                    target_object_data
                )
            else:
                # Planets
                target_object = observation.local_planets.find_by_name(target_name)

    if not target_object:
        fig, ax = pyplot.subplots(figsize=(10, 10))
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])
        ax.text(
            0.5,
            0.5,
            gettext_("Object '{target_name}' not found.").format(
                target_name=target_name
            ),
            horizontalalignment="center",
            verticalalignment="center",
            transform=ax.transAxes,
            color=style["TEXT_COLOR"],
        )
        ax.set_title(
            gettext_("Skymap (Generated: {generation_time_str})").format(
                generation_time_str=generation_time_str
            ),
            color=style["TEXT_COLOR"],
        )
        return fig

    target_alt, target_az, _ = observer.observe(target_object).apparent().altaz()
    target_ra, target_dec, _ = observer.observe(target_object).apparent().radec()

    if zoom_deg is not None:
        if coordinate_system == CoordinateSystem.HORIZONTAL and target_alt.degrees < 0:
            fig, ax = pyplot.subplots(figsize=(10, 10))
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            ax.text(
                0.5,
                0.5,
                gettext_("Target '{target_name}' is below the horizon.").format(
                    target_name=target_name
                ),
                horizontalalignment="center",
                verticalalignment="center",
                transform=ax.transAxes,
                color=style["TEXT_COLOR"],
            )
            ax.set_title(
                gettext_(
                    "Skymap for {target_name} (Generated: {generation_time_str})"
                ).format(
                    target_name=target_name, generation_time_str=generation_time_str
                ),
                color=style["TEXT_COLOR"],
            )
            return fig

        fig, ax = pyplot.subplots(figsize=(10, 10))
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])

        if coordinate_system == CoordinateSystem.HORIZONTAL:
            ax.set_xlabel(gettext_("Azimuth (°)"), color=style["TEXT_COLOR"])
            ax.set_ylabel(gettext_("Altitude (°)"), color=style["TEXT_COLOR"])
            half_zoom = zoom_deg / 2
            ax.set_xlim(target_az.degrees - half_zoom, target_az.degrees + half_zoom)
            ax.set_ylim(target_alt.degrees - half_zoom, target_alt.degrees + half_zoom)
            ax.set_aspect("equal", adjustable="box")
        else:  # Equatorial
            ax.set_xlabel(
                gettext_("Right Ascension (hours)"), color=style["TEXT_COLOR"]
            )
            ax.set_ylabel(gettext_("Declination (°)"), color=style["TEXT_COLOR"])
            dec_rad = numpy.deg2rad(target_dec.degrees)
            half_zoom_dec = zoom_deg / 2.0
            half_zoom_ra_hours = half_zoom_dec / (15.0 * numpy.cos(dec_rad))
            ax.set_xlim(
                target_ra.hours - half_zoom_ra_hours,
                target_ra.hours + half_zoom_ra_hours,
            )
            ax.set_ylim(
                target_dec.degrees - half_zoom_dec, target_dec.degrees + half_zoom_dec
            )
            ax.set_aspect(1.0 / (15.0 * numpy.cos(dec_rad)))

        ax.tick_params(axis="x", colors=style["TEXT_COLOR"])
        ax.tick_params(axis="y", colors=style["TEXT_COLOR"])
        ax.spines["left"].set_color(style["AXIS_COLOR"])
        ax.spines["bottom"].set_color(style["AXIS_COLOR"])
        ax.spines["top"].set_color(style["AXIS_COLOR"])
        ax.spines["right"].set_color(style["AXIS_COLOR"])
        ax.grid(True, color=style["GRID_COLOR"], linestyle="--", linewidth=0.5)

        if plot_stars:
            _plot_stars_on_skymap(
                observation,
                ax,
                observer,
                star_magnitude_limit,
                is_polar=False,
                style=style,
                zoom_deg=zoom_deg,
                target_object=target_object,
                coordinate_system=coordinate_system,
            )
            _plot_bright_stars_on_skymap(
                observation,
                ax,
                observer,
                is_polar=False,
                style=style,
                zoom_deg=zoom_deg,
                coordinate_system=coordinate_system,
            )
        if plot_messier:
            _plot_messier_on_skymap(
                observation,
                ax,
                observer,
                is_polar=False,
                target_name=target_name,
                flipped_horizontally=flipped_horizontally,
                flipped_vertically=flipped_vertically,
                coordinate_system=coordinate_system,
            )
        if plot_ngc:
            _plot_ngc_on_skymap(
                observation,
                ax,
                observer,
                is_polar=False,
                target_name=target_name,
                star_magnitude_limit=star_magnitude_limit,
                zoom_deg=zoom_deg,
                target_object=target_object,
                flipped_horizontally=flipped_horizontally,
                flipped_vertically=flipped_vertically,
                coordinate_system=coordinate_system,
            )
        if plot_planets:
            _plot_planets_on_skymap(
                observation,
                ax,
                observer,
                is_polar=False,
                effective_dark_mode=effective_dark_mode,
                style=style,
                target_name=target_name,
                coordinate_system=coordinate_system,
            )
        if plot_sun and target_name != "Sun":
            _plot_solar_system_object_on_skymap(
                observation,
                ax,
                observer,
                is_polar=False,
                style=style,
                object_name="Sun",
                coordinate_system=coordinate_system,
            )
        if plot_moon and target_name != "Moon":
            _plot_solar_system_object_on_skymap(
                observation,
                ax,
                observer,
                is_polar=False,
                style=style,
                object_name="Moon",
                coordinate_system=coordinate_system,
            )
        if target_object_data is not None:
            width_arcmin = target_object_data.get(ObjectTableLabels.WIDTH, 0)
            width_arcmin = getattr(width_arcmin, "magnitude", width_arcmin)
            width_deg = width_arcmin / 60.0

            height_arcmin = target_object_data.get("Height", width_arcmin)
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

            if dec is not None:
                parallactic_angle = calculate_parallactic_angle(
                    observation.place.lat, dec, target_az
                )
                angle = calculate_ellipse_angle(
                    pos_angle,
                    parallactic_angle,
                    coordinate_system,
                    flipped_horizontally,
                    flipped_vertically,
                )
            else:
                angle = pos_angle

            magnitude = target_object_data.get("Magnitude")
            if pd.isna(magnitude) or magnitude is None:
                magnitude = target_object_data.get("Mag")
            if pd.isna(magnitude) or magnitude is None:
                magnitude = target_object_data.get("magnitude")
            face_color = get_brightness_color(magnitude)

            x_coord, y_coord = (
                (target_az.degrees, target_alt.degrees)
                if coordinate_system == CoordinateSystem.HORIZONTAL
                else (target_ra.hours, target_dec.degrees)
            )
            ellipse_width = (
                width_deg
                if coordinate_system == CoordinateSystem.HORIZONTAL
                else width_deg / (15 * numpy.cos(numpy.deg2rad(target_dec.degrees)))
            )

            ellipse = Ellipse(
                xy=(x_coord, y_coord),
                width=ellipse_width,
                height=height_deg,
                angle=angle,
                edgecolor="yellow",
                facecolor=face_color,
                linewidth=2,
                linestyle="--",
                alpha=0.6,
            )
            ax.add_patch(ellipse)
        elif observation.local_planets.find_by_name(target_name) is not None:
            _plot_solar_system_object_on_skymap(
                observation,
                ax,
                observer,
                is_polar=False,
                style=style,
                object_name=target_name,
                is_target=True,
                coordinate_system=coordinate_system,
            )
        else:
            x_coord, y_coord = (
                (target_az.degrees, target_alt.degrees)
                if coordinate_system == CoordinateSystem.HORIZONTAL
                else (target_ra.hours, target_dec.degrees)
            )
            ax.scatter(
                x_coord,
                y_coord,
                s=200,
                facecolors="none",
                edgecolors="yellow",
                marker="o",
                linewidths=2,
            )

        annotate_coords = (
            (target_az.degrees, target_alt.degrees)
            if coordinate_system == CoordinateSystem.HORIZONTAL
            else (target_ra.hours, target_dec.degrees)
        )
        ax.annotate(
            target_name,
            annotate_coords,
            textcoords="offset points",
            xytext=(0, 15),
            color="yellow",
            ha="center",
            fontsize=12,
        )

        ax.set_title(
            gettext_(
                "Skymap for {target_name} ({zoom_deg}° view, Generated: {generation_time_str})"
            ).format(
                target_name=target_name,
                zoom_deg=zoom_deg,
                generation_time_str=generation_time_str,
            ),
            color=style["TEXT_COLOR"],
        )
        if flipped_horizontally:
            ax.invert_xaxis()
        if flipped_vertically:
            ax.invert_yaxis()
        if flipped_horizontally or flipped_vertically:
            flip_str = gettext_("Flipped") + " "
            if flipped_horizontally:
                flip_str += "H"
            if flipped_vertically:
                flip_str += "V"
            ax.text(
                0.05,
                0.95,
                flip_str,
                transform=ax.transAxes,
                fontsize=12,
                verticalalignment="top",
                color=style["TEXT_COLOR"],
            )

        return fig
    else:
        fig, ax = pyplot.subplots(figsize=(10, 10), subplot_kw={"projection": "polar"})
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])

        polar_ax = cast(Any, ax)
        if coordinate_system == CoordinateSystem.HORIZONTAL:
            polar_ax.set_rlim(0, 90)
            polar_ax.set_theta_zero_location("N")
            polar_ax.set_theta_direction(-1)
            polar_ax.set_yticks([0, 30, 60, 90])
            polar_ax.set_yticklabels(
                ["90°", "60°", "30°", "0°"], color=style["TEXT_COLOR"]
            )
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
            polar_ax.set_theta_zero_location("N")
            polar_ax.set_theta_direction(1)  # RA increases eastward
            polar_ax.set_yticks([0, 30, 60, 90])
            polar_ax.set_yticklabels(
                ["90°", "60°", "30°", "0°"], color=style["TEXT_COLOR"]
            )
            polar_ax.set_rlabel_position(22.5)
            ra_labels = [f"{h}h" for h in range(0, 24, 3)]
            polar_ax.set_xticklabels(ra_labels, color=style["TEXT_COLOR"])

        ax.grid(True, color=style["GRID_COLOR"], linestyle="--", linewidth=0.5)

        good_condition_color = style.get(
            "GOOD_CONDITION_HL_COLOR",
            "#90EE90" if not effective_dark_mode else "#007447",
        )

        if coordinate_system == CoordinateSystem.HORIZONTAL:
            r_inner_good = 0
            r_outer_good = 90 - observation.conditions.min_object_altitude

            min_az_rad = numpy.deg2rad(
                float(observation.conditions.min_object_azimuth)
            )
            max_az_rad = numpy.deg2rad(
                float(observation.conditions.max_object_azimuth)
            )

            if (r_outer_good > 0) or not (
                float(observation.conditions.min_object_azimuth) == 0.0
                and float(observation.conditions.max_object_azimuth) == 360.0
            ):
                if min_az_rad > max_az_rad:  # Crosses North
                    theta1 = numpy.linspace(min_az_rad, 2 * numpy.pi, 50)
                    ax.fill_between(
                        theta1,
                        r_inner_good,
                        r_outer_good,
                        color=good_condition_color,
                        alpha=0.1,
                    )
                    theta2 = numpy.linspace(0, max_az_rad, 50)
                    ax.fill_between(
                        theta2,
                        r_inner_good,
                        r_outer_good,
                        color=good_condition_color,
                        alpha=0.1,
                    )
                else:
                    theta = numpy.linspace(min_az_rad, max_az_rad, 100)
                    ax.fill_between(
                        theta,
                        r_inner_good,
                        r_outer_good,
                        color=good_condition_color,
                        alpha=0.1,
                    )

            if r_outer_good > 0:
                ax.plot(
                    numpy.linspace(0, 2 * numpy.pi, 100),
                    [90 - observation.conditions.min_object_altitude] * 100,
                    color=style["GRID_COLOR"],
                    linestyle="--",
                    linewidth=1,
                )
                ax.text(
                    numpy.deg2rad(90),
                    90 - observation.conditions.min_object_altitude,
                    f"{observation.conditions.min_object_altitude}°",
                    ha="center",
                    va="bottom",
                    color=style["TEXT_COLOR"],
                    fontsize=10,
                    bbox=dict(
                        facecolor=style["AXES_FACE_COLOR"],
                        edgecolor="none",
                        boxstyle="round,pad=0.2",
                    ),
                )

            if not (
                float(observation.conditions.min_object_azimuth) == 0.0
                and float(observation.conditions.max_object_azimuth) == 360.0
            ):
                ax.plot(
                    [min_az_rad, min_az_rad],
                    [0, 90],
                    color=style["GRID_COLOR"],
                    linestyle=":",
                    linewidth=1,
                )
                ax.plot(
                    [max_az_rad, max_az_rad],
                    [0, 90],
                    color=style["GRID_COLOR"],
                    linestyle=":",
                    linewidth=1,
                )
        else:  # Equatorial
            # Create a grid in polar coordinates (RA, Dec)
            num_ra = 120  # ~3 degree resolution
            num_dec = 30  # ~3 degree resolution
            theta = numpy.linspace(0, 2 * numpy.pi, num_ra)  # RA
            r = numpy.linspace(0, 90, num_dec)  # Radius (90-Dec)
            theta_grid, r_grid = numpy.meshgrid(theta, r)

            # Convert polar grid to RA/Dec
            ra_rad = theta_grid
            dec_deg = 90 - r_grid
            ra_hours = ra_rad * 12 / numpy.pi

            # Create Skyfield Star objects for the entire grid
            grid_stars = SkyfieldStar(
                ra_hours=ra_hours.ravel(), dec_degrees=dec_deg.ravel()
            )
            alt_flat, az_flat, _ = observer.observe(grid_stars).apparent().altaz()
            alt = Angle(degrees=alt_flat.degrees.reshape(ra_hours.shape))
            az = Angle(degrees=az_flat.degrees.reshape(ra_hours.shape))

            # Reshape the results back to the grid shape
            alt_deg_grid = cast(Any, alt.degrees).reshape(theta_grid.shape)
            az_deg_grid = cast(Any, az.degrees).reshape(theta_grid.shape)

            # Check conditions
            min_alt = float(observation.conditions.min_object_altitude)
            min_az = float(observation.conditions.min_object_azimuth)
            max_az = float(observation.conditions.max_object_azimuth)

            # Create a mask for "good" conditions
            alt_mask = alt_deg_grid >= min_alt
            if min_az <= max_az:
                az_mask = (az_deg_grid >= min_az) & (az_deg_grid <= max_az)
            else:  # Azimuth range crosses 0/360
                az_mask = (az_deg_grid >= min_az) | (az_deg_grid <= max_az)
            good_mask = alt_mask & az_mask

            # Use contourf to shade the "good" area
            # We plot where the mask is True (1)
            ax.contourf(
                theta_grid,
                r_grid,
                good_mask.astype(int),
                levels=[0.5, 1.5],
                colors=[good_condition_color],
                alpha=0.1,
            )

        if plot_stars:
            _plot_stars_on_skymap(
                observation,
                ax,
                observer,
                star_magnitude_limit,
                is_polar=True,
                style=style,
                zoom_deg=zoom_deg,
                target_object=target_object,
                coordinate_system=coordinate_system,
            )
            _plot_bright_stars_on_skymap(
                observation,
                ax,
                observer,
                is_polar=True,
                style=style,
                zoom_deg=zoom_deg,
                coordinate_system=coordinate_system,
            )
        if plot_messier:
            _plot_messier_on_skymap(
                observation,
                ax,
                observer,
                is_polar=True,
                target_name=target_name,
                flipped_horizontally=flipped_horizontally,
                flipped_vertically=flipped_vertically,
                coordinate_system=coordinate_system,
            )
        if plot_ngc:
            _plot_ngc_on_skymap(
                observation,
                ax,
                observer,
                is_polar=True,
                target_name=target_name,
                star_magnitude_limit=star_magnitude_limit,
                zoom_deg=zoom_deg,
                target_object=target_object,
                flipped_horizontally=flipped_horizontally,
                flipped_vertically=flipped_vertically,
                coordinate_system=coordinate_system,
            )
        if plot_planets:
            _plot_planets_on_skymap(
                observation,
                ax,
                observer,
                is_polar=True,
                effective_dark_mode=effective_dark_mode,
                style=style,
                target_name=target_name,
                coordinate_system=coordinate_system,
            )
        if plot_sun and target_name != "Sun":
            _plot_solar_system_object_on_skymap(
                observation,
                ax,
                observer,
                is_polar=True,
                style=style,
                object_name="Sun",
                coordinate_system=coordinate_system,
            )
        if plot_moon and target_name != "Moon":
            _plot_solar_system_object_on_skymap(
                observation,
                ax,
                observer,
                is_polar=True,
                style=style,
                object_name="Moon",
                coordinate_system=coordinate_system,
            )
        if observation.local_planets.find_by_name(target_name) is not None:
            _plot_solar_system_object_on_skymap(
                observation,
                ax,
                observer,
                is_polar=True,
                style=style,
                object_name=target_name,
                is_target=True,
                coordinate_system=coordinate_system,
            )

        if coordinate_system == CoordinateSystem.HORIZONTAL and bool(
            numpy.any(target_alt.degrees > 0)
        ):
            if target_object_data is not None:
                width_arcmin = target_object_data.get(ObjectTableLabels.WIDTH, 0)
                width_arcmin = getattr(width_arcmin, "magnitude", width_arcmin)
                width_deg = width_arcmin / 60.0

                height_arcmin = target_object_data.get("Height", width_arcmin)
                height_arcmin = getattr(height_arcmin, "magnitude", height_arcmin)
                height_deg = height_arcmin / 60.0

                size = (width_deg + height_deg) / 2 * 100
                polar_ax.scatter(
                    target_az.radians,
                    90 - target_alt.degrees,
                    s=size,
                    color="yellow",
                    marker="+",
                )
            else:
                polar_ax.scatter(
                    target_az.radians,
                    90 - target_alt.degrees,
                    s=200,
                    facecolors="none",
                    edgecolors="yellow",
                    marker="o",
                    linewidths=2,
                )
            polar_ax.annotate(
                target_name,
                (target_az.radians, 90 - target_alt.degrees),
                textcoords="offset points",
                xytext=(0, 15),
                color="yellow",
                ha="center",
                fontsize=12,
            )
        elif coordinate_system == CoordinateSystem.EQUATORIAL:
            if target_object_data is not None:
                width_arcmin = target_object_data.get(ObjectTableLabels.WIDTH, 0)
                width_arcmin = getattr(width_arcmin, "magnitude", width_arcmin)
                width_deg = width_arcmin / 60.0

                height_arcmin = target_object_data.get("Height", width_arcmin)
                height_arcmin = getattr(height_arcmin, "magnitude", height_arcmin)
                height_deg = height_arcmin / 60.0

                size = (width_deg + height_deg) / 2 * 100
                polar_ax.scatter(
                    target_ra.radians,
                    90 - target_dec.degrees,
                    s=size,
                    color="yellow",
                    marker="+",
                )
            else:
                polar_ax.scatter(
                    target_ra.radians,
                    90 - target_dec.degrees,
                    s=200,
                    facecolors="none",
                    edgecolors="yellow",
                    marker="o",
                    linewidths=2,
                )
            polar_ax.annotate(
                target_name,
                (target_ra.radians, 90 - target_dec.degrees),
                textcoords="offset points",
                xytext=(0, 15),
                color="yellow",
                ha="center",
                fontsize=12,
            )

        ax.set_title(
            gettext_(
                "Skymap for {target_name} (Generated: {generation_time_str})"
            ).format(target_name=target_name, generation_time_str=generation_time_str),
            color=style["TEXT_COLOR"],
        )

        return fig

def plot_skymap(
    observation: "Observation",
    target_name: str,
    dark_mode_override: Optional[bool] = None,
    zoom_deg: Optional[float] = None,
    star_magnitude_limit: Optional[float] = None,
    plot_stars: bool = True,
    plot_messier: bool = False,
    plot_ngc: bool = False,
    plot_planets: bool = False,
    plot_sun: bool = False,
    plot_moon: bool = False,
    plot_date: Optional[datetime] = None,
    equipment_id: Optional[int] = None,
    flip_horizontally: Optional[bool] = None,
    flip_vertically: Optional[bool] = None,
    coordinate_system: CoordinateSystem = cast(CoordinateSystem, CoordinateSystem.HORIZONTAL),
    **kwargs,
):
    flipped_horizontally = False
    flipped_vertically = False
    if flip_horizontally is not None:
        flipped_horizontally = flip_horizontally
    if flip_vertically is not None:
        flipped_vertically = flip_vertically
    elif equipment_id is not None and zoom_deg is not None:
        equipment_data = observation.equipment.data()
        if not equipment_data.empty and equipment_id in equipment_data["ID"].values:
            row = equipment_data.loc[equipment_data["ID"] == equipment_id]
            flipped_horizontally = row["Flipped Horizontally"].iloc[0]
            flipped_vertically = row["Flipped Vertically"].iloc[0]

    return _generate_plot_skymap(
        observation,
        target_name=target_name,
        dark_mode_override=dark_mode_override,
        zoom_deg=zoom_deg,
        star_magnitude_limit=star_magnitude_limit,
        plot_stars=plot_stars,
        plot_messier=plot_messier,
        plot_ngc=plot_ngc,
        plot_planets=plot_planets,
        plot_sun=plot_sun,
        plot_moon=plot_moon,
        plot_date=plot_date,
        flipped_horizontally=flipped_horizontally,
        flipped_vertically=flipped_vertically,
        coordinate_system=coordinate_system,
        **kwargs,
    )
