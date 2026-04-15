from typing import TYPE_CHECKING, Optional, cast, Any

import numpy
import pandas as pd
from skyfield.api import Star

from apts.constants.plot import CoordinateSystem
if TYPE_CHECKING:
    from apts.observations import Observation


def _plot_bright_stars_on_skymap(
    observation: "Observation",
    ax,
    observer,
    is_polar,
    style: dict,
    zoom_deg: Optional[float] = None,
    coordinate_system: Optional[CoordinateSystem] = None,
    target_name: Optional[str] = None,
    plot_labels: bool = True,
    ignore_horizon: bool = False,
):
    import apts.plotting.skymap_objects as api
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
    # For Horizontal plots, we only want stars above the horizon unless ignore_horizon is True.
    if coordinate_system == CoordinateSystem.HORIZONTAL and not ignore_horizon:
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

    if not is_polar:
        if coordinate_system == CoordinateSystem.HORIZONTAL:
            if zoom_deg is not None:
                xlim = ax.get_xlim()
                ylim = ax.get_ylim()

                zoom_mask = (
                    (az_visible_deg >= xlim[0])
                    & (az_visible_deg <= xlim[1])
                    & (alt_visible_deg >= ylim[0])
                    & (alt_visible_deg <= ylim[1])
                )

                df_zoomed = df_visible[zoom_mask]
                alt_plot = alt_visible_deg[zoom_mask]
                az_plot = az_visible_deg[zoom_mask]
                names_plot = df_zoomed["Name"]
            else:
                zoom_mask = numpy.ones(len(df_visible), dtype=bool)
                alt_plot = alt_visible_deg
                az_plot = az_visible_deg
                names_plot = df_visible["Name"]

            if len(az_plot) == 0:
                return

            ax.scatter(az_plot, alt_plot, s=40, color=star_color, marker="*")

            if plot_labels:
                for name, x, y in zip(names_plot, az_plot, alt_plot):
                    ax.annotate(
                        name,
                        (x, y),
                        textcoords="offset points",
                        xytext=(5, 5),
                        color=star_color,
                        fontsize=8,
                    )
        else:  # EQUATORIAL
            ra_hours_apparent = ra.hours[visible_mask]
            dec_degrees_apparent = dec.degrees[visible_mask]

            if zoom_deg is not None:
                xlim = ax.get_xlim()
                ylim = ax.get_ylim()

                zoom_mask = api.create_ra_zoom_mask(ra_hours_apparent, xlim) & (
                    (dec_degrees_apparent >= ylim[0]) & (dec_degrees_apparent <= ylim[1])
                )

                df_zoomed = df_visible[zoom_mask]
                ra_plot = ra_hours_apparent[zoom_mask]
                dec_plot = dec_degrees_apparent[zoom_mask]
                names_plot = df_zoomed["Name"]
            else:
                zoom_mask = numpy.ones(len(df_visible), dtype=bool)
                ra_plot = ra_hours_apparent
                dec_plot = dec_degrees_apparent
                names_plot = df_visible["Name"]

            if len(ra_plot) == 0:
                return

            ax.scatter(ra_plot, dec_plot, s=40, color=star_color, marker="*")

            if plot_labels:
                for name, x, y in zip(names_plot, ra_plot, dec_plot):
                    ax.annotate(
                        name,
                        (x, y),
                        textcoords="offset points",
                        xytext=(5, 5),
                        color=star_color,
                        fontsize=8,
                    )
    else:  # is_polar
        if coordinate_system == CoordinateSystem.HORIZONTAL:
            ax.scatter(
                az_visible_rad,
                90 - alt_visible_deg,
                s=40,
                color=star_color,
                marker="*",
            )
            if plot_labels:
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
            if plot_labels:
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
    plot_labels: bool = True,
    ignore_horizon: bool = False,
):
    import apts.plotting.skymap_objects as api
    stars = api.get_hipparcos_data()

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

    if coordinate_system == CoordinateSystem.HORIZONTAL and not ignore_horizon:
        visible = numpy.atleast_1d(alt.degrees > 0)
    else:
        visible = numpy.ones(len(bright_stars), dtype=bool)

    if not any(visible) and not ignore_horizon:
        return

    if not is_polar:
        if coordinate_system == CoordinateSystem.HORIZONTAL:
            az_apparent = az.degrees[visible]
            alt_apparent = alt.degrees[visible]
            mag_apparent = bright_stars[visible]["magnitude"]

            if zoom_deg is not None:
                xlim = ax.get_xlim()
                ylim = ax.get_ylim()

                zoom_mask = (
                    (az_apparent >= xlim[0])
                    & (az_apparent <= xlim[1])
                    & (alt_apparent >= ylim[0])
                    & (alt_apparent <= ylim[1])
                )

                az_plot = az_apparent[zoom_mask]
                alt_plot = alt_apparent[zoom_mask]
                mag_plot = mag_apparent[zoom_mask]
            else:
                az_plot = az_apparent
                alt_plot = alt_apparent
                mag_plot = mag_apparent

            if len(az_plot) == 0:
                return

            sizes = (limit + 1 - numpy.array(mag_plot)) * 3
            ax.scatter(
                az_plot,
                alt_plot,
                s=sizes,
                color=style["TEXT_COLOR"],
                marker=".",
            )
        else:  # EQUATORIAL
            ra_hours_apparent = ra.hours[visible]
            dec_degrees_apparent = dec.degrees[visible]
            mag_apparent = bright_stars[visible]["magnitude"]

            if zoom_deg is not None:
                xlim = ax.get_xlim()
                ylim = ax.get_ylim()

                zoom_mask = api.create_ra_zoom_mask(ra_hours_apparent, xlim) & (
                    (dec_degrees_apparent >= ylim[0]) & (dec_degrees_apparent <= ylim[1])
                )

                ra_plot = ra_hours_apparent[zoom_mask]
                dec_plot = dec_degrees_apparent[zoom_mask]
                mag_plot = mag_apparent[zoom_mask]
            else:
                ra_plot = ra_hours_apparent
                dec_plot = dec_degrees_apparent
                mag_plot = mag_apparent

            if len(ra_plot) == 0:
                return

            sizes = (limit + 1 - numpy.array(mag_plot)) * 3
            ax.scatter(
                ra_plot,
                dec_plot,
                s=sizes,
                color=style["TEXT_COLOR"],
                marker=".",
            )
    else:  # is_polar
        sizes = (limit + 1 - numpy.array(bright_stars["magnitude"][visible])) * 5
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
