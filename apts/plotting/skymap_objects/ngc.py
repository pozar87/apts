from typing import TYPE_CHECKING, Any, Optional, cast

import numpy
import pandas as pd
from skyfield.api import Star

from apts.constants.plot import CoordinateSystem

from ...constants import ObjectTableLabels
from .utils import _plot_celestial_object

if TYPE_CHECKING:
    from apts.observations import Observation


def _filter_ngc_by_zoom(
    observation: "Observation",
    ignore_horizon: bool,
    zoom_deg: Optional[float],
    target_object: Any,
    star_magnitude_limit: Optional[float],
    observer: Any,
) -> pd.DataFrame:
    """Helper to fetch visible NGC objects and perform box/angular separation filtering."""
    visible_ngc = pd.DataFrame()
    if (zoom_deg is not None and target_object is not None) or ignore_horizon:
        # Use direct reference to avoid costly copy of 14k entries
        visible_ngc = observation.local_ngc.objects
    else:
        # In a real scenario we'd need to ensure CoordinateSystem is imported.
        # It's better to import it at the top level or within the function if needed.
        visible_ngc = observation.get_visible_ngc(
            star_magnitude_limit=star_magnitude_limit
        )

    if not cast(pd.DataFrame, visible_ngc).empty:
        # Optimization: pre-calculate float coords if missing (e.g. in tests)
        # using faster vectorized approach from catalogs.ngc
        visible_ngc = _ensure_ngc_coordinates(visible_ngc)

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

            ngc_in_box = visible_ngc[
                (visible_ngc["ra_hours"] >= ra_min)
                & (visible_ngc["ra_hours"] <= ra_max)
                & (visible_ngc["dec_degrees"] >= dec_min)
                & (visible_ngc["dec_degrees"] <= dec_max)
            ]

            if not ngc_in_box.empty:
                # Use target_object's position directly
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
    return cast(pd.DataFrame, visible_ngc)


def _ensure_ngc_coordinates(visible_ngc: pd.DataFrame) -> pd.DataFrame:
    """Ensure coordinate columns exist (they should be in the catalog, but might be missing in tests)."""
    if not visible_ngc.empty:
        if (
            "ra_hours" not in visible_ngc.columns
            or "dec_degrees" not in visible_ngc.columns
        ):
            visible_ngc = visible_ngc.copy()
            if "RA_parsed" in visible_ngc.columns:
                visible_ngc["ra_hours"] = visible_ngc["RA_parsed"]
            elif "RA" in visible_ngc.columns:
                # Optimization: use vectorized parsing instead of .apply()
                ras_split = visible_ngc["RA"].str.split(":", expand=True)
                for col in range(3):
                    if col not in ras_split.columns:
                        ras_split[col] = 0
                h_ra = pd.to_numeric(ras_split[0], errors="coerce")  # type: ignore[union-attr]
                m_ra = pd.to_numeric(ras_split[1], errors="coerce").fillna(0)  # type: ignore[union-attr]
                s_ra = pd.to_numeric(ras_split[2], errors="coerce").fillna(0)  # type: ignore[union-attr]
                visible_ngc["ra_hours"] = h_ra + m_ra / 60.0 + s_ra / 3600.0  # type: ignore[operator]

            if "Dec_parsed" in visible_ngc.columns:
                visible_ngc["dec_degrees"] = visible_ngc["Dec_parsed"]
            elif "Dec" in visible_ngc.columns:
                # Optimization: use vectorized parsing instead of .apply()
                decs_signs = (
                    visible_ngc["Dec"]
                    .str.startswith("-", na=False)
                    .map({True: -1, False: 1})
                )
                decs_split = (
                    visible_ngc["Dec"].str.lstrip("+-").str.split(":", expand=True)
                )
                for col in range(3):
                    if col not in decs_split.columns:
                        decs_split[col] = 0
                h_dec = pd.to_numeric(decs_split[0], errors="coerce")  # type: ignore[union-attr]
                m_dec = pd.to_numeric(decs_split[1], errors="coerce").fillna(0)  # type: ignore[union-attr]
                s_dec = pd.to_numeric(decs_split[2], errors="coerce").fillna(0)  # type: ignore[union-attr]
                visible_ngc["dec_degrees"] = decs_signs * (
                    h_dec + m_dec / 60.0 + s_dec / 3600.0  # type: ignore[operator]
                )
    return visible_ngc


