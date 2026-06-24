import logging
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional, Any, Dict

from matplotlib import figure, pyplot
from matplotlib.patches import Circle, Ellipse

from apts.config import get_dark_mode
from apts.constants.graphconstants import get_planet_color, get_plot_style
from apts.i18n import gettext_
from apts.cache import get_timescale
from .calculations import calculate_jovian_state, JovianSystemState

if TYPE_CHECKING:
    from ...observations import Observation
    from skyfield.api import Time

logger = logging.getLogger(__name__)

def _get_effective_time(observation: "Observation", plot_date: Optional[datetime]) -> "Time":
    ts = get_timescale()
    if plot_date is not None:
        if plot_date.tzinfo is None:
            plot_date = plot_date.replace(tzinfo=timezone.utc)
        return ts.utc(plot_date)
    elif observation.effective_date is not None:
        return observation.effective_date
    else:
        return ts.now()

def _setup_axes(ax: Any, style: Dict[str, str], zoom_arcmin: float):
    # Set limits (in arcseconds)
    limit = (zoom_arcmin / 2.0) * 60
    ax.set_xlim(limit, -limit)  # RA increases to the left
    ax.set_ylim(-limit, limit)
    ax.set_aspect("equal")

    ax.set_xlabel(gettext_("Relative RA (arcsec)"), color=style["TEXT_COLOR"])
    ax.set_ylabel(gettext_("Relative Dec (arcsec)"), color=style["TEXT_COLOR"])

    ax.tick_params(colors=style["TICK_COLOR"])
    for spine in ax.spines.values():
        spine.set_color(style["AXES_EDGE_COLOR"])

def _draw_jupiter(ax: Any, state: JovianSystemState, effective_dark_mode: bool):
    j_color = get_planet_color("Jupiter", effective_dark_mode, "orange")
    jupiter_disk = Ellipse(
        (0, 0),
        width=state.jupiter_radius_arcsec * 2,
        height=state.jupiter_polar_radius_arcsec * 2,
        color=j_color,
        label="Jupiter",
    )
    ax.add_patch(jupiter_disk)

def _draw_moons(ax: Any, state: JovianSystemState, style: Dict[str, str]):
    for moon_id, m_pos in state.moons.items():
        if not m_pos.is_behind:
            moon_color = "white" if not m_pos.is_transit else "gray"
            moon_disk = Circle((m_pos.dx, m_pos.dy), m_pos.radius_arcsec, color=moon_color)
            ax.add_patch(moon_disk)
            ax.text(
                m_pos.dx,
                m_pos.dy + m_pos.radius_arcsec + 2,
                gettext_(m_pos.name),
                color=style["TEXT_COLOR"],
                ha="center",
                va="bottom",
                fontsize=10,
            )

def _apply_flips(ax: Any, style: Dict[str, str], flipped_h: bool, flipped_v: bool):
    if flipped_h:
        ax.invert_xaxis()
    if flipped_v:
        ax.invert_yaxis()

    if flipped_h or flipped_v:
        flip_str = gettext_("Flipped") + " "
        if flipped_h:
            flip_str += "H"
        if flipped_v:
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
    """
    effective_dark_mode = dark_mode_override if dark_mode_override is not None else get_dark_mode()
    style = get_plot_style(effective_dark_mode)
    t = _get_effective_time(observation, plot_date)
    state = calculate_jovian_state(observation, t)

    figsize = kwargs.get("figsize", (10, 10))
    fig, ax = pyplot.subplots(figsize=figsize)
    fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    _setup_axes(ax, style, zoom_arcmin)
    _draw_jupiter(ax, state, effective_dark_mode)
    _draw_moons(ax, state, style)
    _apply_flips(ax, style, flipped_horizontally, flipped_vertically)

    from skyfield.api import Time as SkyfieldTime
    t_dt = t.utc_datetime().astimezone(observation.place.local_timezone) if isinstance(t, SkyfieldTime) else t.astimezone(observation.place.local_timezone)

    ax.set_title(
        gettext_("Jupiter and Galilean Moons ({date})").format(
            date=t_dt.strftime("%Y-%m-%d %H:%M %Z")
        ),
        color=style["TEXT_COLOR"],
    )

    return fig
