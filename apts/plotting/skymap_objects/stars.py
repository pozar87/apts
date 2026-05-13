from typing import TYPE_CHECKING, Optional, cast, Any

import numpy
import pandas as pd
from skyfield.api import Star

from apts.constants.plot import CoordinateSystem
if TYPE_CHECKING:
    from apts.observations import Observation


def _apply_zoom_and_horizon_filter(
    ax,
    coordinate_system,
    zoom_deg,
    alt_deg,
    az_deg,
    az_rad,
    ra_hours,
    ra_rad,
    dec_deg,
    is_polar,
):
    """
    Applies zoom and horizon filtering to star coordinates.
    Returns a mask of visible/zoomed stars.
    """
    import apts.plotting.skymap_objects as api

    if is_polar:
        # For polar plots, we already have visible mask from horizon check
        return numpy.ones(len(alt_deg), dtype=bool)

    if zoom_deg is None:
        return numpy.ones(len(alt_deg), dtype=bool)

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    if coordinate_system == CoordinateSystem.HORIZONTAL:
        return (
            (az_deg >= xlim[0])
            & (az_deg <= xlim[1])
            & (alt_deg >= ylim[0])
            & (alt_deg <= ylim[1])
        )
    else:  # EQUATORIAL
        return api.create_ra_zoom_mask(ra_hours, xlim) & (
            (dec_deg >= ylim[0]) & (dec_deg <= ylim[1])
        )


def _add_star_scatter_and_labels(
    ax,
    coordinate_system,
    is_polar,
    alt_plot,
    az_plot_rad,
    az_plot_deg,
    ra_plot_rad,
    ra_plot_hours,
    dec_plot_deg,
    names_plot,
    sizes,
    color,
    marker,
    plot_labels,
    is_sh=False,
    edge_color=None,
):
    """
    Adds star scatter points and labels to the plot.
    """
    if not is_polar:
        x_plot = (
            az_plot_deg
            if coordinate_system == CoordinateSystem.HORIZONTAL
            else ra_plot_hours
        )
        y_plot = (
            alt_plot
            if coordinate_system == CoordinateSystem.HORIZONTAL
            else dec_plot_deg
        )
    else:
        x_plot = (
            az_plot_rad
            if coordinate_system == CoordinateSystem.HORIZONTAL
            else ra_plot_rad
        )
        radius = (
            90 - alt_plot
            if coordinate_system == CoordinateSystem.HORIZONTAL
            else (90 + dec_plot_deg if is_sh else 90 - dec_plot_deg)
        )
        y_plot = radius

    if len(x_plot) == 0:
        return

    scatter_kwargs = {"s": sizes, "color": color, "marker": marker}
    if edge_color:
        scatter_kwargs["edgecolors"] = edge_color

    ax.scatter(x_plot, y_plot, **scatter_kwargs)

    if plot_labels and names_plot is not None:
        for name, x, y in zip(names_plot, x_plot, y_plot):
            ax.annotate(
                name,
                (x, y),
                textcoords="offset points",
                xytext=(5, 5),
                color=color if not edge_color else edge_color,
                fontsize=8,
            )


def _is_southern_hemisphere(observation):
    """Helper to safely check if observer is in Southern Hemisphere, handling mocks."""
    lat = getattr(observation.place, "lat_decimal", 0)
    # If lat is a mock, it might fail comparison. Use a default.
    try:
        return float(lat) < 0
    except (TypeError, ValueError):
        return False