def _observe_ngc_batch(visible_ngc: pd.DataFrame, observer: Any):
    """Observe all visible NGC objects at once before plotting."""

    def to_array(val, n):
        arr = numpy.atleast_1d(val)
        if arr.size == 1 and n > 1:
            return numpy.full(n, arr[0])
        return arr

    visible_ngc_copy = visible_ngc.copy()
    visible_ngc_copy["epoch_year"] = 2000.0
    ngc_stars = Star.from_dataframe(visible_ngc_copy)
    all_positions = observer.observe(ngc_stars).apparent()

    num_objects = len(visible_ngc)
    alt_all_deg = to_array(all_positions.altaz()[0].degrees, num_objects)
    az_all_deg = to_array(all_positions.altaz()[1].degrees, num_objects)
    ra_all_hours = to_array(all_positions.radec()[0].hours, num_objects)
    dec_all_deg = to_array(all_positions.radec()[1].degrees, num_objects)
    ra_all_rad = to_array(all_positions.radec()[0].radians, num_objects)

    return alt_all_deg, az_all_deg, ra_all_hours, dec_all_deg, ra_all_rad


def _get_ngc_plot_mask(
    visible_ngc_plot: pd.DataFrame,
    target_name: str,
    alt_all_deg: numpy.ndarray,
    ignore_horizon: bool,
):
    """Determine which objects should be plotted based on name, horizon, and position."""
    names = (
        visible_ngc_plot[ObjectTableLabels.NGC]
        .fillna(visible_ngc_plot[ObjectTableLabels.NAME])
        .to_numpy()
    )

    if ignore_horizon:
        is_above_horizon = numpy.ones(len(alt_all_deg), dtype=bool)
    else:
        is_above_horizon = alt_all_deg > 0

    mask = (~numpy.isin(names, [target_name])) & is_above_horizon
    return mask, names


def _get_ngc_dimensions(visible_ngc_plot: pd.DataFrame, mask: numpy.ndarray):
    """Retrieve and normalize physical dimensions and position angles."""

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
        with pd.option_context("future.no_silent_downcasting", True):
            vals = vals.fillna(1.0)
        return numpy.array([getattr(x, "magnitude", x) for x in vals], dtype=float)

    widths_deg = get_dim(ObjectTableLabels.SIZE_MAJOR) / 60.0
    heights_deg = get_dim(ObjectTableLabels.SIZE_MINOR) / 60.0
    pos_angles = get_dim("PosAng")

    return widths_deg, heights_deg, pos_angles


def _draw_ngc_polar(
    ax,
    widths_deg: numpy.ndarray,
    heights_deg: numpy.ndarray,
    observation: "Observation",
    coordinate_system: CoordinateSystem,
    active_azs: numpy.ndarray,
    active_alts: numpy.ndarray,
    active_ras_r: numpy.ndarray,
    active_decs: numpy.ndarray,
    active_names: numpy.ndarray,
    plot_labels: bool,
):
    """Handle polar projection plotting."""
    sizes = (widths_deg + heights_deg) / 2 * 100
    is_sh = observation.place.lat_decimal < 0

    if coordinate_system == CoordinateSystem.HORIZONTAL:
        x_vals, y_vals = numpy.deg2rad(active_azs), 90 - active_alts
    else:
        x_vals, y_vals = active_ras_r, (90 + active_decs if is_sh else 90 - active_decs)

    ax.scatter(x_vals, y_vals, s=sizes, color="green", marker="+")

    # Annotation loop still needed but optimized to avoid iterrows()
    if plot_labels:
        for name, x, y in zip(active_names, x_vals, y_vals):
            ax.annotate(
                name,
                (x, y),
                textcoords="offset points",
                xytext=(5, 5),
                color="green",
            )


