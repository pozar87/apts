import logging
from datetime import datetime
from typing import TYPE_CHECKING, Optional, cast

import numpy as np
import pandas as pd
from matplotlib import figure, pyplot
from matplotlib.patches import Circle, Ellipse

from apts.cache import get_jovian_ephemeris, get_timescale
from apts.config import get_dark_mode
from apts.constants import astronomy
from apts.constants.graphconstants import get_planet_color, get_plot_style
from apts.i18n import gettext_
from apts.skyfield_searches.jovian.moons import JovianMoonState
from apts.skyfield_searches.jovian.utils import JovianSearchContext

if TYPE_CHECKING:
    from ..observations import Observation

logger = logging.getLogger(__name__)


def generate_plot_jovian_moons(
    observation: "Observation",
    plot_date: Optional[datetime] = None,
    dark_mode_override: Optional[bool] = None,
    zoom_arcmin: float = 20.0,
    flipped_horizontally: bool = False,
    flipped_vertically: bool = False,
    **kwargs,
) -> figure.Figure:
    """
    Generates a zoomed-in visualization of Jupiter and its Galilean moons.

    Args:
        observation: The observation object.
        plot_date: Specific date/time for the visualization. Defaults to observation middle.
        dark_mode_override: Override for dark mode.
        zoom_arcmin: Field of view in arcminutes. Defaults to 20.0.
        flipped_horizontally: Whether to flip the plot horizontally.
        flipped_vertically: Whether to flip the plot vertically.
        **kwargs: Additional arguments for matplotlib (e.g., figsize).

    Returns:
        A matplotlib Figure object.
    """
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)
    ts = get_timescale()

    if plot_date is not None:
        if plot_date.tzinfo is None:
            import datetime

            plot_date = plot_date.replace(tzinfo=datetime.timezone.utc)
        t = ts.utc(plot_date)
    elif observation.effective_date is not None:
        t = observation.effective_date
    else:
        t = ts.now()

    eph = get_jovian_ephemeris()
    ctx = JovianSearchContext(observation.place.observer, eph, ts)
    state_func = JovianMoonState(ctx)

    # Get Jupiter position and distance
    j_obs = observation.place.observer.at(t).observe(ctx.jupiter).apparent()
    j_ra, j_dec, j_dist = j_obs.radec()
    j_dist_km = j_dist.km

    # Calculate Jupiter angular radius in arcseconds
    j_radius_arcsec = (
        np.degrees(np.arctan2(astronomy.JUPITER_RADIUS_KM, j_dist_km)) * 3600
    )
    j_polar_radius_arcsec = (
        np.degrees(np.arctan2(astronomy.JUPITER_POLAR_RADIUS_KM, j_dist_km)) * 3600
    )

    # Setup plot
    figsize = kwargs.get("figsize", (10, 10))
    fig, ax = pyplot.subplots(figsize=figsize)
    fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    # Jupiter color
    j_color = get_planet_color("Jupiter", effective_dark_mode, "orange")

    # Plot Jupiter
    # We use (0,0) as center for simplicity and set limits based on zoom_arcmin
    # dx is in arcseconds: (ra - j_ra) * 15 * 3600 * cos(dec)
    # dy is in arcseconds: (dec - j_dec) * 3600

    # Actually, we can use a more precise projection if needed, but for 20 arcmin,
    # tangent plane approximation is fine.

    jupiter_disk = Ellipse(
        (0, 0),
        width=j_radius_arcsec * 2,
        height=j_polar_radius_arcsec * 2,
        color=j_color,
        label="Jupiter",
    )
    ax.add_patch(jupiter_disk)

    # Moon data
    moons_radii = {
        501: astronomy.IO_RADIUS_KM,
        502: astronomy.EUROPA_RADIUS_KM,
        503: astronomy.GANYMEDE_RADIUS_KM,
        504: astronomy.CALLISTO_RADIUS_KM,
    }

    mask = state_func(t)

    cos_j_dec = np.cos(j_dec.radians)

    for i, (moon_id, moon_name) in enumerate(ctx.moon_map.items()):
        if moon_id not in ctx.moon_objs:
            continue
        m_obs = (
            observation.place.observer.at(t).observe(ctx.moon_objs[moon_id]).apparent()
        )
        m_ra, m_dec, m_dist = m_obs.radec()

        dx = (m_ra.hours - j_ra.hours) * 15 * 3600 * cos_j_dec
        dy = (m_dec.degrees - j_dec.degrees) * 3600

        moon_mask = (mask >> (4 * i)) & 0xF

        # Check if moon is behind Jupiter (Occultation or Eclipse)
        is_behind = bool(moon_mask & (2 | 8))
        # Check if moon is in front (Transit)
        is_transit = bool(moon_mask & 1)
        # Check if shadow is on Jupiter
        # is_shadow = bool(moon_mask & 4)

        if not is_behind:
            m_radius_arcsec = (
                np.degrees(np.arctan2(moons_radii[moon_id], m_dist.km)) * 3600
            )
            # Draw moon
            moon_color = "white" if not is_transit else "gray"
            moon_disk = Circle((dx, dy), m_radius_arcsec, color=moon_color)
            ax.add_patch(moon_disk)

            # Label
            ax.text(
                dx,
                dy + m_radius_arcsec + 2,
                gettext_(moon_name),
                color=style["TEXT_COLOR"],
                ha="center",
                va="bottom",
                fontsize=10,
            )

    # Set limits (in arcseconds)
    limit = (zoom_arcmin / 2.0) * 60
    ax.set_xlim(limit, -limit)  # RA increases to the left
    ax.set_ylim(-limit, limit)
    ax.set_aspect("equal")

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

    ax.set_xlabel(gettext_("Relative RA (arcsec)"), color=style["TEXT_COLOR"])
    ax.set_ylabel(gettext_("Relative Dec (arcsec)"), color=style["TEXT_COLOR"])

    # t can be either a datetime (from observation.effective_date) or a Skyfield Time
    if hasattr(t, "utc_datetime"):
        t_dt = t.utc_datetime().astimezone(observation.place.local_timezone)
    else:
        t_dt = t.astimezone(observation.place.local_timezone)
    ax.set_title(
        gettext_("Jupiter and Galilean Moons ({date})").format(
            date=t_dt.strftime("%Y-%m-%d %H:%M %Z")
        ),
        color=style["TEXT_COLOR"],
    )

    ax.tick_params(colors=style["TICK_COLOR"])
    for spine in ax.spines.values():
        spine.set_color(style["AXES_EDGE_COLOR"])

    return fig


