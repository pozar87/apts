from typing import TYPE_CHECKING, cast, Any

import numpy
import pandas as pd
from skyfield.api import Star

from apts.config import get_dark_mode
from apts.constants.graphconstants import get_messier_color
from apts.constants.plot import CoordinateSystem
from apts.i18n import gettext_
from apts.plotting.utils import (
    calculate_ellipse_angle,
    calculate_parallactic_angle,
    get_brightness_color,
)
from ...constants import ObjectTableLabels
from .utils import _plot_celestial_object

if TYPE_CHECKING:
    from ...observations import Observation


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
    plot_labels: bool = True,
    ignore_horizon: bool = False,
):
    if ignore_horizon:
        visible_messier = observation.local_messier.objects
    else:
        visible_messier = observation.get_visible_messier()
    if visible_messier.empty:
        return

    # Filter out target object and reset index for array matching/safe iteration
    plot_df = visible_messier[
        visible_messier[ObjectTableLabels.MESSIER] != target_name
    ].copy().reset_index(drop=True)

    if plot_df.empty:
        return

    # Ensure RA/Dec float columns exist for vectorization (handling mocks/incomplete data in tests)
    # Optimization: reset_index(drop=True) is called here to ensure positional access is safe.
    plot_df = plot_df.reset_index(drop=True)
    if "ra_hours" not in plot_df.columns or "dec_degrees" not in plot_df.columns:
        # Reset index to ensure loc[i] works correctly after filtering
        plot_df = plot_df.reset_index(drop=True)
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

    widths_deg = get_dim(ObjectTableLabels.SIZE_MAJOR) / 60.0
    heights_deg = get_dim(ObjectTableLabels.SIZE_MINOR) / 60.0
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
        # Restore original filtering: only plot objects above the horizon unless ignore_horizon is True
        if alt_deg[i] <= 0 and not ignore_horizon:
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
            plot_labels=plot_labels,
        )
