import logging
from datetime import datetime
from math import copysign
from typing import TYPE_CHECKING, Any, Optional, cast

from ...config import get_dark_mode
from ...constants.graphconstants import get_plot_style
from ...i18n import gettext_
from ...utils.plot import PlotUtils
from .utils import MOON_FONT, is_southern_hemisphere, setup_cardinal_markers

if TYPE_CHECKING:
    from ...place import Place

logger = logging.getLogger(__name__)


def _setup_moon_path_style_and_data(
    place: "Place", dark_mode_override: Optional[bool] = None
):
    """Retrieves style settings and prepares moon path data."""
    effective_dark_mode = (
        dark_mode_override if dark_mode_override is not None else get_dark_mode()
    )
    style = get_plot_style(effective_dark_mode)
    data = place.moon_path()
    is_southern = is_southern_hemisphere(place)

    if is_southern:
        data["Azimuth"] = (data["Azimuth"] + 180) % 360 - 180

    return effective_dark_mode, style, data, is_southern


def _plot_moon_phase_info(
    place: "Place", ax: Any, style: dict, effective_dark_mode: bool, is_southern: bool
):
    """Plots Moon phase icon and illumination text."""
    if is_southern:
        icon_x_pos, icon_y_pos = 0, 20
        text_y_pos = icon_y_pos - 13
    else:
        icon_x_pos, icon_y_pos = 180, 10
        text_y_pos = -3

    if effective_dark_mode:
        ax.plot(
            icon_x_pos,
            icon_y_pos,
            marker="o",
            markersize=45,
            color=style["TEXT_COLOR"],
            linestyle="None",
        )
        text_color = style["AXES_FACE_COLOR"]
    else:
        text_color = style["TEXT_COLOR"]

    ax.text(
        icon_x_pos,
        icon_y_pos,
        place._moon_phase_letter(),
        fontproperties=MOON_FONT,
        horizontalalignment="center",
        verticalalignment="center",
        color=text_color,
    )

    illumination = place.moon_illumination()
    # Handle MagicMock which fails on float formatting
    if hasattr(illumination, "__float__") or isinstance(illumination, (int, float)):
        illumination_text = f"{illumination:.0f}%"
    else:
        illumination_text = f"{illumination}%"

    ax.text(
        icon_x_pos,
        text_y_pos,
        illumination_text,
        color=style["TEXT_COLOR"],
        alpha=0.7,
        horizontalalignment="center",
    )


def _annotate_moon_path_times(ax: Any, data: Any, style: dict, is_southern: bool):
    """Annotates time for altitudes on the moon path plot."""
    # Optimization: Using to_dict('records') for small loops is faster than iterrows()
    # and more robust than itertuples() when column names contain spaces or vary (mocks).
    for obj_row in data.dropna().iloc[::6, :].to_dict("records"):
        altitude = obj_row.get("Moon altitude", 0)
        azimuth = obj_row.get("Azimuth", 0)
        local_time = obj_row.get("Local_time", "")

        if altitude > 0:
            if is_southern:
                x_offset = copysign(10, azimuth) + 10
            else:
                x_offset = copysign(10, azimuth - 180) - 8

            ax.annotate(
                local_time,
                (azimuth + x_offset, altitude + 1),
                color=style["TEXT_COLOR"],
            )


def generate_plot_moon_path(
    place: "Place", dark_mode_override: Optional[bool] = None, **args
):
    effective_dark_mode, style, data, is_southern = _setup_moon_path_style_and_data(
        place, dark_mode_override
    )

    passed_ax = args.pop("ax", None)
    plot_kwargs = {
        "x": "Azimuth",
        "y": "Moon altitude",
        "title": "Moon altitude",
        "style": ".-",
        **args,
    }

    if passed_ax is not None:
        plot_kwargs["ax"] = passed_ax
        data.plot(**plot_kwargs)
        ax = passed_ax
    else:
        ax = data.plot(**plot_kwargs)

    fig = ax.figure
    fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    if ax.lines:
        ax.lines[0].set_color(style["TEXT_COLOR"])

    setup_cardinal_markers(ax, is_southern, style)

    PlotUtils.annotate_plot(
        ax,
        gettext_("Altitude [°]"),
        effective_dark_mode,
        place.local_timezone,
        x_label=gettext_("Azimuth [°]"),
    )

    # Plot horizon
    ax.axhspan(0, -50, color=style["GRID_COLOR"], alpha=0.3)
    ax.locator_params(nbins=20)
    ax.set_ylim(bottom=-10, top=90)

    _plot_moon_phase_info(place, ax, style, effective_dark_mode, is_southern)
    _annotate_moon_path_times(ax, data, style, is_southern)

    ax.set_title(
        gettext_("Moon Path")
        + f" on {cast(datetime, place.date.utc_datetime()).strftime('%Y-%m-%d')}",
        color=style["TEXT_COLOR"],
    )
    PlotUtils.style_legend(ax, style)
    return ax