def plot_jovian_moons(
    observation: "Observation",
    plot_date: Optional[datetime] = None,
    dark_mode_override: Optional[bool] = None,
    zoom_arcmin: float = 20.0,
    equipment_id: Optional[int] = None,
    flip_horizontally: Optional[bool] = None,
    flip_vertically: Optional[bool] = None,
    **kwargs,
) -> figure.Figure:
    """
    High-level function to plot Jovian moons with support for flipping and equipment lookup.
    """
    flipped_horizontally = False
    flipped_vertically = False

    if equipment_id is not None:
        # Check if equipment has data method, otherwise assume it's already a DataFrame
        equipment_data = cast(
            pd.DataFrame,
            observation.equipment.data()
            if hasattr(observation.equipment, "data")
            else observation.equipment,
        )
        if (
            equipment_data is not None
            and not equipment_data.empty
            and "ID" in equipment_data.columns
            and equipment_id in equipment_data["ID"].values
        ):
            row = equipment_data.loc[equipment_data["ID"] == equipment_id]
            if "Flipped Horizontally" in row.columns:
                flipped_horizontally = row["Flipped Horizontally"].iloc[0]
            if "Flipped Vertically" in row.columns:
                flipped_vertically = row["Flipped Vertically"].iloc[0]

    if flip_horizontally is not None:
        flipped_horizontally = flip_horizontally
    if flip_vertically is not None:
        flipped_vertically = flip_vertically

    return generate_plot_jovian_moons(
        observation,
        plot_date=plot_date,
        dark_mode_override=dark_mode_override,
        zoom_arcmin=zoom_arcmin,
        flipped_horizontally=flipped_horizontally,
        flipped_vertically=flipped_vertically,
        **kwargs,
    )
