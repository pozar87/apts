from typing import TYPE_CHECKING, Any, Optional, cast

import numpy
import pandas as pd
from skyfield.api import Star

from apts.constants.plot import CoordinateSystem

if TYPE_CHECKING:
    from apts.observations import Observation


def _ensure_coordinate_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Ensures that the DataFrame has ra_hours, dec_degrees, and magnitude columns as floats."""
    if df.empty:
        return df

    df = df.copy()

    # RA handling
    if "ra_hours" not in df.columns and "RA" in df.columns:
        if hasattr(df["RA"].iloc[0], "magnitude"):  # type: ignore
            # Optimization: list comprehension over .values is faster than .apply() for simple attribute access.
            df["ra_hours"] = [getattr(x, "magnitude", x) for x in df["RA"].values]
        else:
            df["ra_hours"] = df["RA"]

    # Dec handling
    if "dec_degrees" not in df.columns and "Dec" in df.columns:
        if hasattr(df["Dec"].iloc[0], "magnitude"):  # type: ignore
            # Optimization: list comprehension over .values is faster than .apply() for simple attribute access.
            df["dec_degrees"] = [getattr(x, "magnitude", x) for x in df["Dec"].values]
        else:
            df["dec_degrees"] = df["Dec"]

    # Magnitude handling
    if "magnitude" not in df.columns:
        if "Magnitude_float" in df.columns:
            df["magnitude"] = df["Magnitude_float"]
        elif "Magnitude" in df.columns:
            if hasattr(df["Magnitude"].iloc[0], "magnitude"):  # type: ignore
                # Optimization: list comprehension over .values is faster than .apply() for simple attribute access.
                df["magnitude"] = [
                    getattr(x, "magnitude", x) for x in df["Magnitude"].values
                ]
            else:
                df["magnitude"] = df["Magnitude"]

    # Add epoch_year for Skyfield
    df["epoch_year"] = 2000.0

    # Filter out stars with missing coordinates to avoid Skyfield errors
    return cast(pd.DataFrame, df.dropna(subset=["ra_hours", "dec_degrees"]))


def _filter_stars_by_proximity(
    stars: pd.DataFrame,
    observer,
    target_object,
    zoom_deg: float,
) -> pd.DataFrame:
    """Filters stars to those within zoom_deg of the target_object."""
    if stars.empty:
        return stars

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
    deg_margin = zoom_deg * 2
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

    if stars_in_box.empty:
        return cast(pd.DataFrame, stars_in_box)

    # Precise separation calculation
    if hasattr(target_object, "ra"):
        center = Star(ra=target_object.ra, dec=target_object.dec)
    else:
        ra, dec, _ = observer.observe(target_object).radec()
        center = Star(ra_hours=ra.hours, dec_degrees=dec.degrees)
    observed_center = observer.observe(center)

    all_stars_vectors = Star.from_dataframe(stars_in_box)
    observed_all_stars = observer.observe(all_stars_vectors)

    vec_center_np = observed_center.position.au
    vec_all_stars_np = observed_all_stars.position.au

    dot_product = numpy.dot(vec_center_np, vec_all_stars_np)
    len_center = numpy.linalg.norm(vec_center_np, axis=0)
    len_all_stars = numpy.linalg.norm(vec_all_stars_np, axis=0)

    cosine_angle = dot_product / (len_center * len_all_stars)
    cosine_angle = numpy.clip(cosine_angle, -1.0, 1.0)

    separation = numpy.degrees(numpy.arccos(cosine_angle))
    return cast(pd.DataFrame, stars_in_box[separation < zoom_deg])


def _apply_zoom_and_horizon_filter(
    df: pd.DataFrame,
    alt_deg: numpy.ndarray,
    az_deg: numpy.ndarray,
    ra_hours: numpy.ndarray,
    dec_deg: numpy.ndarray,
    coordinate_system: CoordinateSystem,
    ignore_horizon: bool,
    zoom_deg: Optional[float],
    ax,
):
    """Calculates visibility and zoom masks for the given stars."""
    import apts.plotting.skymap_objects as api

    # Horizon filtering
    if coordinate_system == CoordinateSystem.HORIZONTAL and not ignore_horizon:
        visible_mask = numpy.atleast_1d(alt_deg > 0)
    else:
        visible_mask = numpy.ones(len(df), dtype=bool)

    if not numpy.any(visible_mask):
        return visible_mask, visible_mask  # Both masks are false

    # Zoom filtering
    if zoom_deg is not None:
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        if coordinate_system == CoordinateSystem.HORIZONTAL:
            zoom_mask = (
                (az_deg >= xlim[0])
                & (az_deg <= xlim[1])
                & (alt_deg >= ylim[0])
                & (alt_deg <= ylim[1])
            )
        else:  # EQUATORIAL
            zoom_mask = api.create_ra_zoom_mask(ra_hours, xlim) & (
                (dec_deg >= ylim[0]) & (dec_deg <= ylim[1])
            )
    else:
        zoom_mask = numpy.ones(len(df), dtype=bool)

    return visible_mask, zoom_mask


def _add_star_scatter_and_labels(
    ax,
    names: numpy.ndarray,
    x_plot: numpy.ndarray,
    y_plot: numpy.ndarray,
    sizes: Any,
    color: str,
    marker: str,
    plot_labels: bool,
    edge_color: Optional[str] = None,
):
    """Adds star scatter plot and labels to the axes."""
    if len(x_plot) == 0:
        return

    ax.scatter(
        x_plot,
        y_plot,
        s=sizes,
        color=color,
        marker=marker,
        edgecolors=edge_color,
    )

    if plot_labels:
        for name, x, y in zip(names, x_plot, y_plot):
            ax.annotate(
                name,
                (x, y),
                textcoords="offset points",
                xytext=(5, 5),
                color=color if edge_color is None else edge_color,
                fontsize=8,
            )


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
    bright_stars_df = cast(pd.DataFrame, observation.local_stars.objects.copy())
    if target_name:
        bright_stars_df = cast(
            pd.DataFrame,
            bright_stars_df[~bright_stars_df["Name"].isin([target_name])],
        )

    bright_stars_df = _ensure_coordinate_columns(bright_stars_df)
    if bright_stars_df.empty:
        return

    star_positions = observer.observe(Star.from_dataframe(bright_stars_df))
    apparent = star_positions.apparent()
    alt, az, _ = apparent.altaz()
    ra, dec, _ = apparent.radec()

    visible_mask, zoom_mask = _apply_zoom_and_horizon_filter(
        bright_stars_df,
        alt.degrees,
        az.degrees,
        ra.hours,
        dec.degrees,
        cast(CoordinateSystem, coordinate_system),
        ignore_horizon,
        zoom_deg,
        ax,
    )

    full_mask = visible_mask & zoom_mask
    if not numpy.any(full_mask):
        return

    df_plot = cast(pd.DataFrame, bright_stars_df[full_mask])
    star_color = style.get("EMPHASIS_COLOR", "yellow")

    if not is_polar:
        if coordinate_system == CoordinateSystem.HORIZONTAL:
            x_plot, y_plot = az.degrees[full_mask], alt.degrees[full_mask]
        else:  # EQUATORIAL
            x_plot, y_plot = ra.hours[full_mask], dec.degrees[full_mask]

        _add_star_scatter_and_labels(
            ax,
            df_plot["Name"].to_numpy(),
            x_plot,
            y_plot,
            sizes=40,
            color=star_color,
            marker="*",
            plot_labels=plot_labels,
        )
    else:  # is_polar
        if coordinate_system == CoordinateSystem.HORIZONTAL:
            x_plot, y_plot = az.radians[full_mask], 90 - alt.degrees[full_mask]
        else:
            is_sh = observation.place.lat_decimal < 0
            x_plot = ra.radians[full_mask]
            y_plot = (
                90 + dec.degrees[full_mask] if is_sh else 90 - dec.degrees[full_mask]
            )

        _add_star_scatter_and_labels(
            ax,
            df_plot["Name"].to_numpy(),
            x_plot,
            y_plot,
            sizes=40,
            color=star_color,
            marker="*",
            plot_labels=plot_labels,
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
        stars = _filter_stars_by_proximity(stars, observer, target_object, zoom_deg)

    if mag_limit is not None:
        limit = mag_limit
    elif is_polar:
        limit = 4.5
    elif zoom_deg is not None:
        limit = 7.5
    else:
        limit = 6.0

    bright_stars = cast(pd.DataFrame, stars[stars["magnitude"] <= limit])
    bright_stars = _ensure_coordinate_columns(bright_stars)

    if bright_stars.empty:
        return

    star_positions = observer.observe(Star.from_dataframe(bright_stars))
    apparent = star_positions.apparent()
    alt, az, _ = apparent.altaz()
    ra, dec, _ = apparent.radec()

    visible_mask, zoom_mask = _apply_zoom_and_horizon_filter(
        bright_stars,
        alt.degrees,
        az.degrees,
        ra.hours,
        dec.degrees,
        coordinate_system,
        ignore_horizon,
        zoom_deg,
        ax,
    )

    full_mask = visible_mask & zoom_mask
    if not numpy.any(full_mask):
        return

    mag_plot = bright_stars[full_mask]["magnitude"]

    if not is_polar:
        if coordinate_system == CoordinateSystem.HORIZONTAL:
            x_plot, y_plot = az.degrees[full_mask], alt.degrees[full_mask]
        else:  # EQUATORIAL
            x_plot, y_plot = ra.hours[full_mask], dec.degrees[full_mask]

        sizes = (limit + 1 - numpy.array(mag_plot)) * 3
        _add_star_scatter_and_labels(
            ax,
            numpy.array([]),  # No labels for regular stars
            x_plot,
            y_plot,
            sizes=sizes,
            color=style["TEXT_COLOR"],
            marker=".",
            plot_labels=False,
        )
    else:  # is_polar
        sizes = (limit + 1 - numpy.array(mag_plot)) * 5
        if coordinate_system == CoordinateSystem.HORIZONTAL:
            x_plot, y_plot = az.radians[full_mask], 90 - alt.degrees[full_mask]
        else:
            is_sh = observation.place.lat_decimal < 0
            x_plot = ra.radians[full_mask]
            y_plot = (
                90 + dec.degrees[full_mask] if is_sh else 90 - dec.degrees[full_mask]
            )

        _add_star_scatter_and_labels(
            ax,
            numpy.array([]),
            x_plot,
            y_plot,
            sizes=sizes,
            color=ax.get_facecolor(),
            marker=".",
            plot_labels=False,
            edge_color=style["TEXT_COLOR"],
        )
