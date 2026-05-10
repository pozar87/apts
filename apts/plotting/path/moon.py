import logging
from math import copysign
from typing import TYPE_CHECKING, Optional

from ...config import get_dark_mode
from ...constants.graphconstants import get_plot_style
from ...i18n import gettext_
from ...utils.plot import PlotUtils
from .utils import is_southern_hemisphere, setup_cardinal_markers, MOON_FONT

if TYPE_CHECKING:
    from ...place import Place

logger = logging.getLogger(__name__)

def generate_plot_moon_path(
    place: "Place", dark_mode_override: Optional[bool] = None, **args
):
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)

    data = place.moon_path()
    is_southern = is_southern_hemisphere(place)

    if is_southern:
        data["Azimuth"] = (data["Azimuth"] + 180) % 360 - 180

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
        fig = ax.figure
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

    # --- Plot Moon Phase Icon and Illumination Text ---
    if is_southern:
        icon_x_position = 0
        icon_y_position = 20
        text_y_position = icon_y_position - 13
    else:
        icon_x_position = 180
        icon_y_position = 10
        text_y_position = -3

    if effective_dark_mode:
        ax.plot(
            icon_x_position,
            icon_y_position,
            marker="o",
            markersize=45,
            color=style["TEXT_COLOR"],
            linestyle="None",
        )
        ax.text(
            icon_x_position,
            icon_y_position,
            place._moon_phase_letter(),
            fontproperties=MOON_FONT,
            horizontalalignment="center",
            verticalalignment="center",
            color=style["AXES_FACE_COLOR"],
        )
    else:
        ax.text(
            icon_x_position,
            icon_y_position,
            place._moon_phase_letter(),
            fontproperties=MOON_FONT,
            horizontalalignment="center",
            verticalalignment="center",
            color=style["TEXT_COLOR"],
        )
    illumination = place.moon_illumination()
    # Handle MagicMock which fails on float formatting
    if hasattr(illumination, "__float__") or isinstance(illumination, (int, float)):
        illumination_text = f"{illumination:.0f}%"
    else:
        illumination_text = f"{illumination}%"

    ax.text(
        icon_x_position,
        text_y_position,
        illumination_text,
        color=style["TEXT_COLOR"],
        alpha=0.7,
        horizontalalignment="center",
    )

    # Plot time for altitudes
    for _, obj_row in data.dropna().iloc[::6, :].iterrows():
        altitude = obj_row["Moon altitude"]
        azimuth = obj_row["Azimuth"]
        local_time = obj_row["Local_time"]

        if altitude > 0:
            if is_southern:
                offset_direction = azimuth
                x_offset = copysign(10, offset_direction) + 10
            else:
                x_offset = copysign(10, azimuth - 180) - 8

            ax.annotate(
                local_time,
                (azimuth + x_offset, altitude + 1),
                color=style["TEXT_COLOR"],
            )
    ax.set_title(
        gettext_("Moon Path")
        + f" on {place.date.utc_datetime().strftime('%Y-%m-%d')}",
        color=style["TEXT_COLOR"],
    )
    PlotUtils.style_legend(ax, style)
    return ax
