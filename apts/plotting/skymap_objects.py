from typing import TYPE_CHECKING, Optional, cast, Any

import numpy
import pandas as pd
from matplotlib.patches import Ellipse
from skyfield.api import Star

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

    # Use pre-calculated float versions if available, otherwise extract from Quantities
    if "ra_hours" not in bright_stars_df.columns:
        if hasattr(bright_stars_df["RA"].iloc[0], "magnitude"):  # type: ignore
            bright_stars_df["RA"] = bright_stars_df["RA"].apply(lambda x: x.magnitude)  # type: ignore
        bright_stars_df.rename(columns={"RA": "ra_hours"}, inplace=True)  # type: ignore

    if "dec_degrees" not in bright_stars_df.columns:
        if hasattr(bright_stars_df["Dec"].iloc[0], "magnitude"):  # type: ignore
            bright_stars_df["Dec"] = bright_stars_df["Dec"].apply(lambda x: x.magnitude)  # type: ignore
        bright_stars_df.rename(columns={"Dec": "dec_degrees"}, inplace=True)  # type: ignore

    if "Magnitude_float" in bright_stars_df.columns:
        bright_stars_df["Magnitude"] = bright_stars_df["Magnitude_float"]
    elif hasattr(bright_stars_df["Magnitude"].iloc[0], "magnitude"):  # type: ignore
        bright_stars_df["Magnitude"] = bright_stars_df["Magnitude"].apply(  # type: ignore
            lambda x: x.magnitude
        )

    bright_stars_df["epoch_year"] = 2000.0

    # Filter out stars with missing coordinates to avoid Skyfield errors
    bright_stars_df = cast(Any, bright_stars_df).dropna(
        subset=["ra_hours", "dec_degrees"]
    )

    if bright_stars_df.empty:
        return

    star_positions = observer.observe(Star.from_dataframe(bright_stars_df))
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

        for name, x, y in zip(df_zoomed["Name"], az_zoomed_deg, alt_zoomed_deg):
            ax.annotate(
                name,
                (x, y),
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

        for name, x, y in zip(df_zoomed["Name"], ra_zoomed, dec_zoomed):
            ax.annotate(
                name,
                (x, y),
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
                for name, x, y in zip(
                    df_visible["Name"], az_visible_rad, 90 - alt_visible_deg
                ):
                    ax.annotate(
                        name,
                        (x, y),
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
                ra_rad_visible = ra.radians[visible_mask]
                for name, x, y in zip(df_visible["Name"], ra_rad_visible, radius):
                    ax.annotate(
                        name,
                        (x, y),
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
            for name, x, y in zip(df_visible["Name"], az_visible_deg, alt_visible_deg):
                ax.annotate(
                    name,
                    (x, y),
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
                center = Star(ra=target_object.ra, dec=target_object.dec)
            else:
                ra, dec, _ = observer.observe(target_object).radec()
                center = Star(ra_hours=ra.hours, dec_degrees=dec.degrees)
            observed_center = observer.observe(center)

            all_stars_vectors = Star.from_dataframe(stars_in_box)
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

    # Filter out stars with missing coordinates to avoid Skyfield errors
    bright_stars = cast(Any, bright_stars).dropna(subset=["ra_hours", "dec_degrees"])

    if bright_stars.empty:  # type: ignore
        return

    star_positions = observer.observe(Star.from_dataframe(bright_stars))
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
    if visible_messier.empty:
        return

    # Filter out target object
    plot_df = visible_messier[
        visible_messier[ObjectTableLabels.MESSIER] != target_name
    ].copy()

    if plot_df.empty:
        return

    # Ensure RA/Dec float columns exist for vectorization (handling mocks/incomplete data in tests)
    if "ra_hours" not in plot_df.columns or "dec_degrees" not in plot_df.columns:
        ras, decs = [], []
        # Using index-based loop to avoid potential issues with MagicMock Series
        for i in range(len(plot_df)):
            m_name = plot_df.iloc[i][ObjectTableLabels.MESSIER]
            # Try to get coordinates from the catalog or object itself
            m_obj = observation.local_messier.find_by_name(m_name)
            if m_obj and hasattr(m_obj, "ra"):
                ras.append(m_obj.ra.hours)
                decs.append(m_obj.dec.degrees)
            else:
                # Fallback to direct column access with Quantity support
                row = plot_df.iloc[i]
                r_val = row.get("ra_hours", row.get(ObjectTableLabels.RA, numpy.nan))
                d_val = row.get("dec_degrees", row.get(ObjectTableLabels.DEC, numpy.nan))
                ras.append(getattr(r_val, "magnitude", r_val))
                decs.append(getattr(d_val, "magnitude", d_val))
        plot_df["ra_hours"] = ras
        plot_df["dec_degrees"] = decs

    # Ensure valid coordinates and reset index for array matching
    plot_df = (
        cast(pd.DataFrame, plot_df)
        .dropna(subset=["ra_hours", "dec_degrees"])
        .reset_index(drop=True)
    )

    if plot_df.empty:
        return

    # Restoration of original plotting logic: use individual observations if bulk fails (for tests)
    # or if we are dealing with a non-vectorized observer.
    try:
        # 1. Attempt bulk observation
        stars_vector = Star(
            ra_hours=plot_df["ra_hours"].to_numpy(),
            dec_degrees=plot_df["dec_degrees"].to_numpy(),
        )
        astrometric = observer.observe(stars_vector).apparent()

        alt_obj, az_obj, _ = astrometric.altaz()
        ra_obj, dec_obj, _ = astrometric.radec()

        alt_deg = numpy.atleast_1d(alt_obj.degrees)
        az_deg = numpy.atleast_1d(az_obj.degrees)
        ra_hours = numpy.atleast_1d(ra_obj.hours)
        dec_deg = numpy.atleast_1d(dec_obj.degrees)
        ra_rad = numpy.atleast_1d(ra_obj.radians)
    except Exception:
        # 2. Fallback to individual observation (safest for mocks/complex test cases)
        alt_deg, az_deg = [], []
        ra_hours, dec_deg, ra_rad = [], [], []
        for i in range(len(plot_df)):
            m_name = plot_df.iloc[i][ObjectTableLabels.MESSIER]
            m_obj = observation.local_messier.find_by_name(m_name)
            if m_obj:
                obs = observer.observe(m_obj).apparent()
                # Handle potential scalar/mock results
                alt_o, az_o, _ = obs.altaz()
                ra_o, dec_o, _ = obs.radec()
                alt_deg.append(alt_o.degrees if hasattr(alt_o, "degrees") else alt_o)
                az_deg.append(az_o.degrees if hasattr(az_o, "degrees") else az_o)
                ra_hours.append(ra_o.hours if hasattr(ra_o, "hours") else ra_o)
                dec_deg.append(dec_o.degrees if hasattr(dec_o, "degrees") else dec_o)
                ra_rad.append(ra_o.radians if hasattr(ra_o, "radians") else ra_o)
            else:
                alt_deg.append(numpy.nan)
                az_deg.append(numpy.nan)
                ra_hours.append(numpy.nan)
                dec_deg.append(numpy.nan)
                ra_rad.append(numpy.nan)
        alt_deg = numpy.atleast_1d(alt_deg)
        az_deg = numpy.atleast_1d(az_deg)
        ra_hours = numpy.atleast_1d(ra_hours)
        dec_deg = numpy.atleast_1d(dec_deg)
        ra_rad = numpy.atleast_1d(ra_rad)

    # Extract dimensions using vectorized pandas operations to avoid pint Quantity overhead
    def get_dim(col_name, default_val=1.0):
        if col_name in plot_df.columns:
            # Handle mixed Quantity/float Series efficiently
            return numpy.array(
                [getattr(x, "magnitude", x) for x in plot_df[col_name].values],
                dtype=float,
            )
        return numpy.full(len(plot_df), default_val)

    widths_deg = get_dim(ObjectTableLabels.WIDTH) / 60.0
    heights_deg = get_dim("Height", numpy.nan) / 60.0
    # Fallback height to width if missing
    heights_deg = numpy.where(numpy.isnan(heights_deg), widths_deg, heights_deg)
    pos_angles = get_dim("PosAng", 0.0)

    # Determine colors based on type and magnitude
    effective_dark_mode = get_dark_mode()
    # Cast potential Series outputs from .get() to satisfy Pyright
    types_raw = cast(Any, plot_df).get("Type", ["Other"] * len(plot_df))
    types = [gettext_(t) for t in cast(list, types_raw)]
    edge_colors = [get_messier_color(t, effective_dark_mode) for t in types]
    magnitudes_raw = cast(Any, plot_df).get("Magnitude", [10.0] * len(plot_df))
    magnitudes = [
        getattr(x, "magnitude", x) for x in cast(list, magnitudes_raw)
    ]
    face_colors = [get_brightness_color(m) for m in magnitudes]

    # Names for annotation
    names = plot_df[ObjectTableLabels.MESSIER].to_numpy()

    # Restoration of original plotting loop with helper function to ensure visual consistency
    # while retaining the performance benefits of bulk Skyfield observations.
    for i in range(len(alt_deg)):
        # Restore original filtering: only plot objects above the horizon
        if alt_deg[i] <= 0:
            continue

        parallactic_angle = calculate_parallactic_angle(
            observation.place.lat, dec_deg[i], az_deg[i]
        )
        angle = calculate_ellipse_angle(
            pos_angles[i],
            parallactic_angle,
            coordinate_system,
            flipped_horizontally,
            flipped_vertically,
        )

        _plot_celestial_object(
            ax,
            name=cast(str, names[i]),
            alt_deg=float(alt_deg[i]),
            az_deg=float(az_deg[i]),
            ra_hours=float(ra_hours[i]),
            dec_deg=float(dec_deg[i]),
            width_deg=float(widths_deg[i]),
            height_deg=float(heights_deg[i]),
            angle=angle,
            face_color=face_colors[i],
            edge_color=edge_colors[i],
            is_polar=is_polar,
            ra_rad=float(ra_rad[i]),
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
        # Use direct reference to avoid costly copy of 14k entries
        visible_ngc = observation.local_ngc.objects
    else:
        visible_ngc = observation.get_visible_ngc(
            star_magnitude_limit=star_magnitude_limit
        )

    if not cast(pd.DataFrame, visible_ngc).empty:
        if zoom_deg is not None and target_object is not None:
            if hasattr(target_object, "ra"):
                ra_center_hours = target_object.ra.hours
                dec_center_degrees = target_object.dec.degrees
            else:
                # It's a planet or other solar system body
                ra_p, dec_p, _ = observer.observe(target_object).radec()
                ra_center_hours = ra_p.hours
                dec_center_degrees = dec_p.degrees

            deg_margin = zoom_deg * 2
            ra_margin_hours = deg_margin / 15.0
            ra_min = ra_center_hours - ra_margin_hours
            ra_max = ra_center_hours + ra_margin_hours
            dec_min = dec_center_degrees - deg_margin
            dec_max = dec_center_degrees + deg_margin

            # Optimization: use pre-calculated float coords from catalog
            if (
                "ra_hours" not in visible_ngc.columns
                or "dec_degrees" not in visible_ngc.columns
            ):
                visible_ngc["ra_hours"] = visible_ngc["RA"].apply(_parse_ra)
                visible_ngc["dec_degrees"] = visible_ngc["Dec"].apply(_parse_dec)

            ngc_in_box = visible_ngc[
                (visible_ngc["ra_hours"] >= ra_min)
                & (visible_ngc["ra_hours"] <= ra_max)
                & (visible_ngc["dec_degrees"] >= dec_min)
                & (visible_ngc["dec_degrees"] <= dec_max)
            ]

            if not ngc_in_box.empty:
                # Use target object's position directly
                observed_center = observer.observe(target_object)

                # Vectorized Skyfield observation for separation calculation
                ngc_in_box_copy = ngc_in_box.copy()
                ngc_in_box_copy["epoch_year"] = 2000.0
                all_ngc_stars = Star.from_dataframe(ngc_in_box_copy)
                observed_all_ngc = observer.observe(all_ngc_stars)

                vec_center_np = observed_center.position.au
                vec_all_ngc_np = observed_all_ngc.position.au

                dot_product = numpy.dot(vec_center_np, vec_all_ngc_np)

                len_center = numpy.linalg.norm(vec_center_np)
                len_all_ngc = numpy.linalg.norm(vec_all_ngc_np, axis=0)

                cosine_angle = dot_product / (len_center * len_all_ngc)
                cosine_angle = numpy.clip(cosine_angle, -1.0, 1.0)

                separation_radians = numpy.arccos(cosine_angle)
                separation = numpy.degrees(separation_radians)
                nearby_mask = numpy.atleast_1d(separation < zoom_deg)
                # Use integer indexing to avoid KeyError with boolean arrays on some pandas versions
                # or when indexing with MagicMocks in tests.
                visible_ngc = ngc_in_box.iloc[numpy.where(nearby_mask)[0]].copy()
            else:
                visible_ngc = ngc_in_box

    if not cast(pd.DataFrame, visible_ngc).empty:
        # Ensure coordinate columns exist (they should be in the catalog, but might be missing in tests)
        if (
            "ra_hours" not in visible_ngc.columns
            or "dec_degrees" not in visible_ngc.columns
        ):
            visible_ngc = cast(pd.DataFrame, visible_ngc).copy()
            if "RA_parsed" in visible_ngc.columns:
                visible_ngc["ra_hours"] = visible_ngc["RA_parsed"]
            else:
                visible_ngc["ra_hours"] = visible_ngc["RA"].apply(_parse_ra)

            if "Dec_parsed" in visible_ngc.columns:
                visible_ngc["dec_degrees"] = visible_ngc["Dec_parsed"]
            else:
                visible_ngc["dec_degrees"] = visible_ngc["Dec"].apply(_parse_dec)

        # Optimization: Observe all visible NGC objects at once before plotting
        visible_ngc_copy = visible_ngc.copy()
        visible_ngc_copy["epoch_year"] = 2000.0
        ngc_stars = Star.from_dataframe(visible_ngc_copy)
        all_positions = observer.observe(ngc_stars).apparent()

        def to_array(val, n):
            arr = numpy.atleast_1d(val)
            if arr.size == 1 and n > 1:
                return numpy.full(n, arr[0])
            return arr

        num_objects = len(visible_ngc)
        alt_all_deg = to_array(all_positions.altaz()[0].degrees, num_objects)
        az_all_deg = to_array(all_positions.altaz()[1].degrees, num_objects)
        ra_all_hours = to_array(all_positions.radec()[0].hours, num_objects)
        dec_all_deg = to_array(all_positions.radec()[1].degrees, num_objects)
        ra_all_rad = to_array(all_positions.radec()[0].radians, num_objects)

        # Reset index to ensure i matches the position in all_positions arrays
        visible_ngc_plot = cast(pd.DataFrame, visible_ngc).reset_index(drop=True)

        # Optimization: use vectorized coordinates for visibility and basic plot values
        # This handles the alt_deg > 0 check efficiently for all objects.
        is_above_horizon = alt_all_deg > 0
        if not numpy.any(is_above_horizon):
            return

        # Prepare data for plotting
        # Optimization: replace iterrows() with faster zip() and vectorized operations
        names = (
            visible_ngc_plot[ObjectTableLabels.NGC]
            .fillna(visible_ngc_plot[ObjectTableLabels.NAME])
            .to_numpy()
        )
        # Filter by name and horizon at once
        mask = (names != target_name) & is_above_horizon
        if not numpy.any(mask):
            return

        active_indices = numpy.where(mask)[0]
        active_names = names[mask]
        active_alts = alt_all_deg[mask]
        active_azs = az_all_deg[mask]
        active_ras_h = ra_all_hours[mask]
        active_ras_r = ra_all_rad[mask]
        active_decs = dec_all_deg[mask]

        # Extract dimensions and other properties using vectorized pandas methods
        # To avoid pint Quantity overhead, we use pre-calculated floats if possible
        # or convert once.
        def get_dim(col_name, default_col=None):
            if col_name in visible_ngc_plot.columns:
                vals = visible_ngc_plot.loc[mask, col_name]
            else:
                vals = pd.Series(numpy.nan, index=visible_ngc_plot.index[mask])

            if (
                default_col
                and default_col in visible_ngc_plot.columns
                and vals.isna().any()
            ):
                vals = vals.fillna(visible_ngc_plot.loc[mask, default_col])
            vals = vals.fillna(1.0)
            return numpy.array([getattr(x, "magnitude", x) for x in vals], dtype=float)

        widths_deg = get_dim("Size", "MajAx") / 60.0
        heights_deg = get_dim("MinAx", "Size") / 60.0
        pos_angles = get_dim("PosAng")

        if is_polar:
            # Vectorized scatter for all NGC objects in polar view
            # This provides a massive speedup by reducing thousands of Matplotlib calls to one.
            sizes = (widths_deg + heights_deg) / 2 * 100
            is_sh = observation.place.lat_decimal < 0

            if coordinate_system == CoordinateSystem.HORIZONTAL:
                x_vals, y_vals = numpy.deg2rad(active_azs), 90 - active_alts
            else:
                x_vals, y_vals = active_ras_r, (
                    90 + active_decs if is_sh else 90 - active_decs
                )

            ax.scatter(x_vals, y_vals, s=sizes, color="green", marker="+")

            # Annotation loop still needed but optimized to avoid iterrows()
            for name, x, y in zip(active_names, x_vals, y_vals):
                ax.annotate(
                    name,
                    (x, y),
                    textcoords="offset points",
                    xytext=(5, 5),
                    color="green",
                )
        else:
            # Cartesian / Zoomed view - still using loop for Ellipse patches but optimized
            # (PatchCollection could be used but Ellipse initialization is still per-object)
            if "Mag" in visible_ngc_plot.columns:
                magnitudes = visible_ngc_plot.loc[mask, "Mag"].to_numpy()
            elif "Magnitude" in visible_ngc_plot.columns:
                magnitudes = visible_ngc_plot.loc[mask, "Magnitude"].to_numpy()
            else:
                magnitudes = numpy.full(len(active_indices), 10.0)

            for i, idx in enumerate(active_indices):
                parallactic_angle = calculate_parallactic_angle(
                    observation.place.lat, active_decs[i], active_azs[i]
                )
                angle = calculate_ellipse_angle(
                    pos_angles[i],
                    parallactic_angle,
                    coordinate_system,
                    flipped_horizontally,
                    flipped_vertically,
                )
                face_color = get_brightness_color(magnitudes[i])

                _plot_celestial_object(
                    ax,
                    name=cast(str, active_names[i]),
                    alt_deg=float(active_alts[i]),
                    az_deg=float(active_azs[i]),
                    ra_hours=float(active_ras_h[i]),
                    dec_deg=float(active_decs[i]),
                    width_deg=float(widths_deg[i]),
                    height_deg=float(heights_deg[i]),
                    angle=angle,
                    face_color=face_color,
                    edge_color="green",
                    is_polar=False,
                    ra_rad=float(active_ras_r[i]),
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

    # Optimization: perform a single observation and apparent position calculation.
    # Apparent positions are expensive; reusing the result for Alt/Az and RA/Dec avoids redundant work.
    astrometric = observer.observe(obj).apparent()
    alt, az, _ = astrometric.altaz()
    ra, dec, _ = astrometric.radec()

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