def _ensure_coordinate_columns(df):
    """Ensures bright stars dataframe has ra_hours and dec_degrees."""
    for col, attr in [("ra_hours", "RA"), ("dec_degrees", "Dec")]:
        if col not in df.columns:
            if hasattr(df[attr].iloc[0], "magnitude"):
                df[col] = df[attr].apply(lambda x: x.magnitude)
            else:
                df.rename(columns={attr: col}, inplace=True)

    if "Magnitude_float" in df.columns:
        df["Magnitude"] = df["Magnitude_float"]
    elif hasattr(df["Magnitude"].iloc[0], "magnitude"):
        df["Magnitude"] = df["Magnitude"].apply(lambda x: x.magnitude)


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
        bright_stars_df = bright_stars_df[bright_stars_df["Name"] != target_name]

    if bright_stars_df.empty:
        return

    _ensure_coordinate_columns(bright_stars_df)
    bright_stars_df["epoch_year"] = 2000.0
    bright_stars_df = cast(Any, bright_stars_df).dropna(
        subset=["ra_hours", "dec_degrees"]
    )

    if bright_stars_df.empty:
        return

    star_positions = observer.observe(Star.from_dataframe(bright_stars_df))
    alt, az, _ = star_positions.apparent().altaz()
    ra, dec, _ = star_positions.apparent().radec()

    if coordinate_system == CoordinateSystem.HORIZONTAL and not ignore_horizon:
        visible_mask = alt.degrees > 0
    else:
        visible_mask = numpy.ones(len(bright_stars_df), dtype=bool)

    df_visible = bright_stars_df[visible_mask]
    if df_visible.empty:
        return

    zoom_mask = _apply_zoom_and_horizon_filter(
        ax,
        coordinate_system,
        zoom_deg,
        alt.degrees[visible_mask],
        az.degrees[visible_mask],
        az.radians[visible_mask],
        ra.hours[visible_mask],
        ra.radians[visible_mask],
        dec.degrees[visible_mask],
        is_polar,
    )

    _add_star_scatter_and_labels(
        ax,
        coordinate_system,
        is_polar,
        alt.degrees[visible_mask][zoom_mask],
        az.radians[visible_mask][zoom_mask],
        az.degrees[visible_mask][zoom_mask],
        ra.radians[visible_mask][zoom_mask],
        ra.hours[visible_mask][zoom_mask],
        dec.degrees[visible_mask][zoom_mask],
        df_visible["Name"][zoom_mask],
        40,
        style.get("EMPHASIS_COLOR", "yellow"),
        "*",
        plot_labels,
        is_sh=_is_southern_hemisphere(observation),
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
        if hasattr(target_object, "ra"):
            ra_center_hours, dec_center_degrees = (
                target_object.ra.hours,
                target_object.dec.degrees,
            )
        else:
            ra_p, dec_p, _ = observer.observe(target_object).radec()
            ra_center_hours, dec_center_degrees = ra_p.hours, dec_p.degrees

        deg_margin = zoom_deg * 2
        ra_margin_hours = deg_margin / 15.0
        stars_in_box = stars[
            (stars["ra_hours"] >= ra_center_hours - ra_margin_hours)
            & (stars["ra_hours"] <= ra_center_hours + ra_margin_hours)
            & (stars["dec_degrees"] >= dec_center_degrees - deg_margin)
            & (stars["dec_degrees"] <= dec_center_degrees + deg_margin)
        ]

        if not stars_in_box.empty:
            if hasattr(target_object, "ra"):
                center = Star(ra=target_object.ra, dec=target_object.dec)
            else:
                ra, dec, _ = observer.observe(target_object).radec()
                center = Star(ra_hours=ra.hours, dec_degrees=dec.degrees)

            observed_center = observer.observe(center)
            observed_all_stars = observer.observe(Star.from_dataframe(stars_in_box))

            dot_product = numpy.dot(
                observed_center.position.au, observed_all_stars.position.au
            )
            len_center = numpy.linalg.norm(observed_center.position.au, axis=0)
            len_all_stars = numpy.linalg.norm(observed_all_stars.position.au, axis=0)

            cosine_angle = numpy.clip(
                dot_product / (len_center * len_all_stars), -1.0, 1.0
            )
            stars = stars_in_box[numpy.degrees(numpy.arccos(cosine_angle)) < zoom_deg]
        else:
            stars = stars_in_box

    limit = (
        mag_limit
        if mag_limit is not None
        else (4.5 if is_polar else (7.5 if zoom_deg is not None else 6.0))
    )
    bright_stars = stars[stars["magnitude"] <= limit].dropna(
        subset=["ra_hours", "dec_degrees"]
    )

    if bright_stars.empty:
        return

    star_positions = observer.observe(Star.from_dataframe(bright_stars))
    alt, az, _ = star_positions.apparent().altaz()
    ra, dec, _ = star_positions.apparent().radec()

    visible = (
        numpy.atleast_1d(alt.degrees > 0)
        if coordinate_system == CoordinateSystem.HORIZONTAL and not ignore_horizon
        else numpy.ones(len(bright_stars), dtype=bool)
    )
    if not any(visible) and not ignore_horizon:
        return

    zoom_mask = _apply_zoom_and_horizon_filter(
        ax,
        coordinate_system,
        zoom_deg,
        alt.degrees[visible],
        az.degrees[visible],
        az.radians[visible],
        ra.hours[visible],
        ra.radians[visible],
        dec.degrees[visible],
        is_polar,
    )

    mag_plot = bright_stars[visible]["magnitude"][zoom_mask]
    sizes = (limit + 1 - numpy.array(mag_plot)) * (5 if is_polar else 3)

    _add_star_scatter_and_labels(
        ax,
        coordinate_system,
        is_polar,
        alt.degrees[visible][zoom_mask],
        az.radians[visible][zoom_mask],
        az.degrees[visible][zoom_mask],
        ra.radians[visible][zoom_mask],
        ra.hours[visible][zoom_mask],
        dec.degrees[visible][zoom_mask],
        None,
        sizes,
        ax.get_facecolor() if is_polar else style["TEXT_COLOR"],
        "." if not is_polar else ".",
        plot_labels,
        is_sh=_is_southern_hemisphere(observation),
        edge_color=style["TEXT_COLOR"] if is_polar else None,
    )
