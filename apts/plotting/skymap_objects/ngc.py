from typing import TYPE_CHECKING, Optional, cast

import numpy
import pandas as pd
from skyfield.api import Star

from apts.constants.plot import CoordinateSystem
from ...constants import ObjectTableLabels
from .utils import _parse_ra, _parse_dec, _plot_celestial_object

if TYPE_CHECKING:
    from apts.observations import Observation


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
    import apts.plotting.skymap_objects as api
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
        if ignore_horizon:
            is_above_horizon = numpy.ones(len(alt_all_deg), dtype=bool)
        else:
            is_above_horizon = alt_all_deg > 0

        if not numpy.any(is_above_horizon) and not ignore_horizon:
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

        widths_deg = get_dim(ObjectTableLabels.SIZE_MAJOR) / 60.0
        heights_deg = get_dim(ObjectTableLabels.SIZE_MINOR) / 60.0
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
            if plot_labels:
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
                parallactic_angle = api.calculate_parallactic_angle(
                    observation.place.lat, active_decs[i], active_azs[i]
                )
                angle = api.calculate_ellipse_angle(
                    pos_angles[i],
                    parallactic_angle,
                    coordinate_system,
                    flipped_horizontally,
                    flipped_vertically,
                )
                face_color = api.get_brightness_color(magnitudes[i])

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
                    plot_labels=plot_labels,
                )
