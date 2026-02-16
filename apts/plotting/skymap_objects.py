from typing import TYPE_CHECKING, Optional, cast

import numpy
import pandas as pd
from matplotlib.patches import Ellipse
from skyfield.api import Star as SkyfieldStar

from apts.config import get_dark_mode
from apts.constants.graphconstants import get_messier_color, get_planet_color
from apts.constants.plot import CoordinateSystem
from apts.i18n import gettext_
from apts.plotting.utils import (
    calculate_ellipse_angle,
    calculate_parallactic_angle,
    create_ra_zoom_mask,
    get_brightness_color,
    get_object_angular_size_deg,
)
from apts.utils import planetary
from ..cache import get_hipparcos_data
from ..constants import ObjectTableLabels

if TYPE_CHECKING:
    from ..observations import Observation


def _plot_bright_stars_on_skymap(
    observation: "Observation",
    ax,
    observer,
    is_polar,
    style: dict,
    zoom_deg: Optional[float] = None,
    coordinate_system: Optional[CoordinateSystem] = None,
    target_name: Optional[str] = None,
):
    bright_stars_df = cast(pd.DataFrame, observation.local_stars.objects.copy())
    if target_name:
        bright_stars_df = bright_stars_df[bright_stars_df["Name"] != target_name]

    if bright_stars_df.empty:
        return

    if hasattr(bright_stars_df["RA"].iloc[0], "magnitude"):  # type: ignore
        bright_stars_df["RA"] = bright_stars_df["RA"].apply(lambda x: x.magnitude)  # type: ignore
    if hasattr(bright_stars_df["Dec"].iloc[0], "magnitude"):  # type: ignore
        bright_stars_df["Dec"] = bright_stars_df["Dec"].apply(lambda x: x.magnitude)  # type: ignore
    if hasattr(bright_stars_df["Magnitude"].iloc[0], "magnitude"):  # type: ignore
        bright_stars_df["Magnitude"] = bright_stars_df["Magnitude"].apply(  # type: ignore
            lambda x: x.magnitude
        )

    bright_stars_df["epoch_year"] = 2000.0
    bright_stars_df.rename(
        columns={"RA": "ra_hours", "Dec": "dec_degrees"}, inplace=True  # type: ignore
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

    if df_visible.empty:  # type: ignore
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
                    star = df_visible.iloc[i]  # type: ignore
                    ax.annotate(
                        star["Name"],
                        (az_visible_rad[i], 90 - alt_visible_deg[i]),
                        textcoords="offset points",
                        xytext=(5, 5),
                        color=star_color,
                        fontsize=8,
                    )
            else:
                is_sh = observation.place.lat_decimal < 0
                radius = (
                    90 + dec.degrees[visible_mask]
                    if is_sh
                    else 90 - dec.degrees[visible_mask]
                )
                ax.scatter(
                    ra.radians[visible_mask],
                    radius,
                    s=40,
                    color=star_color,
                    marker="*",
                )
                for i in range(len(df_visible)):
                    star = df_visible.iloc[i]  # type: ignore
                    ax.annotate(
                        star["Name"],
                        (
                            ra.radians[visible_mask][i],
                            radius[i],
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
                star = df_visible.iloc[i]  # type: ignore
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
    target_name: Optional[str] = None,
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
                is_sh = observation.place.lat_decimal < 0
                radius = (
                    90 + dec.degrees[visible] if is_sh else 90 - dec.degrees[visible]
                )
                ax.scatter(
                    ra.radians[visible],
                    radius,
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
    is_sh: bool = False,
):
    """Helper function to plot a celestial object on a skymap."""
    if is_polar:
        size = (width_deg + height_deg) / 2 * 100
        if coordinate_system == CoordinateSystem.HORIZONTAL:
            x, y = numpy.deg2rad(az_deg), 90 - alt_deg
        else:
            x, y = ra_rad, 90 + dec_deg if is_sh else 90 - dec_deg

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

                    obj_type = gettext_(m_obj.get("Type", "Other"))
                    effective_dark_mode = get_dark_mode()
                    edge_color = get_messier_color(obj_type, effective_dark_mode)

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
                        edge_color=edge_color,
                        is_polar=is_polar,
                        ra_rad=ra.radians,
                        coordinate_system=coordinate_system,
                        is_sh=observation.place.lat_decimal < 0,
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
                        is_sh=observation.place.lat_decimal < 0,
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
        target_technical_name = (
            planetary.get_technical_name(target_name) if target_name else None
        )
        for _, p_obj in visible_planets.iterrows():
            planet_name = p_obj[ObjectTableLabels.NAME]
            technical_name = p_obj["TechnicalName"]
            if (
                planet_name == target_name
                or technical_name == target_name
                or technical_name == target_technical_name
            ):
                continue  # Skip the target object, it will be plotted separately
            _plot_solar_system_object_on_skymap(
                observation,
                ax,
                observer,
                is_polar,
                style,
                str(technical_name),
                display_name=cast(str, planet_name),
                coordinate_system=coordinate_system,
            )


def _plot_solar_system_object_on_skymap(
    observation: "Observation",
    ax,
    observer,
    is_polar,
    style,
    object_name: str,
    display_name: Optional[str] = None,
    is_target: bool = False,
    coordinate_system: CoordinateSystem = cast(
        CoordinateSystem, CoordinateSystem.HORIZONTAL
    ),
):
    """Helper to plot a solar system object, handling regular and target styles."""
    obj = observation.local_planets.find_by_name(object_name)
    if not obj:
        return  # Object not found

    if display_name is None:
        display_name = gettext_(planetary.get_simple_name(object_name))

    alt, az, _ = observer.observe(obj).apparent().altaz()
    ra, dec, _ = observer.observe(obj).apparent().radec()

    is_below_horizon = numpy.all(numpy.asarray(alt.degrees) <= 0)
    if is_below_horizon and coordinate_system == CoordinateSystem.HORIZONTAL:
        return

    size_deg = get_object_angular_size_deg(observation, object_name)

    # Determine colors and markers
    effective_dark_mode = get_dark_mode()
    default_color = style.get("EMPHASIS_COLOR", "yellow")
    edge_color = get_planet_color(
        planetary.get_simple_name(object_name), effective_dark_mode, default_color
    )
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
        # Use a combination of actual angular size and visual size based on magnitude
        # just like stars, but only as a minimum for visibility on the whole sky map.
        visual_size = 0
        if not is_target:
            try:
                # Find the planet data to get its magnitude
                technical_name = planetary.get_technical_name(object_name)
                planets_df = observation.local_planets.objects
                object_data = planets_df[
                    planets_df[ObjectTableLabels.NAME] == technical_name
                ]
                if not object_data.empty:
                    magnitude = object_data.iloc[0].get(ObjectTableLabels.MAGNITUDE)
                    if hasattr(magnitude, "magnitude"):
                        magnitude = magnitude.magnitude
                    if pd.notna(magnitude):
                        # Default limit for polar skymaps is 4.5
                        limit = 4.5
                        visual_size = (limit + 1 - float(magnitude)) * 5
            except Exception:
                # Fallback to a sensible default if magnitude calculation fails
                visual_size = 20

        size = max(size_deg * 200, visual_size)

        if coordinate_system == CoordinateSystem.HORIZONTAL:
            x, y = az.radians, 90 - alt.degrees
        else:
            is_sh = observation.place.lat_decimal < 0
            x, y = ra.radians, 90 + dec.degrees if is_sh else 90 - dec.degrees
        ax.scatter(x, y, s=size, color=edge_color, marker=marker)
        if not is_target:
            ax.annotate(
                display_name,
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
                display_name,
                (x_coord, y_coord),
                textcoords="offset points",
                xytext=(5, 5),
                color=edge_color,
            )
