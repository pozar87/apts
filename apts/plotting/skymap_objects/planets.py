from typing import TYPE_CHECKING, Optional, cast

import numpy
import pandas as pd
from matplotlib.patches import Ellipse

from apts.constants.graphconstants import get_planet_color
from apts.constants.plot import CoordinateSystem
from apts.i18n import gettext_
from apts.utils import planetary
from ...constants import ObjectTableLabels

if TYPE_CHECKING:
    from apts.observations import Observation


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
    plot_labels: bool = True,
    ignore_horizon: bool = False,
):
    if ignore_horizon:
        visible_planets = observation.local_planets.objects.copy()
        visible_planets["TechnicalName"] = visible_planets[ObjectTableLabels.NAME]
    else:
        visible_planets = observation.get_visible_planets()
    if not visible_planets.empty:
        target_technical_name = (
            planetary.get_technical_name(target_name) if target_name else None
        )
        for _, p_obj in visible_planets.iterrows():
            planet_name = p_obj[ObjectTableLabels.NAME]
            technical_name = p_obj.get("TechnicalName", planet_name)
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
                plot_labels=plot_labels,
                ignore_horizon=ignore_horizon,
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
    plot_labels: bool = True,
    ignore_horizon: bool = False,
):
    """Helper to plot a solar system object, handling regular and target styles."""
    import apts.plotting.skymap_objects as api
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
    if (
        is_below_horizon
        and coordinate_system == CoordinateSystem.HORIZONTAL
        and not ignore_horizon
    ):
        return

    size_deg = api.get_object_angular_size_deg(observation, object_name)

    # Determine colors and markers
    effective_dark_mode = api.get_dark_mode()
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
        if not is_target and plot_labels:
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
        if not is_target and plot_labels:
            ax.annotate(
                display_name,
                (x_coord, y_coord),
                textcoords="offset points",
                xytext=(5, 5),
                color=edge_color,
            )