def _draw_ngc_cartesian(
    visible_ngc_plot: pd.DataFrame,
    mask: numpy.ndarray,
    observation: "Observation",
    active_decs: numpy.ndarray,
    active_azs: numpy.ndarray,
    pos_angles: numpy.ndarray,
    coordinate_system: CoordinateSystem,
    flipped_horizontally: bool,
    flipped_vertically: bool,
    ax,
    active_names: numpy.ndarray,
    active_alts: numpy.ndarray,
    active_ras_h: numpy.ndarray,
    widths_deg: numpy.ndarray,
    heights_deg: numpy.ndarray,
    active_ras_r: numpy.ndarray,
    plot_labels: bool,
):
    """Handle cartesian/zoomed projection plotting."""
    import apts.plotting.skymap_objects as api

    if "Mag" in visible_ngc_plot.columns:
        magnitudes = visible_ngc_plot.loc[mask, "Mag"].to_numpy()
    elif "Magnitude" in visible_ngc_plot.columns:
        magnitudes_raw = visible_ngc_plot.loc[mask, "Magnitude"].values
        magnitudes = numpy.array(
            [getattr(m, "magnitude", m) for m in magnitudes_raw], dtype=float
        )
    else:
        magnitudes = numpy.full(len(active_names), 10.0)

    # Optimization: pre-calculate all rotation angles using vectorized geometric functions
    parallactic_angles = api.calculate_parallactic_angle(
        observation.place.lat_decimal, active_decs, active_azs
    )
    angles = api.calculate_ellipse_angle(
        pos_angles,
        parallactic_angles,
        coordinate_system,
        flipped_horizontally,
        flipped_vertically,
    )
    # Optimization: use vectorized brightness color calculation
    face_colors = api.get_brightness_color(magnitudes)
    # Broadcast scalar face_colors to array if needed
    if isinstance(face_colors, str):
        face_colors = numpy.full(len(active_names), face_colors)

    for i in range(len(active_names)):
        _plot_celestial_object(
            ax,
            name=cast(str, active_names[i]),
            alt_deg=float(active_alts[i]),
            az_deg=float(active_azs[i]),
            ra_hours=float(active_ras_h[i]),
            dec_deg=float(active_decs[i]),
            width_deg=float(widths_deg[i]),
            height_deg=float(heights_deg[i]),
            angle=float(angles[i])
            if isinstance(angles, numpy.ndarray)
            else float(angles),
            face_color=str(face_colors[i]),
            edge_color="green",
            is_polar=False,
            ra_rad=float(active_ras_r[i]),
            coordinate_system=coordinate_system,
            is_sh=observation.place.lat_decimal < 0,
            plot_labels=plot_labels,
        )


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
    plot_labels: bool = True,
    ignore_horizon: bool = False,
):
    visible_ngc = _filter_ngc_by_zoom(
        observation,
        ignore_horizon,
        zoom_deg,
        target_object,
        star_magnitude_limit,
        observer,
    )

    if visible_ngc.empty:
        return

    visible_ngc = _ensure_ngc_coordinates(visible_ngc)
    (
        alt_all_deg,
        az_all_deg,
        ra_all_hours,
        dec_all_deg,
        ra_all_rad,
    ) = _observe_ngc_batch(visible_ngc, observer)

    # Reset index to ensure i matches the position in all_positions arrays
    visible_ngc_plot = visible_ngc.reset_index(drop=True)

    mask, names = _get_ngc_plot_mask(
        visible_ngc_plot, target_name, alt_all_deg, ignore_horizon
    )

    if not numpy.any(mask):
        return

    active_names = names[mask]
    active_alts = alt_all_deg[mask]
    active_azs = az_all_deg[mask]
    active_ras_h = ra_all_hours[mask]
    active_ras_r = ra_all_rad[mask]
    active_decs = dec_all_deg[mask]

    widths_deg, heights_deg, pos_angles = _get_ngc_dimensions(visible_ngc_plot, mask)

    if is_polar:
        _draw_ngc_polar(
            ax,
            widths_deg,
            heights_deg,
            observation,
            coordinate_system,
            active_azs,
            active_alts,
            active_ras_r,
            active_decs,
            active_names,
            plot_labels,
        )
    else:
        _draw_ngc_cartesian(
            visible_ngc_plot,
            mask,
            observation,
            active_decs,
            active_azs,
            pos_angles,
            coordinate_system,
            flipped_horizontally,
            flipped_vertically,
            ax,
            active_names,
            active_alts,
            active_ras_h,
            widths_deg,
            heights_deg,
            active_ras_r,
            plot_labels,
        )
